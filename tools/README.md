# SURIOTA Lead Generation & Email Campaign Tools

Tools untuk lead generation dan email campaign menggunakan Hunter.io API.

## Folder Structure

```
tools/
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
├── scripts/                  # Python scripts
│   ├── hunter_lead_finder.py # Hunter.io API client
│   ├── apollo_lead_finder.py # Apollo.io API client (requires paid plan)
│   ├── lead_manager.py       # Lead classification & email generation
│   ├── merge_leads.py        # Merge multiple lead files
│   └── export_email_campaign.py # Export to campaign-ready CSV
├── domains/                  # Target domain lists
│   ├── batam_batch1.txt      # Oil & Gas + Energy (15 domains)
│   ├── batam_batch2.txt      # Manufacturing (10 domains)
│   ├── batam_batch3.txt      # Healthcare + Utilities (15 domains)
│   ├── batam_comprehensive.txt # All Batam domains
│   ├── batam_priority.txt    # Priority targets
│   ├── target.txt            # General targets
│   └── top10.txt             # Top 10 targets
└── output/                   # Generated files
    ├── leads/                # Raw lead data (CSV/JSON)
    ├── campaigns/            # Email campaign CSVs
    ├── drafts/               # Email draft JSONs
    └── EMAIL_SAMPLES_PREVIEW.txt
```

## Setup

```bash
cd tools
pip install -r requirements.txt
```

## Quick Start

### 1. Fetch Leads from Domain

```bash
python scripts/hunter_lead_finder.py --domain pertamina.com
```

### 2. Batch Fetch from Domain List

```bash
python scripts/hunter_lead_finder.py --domains domains/batam_batch1.txt
```

### 3. Classify Leads by Product

```bash
python scripts/lead_manager.py --input output/leads/ALL_BATAM_LEADS.json
```

### 4. Generate Email Drafts

```bash
python scripts/lead_manager.py --generate-emails --template compro
python scripts/lead_manager.py --generate-emails --template srt-mgate
python scripts/lead_manager.py --generate-emails --template surge
python scripts/lead_manager.py --generate-emails --template sricare
```

### 5. Export to Campaign CSV

```bash
python scripts/export_email_campaign.py
```

### 6. Convert to Excel (Styled)

```bash
python scripts/convert_to_excel.py
```

## Scripts

### hunter_lead_finder.py

Hunter.io API client untuk mencari email kontak perusahaan.

```bash
# Check account status
python scripts/hunter_lead_finder.py --status

# Search single domain
python scripts/hunter_lead_finder.py --domain pertamina.com

# Search multiple domains
python scripts/hunter_lead_finder.py --domains domains/target.txt

# Find specific person
python scripts/hunter_lead_finder.py --find "John Doe" --domain pertamina.com

# Verify email
python scripts/hunter_lead_finder.py --verify john.doe@pertamina.com
```

### lead_manager.py

Klasifikasi leads berdasarkan relevansi produk SURIOTA.

```bash
# Classify leads
python scripts/lead_manager.py --input output/leads/ALL_BATAM_LEADS.json

# Generate email drafts
python scripts/lead_manager.py --generate-emails --template compro

# Export to Mailchimp format
python scripts/lead_manager.py --export-mailchimp
```

### merge_leads.py

Merge multiple lead CSV files dan deduplikasi.

```bash
python scripts/merge_leads.py
```

## Output Files

### Leads (output/leads/)

| File | Description |
|------|-------------|
| ALL_BATAM_LEADS.xlsx | All 281 unique leads (styled) |
| LEADS_srt_mgate.xlsx | 106 leads for SRT-MGATE-1210 |
| LEADS_surge.xlsx | 126 leads for SURGE Platform |
| LEADS_sricare.xlsx | 32 leads for SRICARE |

### Campaigns (output/campaigns/)

| File | Emails | Target |
|------|--------|--------|
| EMAIL_CAMPAIGN_COMPRO.xlsx | 281 | Company Profile |
| EMAIL_CAMPAIGN_SRT_MGATE.xlsx | 106 | Industrial Gateway |
| EMAIL_CAMPAIGN_SURGE.xlsx | 126 | IoT Platform |
| EMAIL_CAMPAIGN_SRICARE.xlsx | 32 | Healthcare Partnership |
| MAILCHIMP_EXPORT.xlsx | 281 | Mailchimp import |

### Drafts (output/drafts/)

| File | Description |
|------|-------------|
| email_drafts_compro.json | Company profile email drafts |
| email_drafts_srt_mgate.json | SRT-MGATE-1210 email drafts |
| email_drafts_surge.json | SURGE platform email drafts |
| email_drafts_sricare.json | SRICARE partnership email drafts |

## How to Send Emails

### Option 1: Gmail Mail Merge (FREE)

1. Install "Yet Another Mail Merge" for Google Sheets
2. Upload CSV to Google Sheets
3. Create template with `{{first_name}}`, `{{company}}` variables
4. Send via YAMM

### Option 2: Mailchimp

1. Import `MAILCHIMP_EXPORT.csv` to Audience
2. Create campaign with merge tags `*|FNAME|*`, `*|COMPANY|*`
3. Schedule and send

### Option 3: Manual (VIP Contacts)

1. Open CSV in Excel
2. Filter by position (CEO, VP, Director)
3. Copy-paste and personalize

## API Information

### Hunter.io

- **Free Tier**: 25 searches/month + 50 verifications/month
- **Rate Limit**: ~10 requests/second
- **Docs**: https://hunter.io/api-documentation

### Apollo.io

- **Note**: Free plan tidak support API search endpoints
- **Requires**: Paid plan ($49+/month)
- **Docs**: https://apolloio.github.io/apollo-api-docs/

## Best Practices

1. **Limit sending**: Max 50-100 emails/day/account
2. **Personalize**: Add personal touch for VIP contacts
3. **Include unsubscribe**: Legal requirement
4. **Track responses**: Use CRM or spreadsheet
5. **Follow up**: Re-contact non-responders after 3-5 days

## Legal Notes

- Hunter.io collects data from **public sources only**
- Comply with **UU PDP Indonesia** for data protection
- Use for **B2B outreach only**, not spam
- Always include **unsubscribe option** in emails
