"""
SURIOTA Lead Manager
====================
Kombinasi tool untuk:
1. Manage leads dari Hunter.io
2. Filter & prioritize berdasarkan SURIOTA products
3. Export ke format email campaign
4. Generate personalized email drafts

Usage:
    python lead_manager.py --analyze leads.csv
    python lead_manager.py --filter-product SRT-MGATE-1210 --input leads.csv
    python lead_manager.py --export-mailchimp --input leads.csv
    python lead_manager.py --generate-emails --input leads.csv --template compro

Author: SURIOTA Sales Team
"""

import csv
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import re

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# ============================================
# SURIOTA PRODUCT MAPPING
# ============================================

# Keywords to identify product relevance
PRODUCT_KEYWORDS = {
    "SRT-MGATE-1210": {
        "titles": [
            "plant manager", "engineering", "automation", "process",
            "maintenance", "technical", "it manager", "technology",
            "operations", "manufacturing", "production", "supply chain"
        ],
        "industries": [
            "manufacturing", "electronics", "automotive", "industrial",
            "semiconductor", "automation", "engineering"
        ],
        "companies": [
            "flex", "jabil", "celestica", "sanmina", "schneider",
            "siemens", "panasonic", "infineon", "venture"
        ]
    },
    "SURGE": {
        "titles": [
            "operations", "fleet", "asset", "facility", "energy",
            "utility", "environmental", "sustainability", "port",
            "marine", "shipping", "vessel", "logistics"
        ],
        "industries": [
            "energy", "oil", "gas", "maritime", "shipping", "port",
            "utility", "water", "power", "logistics"
        ],
        "companies": [
            "pln", "pertamina", "medco", "pelindo", "samudera",
            "pgn", "meratus", "spil"
        ]
    },
    "SRICARE": {
        "titles": [
            "hospital", "medical", "healthcare", "clinical",
            "nursing", "patient", "health", "cmo", "ceo", "director"
        ],
        "industries": [
            "hospital", "healthcare", "medical", "health", "clinic"
        ],
        "companies": [
            "siloam", "mayapada", "mitra keluarga", "rs", "hospital",
            "prodia", "hermina"
        ]
    }
}


# ============================================
# EMAIL TEMPLATES
# ============================================

EMAIL_TEMPLATES = {
    "compro": {
        "subject": "PT Surya Inovasi Prioritas - Industrial IoT Solutions",
        "body": """Dear {first_name},

I hope this email finds you well. I'm reaching out from PT Surya Inovasi Prioritas (SURIOTA), a technology company specializing in Industrial IoT Services and System Integration based in Batam, Indonesia.

We noticed {company} operates in the {industry} sector, and we believe our solutions could help optimize your operations:

- **System Integration** - PLC/SCADA to Cloud connectivity
- **Predictive Maintenance** - Vibration & temperature monitoring
- **Remote Monitoring** - Real-time dashboards & mobile apps
- **Energy Management** - Power monitoring & carbon footprint tracking

We've successfully delivered 55+ projects across Manufacturing, Energy, Maritime, and Logistics sectors.

Would you be open to a brief 15-minute call to discuss how we might help {company}?

Best regards,
SURIOTA Sales Team
PT Surya Inovasi Prioritas
Website: www.suriota.com
Phone: +62 858-3567-2476
"""
    },

    "srt-mgate": {
        "subject": "SRT-MGATE-1210: Industrial Modbus-to-MQTT Gateway",
        "body": """Dear {first_name},

I'm reaching out regarding our SRT-MGATE-1210, an Industrial Modbus-to-MQTT Gateway designed for modern IIoT connectivity.

Key features that set us apart:
- **BLE Mobile Configuration** - Setup via smartphone in 5 minutes
- **WiFi Auto Failover** - Automatic switch from Ethernet to WiFi
- **RTC with Battery Backup** - Accurate timestamps even after power loss
- **Industrial Grade** - Operating temp -40C to +75C

At Rp 2,700,000 (~$169), we're 20-70% more affordable than USR-IOT, BLIIoT, ICP DAS, and Moxa - while offering features they don't have.

Given {company}'s operations, this could streamline your Modbus device connectivity to cloud platforms like AWS, Grafana, or our SURGE Platform.

Would you be interested in a technical demo or product samples?

Best regards,
SURIOTA Technical Sales
PT Surya Inovasi Prioritas
"""
    },

    "surge": {
        "subject": "SURGE Platform - Industrial IoT Monitoring Solution",
        "body": """Dear {first_name},

I wanted to introduce SURGE, our Multi-Tenant SaaS Platform for industrial IoT monitoring.

SURGE offers 3 integrated modules:
- **Water Analytics** - pH, COD, TSS monitoring for IPAL/STP/PDAM
- **Energy Mapping** - kWh, kVA, Power Factor for buildings/factories
- **Vessel Tracking** - GPS, Fuel, RPM for maritime/fleet

Key differentiators:
- **Unlimited locations** in all pricing tiers (unique!)
- **KLHK Compliance** ready for Indonesian environmental reporting
- **70% cheaper** than ThingsBoard
- Starting at just $29/month

Given {company}'s operations in {industry}, I believe SURGE could provide significant value.

Would you be open to a demo? We offer a free trial to get started.

Best regards,
SURIOTA Platform Team
PT Surya Inovasi Prioritas
"""
    },

    "sricare": {
        "subject": "SRICARE - Patient Companion & Home Care App Partnership",
        "body": """Dear {first_name},

I'm reaching out regarding a potential partnership opportunity with SRICARE, our upcoming patient companion and home care mobile application.

SRICARE connects patients with professional Caregivers for:
- **Hospital Companion** - Patient accompaniment during hospitalization
- **Dialysis Support** - Accompaniment for hemodialysis sessions
- **Medical Escort** - Transportation to/from medical appointments
- **Home Care** - Post-surgery and elderly care at home

We're currently seeking hospital partners in Batam for our pilot launch. Partnership benefits include:
- Additional service offering for your patients
- Revenue sharing opportunity
- Enhanced patient care experience

Would {company} be interested in exploring a partnership discussion?

Best regards,
SURIOTA Healthcare Team
PT Surya Inovasi Prioritas
"""
    }
}


