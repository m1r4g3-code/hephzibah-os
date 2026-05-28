"""
Pull new nodes from hephzibah-brain into wiki/.

Usage:
  python scripts/pull_brain.py           # pull if brain has new commits
  python scripts/pull_brain.py --force   # pull even if already up to date
  python scripts/pull_brain.py --dry-run # show what would change, no writes

How it works:
  1. Fetch brain remote
  2. Compare brain/main HEAD vs last known brain commit (stored in .brain_last_pull)
  3. If new commits exist: extract via git archive, copy into wiki/, commit
  4. Record new HEAD in .brain_last_pull

Run automatically via Windows Task Scheduler (see scripts/setup_brain_scheduler.py)
"""
import subprocess
import sys
import shutil
import tempfile
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"
LAST_PULL_FILE = ROOT / ".brain_last_pull"
FORCE = "--force" in sys.argv
DRY_RUN = "--dry-run" in sys.argv


def run(cmd: list[str], cwd: Path = None, check: bool = True) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"ERROR: {' '.join(cmd)}")
        print(f"  {result.stderr.strip()}")
        sys.exit(1)
    return result


def get_brain_head() -> str:
    result = run(["git", "rev-parse", "brain/main"])
    return result.stdout.strip()


def get_last_pull() -> str:
    if LAST_PULL_FILE.exists():
        return LAST_PULL_FILE.read_text().strip()
    return ""


def has_changes(old_sha: str, new_sha: str) -> bool:
    if old_sha == new_sha:
        return False
    result = run(["git", "diff", "--stat", f"{old_sha}..{new_sha}", "--"], check=False)
    return bool(result.stdout.strip())


def get_changed_files(old_sha: str, new_sha: str) -> list[str]:
    result = run(["git", "diff", "--name-only", f"{old_sha}..{new_sha}"])
    return [f for f in result.stdout.strip().splitlines() if f]


def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Checking hephzibah-brain for new commits...")

    # 1. Fetch latest from brain
    run(["git", "fetch", "brain"])

    new_sha = get_brain_head()
    old_sha = get_last_pull()

    if not old_sha:
        # First run — record current state and exit (don't overwrite existing wiki)
        LAST_PULL_FILE.write_text(new_sha)
        print(f"  First run. Recorded brain HEAD: {new_sha[:8]}. Future pulls will detect new commits.")
        return

    if new_sha == old_sha and not FORCE:
        print(f"  Brain is up to date ({new_sha[:8]}). Nothing to pull.")
        return

    # 2. Show what changed
    changed = get_changed_files(old_sha, new_sha)
    print(f"  New commits found: {old_sha[:8]} → {new_sha[:8]}")
    print(f"  {len(changed)} file(s) changed:")
    for f in changed:
        print(f"    + {f}")

    if DRY_RUN:
        print("\nDry run — no changes written.")
        return

    # 3. Check for uncommitted local changes
    status = run(["git", "status", "--porcelain"])
    if status.stdout.strip():
        print("\nWorking tree has uncommitted changes — cannot auto-pull.")
        print("Commit or stash local changes first, then re-run.")
        sys.exit(1)

    # 4. Extract brain/main via git archive into temp dir
    tmpdir = Path(tempfile.mkdtemp(prefix="brain_pull_"))
    try:
        archive = run(["git", "archive", "brain/main"])
        extract = subprocess.run(
            ["tar", "-C", str(tmpdir), "-xf", "-"],
            input=archive.stdout.encode(),
            capture_output=True
        )
        if extract.returncode != 0:
            print(f"ERROR extracting archive: {extract.stderr.decode()}")
            sys.exit(1)

        # 5. Copy only the changed files into wiki/
        copied = []
        for rel_path in changed:
            src = tmpdir / rel_path
            dest = WIKI / rel_path
            if src.exists():
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                copied.append(rel_path)
            else:
                # File was deleted in brain — leave local copy intact
                print(f"  SKIP (deleted in brain): {rel_path}")

    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

    if not copied:
        print("  No files to copy.")
        LAST_PULL_FILE.write_text(new_sha)
        return

    # 6. Commit
    run(["git", "add"] + [f"wiki/{f}" for f in copied], check=False)

    # Check if there's actually something staged
    staged = run(["git", "diff", "--cached", "--name-only"])
    if not staged.stdout.strip():
        print("  No changes after copy (files may already be up to date).")
        LAST_PULL_FILE.write_text(new_sha)
        return

    short_summary = f"{len(copied)} node(s) from {new_sha[:8]}"
    run(["git", "commit", "-m", f"brain: pull {short_summary} — auto-sync"])
    run(["git", "push", "origin", "main"])

    # 7. Record new HEAD
    LAST_PULL_FILE.write_text(new_sha)

    print(f"\n  Pulled and committed {len(copied)} file(s). Brain is now at {new_sha[:8]}.")


if __name__ == "__main__":
    main()
