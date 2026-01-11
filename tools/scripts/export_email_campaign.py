"""
Export Email Campaign Ready Files
=================================
Creates CSV files ready for email tools (Mailchimp, Gmail, etc.)
"""

import json
import csv
from pathlib import Path
from datetime import datetime

# Output directories
TOOLS_DIR = Path(__file__).parent.parent
OUTPUT_DIR = TOOLS_DIR / "output"
DRAFTS_DIR = OUTPUT_DIR / "drafts"
CAMPAIGNS_DIR = OUTPUT_DIR / "campaigns"

def export_to_csv(json_file, csv_file):
    """Convert email drafts JSON to CSV format."""
    with open(json_file, "r", encoding="utf-8") as f:
        drafts = json.load(f)

    # CSV format for email tools
    rows = []
    for draft in drafts:
        rows.append({
            "email": draft.get("to", ""),
            "first_name": draft.get("first_name", ""),
            "last_name": draft.get("last_name", ""),
            "company": draft.get("company", ""),
            "subject": draft.get("subject", ""),
            "body": draft.get("body", "").replace("\n", "<br>")  # HTML line breaks
        })

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print(f"[Exported] {len(rows)} emails to {csv_file}")
    return rows


def create_sample_emails(json_file, sample_file, count=5):
    """Create sample email file for review."""
    with open(json_file, "r", encoding="utf-8") as f:
        drafts = json.load(f)

    with open(sample_file, "w", encoding="utf-8") as f:
        for i, draft in enumerate(drafts[:count], 1):
            f.write("=" * 70 + "\n")
            f.write(f"EMAIL {i}/{count}\n")
            f.write("=" * 70 + "\n")
            f.write(f"To: {draft.get('to', '')}\n")
            f.write(f"Name: {draft.get('first_name', '')} {draft.get('last_name', '')}\n")
            f.write(f"Company: {draft.get('company', '')}\n")
            f.write(f"Subject: {draft.get('subject', '')}\n")
            f.write("-" * 70 + "\n")
            f.write(draft.get("body", "") + "\n\n")

    print(f"[Sample] {count} sample emails saved to {sample_file}")


def main():
    print("=" * 60)
    print("  SURIOTA Email Campaign Exporter")
    print("=" * 60)
    print()

    timestamp = datetime.now().strftime("%Y%m%d")

    # Export each category
    categories = [
        ("email_drafts_compro.json", "CAMPAIGN_COMPRO"),
        ("email_drafts_srt_mgate.json", "CAMPAIGN_SRT_MGATE"),
        ("email_drafts_surge.json", "CAMPAIGN_SURGE"),
        ("email_drafts_sricare.json", "CAMPAIGN_SRICARE"),
    ]

    for json_name, prefix in categories:
        json_file = DRAFTS_DIR / json_name
        if json_file.exists():
            csv_file = CAMPAIGNS_DIR / f"{prefix}_{timestamp}.csv"
            sample_file = CAMPAIGNS_DIR / f"{prefix}_SAMPLES_{timestamp}.txt"

            export_to_csv(json_file, csv_file)
            create_sample_emails(json_file, sample_file)
            print()

    print("=" * 60)
    print("  DONE! Email campaigns ready for sending.")
    print("=" * 60)
    print()
    print("Next steps:")
    print("1. Review *_SAMPLES_*.txt files for email preview")
    print("2. Import *_CAMPAIGN_*.csv to your email tool")
    print("3. Use mail merge for personalized sending")


if __name__ == "__main__":
    main()
