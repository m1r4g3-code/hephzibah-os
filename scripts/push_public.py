"""
Push sensitivity:public nodes to hephzibah-brain-public GitHub repo.

Usage: python scripts/push_public.py [--dry-run]

How it works:
  1. Creates a temp clone of brain-public (or uses cached .brain-public-staging/)
  2. Wipes all .md files from the staging clone
  3. Copies only sensitivity:public wiki nodes, preserving folder structure
  4. Commits + force-pushes to origin main

Requirements:
  - git remote 'brain-public' must be configured:
    git remote add brain-public https://github.com/m1r4g3-code/hephzibah-brain-public.git
  - GitHub repo hephzibah-brain-public must exist
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WIKI = ROOT / "wiki"
STAGING = ROOT / ".brain-public-staging"
REMOTE_URL = "https://github.com/m1r4g3-code/hephzibah-brain-public.git"
DRY_RUN = "--dry-run" in sys.argv


def get_sensitivity(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"^sensitivity:\s*(\w+)", text, re.MULTILINE)
    return match.group(1) if match else "private"


def run(cmd: list[str], cwd: Path = None) -> subprocess.CompletedProcess:
    result = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: {' '.join(cmd)}")
        print(f"  stderr: {result.stderr.strip()}")
        sys.exit(1)
    return result


def main():
    # 1. Collect public files
    public_files = [
        f for f in WIKI.rglob("*.md")
        if get_sensitivity(f) == "public"
    ]
    print(f"Found {len(public_files)} public nodes\n")

    if DRY_RUN:
        for f in sorted(public_files):
            print(f"  + {f.relative_to(WIKI)}")
        print("\nDry run — no changes made.")
        return

    # 2. Set up staging dir (clone or pull)
    if STAGING.exists():
        print("Staging dir exists — pulling latest...")
        run(["git", "fetch", "origin"], cwd=STAGING)
        run(["git", "reset", "--hard", "origin/main"], cwd=STAGING)
    else:
        print(f"Cloning {REMOTE_URL}...")
        result = subprocess.run(
            ["git", "clone", REMOTE_URL, str(STAGING)],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            # Repo might be empty — init fresh
            STAGING.mkdir(parents=True, exist_ok=True)
            run(["git", "init"], cwd=STAGING)
            run(["git", "remote", "add", "origin", REMOTE_URL], cwd=STAGING)

    # Always set identity in staging dir — never inherit global git config
    run(["git", "config", "user.email", "adekoyaemmanuel15@gmail.com"], cwd=STAGING)
    run(["git", "config", "user.name", "m1r4g3-code"], cwd=STAGING)

    # 3. Wipe existing .md files from staging
    for existing in STAGING.rglob("*.md"):
        if ".git" not in existing.parts:
            existing.unlink()

    # 4. Copy public files preserving structure
    for src in public_files:
        rel = src.relative_to(WIKI)
        dest = STAGING / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        print(f"  + {rel}")

    # 5. Commit and push
    run(["git", "add", "-A"], cwd=STAGING)

    # Check if there are changes to commit
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=STAGING, capture_output=True, text=True
    )
    if not status.stdout.strip():
        print("\nNo changes — public brain is already up to date.")
        return

    run(
        ["git", "commit", "-m", "brain-public: sync public nodes from hephzibah-brain"],
        cwd=STAGING
    )
    run(["git", "push", "-u", "origin", "main", "--force"], cwd=STAGING)
    print(f"\nPushed {len(public_files)} public nodes to hephzibah-brain-public")


if __name__ == "__main__":
    main()
