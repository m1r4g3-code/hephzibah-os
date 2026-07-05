"""
Push wiki/ nodes to the private hephzibah-brain GitHub repo.

Usage: python scripts/push_brain.py [--dry-run]

Replaces `git subtree push --prefix=wiki brain main`, which permanently breaks
once the brain receives commits from any other OS instance (pull side is a
file-copy sync, so the subtree's synthetic history can never fast-forward).

How it works:
  1. Creates a temp clone of hephzibah-brain (or reuses cached .brain-staging/)
  2. Resets staging to origin/main (integrates other OS instances' pushes)
  3. Copies ALL local wiki files over it, preserving structure
     — never deletes nodes that exist only in the brain (append, don't delete)
  4. Commits + pushes to origin main (fast-forward, no force)
  5. Records the new brain HEAD in .brain_last_pull so pull_brain.py
     doesn't echo our own push back

Requirements:
  - git remote 'brain' configured:
    git remote add brain https://github.com/m1r4g3-code/hephzibah-brain.git
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"
STAGING = ROOT / ".brain-staging"
LAST_PULL_FILE = ROOT / ".brain_last_pull"
REMOTE_URL = "https://github.com/m1r4g3-code/hephzibah-brain.git"
DRY_RUN = "--dry-run" in sys.argv


def run(cmd: list[str], cwd: Path = None) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: {' '.join(cmd)}")
        print(f"  stderr: {result.stderr.strip()}")
        sys.exit(1)
    return result


def main():
    files = [f for f in WIKI.rglob("*") if f.is_file()]
    print(f"Found {len(files)} wiki files\n")

    if DRY_RUN:
        for f in sorted(files):
            print(f"  + {f.relative_to(WIKI)}")
        print("\nDry run — no changes made.")
        return

    # 1. Set up staging dir (clone or fetch+reset)
    if STAGING.exists():
        print("Staging dir exists — resetting to origin/main...")
        run(["git", "fetch", "origin"], cwd=STAGING)
        run(["git", "reset", "--hard", "origin/main"], cwd=STAGING)
    else:
        print(f"Cloning {REMOTE_URL}...")
        run(["git", "clone", REMOTE_URL, str(STAGING)])

    # Always set identity in staging dir — never inherit global git config
    run(["git", "config", "user.email", "adekoyaemmanuel15@gmail.com"], cwd=STAGING)
    run(["git", "config", "user.name", "m1r4g3-code"], cwd=STAGING)

    # 2. Copy all wiki files over staging, preserving structure.
    #    No wipe first: nodes that exist only in the brain must survive.
    for src in files:
        rel = src.relative_to(WIKI)
        dest = STAGING / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    # 3. Commit and push
    run(["git", "add", "-A"], cwd=STAGING)

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=STAGING, capture_output=True, text=True
    )
    if not status.stdout.strip():
        print("Brain is already up to date — nothing to push.")
        return

    changed = [line[3:] for line in status.stdout.strip().splitlines()]
    for f in changed:
        print(f"  ~ {f}")

    local_sha = run(["git", "rev-parse", "--short", "HEAD"]).stdout.strip()
    run(
        ["git", "commit", "-m", f"brain: push {len(changed)} node(s) from hephzibah-OS {local_sha} — auto-sync"],
        cwd=STAGING
    )
    run(["git", "push", "origin", "main"], cwd=STAGING)

    # 4. Record new brain HEAD so pull_brain.py doesn't re-pull our own push
    new_head = run(["git", "rev-parse", "HEAD"], cwd=STAGING).stdout.strip()
    LAST_PULL_FILE.write_text(new_head)

    print(f"\nPushed {len(changed)} node(s) to hephzibah-brain ({new_head[:8]})")


if __name__ == "__main__":
    main()
