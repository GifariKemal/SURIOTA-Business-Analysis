"""
Generate Email Campaign for Medium Company - Company Profile
=============================================================
Target: Perusahaan menengah di Batam (EPC, Fabrication, Engineering, Manufacturing)
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

# Email Template for Medium Company - Company Profile (B2B Partnership)
EMAIL_TEMPLATE = {
    "subject": "Solusi Industrial IoT untuk {company} - SURIOTA",
    "subject_en": "Industrial IoT Solutions for {company} - SURIOTA",
    "body_id": """Kepada Yth. {name},
{position_line}
Salam hangat dari PT Surya Inovasi Prioritas (SURIOTA).

Kami adalah perusahaan teknologi yang bergerak di bidang Industrial IoT Services dan System Integration berbasis di Batam. Melihat {company} sebagai perusahaan terkemuka di bidang {industry}, kami yakin ada peluang kolaborasi yang dapat saling menguntungkan.

**Layanan Kami yang Relevan untuk Industri Anda:**

1. **System Integration** - Koneksi PLC/SCADA ke Cloud, Modbus ke MQTT
2. **Predictive Maintenance** - Monitoring vibrasi & suhu untuk mencegah downtime
3. **Remote Monitoring Dashboard** - Real-time monitoring via web & mobile app
4. **Energy Management System** - Monitoring konsumsi listrik & carbon footprint
5. **Custom IoT Development** - Solusi custom sesuai kebutuhan operasional

**Produk Unggulan:**
- **SRT-MGATE-1210** - Industrial Modbus-to-MQTT Gateway (Rp 2.7jt)
- **SURGE Platform** - Multi-tenant IoT Monitoring SaaS (mulai $29/bulan)

**Track Record:**
- 55+ proyek sukses di sektor Manufacturing, Energy, Maritime, dan Logistics
- Klien: Industrial parks, Water utilities, Energy companies

Apakah Bapak/Ibu berkenan untuk meeting singkat (15-20 menit) via Zoom atau kunjungan ke kantor untuk diskusi lebih lanjut tentang kebutuhan {company}?

Hormat kami,

Tim SURIOTA
PT Surya Inovasi Prioritas
Website: www.suriota.com
WhatsApp: +62 858-3567-2476
Email: sales@suriota.com
""",
    "body_en": """Dear {name},
{position_line}
Warm greetings from PT Surya Inovasi Prioritas (SURIOTA).

We are a technology company specializing in Industrial IoT Services and System Integration based in Batam. Recognizing {company} as a leading company in {industry}, we believe there are mutually beneficial collaboration opportunities.

**Our Services Relevant to Your Industry:**

1. **System Integration** - PLC/SCADA to Cloud, Modbus to MQTT connectivity
2. **Predictive Maintenance** - Vibration & temperature monitoring to prevent downtime
3. **Remote Monitoring Dashboard** - Real-time monitoring via web & mobile app
4. **Energy Management System** - Power consumption & carbon footprint tracking
5. **Custom IoT Development** - Tailored solutions for your operational needs

**Key Products:**
- **SRT-MGATE-1210** - Industrial Modbus-to-MQTT Gateway (~$169)
- **SURGE Platform** - Multi-tenant IoT Monitoring SaaS (from $29/month)

**Track Record:**
- 55+ successful projects in Manufacturing, Energy, Maritime, and Logistics
- Clients: Industrial parks, Water utilities, Energy companies

Would you be available for a brief meeting (15-20 minutes) via Zoom or an office visit to discuss {company}'s specific needs?

Best regards,

SURIOTA Team
PT Surya Inovasi Prioritas
Website: www.suriota.com
WhatsApp: +62 858-3567-2476
Email: sales@suriota.com
"""
}


def main():
    # Load leads
    leads_path = LEADS_DIR / "MEDIUM_COMPANY_BATAM_COMPRO.json"

    with open(leads_path, "r", encoding="utf-8") as f:
        leads = json.load(f)

    print(f"[Loaded] {len(leads)} leads from {leads_path}")

    # Generate email campaign
    campaign_rows = []
    seen_emails = set()

    for lead in leads:
        # Skip if no email or duplicate
        email = lead.get("email", "")
        if not email or "@" not in email:
            continue
        if email in seen_emails:
            continue
        seen_emails.add(email)

        name = lead.get("name", "Bapak/Ibu")
        company = lead.get("company", "perusahaan Anda")
        industry = lead.get("industry", "industri Anda")
        phone = lead.get("phone", "")
        position = lead.get("position", "")

        # Create position line if available
        position_line = f"({position})\n" if position and position not in ["Sales", "Contact", "Admin", "Support", "Contact Person", "Sales Team", "Info Team", "Admin Team"] else ""

        # Generate personalized email
        subject = EMAIL_TEMPLATE["subject"].format(company=company)
        body_id = EMAIL_TEMPLATE["body_id"].format(
            name=name,
            company=company,
            industry=industry,
            position_line=position_line
        )
        body_en = EMAIL_TEMPLATE["body_en"].format(
            name=name,
            company=company,
            industry=industry,
            position_line=position_line
        )

        campaign_rows.append({
            "email": email,
            "name": name,
            "company": company,
            "position": position,
            "industry": industry,
            "phone": phone,
            "category": lead.get("category", ""),
            "city": lead.get("city", "Batam"),
            "subject": subject,
            "body_id": body_id,
            "body_en": body_en,
            "confidence": lead.get("confidence", ""),
            "source": lead.get("source", "")
        })

    print(f"[Generated] {len(campaign_rows)} email campaigns (deduplicated)")

    # Save to CSV
    timestamp = datetime.now().strftime("%Y%m%d")
    csv_path = CAMPAIGNS_DIR / f"EMAIL_CAMPAIGN_MEDIUM_COMPRO_{timestamp}.csv"

    if campaign_rows:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campaign_rows[0].keys())
            writer.writeheader()
            writer.writerows(campaign_rows)

        print(f"[Saved] {csv_path}")

    # Also save JSON version
    json_path = CAMPAIGNS_DIR / f"EMAIL_CAMPAIGN_MEDIUM_COMPRO_{timestamp}.json"
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
        print(campaign_rows[0]['body_id'][:1000])
        print("...")

    # Summary
    print("\n" + "="*60)
    print("[Summary]")
    print("="*60)
    print(f"Total leads: {len(leads)}")
    print(f"Valid emails (deduplicated): {len(campaign_rows)}")
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

    # Company breakdown
    companies = {}
    for row in campaign_rows:
        comp = row.get("company", "Unknown")
        companies[comp] = companies.get(comp, 0) + 1

    print("\n[By Company]")
    for comp, count in sorted(companies.items(), key=lambda x: -x[1]):
        print(f"  {comp}: {count}")


if __name__ == "__main__":
    main()
