"""
Merge and Analyze All SURIOTA Leads
===================================
Combines all batch CSV files and provides analysis.
"""

import csv
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Output directories
TOOLS_DIR = Path(__file__).parent.parent
OUTPUT_DIR = TOOLS_DIR / "output"
LEADS_DIR = OUTPUT_DIR / "leads"

def merge_csv_files(file_patterns):
    """Merge multiple CSV files into one."""
    all_leads = []
    seen_emails = set()

    for pattern in file_patterns:
        for filepath in OUTPUT_DIR.glob(pattern):
            print(f"[Loading] {filepath.name}")
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    email = row.get("email", "").lower()
                    if email and email not in seen_emails:
                        seen_emails.add(email)
                        all_leads.append(row)

    return all_leads


def classify_lead(lead):
    """Classify lead by SURIOTA product relevance."""
    products = []

    company = (lead.get("company", "") or lead.get("domain", "")).lower()
    position = (lead.get("position", "") or lead.get("title", "")).lower()
    industry = lead.get("industry", "").lower()

    # SRT-MGATE-1210 (Industrial IoT Gateway)
    srt_keywords = ["manufacturing", "plant", "engineering", "automation", "process",
                    "maintenance", "technical", "it ", "technology", "production",
                    "operations", "factory", "industrial", "quality"]
    srt_companies = ["infineon", "panasonic", "excelitas", "sanmina", "dynacast",
                     "yokohama", "flex", "jabil", "celestica", "schneider"]

    if any(kw in position for kw in srt_keywords) or any(c in company for c in srt_companies):
        products.append("SRT-MGATE-1210")

    # SURGE Platform (Energy/Water/Vessel)
    surge_keywords = ["energy", "power", "utility", "water", "marine", "vessel",
                      "fleet", "port", "offshore", "oil", "gas", "environmental",
                      "asset", "facility", "hse", "safety"]
    surge_companies = ["pln", "pertamina", "medco", "harbour", "tenaris", "nov",
                       "citra tubindo", "timas", "thiess", "pelindo", "samudera",
                       "spliethoff", "marco polo", "solar", "bredero"]

    if any(kw in position for kw in surge_keywords) or any(c in company for c in surge_companies):
        products.append("SURGE")

    # SRICARE (Healthcare)
    sricare_keywords = ["hospital", "medical", "healthcare", "clinical", "nursing",
                        "patient", "health", "cmo", "doctor", "nurse"]
    sricare_companies = ["siloam", "mayapada", "awal bros", "rs ", "hospital",
                         "prodia", "hermina", "mitra keluarga"]

    if any(kw in position for kw in sricare_keywords) or any(c in company for c in sricare_companies):
        products.append("SRICARE")

    return products if products else ["GENERAL"]


def main():
    print("=" * 60)
    print("  SURIOTA Lead Merger & Analyzer")
    print("=" * 60)
    print()

    # Merge all batch files
    patterns = [
        "batam_oilgas_energy.csv",
        "batam_manufacturing.csv",
        "batam_healthcare_utilities.csv",
        "batam_leads_top10.csv"
    ]

    all_leads = merge_csv_files(patterns)
    print()
    print(f"[Total Unique Leads] {len(all_leads)}")
    print()

    # Classify leads
    product_leads = defaultdict(list)
    company_counts = defaultdict(int)

    for lead in all_leads:
        products = classify_lead(lead)
        lead["suriota_products"] = ", ".join(products)

        for product in products:
            product_leads[product].append(lead)

        company = lead.get("company", "Unknown")
        company_counts[company] += 1

    # Print statistics
    print("[Product Classification]")
    for product in ["SRT-MGATE-1210", "SURGE", "SRICARE", "GENERAL"]:
        count = len(product_leads[product])
        bar = "#" * (count // 5) + "-" * (20 - count // 5)
        print(f"  {product:20} [{bar}] {count}")
    print()

    print("[Top 15 Companies]")
    sorted_companies = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    for company, count in sorted_companies:
        print(f"  {company[:40]:40} {count} leads")
    print()

    # Count leads with email
    with_email = sum(1 for l in all_leads if l.get("email"))
    print(f"[Email Coverage] {with_email}/{len(all_leads)} ({with_email*100//len(all_leads)}%)")
    print()

    # Save merged file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # All leads
    all_filepath = OUTPUT_DIR / f"ALL_BATAM_LEADS_{timestamp}.csv"
    if all_leads:
        fieldnames = list(all_leads[0].keys())
        if "suriota_products" not in fieldnames:
            fieldnames.append("suriota_products")

        with open(all_filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_leads)
        print(f"[Saved] All leads: {all_filepath}")

    # Save JSON
    json_filepath = OUTPUT_DIR / f"ALL_BATAM_LEADS_{timestamp}.json"
    with open(json_filepath, "w", encoding="utf-8") as f:
        json.dump(all_leads, f, indent=2, ensure_ascii=False)
    print(f"[Saved] JSON: {json_filepath}")

    # Save per-product files
    for product in ["SRT-MGATE-1210", "SURGE", "SRICARE"]:
        leads = product_leads[product]
        if leads:
            product_name = product.lower().replace("-", "_")
            filepath = OUTPUT_DIR / f"LEADS_{product_name}_{timestamp}.csv"
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(leads)
            print(f"[Saved] {product}: {filepath} ({len(leads)} leads)")

    # Mailchimp export
    mailchimp_leads = []
    for lead in all_leads:
        if lead.get("email"):
            mailchimp_leads.append({
                "Email Address": lead.get("email", ""),
                "First Name": lead.get("first_name", ""),
                "Last Name": lead.get("last_name", ""),
                "Company": lead.get("company", ""),
                "Job Title": lead.get("position", "") or lead.get("title", ""),
                "Tags": lead.get("suriota_products", "")
            })

    mailchimp_filepath = OUTPUT_DIR / f"MAILCHIMP_EXPORT_{timestamp}.csv"
    with open(mailchimp_filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=mailchimp_leads[0].keys())
        writer.writeheader()
        writer.writerows(mailchimp_leads)
    print(f"[Saved] Mailchimp: {mailchimp_filepath}")

    print()
    print("=" * 60)
    print("  DONE! All leads compiled and ready for outreach.")
    print("=" * 60)


if __name__ == "__main__":
    main()
