"""
Apollo.io Lead Finder for SURIOTA
==================================
Script untuk mencari leads B2B dengan filter advanced:
- Location (Indonesia, Batam, etc.)
- Job Title (Director, Manager, VP, etc.)
- Industry (Manufacturing, Energy, Healthcare, etc.)

Apollo.io lebih powerful dari Hunter.io untuk targeted prospecting.

Usage:
    python apollo_lead_finder.py --search-people --title "Plant Manager" --location "Indonesia"
    python apollo_lead_finder.py --search-people --title "IT Director" --industry "Hospital"
    python apollo_lead_finder.py --search-org --name "Pertamina"
    python apollo_lead_finder.py --enrich --email "john@company.com"
    python apollo_lead_finder.py --suriota-targets

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
APOLLO_API_KEY = "oWZ4vFQCjQ_2zj3o6PNIuw"
BASE_URL = "https://api.apollo.io/v1"

# Output directory
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Headers for API requests
HEADERS = {
    "Content-Type": "application/json",
    "Cache-Control": "no-cache",
    "X-Api-Key": APOLLO_API_KEY
}


# ============================================
# APOLLO.IO API FUNCTIONS
# ============================================

def search_people(
    titles: List[str] = None,
    locations: List[str] = None,
    industries: List[str] = None,
    keywords: List[str] = None,
    company_names: List[str] = None,
    per_page: int = 25,
    page: int = 1
) -> Dict:
    """
    Search for people/contacts with advanced filters.

    This is the main prospecting endpoint.
    """
    endpoint = f"{BASE_URL}/mixed_people/search"

    payload = {
        "per_page": per_page,
        "page": page
    }

    # Add filters
    if titles:
        payload["person_titles"] = titles

    if locations:
        payload["person_locations"] = locations

    if industries:
        payload["organization_industry_tag_ids"] = industries

    if keywords:
        payload["q_keywords"] = " ".join(keywords)

    if company_names:
        payload["q_organization_name"] = " OR ".join(company_names)

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()


def search_organizations(
    name: str = None,
    locations: List[str] = None,
    industries: List[str] = None,
    per_page: int = 25,
    page: int = 1
) -> Dict:
    """
    Search for organizations/companies.
    """
    endpoint = f"{BASE_URL}/mixed_companies/search"

    payload = {
                "per_page": per_page,
        "page": page
    }

    if name:
        payload["q_organization_name"] = name

    if locations:
        payload["organization_locations"] = locations

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()


def enrich_person(email: str = None, first_name: str = None,
                  last_name: str = None, domain: str = None) -> Dict:
    """
    Enrich a person's data with email or name + domain.
    """
    endpoint = f"{BASE_URL}/people/match"

    payload = {
        "api_key": APOLLO_API_KEY
    }

    if email:
        payload["email"] = email
    else:
        if first_name:
            payload["first_name"] = first_name
        if last_name:
            payload["last_name"] = last_name
        if domain:
            payload["organization_domain"] = domain

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()


def enrich_organization(domain: str) -> Dict:
    """
    Enrich organization data by domain.
    """
    endpoint = f"{BASE_URL}/organizations/enrich"

    payload = {
                "domain": domain
    }

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()


def get_email_status(email: str) -> Dict:
    """
    Check email deliverability status.
    """
    endpoint = f"{BASE_URL}/email_verification"

    payload = {
                "email": email
    }

    response = requests.post(endpoint, headers=HEADERS, json=payload)
    return response.json()


# ============================================
# HELPER FUNCTIONS
# ============================================

def print_header():
    """Print script header."""
    print("=" * 60)
    print("  SURIOTA Lead Finder - Apollo.io API")
    print("  Advanced B2B Prospecting Tool")
    print("=" * 60)
    print()


def process_people_results(data: Dict, verbose: bool = True) -> List[Dict]:
    """
    Process and structure people search results.
    """
    people = data.get("people", [])
    leads = []

    for person in people:
        org = person.get("organization", {}) or {}

        lead = {
            "first_name": person.get("first_name", ""),
            "last_name": person.get("last_name", ""),
            "email": person.get("email", ""),
            "title": person.get("title", ""),
            "linkedin": person.get("linkedin_url", ""),
            "phone": person.get("phone_numbers", [{}])[0].get("number", "") if person.get("phone_numbers") else "",
            "city": person.get("city", ""),
            "state": person.get("state", ""),
            "country": person.get("country", ""),
            "company": org.get("name", ""),
            "company_domain": org.get("primary_domain", ""),
            "company_industry": org.get("industry", ""),
            "company_size": org.get("estimated_num_employees", ""),
            "company_linkedin": org.get("linkedin_url", ""),
        }
        leads.append(lead)

        if verbose:
            email_status = "[HAS EMAIL]" if lead["email"] else "[NO EMAIL]"
            print(f"  {lead['first_name']} {lead['last_name']} {email_status}")
            print(f"    Title: {lead['title']}")
            print(f"    Company: {lead['company']}")
            print(f"    Location: {lead['city']}, {lead['country']}")
            if lead["email"]:
                print(f"    Email: {lead['email']}")
            print()

    return leads


def save_to_csv(leads: List[Dict], filename: str = None):
    """Save leads to CSV file."""
    if not leads:
        print("[Warning] No leads to save")
        return

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"apollo_leads_{timestamp}.csv"

    filepath = OUTPUT_DIR / filename

    if leads:
        fieldnames = leads[0].keys()

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(leads)

        print(f"[Saved] {len(leads)} leads to {filepath}")

    return filepath


def save_to_json(leads: List[Dict], filename: str = None):
    """Save leads to JSON file."""
    if not leads:
        print("[Warning] No leads to save")
        return

    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"apollo_leads_{timestamp}.json"

    filepath = OUTPUT_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(leads, f, indent=2, ensure_ascii=False)

    print(f"[Saved] {len(leads)} leads to {filepath}")
    return filepath


# ============================================
# SURIOTA SPECIFIC SEARCHES
# ============================================

# Target job titles for SURIOTA products
SURIOTA_TITLES = {
    "SRT-MGATE-1210": [
        "Plant Manager",
        "Engineering Manager",
        "IT Manager",
        "Automation Engineer",
        "Process Engineer",
        "Maintenance Manager",
        "Operations Manager",
        "Technical Director",
        "Chief Technology Officer",
    ],
    "SURGE": [
        "Operations Manager",
        "Facility Manager",
        "Energy Manager",
        "Fleet Manager",
        "Environmental Manager",
        "Sustainability Manager",
        "Asset Manager",
        "Utility Manager",
    ],
    "SRICARE": [
        "Hospital Director",
        "Chief Operating Officer",
        "Marketing Director",
        "Business Development Manager",
        "IT Director",
        "Chief Medical Officer",
        "Head of Operations",
    ]
}

# Target industries
SURIOTA_INDUSTRIES = {
    "SRT-MGATE-1210": [
        "manufacturing",
        "electronics",
        "automotive",
        "industrial automation",
        "semiconductors",
    ],
    "SURGE": [
        "oil & gas",
        "energy",
        "utilities",
        "maritime",
        "shipping",
        "water treatment",
        "power generation",
    ],
    "SRICARE": [
        "hospital",
        "healthcare",
        "medical",
        "health services",
    ]
}

def search_suriota_targets(product: str = "all", location: str = "Indonesia"):
    """
    Search for SURIOTA-specific targets.
    """
    all_leads = []

    products = [product] if product != "all" else ["SRT-MGATE-1210", "SURGE", "SRICARE"]

    for prod in products:
        titles = SURIOTA_TITLES.get(prod, [])

        print(f"\n[Searching] {prod} targets in {location}")
        print(f"  Titles: {', '.join(titles[:3])}...")

        result = search_people(
            titles=titles,
            locations=[location],
            per_page=25
        )

        if "people" in result:
            print(f"  Found: {len(result['people'])} people")
            leads = process_people_results(result, verbose=True)

            # Add product tag
            for lead in leads:
                lead["suriota_product"] = prod

            all_leads.extend(leads)
        else:
            print(f"  Error or no results: {result.get('error', 'Unknown')}")

        time.sleep(1)  # Rate limiting

    return all_leads


# ============================================
# MAIN CLI
# ============================================

def main():
    parser = argparse.ArgumentParser(
        description="SURIOTA Lead Finder - Apollo.io API Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search people by title and location
  python apollo_lead_finder.py --search-people --title "Plant Manager" --location "Indonesia"

  # Search people by multiple criteria
  python apollo_lead_finder.py --search-people --title "IT Director" --company "Pertamina"

  # Search organizations
  python apollo_lead_finder.py --search-org --name "Siloam"

  # Enrich a specific email
  python apollo_lead_finder.py --enrich --email "john@company.com"

  # Search SURIOTA-specific targets
  python apollo_lead_finder.py --suriota-targets --product SRT-MGATE-1210
  python apollo_lead_finder.py --suriota-targets --product SURGE
  python apollo_lead_finder.py --suriota-targets --product SRICARE
  python apollo_lead_finder.py --suriota-targets --product all
        """
    )

    # Action modes
    parser.add_argument("--search-people", "-sp", action="store_true",
                        help="Search for people/contacts")
    parser.add_argument("--search-org", "-so", action="store_true",
                        help="Search for organizations")
    parser.add_argument("--enrich", "-e", action="store_true",
                        help="Enrich contact data")
    parser.add_argument("--suriota-targets", "-st", action="store_true",
                        help="Search SURIOTA-specific targets")

    # Filters
    parser.add_argument("--title", "-t", nargs="+", help="Job titles to search")
    parser.add_argument("--location", "-l", nargs="+", default=["Indonesia"],
                        help="Locations to search (default: Indonesia)")
    parser.add_argument("--company", "-c", nargs="+", help="Company names")
    parser.add_argument("--industry", "-i", nargs="+", help="Industries")
    parser.add_argument("--name", "-n", help="Organization name (for --search-org)")
    parser.add_argument("--email", help="Email to enrich or verify")
    parser.add_argument("--product", "-p", choices=["SRT-MGATE-1210", "SURGE", "SRICARE", "all"],
                        default="all", help="SURIOTA product target")

    # Output options
    parser.add_argument("--output", "-o", help="Output filename (without extension)")
    parser.add_argument("--format", choices=["csv", "json", "both"], default="both",
                        help="Output format")
    parser.add_argument("--limit", type=int, default=25, help="Results per page (max 100)")

    args = parser.parse_args()

    print_header()

    all_leads = []

    # Search people
    if args.search_people:
        print(f"[Searching People]")
        print(f"  Titles: {args.title}")
        print(f"  Locations: {args.location}")
        print(f"  Companies: {args.company}")
        print()

        result = search_people(
            titles=args.title,
            locations=args.location,
            company_names=args.company,
            industries=args.industry,
            per_page=args.limit
        )

        if "people" in result:
            pagination = result.get("pagination", {})
            print(f"[Results] Page {pagination.get('page', 1)} of {pagination.get('total_pages', 1)}")
            print(f"[Total] {pagination.get('total_entries', 0)} people found")
            print()

            leads = process_people_results(result)
            all_leads.extend(leads)
        else:
            print(f"[Error] {result}")

    # Search organizations
    elif args.search_org:
        print(f"[Searching Organizations]")
        print(f"  Name: {args.name}")
        print(f"  Locations: {args.location}")
        print()

        result = search_organizations(
            name=args.name,
            locations=args.location,
            per_page=args.limit
        )

        if "organizations" in result:
            orgs = result.get("organizations", [])
            print(f"[Found] {len(orgs)} organizations")
            print()

            for org in orgs:
                print(f"  {org.get('name', 'Unknown')}")
                print(f"    Domain: {org.get('primary_domain', 'N/A')}")
                print(f"    Industry: {org.get('industry', 'N/A')}")
                print(f"    Employees: {org.get('estimated_num_employees', 'N/A')}")
                print(f"    LinkedIn: {org.get('linkedin_url', 'N/A')}")
                print()

                all_leads.append({
                    "company": org.get("name", ""),
                    "domain": org.get("primary_domain", ""),
                    "industry": org.get("industry", ""),
                    "employees": org.get("estimated_num_employees", ""),
                    "linkedin": org.get("linkedin_url", ""),
                    "city": org.get("city", ""),
                    "country": org.get("country", ""),
                })
        else:
            print(f"[Error] {result}")

    # Enrich contact
    elif args.enrich and args.email:
        print(f"[Enriching] {args.email}")
        print()

        result = enrich_person(email=args.email)

        if "person" in result:
            person = result["person"]
            org = person.get("organization", {}) or {}

            print(f"  Name: {person.get('first_name', '')} {person.get('last_name', '')}")
            print(f"  Title: {person.get('title', 'N/A')}")
            print(f"  Company: {org.get('name', 'N/A')}")
            print(f"  LinkedIn: {person.get('linkedin_url', 'N/A')}")
            print(f"  City: {person.get('city', 'N/A')}")
            print(f"  Country: {person.get('country', 'N/A')}")

            all_leads.append({
                "email": args.email,
                "first_name": person.get("first_name", ""),
                "last_name": person.get("last_name", ""),
                "title": person.get("title", ""),
                "company": org.get("name", ""),
                "linkedin": person.get("linkedin_url", ""),
            })
        else:
            print(f"[Not Found or Error] {result}")

    # SURIOTA specific search
    elif args.suriota_targets:
        location = args.location[0] if args.location else "Indonesia"
        all_leads = search_suriota_targets(args.product, location)

    else:
        parser.print_help()
        return

    # Save results
    if all_leads:
        print()
        print("=" * 60)
        print(f"[Summary] Total leads: {len(all_leads)}")

        output_name = args.output or f"apollo_leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        if args.format in ["csv", "both"]:
            save_to_csv(all_leads, f"{output_name}.csv")
        if args.format in ["json", "both"]:
            save_to_json(all_leads, f"{output_name}.json")


if __name__ == "__main__":
    main()
