"""
One-time Gmail authorization.

Run this after placing credentials.json in the vault root:
    python scripts/gmail_setup.py

Opens a browser window for Google login. Approve once.
Token saved to .gmail_token.json — never needed again.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.utils import VAULT_ROOT

CREDENTIALS_PATH = VAULT_ROOT / "credentials.json"
TOKEN_PATH = VAULT_ROOT / ".gmail_token.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


def main():
    from rich.console import Console
    console = Console()

    if not CREDENTIALS_PATH.exists():
        console.print("\n[red]credentials.json not found.[/red]")
        console.print(f"  Expected at: [cyan]{CREDENTIALS_PATH}[/cyan]")
        console.print("\n  Steps:")
        console.print("  1. Go to console.cloud.google.com")
        console.print("  2. Create project -> Enable Gmail API")
        console.print("  3. Credentials -> OAuth 2.0 Client ID -> Desktop App -> Download JSON")
        console.print("  4. Rename to credentials.json and drop it in the vault root")
        console.print("  5. Re-run this script")
        sys.exit(1)

    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        console.print("\n[red]Missing Google libraries.[/red] Run:")
        console.print("  [cyan]pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client[/cyan]")
        sys.exit(1)

    console.print("\n[bold]Gmail Setup[/bold] — authorizing draft access")

    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if creds and creds.valid:
        console.print("[green]Already authorized.[/green] Gmail drafts are ready.")
        console.print(f"  Token file: [cyan]{TOKEN_PATH.name}[/cyan]")
        return

    if creds and creds.expired and creds.refresh_token:
        console.print("  Refreshing expired token...")
        creds.refresh(Request())
    else:
        console.print("  Opening browser for Google login...")
        console.print("  [yellow]Approve 'Create and manage your drafts'[/yellow]")
        flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
        creds = flow.run_local_server(port=0)

    TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")

    console.print("\n[bold green]Authorization complete.[/bold green]")
    console.print(f"  Token saved to [cyan]{TOKEN_PATH.name}[/cyan]")
    console.print("  Gmail drafts are now live. Run [cyan]/write-email[/cyan] and the draft lands in your Gmail.")


if __name__ == "__main__":
    main()