# ============================================
# HELPER FUNCTIONS
# ============================================

def load_leads(filepath: str) -> List[Dict]:
    """Load leads from CSV file."""
    leads = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            leads.append(row)
    return leads


def classify_lead(lead: Dict) -> List[str]:
    """
    Classify a lead by relevant SURIOTA products.
    Returns list of product names.
    """
    products = []

    # Get searchable text
    title = (lead.get("position", "") or lead.get("title", "")).lower()
    company = (lead.get("company", "") or lead.get("domain", "")).lower()
    industry = (lead.get("industry", "") or lead.get("company_industry", "")).lower()

    for product, keywords in PRODUCT_KEYWORDS.items():
        score = 0

        # Check title keywords
        for kw in keywords["titles"]:
            if kw in title:
                score += 2
                break

        # Check industry keywords
        for kw in keywords["industries"]:
            if kw in industry:
                score += 1
                break

        # Check company keywords
        for kw in keywords["companies"]:
            if kw in company:
                score += 2
                break

        if score >= 2:
            products.append(product)

    return products if products else ["GENERAL"]


def generate_email(lead: Dict, template_name: str) -> Dict:
    """Generate personalized email from template."""
    template = EMAIL_TEMPLATES.get(template_name, EMAIL_TEMPLATES["compro"])

    # Get lead info with fallbacks
    first_name = lead.get("first_name", "").strip() or "Sir/Madam"
    company = lead.get("company", "") or lead.get("domain", "your company")
    industry = lead.get("industry", "") or lead.get("company_industry", "your industry")

    # Generate email
    subject = template["subject"]
    body = template["body"].format(
        first_name=first_name,
        company=company,
        industry=industry
    )

    return {
        "to": lead.get("email", ""),
        "first_name": first_name,
        "last_name": lead.get("last_name", ""),
        "company": company,
        "subject": subject,
        "body": body
    }


def print_header():
    """Print script header."""
    print("=" * 60)
    print("  SURIOTA Lead Manager")
    print("  Filter, Classify & Export Leads")
    print("=" * 60)
    print()


# ============================================
# MAIN FUNCTIONS
# ============================================

def analyze_leads(filepath: str):
    """Analyze leads and show statistics."""
    leads = load_leads(filepath)

    print(f"[Loaded] {len(leads)} leads from {filepath}")
    print()

    # Classify all leads
    product_counts = {"SRT-MGATE-1210": 0, "SURGE": 0, "SRICARE": 0, "GENERAL": 0}
    company_counts = {}
    has_email = 0

    for lead in leads:
        products = classify_lead(lead)
        for p in products:
            product_counts[p] = product_counts.get(p, 0) + 1

        company = lead.get("company", "Unknown")
        company_counts[company] = company_counts.get(company, 0) + 1

        if lead.get("email"):
            has_email += 1

    # Print stats
    print("[Product Relevance]")
    for product, count in product_counts.items():
        bar = "#" * (count // 2) + "-" * (20 - count // 2)
        print(f"  {product:20} [{bar}] {count}")
    print()

    print("[Companies]")
    sorted_companies = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)
    for company, count in sorted_companies[:10]:
        print(f"  {company}: {count} leads")
    print()

    print("[Email Status]")
    print(f"  With email: {has_email}/{len(leads)} ({has_email*100//len(leads)}%)")
    print()


def filter_by_product(filepath: str, product: str, output: str = None):
    """Filter leads by product relevance."""
    leads = load_leads(filepath)

    filtered = []
    for lead in leads:
        products = classify_lead(lead)
        if product in products or product == "ALL":
            lead["suriota_products"] = ", ".join(products)
            filtered.append(lead)

    print(f"[Filtered] {len(filtered)}/{len(leads)} leads for {product}")

    if filtered:
        if output is None:
            output = f"leads_{product.lower().replace('-', '_')}_{datetime.now().strftime('%Y%m%d')}.csv"

        filepath = OUTPUT_DIR / output

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=filtered[0].keys())
            writer.writeheader()
            writer.writerows(filtered)

        print(f"[Saved] {filepath}")

    return filtered


