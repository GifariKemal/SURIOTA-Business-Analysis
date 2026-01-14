"""
Generate Email Campaign for Micro Company - Company Profile
============================================================
Target: Micro company di Batam (Tech, Digital Marketing, Creative)
"""

import json
import csv
from pathlib import Path
from datetime import datetime

# Paths
TOOLS_DIR = Path(__file__).parent.parent
OUTPUT_DIR = TOOLS_DIR / "output"
LEADS_DIR = OUTPUT_DIR / "leads"
CAMPAIGNS_DIR = OUTPUT_DIR / "campaigns"

# Email Template for Micro Company - Company Profile
EMAIL_TEMPLATE = {
    "subject": "Kolaborasi Teknologi IoT - SURIOTA x {company}",
    "subject_en": "IoT Technology Partnership - SURIOTA x {company}",
    "body_id": """Halo {name},

Saya ingin memperkenalkan PT Surya Inovasi Prioritas (SURIOTA), perusahaan teknologi yang bergerak di bidang Industrial IoT Services dan System Integration yang berbasis di Batam.

Kami melihat {company} aktif di bidang {industry}, dan kami percaya ada peluang kolaborasi yang menarik:

**Layanan Kami:**
- System Integration (PLC/SCADA to Cloud, Modbus to MQTT)
- Remote Monitoring & Dashboard
- Predictive Maintenance Solutions
- Energy Management System
- Custom IoT Development

**Portfolio:**
- 55+ proyek sukses di sektor Manufacturing, Energy, Maritime, dan Logistics
- Klien: Industrial parks, Water utilities, Energy companies
- Produk sendiri: SRT-MGATE-1210 Gateway, SURGE Platform

Apakah {company} tertarik untuk berdiskusi tentang potensi kolaborasi atau referral partnership?

Kami juga terbuka untuk project collaboration di bidang IoT/embedded system.

Salam,
Tim SURIOTA
PT Surya Inovasi Prioritas
Web: www.suriota.com
WA: +62 858-3567-2476
""",
    "body_en": """Hi {name},

I'd like to introduce PT Surya Inovasi Prioritas (SURIOTA), a technology company specializing in Industrial IoT Services and System Integration based in Batam.

We noticed {company} is active in {industry}, and we believe there's an exciting collaboration opportunity:

**Our Services:**
- System Integration (PLC/SCADA to Cloud, Modbus to MQTT)
- Remote Monitoring & Dashboard
- Predictive Maintenance Solutions
- Energy Management System
- Custom IoT Development

**Portfolio:**
- 55+ successful projects in Manufacturing, Energy, Maritime, and Logistics sectors
- Clients: Industrial parks, Water utilities, Energy companies
- Our own products: SRT-MGATE-1210 Gateway, SURGE Platform

Would {company} be interested in discussing potential collaboration or referral partnership?

We're also open to project collaboration in IoT/embedded systems.

Best regards,
SURIOTA Team
PT Surya Inovasi Prioritas
Web: www.suriota.com
WA: +62 858-3567-2476
"""
}


def main():
    # Load leads
    leads_path = LEADS_DIR / "MICRO_COMPANY_BATAM_COMPRO.json"

    with open(leads_path, "r", encoding="utf-8") as f:
        leads = json.load(f)

    print(f"[Loaded] {len(leads)} leads from {leads_path}")

    # Generate email campaign
    campaign_rows = []

    for lead in leads:
        # Skip if no email
        email = lead.get("email", "")
        if not email or "@" not in email:
            continue

        name = lead.get("name", "Sir/Madam")
        company = lead.get("company", "your company")
        industry = lead.get("industry", "your industry")
        phone = lead.get("phone", "")

        # Generate personalized email
        subject = EMAIL_TEMPLATE["subject"].format(company=company)
        body_id = EMAIL_TEMPLATE["body_id"].format(
            name=name,
            company=company,
            industry=industry
        )
        body_en = EMAIL_TEMPLATE["body_en"].format(
            name=name,
            company=company,
            industry=industry
        )

        campaign_rows.append({
            "email": email,
            "name": name,
            "company": company,
            "industry": industry,
            "phone": phone,
            "category": lead.get("category", ""),
            "city": lead.get("city", "Batam"),
            "subject": subject,
            "body_id": body_id,
            "body_en": body_en,
            "source": lead.get("source", "")
        })

    print(f"[Generated] {len(campaign_rows)} email campaigns")

    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d")
    csv_path = CAMPAIGNS_DIR / f"EMAIL_CAMPAIGN_MICRO_COMPRO_{timestamp}.csv"

    if campaign_rows:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campaign_rows[0].keys())
            writer.writeheader()
            writer.writerows(campaign_rows)

        print(f"[Saved] {csv_path}")

    # Also save JSON version
    json_path = CAMPAIGNS_DIR / f"EMAIL_CAMPAIGN_MICRO_COMPRO_{timestamp}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(campaign_rows, f, indent=2, ensure_ascii=False)

    print(f"[Saved] {json_path}")

    # Print preview
    if campaign_rows:
        print("\n" + "="*60)
        print("[Preview - First Email]")
        print("="*60)
        print(f"To: {campaign_rows[0]['email']}")
        print(f"Subject: {campaign_rows[0]['subject']}")
        print("-"*60)
        print(campaign_rows[0]['body_id'][:800])
        print("...")

    # Summary
    print("\n" + "="*60)
    print("[Summary]")
    print("="*60)
    print(f"Total leads: {len(leads)}")
    print(f"Valid emails: {len(campaign_rows)}")
    print(f"Output CSV: {csv_path}")
    print(f"Output JSON: {json_path}")

    # Category breakdown
    categories = {}
    for row in campaign_rows:
        cat = row.get("category", "Unknown")
        categories[cat] = categories.get(cat, 0) + 1

    print("\n[By Category]")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
