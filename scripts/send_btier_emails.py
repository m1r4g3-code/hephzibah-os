"""
Send the 6 verified B-tier emails.
Removes em dashes from bodies, deletes old drafts, sends clean versions.
"""

import sys
import base64
from pathlib import Path
from email.mime.text import MIMEText

sys.path.insert(0, str(Path(__file__).parent))
from modules.outreach.email_engine import _get_gmail_service

EMAILS = [
    {
        "company": "Texas Direct Medical Care",
        "to": "info@txmedicalcare.com",
        "subject": "your HTTP site",
        "draft_id": "r-7775051730383348980",
        "body": """txmedicalcare.com loads over HTTP. No SSL. Browsers increasingly flag this, and it creates hesitation before a patient even reads your content. On top of that, there is no online booking.

For a 4.8-rated practice, those two gaps are the main things standing between you and more new patients. I fix both in about a week.

15 minutes. Worth it for Texas Direct?

Emmanuel""",
    },
    {
        "company": "Balcones Psychiatry and Mental Health",
        "to": "admin@balconespsych.com",
        "subject": "your 3.2 rating",
        "draft_id": "r-771762307611078405",
        "body": """58 reviews and a 3.2 rating is a difficult spot. That is enough volume that patients trust the score, but the score is not working in your favor.

Most sub-4 ratings for psychiatric practices trace to admin friction, not clinical care. Booking confusion, long holds, no online scheduling. I build systems that fix the admin layer.

Would 15 minutes to walk through what that looks like for Balcones be worth it?

Emmanuel""",
    },
    {
        "company": "Clinic Concierge Austin",
        "to": "hello@clinicconcierge.com",
        "subject": "5 stars, no booking",
        "body": """Clinic Concierge has a 5.0 rating. That is rare in Austin. The one gap I noticed: there is no online booking on your site.

For a practice with that reputation, every patient who cannot book online is either calling instead or finding someone who has it. I build booking automation for clinics, usually live in a week.

Would it be worth 15 minutes?

Emmanuel""",
        "draft_id": "r786740146281061699",
    },
    {
        "company": "Hope Medical Clinic",
        "to": "guptexas@gmail.com",
        "subject": "your site timed out",
        "draft_id": "r-4574947188411264977",
        "body": """I tried to reach hopeclinicaustin.org earlier. It timed out. For a 4.8-rated clinic, that is patients who found you on Google hitting a dead end before they could book.

The site also loads on HTTP, which browsers sometimes flag. I build medical practice sites that are fast, secure, and include online booking.

15 minutes. Would it be worth it for Hope Medical?

Emmanuel""",
    },
    {
        "company": "RiverRock Medical Clinic",
        "to": "sales@riverrockmedical.com",
        "subject": "5.0, only 5 reviews",
        "draft_id": "r6216791631333441615",
        "body": """RiverRock has a perfect 5.0 rating. Only 5 people know about it though. A clinic that good should have 200 reviews, not 5.

Most of that gap is mechanical: no review prompts after visits, no booking system to get more patients through consistently. I build systems that fix both.

Would 15 minutes to walk through what that looks like for RiverRock be worth it?

Emmanuel""",
    },
    {
        "company": "Your Functional Health by Xenia Kempf",
        "to": "xenia@yourfunctionalmednp.com",
        "subject": "9 reviews, 4.8 stars",
        "draft_id": "r9094581554085365528",
        "body": """Your Functional Health has a 4.8 rating. Only 9 patients have reviewed it, but all of them loved it. That is a signal worth building on.

The main gap is discoverability and conversion: patients who find you cannot book online, and the low review count means Google ranks you below less-qualified practices. I help functional medicine practices fix both.

15 minutes. Is it worth it?

Emmanuel""",
    },
]


def build_message(to: str, subject: str, body: str) -> dict:
    msg = MIMEText(body)
    msg["to"] = to
    msg["subject"] = subject
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    return {"raw": raw}


def main():
    service = _get_gmail_service()

    print("\nSending 6 B-tier cold emails\n")

    for e in EMAILS:
        # Delete old draft
        try:
            service.users().drafts().delete(userId="me", id=e["draft_id"]).execute()
        except Exception:
            pass  # already gone or not found

        # Send
        try:
            message = build_message(e["to"], e["subject"], e["body"])
            service.users().messages().send(userId="me", body=message).execute()
            print(f"  SENT: {e['company']}")
            print(f"        To: {e['to']}")
            print(f"        Subject: {e['subject']}\n")
        except Exception as ex:
            print(f"  FAILED: {e['company']} -- {ex}\n")

    print("Done.")


if __name__ == "__main__":
    main()
