"""
Hunter.io Lead Finder for SURIOTA
==================================
Script untuk mencari email kontak dari domain perusahaan target
menggunakan Hunter.io API (legal B2B lead generation)

Usage:
    python hunter_lead_finder.py --domain pertamina.com
    python hunter_lead_finder.py --domains domains.txt
    python hunter_lead_finder.py --find "John Doe" --domain company.com
    python hunter_lead_finder.py --verify email@company.com

Author: SURIOTA Sales Team
"""

import requests
import csv
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict
import time

# ============================================
# CONFIGURATION
# ============================================
HUNTER_API_KEY = "aa99858276e102460135bcbe5685a9e9bb42b0e4"
BASE_URL = "https://api.hunter.io/v2"

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================
# HUNTER.IO API FUNCTIONS
# ============================================

def domain_search(domain: str, limit: int = 10) -> Dict:
    """
    Search for all emails associated with a domain.

    Free tier: 25 searches/month
    Returns: company info + list of emails found
    """
    endpoint = f"{BASE_URL}/domain-search"
    params = {
        "domain": domain,
        "api_key": HUNTER_API_KEY,
        "limit": limit
    }

    response = requests.get(endpoint, params=params)
    return response.json()


def email_finder(domain: str, first_name: str = None, last_name: str = None,
                 full_name: str = None) -> Dict:
    """
    Find email address of a specific person at a company.

    Free tier: 25 searches/month
    """
    endpoint = f"{BASE_URL}/email-finder"
    params = {
        "domain": domain,
        "api_key": HUNTER_API_KEY
    }

    if full_name:
        params["full_name"] = full_name
    else:
        if first_name:
            params["first_name"] = first_name
        if last_name:
            params["last_name"] = last_name

    response = requests.get(endpoint, params=params)
    return response.json()


def email_verifier(email: str) -> Dict:
    """
    Verify if an email address is valid and deliverable.

    Free tier: 25 verifications/month
    """
    endpoint = f"{BASE_URL}/email-verifier"
    params = {
        "email": email,
        "api_key": HUNTER_API_KEY
    }

    response = requests.get(endpoint, params=params)
    return response.json()


def get_account_info() -> Dict:
    """
    Get Hunter.io account information and remaining credits.
    """
    endpoint = f"{BASE_URL}/account"
    params = {"api_key": HUNTER_API_KEY}

    response = requests.get(endpoint, params=params)
    return response.json()


# ============================================
# HELPER FUNCTIONS
# ============================================

def print_header():
    """Print script header."""
    print("=" * 60)
    print("  SURIOTA Lead Finder - Hunter.io API")
    print("  Legal B2B Email Discovery Tool")
    print("=" * 60)
    print()


def print_account_status():
    """Print account status and remaining credits."""
    result = get_account_info()

    if "data" in result:
        data = result["data"]
        print("[Account Status]")
        print(f"  Email: {data.get('email', 'N/A')}")
        print(f"  Plan: {data.get('plan_name', 'Free')}")
        print(f"  Searches remaining: {data.get('requests', {}).get('searches', {}).get('available', 0)}")
        print(f"  Verifications remaining: {data.get('requests', {}).get('verifications', {}).get('available', 0)}")
        print()
    else:
        print("[Warning] Could not fetch account info")
        if "errors" in result:
            print(f"  Error: {result['errors']}")
        print()


def process_domain_search(domain: str, verbose: bool = True) -> List[Dict]:
    """
    Process domain search and return structured results.
    """
    if verbose:
        print(f"[Searching] {domain}...")

    result = domain_search(domain)

    if "errors" in result:
        print(f"  [Error] {result['errors']}")
        return []

    data = result.get("data", {})
    emails = data.get("emails", [])

    if verbose:
        print(f"  Company: {data.get('organization', 'Unknown')}")
        print(f"  Industry: {data.get('industry', 'Unknown')}")
        print(f"  Emails found: {len(emails)}")
        print()

    # Structure the results
    leads = []
    for email_data in emails:
        lead = {
            "domain": domain,
            "company": data.get("organization", ""),
            "industry": data.get("industry", ""),
            "email": email_data.get("value", ""),
            "first_name": email_data.get("first_name", ""),
            "last_name": email_data.get("last_name", ""),
            "position": email_data.get("position", ""),
            "department": email_data.get("department", ""),
            "linkedin": email_data.get("linkedin", ""),
            "confidence": email_data.get("confidence", 0),
            "sources": len(email_data.get("sources", []))
        }
        leads.append(lead)

        if verbose:
            confidence_bar = "#" * (lead["confidence"] // 10) + "-" * (10 - lead["confidence"] // 10)
            print(f"    {lead['email']}")
            print(f"      Name: {lead['first_name']} {lead['last_name']}")
            print(f"      Position: {lead['position'] or 'N/A'}")
            print(f"      Confidence: [{confidence_bar}] {lead['confidence']}%")
            print()

    return leads


def save_to_csv(leads: List[Dict], filename: str = None):
    """
    Save leads to CSV file.
    """
    if not leads:
        print("[Warning] No leads to save")
        return

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"leads_{timestamp}.csv"

    filepath = OUTPUT_DIR / filename

    fieldnames = [
        "domain", "company", "industry", "email",
        "first_name", "last_name", "position", "department",
        "linkedin", "confidence", "sources"
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)

    print(f"[Saved] {len(leads)} leads to {filepath}")
    return filepath


def save_to_json(leads: List[Dict], filename: str = None):
    """
    Save leads to JSON file.
    """
    if not leads:
        print("[Warning] No leads to save")
        return

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"leads_{timestamp}.json"

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)

    print(f"[Saved] {len(leads)} leads to {filepath}")
    return filepath


