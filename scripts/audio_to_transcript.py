"""
Audio to transcript — converts call recordings to text.

Usage:
    python audio_to_transcript.py <audio_file>
    python audio_to_transcript.py recording.m4a
    python audio_to_transcript.py "My Call 2026-05-22.mp4"

Supported formats: mp3, mp4, m4a, wav, ogg, opus, webm, flac, aac

Transcription backends (in order of preference):
    1. OpenAI Whisper API  — fast, accurate, requires OPENAI_API_KEY in .env
    2. faster-whisper      — runs locally, free, no API key needed
       Install: pip install faster-whisper

Prerequisites:
    ffmpeg must be in your PATH for audio normalization.
    Download: https://ffmpeg.org/download.html  (Windows: winget install ffmpeg)

Output:
    sources/calls/<YYYY-MM-DD>_<original_stem>.txt
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.logger import EngineLogger
from lib.utils import SOURCES_DIR, VAULT_ROOT, get_env, now_iso

CALLS_DIR = SOURCES_DIR / "calls"
MAX_WHISPER_BYTES = 24 * 1024 * 1024  # 24 MB (API limit is 25 MB)
AUDIO_EXTS = {".mp3", ".mp4", ".m4a", ".wav", ".ogg", ".opus", ".webm", ".flac", ".aac"}


# ── FFMPEG ─────────────────────────────────────────────────────────────────────

def _ffmpeg_available() -> bool:
    return shutil.which("ffmpeg") is not None


def _normalize(src: Path, dst: Path) -> None:
    """Convert any audio to 16kHz mono WAV for optimal Whisper input."""
    subprocess.run(
        [
            "ffmpeg", "-i", str(src),
            "-ar", "16000",
            "-ac", "1",
            "-c:a", "pcm_s16le",
            str(dst),
            "-y", "-loglevel", "error",
        ],
        check=True,
    )


def _compress_mp3(src: Path, dst: Path, bitrate: str = "64k") -> None:
    """Compress to MP3 at voice-quality bitrate to get under Whisper's 25 MB limit."""
    subprocess.run(
        [
            "ffmpeg", "-i", str(src),
            "-b:a", bitrate,
            "-c:a", "libmp3lame",
            str(dst),
            "-y", "-loglevel", "error",
        ],
        check=True,
    )


# ── WHISPER API ────────────────────────────────────────────────────────────────

def _transcribe_whisper_api(audio_path: Path) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        raise RuntimeError("openai package not installed. Run: pip install openai")

    api_key = get_env("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set in .env")

    client = OpenAI(api_key=api_key)

    with audio_path.open("rb") as f:
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            response_format="text",
            language="en",
        )
    # result is a plain string when response_format="text"
    return str(result)


# ── FASTER-WHISPER (local) ─────────────────────────────────────────────────────

def _transcribe_faster_whisper(audio_path: Path) -> str:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise RuntimeError(
            "faster-whisper not installed. Run: pip install faster-whisper\n"
            "Or set OPENAI_API_KEY in .env to use the Whisper API."
        )

    print("  Loading local Whisper model (first run downloads ~150 MB)...")
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(str(audio_path), beam_size=5, language="en")
    return " ".join(seg.text.strip() for seg in segments)


# ── CORE ───────────────────────────────────────────────────────────────────────

def _prepare_audio(src: Path, tmp_dir: Path, logger: EngineLogger) -> Path:
    """
    Normalize audio for Whisper. Returns path to processed file.
    If ffmpeg is unavailable, returns the original (Whisper API can handle most formats).
    """
    if not _ffmpeg_available():
        logger.info("ffmpeg not found — using original audio file")
        print("  [!] ffmpeg not found. Install it for best results:")
        print("      winget install ffmpeg  (Windows)")
        return src

    normalized = tmp_dir / f"{src.stem}_normalized.wav"
    logger.info(f"Normalizing audio → 16kHz mono WAV")
    _normalize(src, normalized)

    # If still too large for the API, compress to MP3
    if normalized.stat().st_size > MAX_WHISPER_BYTES:
        logger.info("Normalized file > 24 MB — compressing to MP3 64k")
        compressed = tmp_dir / f"{src.stem}_compressed.mp3"
        _compress_mp3(normalized, compressed)
        if compressed.stat().st_size > MAX_WHISPER_BYTES:
            logger.info("Still too large after compression — using original")
            print("  [!] File is very large. Consider splitting the recording into parts.")
            return src
        return compressed

    return normalized


def run(audio_path: Path) -> Path:
    logger = EngineLogger("audio_to_transcript")
    logger.start(input_path=str(audio_path))

    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    if audio_path.suffix.lower() not in AUDIO_EXTS:
        raise ValueError(
            f"Unsupported format: {audio_path.suffix}\n"
            f"Supported: {', '.join(sorted(AUDIO_EXTS))}"
        )

    size_mb = audio_path.stat().st_size / (1024 * 1024)
    logger.info(f"Input: {audio_path.name} ({size_mb:.1f} MB)")

    # Determine output path
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_stem = f"{date_str}_{audio_path.stem}"
    output_path = CALLS_DIR / f"{output_stem}.txt"
    CALLS_DIR.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        print(f"  Already transcribed: {output_path.name}")
        return output_path

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        processed = _prepare_audio(audio_path, tmp_dir, logger)

        # Choose backend
        api_key = get_env("OPENAI_API_KEY")

        if api_key:
            print("  Transcribing via OpenAI Whisper API...")
            try:
                transcript = _transcribe_whisper_api(processed)
                backend = "whisper-api"
            except Exception as e:
                print(f"  Whisper API failed ({e}). Falling back to local model...")
                transcript = _transcribe_faster_whisper(processed)
                backend = "faster-whisper"
        else:
            print("  No OPENAI_API_KEY — using local faster-whisper model...")
            transcript = _transcribe_faster_whisper(processed)
            backend = "faster-whisper"

    # Format and write output
    header = (
        f"# Transcript: {audio_path.name}\n"
        f"# Date: {date_str}\n"
        f"# Backend: {backend}\n"
        f"# Generated: {now_iso()}\n"
        f"# Drop this file in sources/calls/ then run /analyze-call\n\n"
    )
    output_path.write_text(header + transcript, encoding="utf-8")

    logger.finish(items_processed=1, output_path=str(output_path))
    return output_path


# ── CLI ────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()

    if len(sys.argv) < 2:
        console.print("[red]Usage:[/red] python audio_to_transcript.py <audio_file>")
        console.print("  Example: python audio_to_transcript.py recording.m4a")
        console.print()
        console.print(f"  Supported: {', '.join(sorted(AUDIO_EXTS))}")
        sys.exit(1)

    audio_file = Path(sys.argv[1])
    if not audio_file.is_absolute():
        audio_file = VAULT_ROOT / audio_file

    console.print(f"\n[bold]Audio → Transcript[/bold]")
    console.print(f"  Input:  [cyan]{audio_file.name}[/cyan]")

    try:
        out = run(audio_file)
        console.print(f"  Output: [green]{out.name}[/green]")
        console.print(f"\n  Next: /analyze-call {out.name}")
    except (FileNotFoundError, ValueError, RuntimeError) as e:
        console.print(f"\n[red]Error:[/red] {e}")
        sys.exit(1)
