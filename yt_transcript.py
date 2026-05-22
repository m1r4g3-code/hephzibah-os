"""
Fetch a YouTube transcript and save it to a .txt file.
Usage: python yt_transcript.py <youtube_url_or_video_id>
Output: <video_id>.txt in the same directory
"""

import sys
import re
import os
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=|youtu\.be/|embed/|shorts/)([A-Za-z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url_or_id):
        return url_or_id
    raise ValueError(f"Could not extract video ID from: {url_or_id}")


def fetch_transcript(video_id: str) -> str:
    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id)
        segments = fetched.snippets
    except NoTranscriptFound:
        transcript_list = api.list(video_id)
        transcript = next(iter(transcript_list))
        fetched = transcript.fetch()
        segments = fetched.snippets
    return " ".join(seg.text for seg in segments)


def main():
    if len(sys.argv) < 2:
        print("Usage: python yt_transcript.py <youtube_url_or_video_id>")
        sys.exit(1)

    raw = sys.argv[1]
    video_id = extract_video_id(raw)
    print(f"Video ID: {video_id}")

    try:
        text = fetch_transcript(video_id)
    except TranscriptsDisabled:
        print("Transcripts are disabled for this video.")
        sys.exit(1)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, f"{video_id}.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Saved to: {out_path}")
    print(f"Characters: {len(text):,}")


if __name__ == "__main__":
    main()
