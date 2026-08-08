"""
Email engine — creates Gmail drafts from generated email content.

The operator reviews the draft in Gmail and clicks Send.
No email is ever sent automatically.

Usage (called by Claude Code after /write-email generates content):
    python email_engine.py --company "Zamora Medical Center" \
                           --to "contact@zamora.com" \
                           --subject "your intake process" \
                           --body "..." \
                           --type cold

Setup (one-time):
    1. Go to console.cloud.google.com
    2. Create project → Enable Gmail API
    3. Credentials → OAuth 2.0 Client ID → Desktop App → Download JSON
    4. Save as credentials.json in the vault root
    5. First run opens browser for authorization — approve once
    6. Token saved to .gmail_token.json (gitignored) — never needed again

Output:
    drafts/<company-slug>_<date>_<type>.md  (always written)
    Gmail draft (if credentials.json exists)
    logs/_email_context.json
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from email.mime.text import MIMEText
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from lib.logger import EngineLogger
from lib.schemas import EmailDraft
from lib.utils import VAULT_ROOT, LOGS_DIR, now_iso, slugify
from lib.vault import write_email_draft

CREDENTIALS_PATH = VAULT_ROOT / "credentials.json"
TOKEN_PATH = VAULT_ROOT / ".gmail_token.json"

SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


# ── GMAIL AUTH ────────────────────────────────────────────────────────────────

def _get_gmail_service():
    """Return an authenticated Gmail API service, or None if not configured."""
    if not CREDENTIALS_PATH.exists():
        return None

    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        return None

    creds = None
    if TOKEN_PATH.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_PATH), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_PATH), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_PATH.write_text(creds.to_json(), encoding="utf-8")

    return build("gmail", "v1", credentials=creds)


# ── DRAFT CREATION ────────────────────────────────────────────────────────────

def _build_mime(to: str, subject: str, body: str, html: bool = False) -> str:
    """Build a base64url-encoded MIME message."""
    msg = MIMEText(body, "html" if html else "plain")
    msg["to"] = to
    msg["subject"] = subject
    return base64.urlsafe_b64encode(msg.as_bytes()).decode()


def create_gmail_draft(
    to: str,
    subject: str,
    body: str,
    html: bool = False,
) -> tuple[str | None, str | None]:
    """
    Create a Gmail draft. Returns (draft_id, draft_url) or (None, None).
    Falls back silently if Gmail is not configured.
    """
    service = _get_gmail_service()
    if not service:
        return None, None

    try:
        raw = _build_mime(to, subject, body, html=html)
        result = service.users().drafts().create(
            userId="me",
            body={"message": {"raw": raw}},
        ).execute()
        draft_id = result.get("id")
        draft_url = f"https://mail.google.com/mail/#drafts/{draft_id}" if draft_id else None
        return draft_id, draft_url
    except Exception as e:
        print(f"  Warning: Gmail draft creation failed — {e}")
        return None, None


# ── MAIN ──────────────────────────────────────────────────────────────────────

def run(
    company: str,
    to_email: str,
    subject: str,
    body: str,
    email_type: str = "cold",
    html: bool = False,
) -> EmailDraft:
    logger = EngineLogger("email_engine")
    logger.start()

    # Create Gmail draft (silently skips if not configured)
    gmail_id, gmail_url = create_gmail_draft(to_email, subject, body, html=html)

    draft = EmailDraft(
        company_name=company,
        to_email=to_email,
        subject=subject,
        body=body,
        email_type=email_type,
        created_at=now_iso(),
        gmail_draft_id=gmail_id,
        gmail_draft_url=gmail_url,
    )

    # Save draft markdown (always)
    draft_path = write_email_draft(draft)

    # Write context for Claude Code
    context = {
        "company": company,
        "to": to_email,
        "subject": subject,
        "email_type": email_type,
        "draft_file": str(draft_path),
        "gmail_draft_id": gmail_id,
        "gmail_draft_url": gmail_url,
        "gmail_configured": CREDENTIALS_PATH.exists(),
        "generated_at": now_iso(),
    }
    LOGS_DIR.mkdir(exist_ok=True)
    (LOGS_DIR / "_email_context.json").write_text(
        json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    logger.finish(items_processed=1, output_path=str(draft_path))
    return draft


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    from rich.console import Console

    console = Console()

    parser = argparse.ArgumentParser(description="Create a Gmail draft from generated email content")
    parser.add_argument("--company", required=True)
    parser.add_argument("--to", required=True, dest="to_email")
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--type", default="cold", dest="email_type",
                        choices=["cold", "follow-up", "sequence"])
    parser.add_argument("--html", action="store_true", help="Send body as HTML instead of plain text")
    args = parser.parse_args()

    console.print(f"\n[bold]Email Engine[/bold] — {args.email_type} email for {args.company}")
    console.print(f"  To:      [cyan]{args.to_email}[/cyan]")
    console.print(f"  Subject: [cyan]{args.subject}[/cyan]")

    draft = run(
        company=args.company,
        to_email=args.to_email,
        subject=args.subject,
        body=args.body,
        email_type=args.email_type,
        html=args.html,
    )

    slug = slugify(args.company)
    draft_path = VAULT_ROOT / "drafts" / f"{slug}_{draft.created_at[:10]}_{args.email_type}.md"

    if draft.gmail_draft_url:
        console.print(f"\n  [bold green]Gmail draft created[/bold green]")
        console.print(f"  Review + send: [cyan]{draft.gmail_draft_url}[/cyan]")
    elif CREDENTIALS_PATH.exists():
        console.print(f"\n  [yellow]Gmail draft failed — check credentials.json[/yellow]")
    else:
        console.print(f"\n  [yellow]Gmail not configured — draft saved locally only[/yellow]")
        console.print(f"  Setup: see README.md -> Email Funnel Setup")

    console.print(f"\n  Draft file: [cyan]{draft_path.name}[/cyan]")
    console.print(f"  Review in Obsidian or VS Code before sending.")