def export_mailchimp(filepath: str, output: str = None):
    """Export leads to Mailchimp-compatible format."""
    leads = load_leads(filepath)

    # Mailchimp format
    mailchimp_leads = []
    for lead in leads:
        if lead.get("email"):
            mailchimp_leads.append({
                "Email Address": lead.get("email", ""),
                "First Name": lead.get("first_name", ""),
                "Last Name": lead.get("last_name", ""),
                "Company": lead.get("company", ""),
                "Job Title": lead.get("position", "") or lead.get("title", ""),
                "Tags": ", ".join(classify_lead(lead))
            })

    if output is None:
        output = f"mailchimp_export_{datetime.now().strftime('%Y%m%d')}.csv"

    filepath = OUTPUT_DIR / output

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=mailchimp_leads[0].keys())
        writer.writeheader()
        writer.writerows(mailchimp_leads)

    print(f"[Exported] {len(mailchimp_leads)} leads to {filepath}")
    print("[Info] Import to Mailchimp: Audience > Import contacts > Upload CSV")


def generate_email_drafts(filepath: str, template: str, output: str = None):
    """Generate email drafts from leads."""
    leads = load_leads(filepath)

    drafts = []
    for lead in leads:
        if lead.get("email"):
            draft = generate_email(lead, template)
            drafts.append(draft)

    if output is None:
        output = f"email_drafts_{template}_{datetime.now().strftime('%Y%m%d')}.json"

    filepath_out = OUTPUT_DIR / output

    with open(filepath_out, "w", encoding="utf-8") as f:
        json.dump(drafts, f, indent=2, ensure_ascii=False)

    print(f"[Generated] {len(drafts)} email drafts to {filepath_out}")

    # Also create a preview
    if drafts:
        print()
        print("[Preview - First Email]")
        print("-" * 40)
        print(f"To: {drafts[0]['to']}")
        print(f"Subject: {drafts[0]['subject']}")
        print("-" * 40)
        print(drafts[0]['body'][:500] + "...")


# ============================================
# MAIN CLI
# ============================================

def main():
    parser = argparse.ArgumentParser(
        description="SURIOTA Lead Manager - Filter, Classify & Export",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze leads
  python lead_manager.py --analyze output/batam_leads_top10.csv

  # Filter by product
  python lead_manager.py --filter-product SRT-MGATE-1210 --input output/batam_leads_top10.csv
  python lead_manager.py --filter-product SURGE --input output/batam_leads_top10.csv
  python lead_manager.py --filter-product SRICARE --input output/batam_leads_top10.csv

  # Export for Mailchimp
  python lead_manager.py --export-mailchimp --input output/batam_leads_top10.csv

  # Generate email drafts
  python lead_manager.py --generate-emails --input output/batam_leads_top10.csv --template compro
  python lead_manager.py --generate-emails --input output/batam_leads_top10.csv --template srt-mgate
  python lead_manager.py --generate-emails --input output/batam_leads_top10.csv --template surge
  python lead_manager.py --generate-emails --input output/batam_leads_top10.csv --template sricare
        """
    )

    # Actions
    parser.add_argument("--analyze", "-a", action="store_true",
                        help="Analyze leads and show statistics")
    parser.add_argument("--filter-product", "-fp",
                        choices=["SRT-MGATE-1210", "SURGE", "SRICARE", "ALL"],
                        help="Filter leads by product relevance")
    parser.add_argument("--export-mailchimp", "-em", action="store_true",
                        help="Export to Mailchimp format")
    parser.add_argument("--generate-emails", "-ge", action="store_true",
                        help="Generate email drafts")

    # Options
    parser.add_argument("--input", "-i", required=False,
                        help="Input CSV file")
    parser.add_argument("--output", "-o", help="Output filename")
    parser.add_argument("--template", "-t",
                        choices=["compro", "srt-mgate", "surge", "sricare"],
                        default="compro",
                        help="Email template to use")

    args = parser.parse_args()

    print_header()

    if not args.input and (args.analyze or args.filter_product or args.export_mailchimp or args.generate_emails):
        # Try to find most recent leads file
        csv_files = list(OUTPUT_DIR.glob("*.csv"))
        if csv_files:
            args.input = str(max(csv_files, key=lambda x: x.stat().st_mtime))
            print(f"[Auto] Using most recent file: {args.input}")
            print()
        else:
            print("[Error] No input file specified and no CSV files found in output/")
            return

    if args.analyze:
        analyze_leads(args.input)

    elif args.filter_product:
        filter_by_product(args.input, args.filter_product, args.output)

    elif args.export_mailchimp:
        export_mailchimp(args.input, args.output)

    elif args.generate_emails:
        generate_email_drafts(args.input, args.template, args.output)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