# ============================================
# SURIOTA TARGET DOMAINS
# ============================================

# Contoh domain perusahaan target untuk SURIOTA (IIoT)
SURIOTA_TARGET_DOMAINS = [
    # Manufacturing
    "astra.co.id",
    "unilever.co.id",
    "nestle.co.id",
    "danone.co.id",
    "wings.co.id",

    # Energy & Oil/Gas
    "pertamina.com",
    "pln.co.id",
    "pgn.co.id",
    "medcoenergi.com",

    # Maritime & Logistics
    "pelindo.co.id",
    "samudera.co.id",
    "jne.co.id",
    "sicepat.com",

    # Palm Oil / Plantation
    "sfrn.co.id",    # Wilmar
    "asiatikapla.com",
    "lonsum.com",

    # Water / PDAM
    "jakartaair.co.id",
    "palyja.co.id",

    # Building Management
    "ciputra.com",
    "lippokarawaci.co.id",
    "pakuwon.com",
]


# ============================================
# MAIN CLI
# ============================================

def main():
    parser = argparse.ArgumentParser(
        description="SURIOTA Lead Finder - Hunter.io API Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python hunter_lead_finder.py --domain pertamina.com
  python hunter_lead_finder.py --domains domains.txt
  python hunter_lead_finder.py --find "John Doe" --domain company.com
  python hunter_lead_finder.py --verify email@company.com
  python hunter_lead_finder.py --targets
  python hunter_lead_finder.py --status
        """
    )

    parser.add_argument("--domain", "-d", help="Single domain to search")
    parser.add_argument("--domains", "-D", help="File with list of domains (one per line)")
    parser.add_argument("--find", "-f", help="Find email for specific person (use with --domain)")
    parser.add_argument("--verify", "-v", help="Verify an email address")
    parser.add_argument("--targets", "-t", action="store_true", help="Search SURIOTA target domains")
    parser.add_argument("--status", "-s", action="store_true", help="Show account status")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Max emails per domain (default: 10)")
    parser.add_argument("--output", "-o", help="Output filename (without extension)")
    parser.add_argument("--format", choices=["csv", "json", "both"], default="both", help="Output format")

    args = parser.parse_args()

    print_header()
    print_account_status()

    all_leads = []

    # Status only
    if args.status:
        return

    # Verify email
    if args.verify:
        print(f"[Verifying] {args.verify}...")
        result = email_verifier(args.verify)

        if "data" in result:
            data = result["data"]
            print(f"  Status: {data.get('status', 'unknown')}")
            print(f"  Score: {data.get('score', 0)}")
            print(f"  Deliverable: {'Yes' if data.get('result') == 'deliverable' else 'No'}")
            print(f"  Disposable: {'Yes' if data.get('disposable') else 'No'}")
            print(f"  Webmail: {'Yes' if data.get('webmail') else 'No'}")
        else:
            print(f"  Error: {result.get('errors', 'Unknown error')}")
        return

    # Find specific person
    if args.find and args.domain:
        print(f"[Finding] {args.find} at {args.domain}...")
        result = email_finder(args.domain, full_name=args.find)

        if "data" in result:
            data = result["data"]
            print(f"  Email: {data.get('email', 'Not found')}")
            print(f"  Score: {data.get('score', 0)}")
            print(f"  Position: {data.get('position', 'N/A')}")

            if data.get("email"):
                all_leads.append({
                    "domain": args.domain,
                    "company": data.get("company", ""),
                    "industry": "",
                    "email": data.get("email", ""),
                    "first_name": data.get("first_name", ""),
                    "last_name": data.get("last_name", ""),
                    "position": data.get("position", ""),
                    "department": data.get("department", ""),
                    "linkedin": data.get("linkedin", ""),
                    "confidence": data.get("score", 0),
                    "sources": len(data.get("sources", []))
                })
        else:
            print(f"  Error: {result.get('errors', 'Unknown error')}")

    # Single domain search
    elif args.domain:
        leads = process_domain_search(args.domain)
        all_leads.extend(leads)

    # Multiple domains from file
    elif args.domains:
        domains_file = Path(args.domains)
        if domains_file.exists():
            with open(domains_file, "r") as f:
                domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]

            print(f"[Loaded] {len(domains)} domains from {args.domains}")
            print()

            for i, domain in enumerate(domains, 1):
                print(f"[{i}/{len(domains)}] ", end="")
                leads = process_domain_search(domain, verbose=True)
                all_leads.extend(leads)

                # Rate limiting - Hunter.io allows ~10 req/sec but let's be nice
                if i < len(domains):
                    time.sleep(1)
        else:
            print(f"[Error] File not found: {args.domains}")
            return

    # SURIOTA target domains
    elif args.targets:
        print(f"[Searching] {len(SURIOTA_TARGET_DOMAINS)} SURIOTA target domains")
        print("[Warning] This will use multiple API credits!")
        print()

        confirm = input("Continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return

        for i, domain in enumerate(SURIOTA_TARGET_DOMAINS, 1):
            print(f"[{i}/{len(SURIOTA_TARGET_DOMAINS)}] ", end="")
            leads = process_domain_search(domain, verbose=True)
            all_leads.extend(leads)

            if i < len(SURIOTA_TARGET_DOMAINS):
                time.sleep(1)

    else:
        parser.print_help()
        return

    # Save results
    if all_leads:
        print()
        print("=" * 60)
        print(f"[Summary] Total leads found: {len(all_leads)}")

        output_name = args.output or f"leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        if args.format in ["csv", "both"]:
            save_to_csv(all_leads, f"{output_name}.csv")
        if args.format in ["json", "both"]:
            save_to_json(all_leads, f"{output_name}.json")


if __name__ == "__main__":
    main()
