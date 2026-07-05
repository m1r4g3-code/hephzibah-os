"""
Register a Windows Task Scheduler task that runs pull_brain.py automatically.

Usage:
  python scripts/setup_brain_scheduler.py          # register task (runs daily at 9am)
  python scripts/setup_brain_scheduler.py --login  # run at every login instead
  python scripts/setup_brain_scheduler.py --remove # unregister the task

The task runs pull_brain.py in the background. Logs are written to:
  logs/brain_pull.log

Run this once. After that, Windows handles it silently.
"""
import subprocess
import sys
import shutil
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.parent
TASK_NAME = "HephzibahBrainPull"
LOG_FILE = ROOT / "logs" / "brain_pull.log"
PULL_SCRIPT = ROOT / "scripts" / "pull_brain.py"


def find_python() -> str:
    for candidate in ["python", "python3", "py"]:
        path = shutil.which(candidate)
        if path:
            # Verify it's actually Python 3
            result = subprocess.run([path, "--version"], capture_output=True, text=True)
            if result.returncode == 0 and "Python 3" in (result.stdout + result.stderr):
                return path
    raise RuntimeError("Python 3 not found on PATH. Install it or set PATH correctly.")


def remove_task():
    result = subprocess.run(
        ["schtasks", "/delete", "/tn", TASK_NAME, "/f"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        print(f"Task '{TASK_NAME}' removed.")
    else:
        if "cannot find" in result.stderr.lower() or "cannot find" in result.stdout.lower():
            print(f"Task '{TASK_NAME}' not found — nothing to remove.")
        else:
            print(f"ERROR removing task: {result.stderr.strip() or result.stdout.strip()}")
            sys.exit(1)


def register_task(on_login: bool = False):
    python = find_python()
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Build the action: python pull_brain.py >> log 2>&1
    # schtasks /create wraps the action in cmd.exe, so we use cmd /c
    action_cmd = (
        f'cmd /c "{python}" "{PULL_SCRIPT}" >> "{LOG_FILE}" 2>&1'
    )

    if on_login:
        schedule_args = ["/sc", "ONLOGON"]
        trigger_desc = "at every login"
    else:
        schedule_args = ["/sc", "DAILY", "/st", "09:00"]
        trigger_desc = "daily at 09:00"

    result = subprocess.run(
        [
            "schtasks", "/create",
            "/tn", TASK_NAME,
            "/tr", action_cmd,
            *schedule_args,
            "/rl", "HIGHEST",   # run with highest available privileges
            "/f",               # overwrite if exists
        ],
        capture_output=True, text=True
    )

    if result.returncode == 0:
        print(f"Task '{TASK_NAME}' registered — fires {trigger_desc}.")
        print(f"Log: {LOG_FILE}")
        print()
        print("Test it now with:")
        print(f"  schtasks /run /tn {TASK_NAME}")
        print()
        print("View log:")
        print(f"  type \"{LOG_FILE}\"")
    else:
        print(f"ERROR registering task:")
        print(f"  {result.stderr.strip() or result.stdout.strip()}")
        sys.exit(1)


def main():
    if "--remove" in sys.argv:
        remove_task()
        return

    on_login = "--login" in sys.argv
    register_task(on_login=on_login)


if __name__ == "__main__":
    main()
