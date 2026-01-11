# SURIOTA Lead Generation Tools

Tools untuk mencari email kontak perusahaan target menggunakan Hunter.io API.

## Setup

```bash
cd tools
pip install -r requirements.txt
```

## Hunter.io API

- **Free Tier**: 25 searches/month + 50 verifications/month
- **Paid Plans**: Starting from $49/month for 500 searches
- **API Docs**: https://hunter.io/api-documentation

## Usage

### 1. Check Account Status

```bash
python hunter_lead_finder.py --status
```

### 2. Search Single Domain

```bash
python hunter_lead_finder.py --domain pertamina.com
```

### 3. Search Multiple Domains

```bash
python hunter_lead_finder.py --domains domains_target.txt
```

### 4. Find Specific Person

```bash
python hunter_lead_finder.py --find "John Doe" --domain pertamina.com
```

### 5. Verify Email

```bash
python hunter_lead_finder.py --verify john.doe@pertamina.com
```

### 6. Search SURIOTA Target Domains

```bash
python hunter_lead_finder.py --targets
```

## Output

Results saved to `tools/output/` folder:

- `leads_YYYYMMDD_HHMMSS.csv` - CSV format
- `leads_YYYYMMDD_HHMMSS.json` - JSON format

## CSV Columns

| Column | Description |
|--------|-------------|
| domain | Company domain |
| company | Company name |
| industry | Industry category |
| email | Email address |
| first_name | First name |
| last_name | Last name |
| position | Job title |
| department | Department |
| linkedin | LinkedIn profile URL |
| confidence | Confidence score (0-100) |
| sources | Number of sources found |

## Target Domains

Edit `domains_target.txt` to customize target companies:

```text
# Manufacturing
unilever.co.id
nestle.co.id

# Energy
pertamina.com
pln.co.id

# Custom targets
yourcompany.com
```

## Rate Limits

- Hunter.io: ~10 requests/second
- Script includes 1-second delay between domains
- Free tier: 25 domain searches/month

## Tips

1. **Prioritize high-value targets** - Focus on decision makers
2. **Filter by confidence** - Use confidence >= 80 for best results
3. **Verify before sending** - Use `--verify` to check deliverability
4. **Track usage** - Check `--status` regularly

## Legal Notes

- Hunter.io collects data from **public sources only**
- Always include **unsubscribe option** in emails
- Comply with **UU PDP Indonesia** for data protection
- Use for **B2B outreach only**, not spam
