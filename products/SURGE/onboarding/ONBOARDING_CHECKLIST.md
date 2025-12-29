# SURGE Platform - Customer Onboarding Checklist

## Panduan Step-by-Step untuk Implementasi Customer Baru

**Version**: 2.0 | **Last Updated**: December 29, 2025

---

# OVERVIEW ONBOARDING PROCESS

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           SURGE ONBOARDING JOURNEY                           │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PHASE 1        PHASE 2         PHASE 3         PHASE 4         PHASE 5    │
│   ────────       ────────        ────────        ────────        ────────   │
│   Pre-Sales      Setup           Installation    Configuration   Go-Live    │
│   (1-2 days)     (1 day)         (1-3 days)      (1 day)         (1 day)    │
│                                                                              │
│   ○ Discovery    ○ Account       ○ Gateway       ○ Parameters    ○ Training │
│   ○ Proposal     ○ Organization  ○ Sensors       ○ Dashboard     ○ Handover │
│   ○ Contract     ○ Users         ○ Network       ○ Alerts        ○ Support  │
│                                                                              │
│   ──────────────────────────────────────────────────────────────────────────│
│   TOTAL TIMELINE: 5-8 HARI KERJA                                             │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

# PHASE 1: PRE-SALES (Day 0)

## 1.1 Discovery Call

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Confirm customer pain points | Sales | [ ] | |
| Identify use case (Water/Energy/Vessel) | Sales | [ ] | |
| Count parameters needed | Sales | [ ] | |
| Count locations/outlets | Sales | [ ] | |
| Inventory existing sensors | Sales | [ ] | |
| Identify network infrastructure | Sales | [ ] | |
| Determine budget range | Sales | [ ] | |
| Identify decision makers | Sales | [ ] | |

**Output:** Discovery Notes Document

---

## 1.2 Proposal & Quotation

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Recommend SURGE tier | Sales | [ ] | |
| Calculate hardware needed | Sales | [ ] | |
| Prepare ROI calculation | Sales | [ ] | |
| Generate quotation | Sales | [ ] | |
| Send proposal document | Sales | [ ] | |
| Follow-up presentation | Sales | [ ] | |

**Output:** Proposal PDF + Quotation

---

## 1.3 Contract & Payment

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Negotiate terms | Sales | [ ] | |
| Draft contract/PO | Sales | [ ] | |
| Get customer signature | Sales | [ ] | |
| Process payment (if prepaid) | Finance | [ ] | |
| Confirm subscription start date | Sales | [ ] | |
| Schedule kickoff call | Sales | [ ] | |

**Output:** Signed Contract + Payment Confirmation

---

# PHASE 2: ACCOUNT SETUP (Day 1)

## 2.1 SURGE Account Creation

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Create organization in SURGE | Support | [ ] | |
| Set organization name & details | Support | [ ] | |
| Upload company logo | Support | [ ] | |
| Configure billing settings | Support | [ ] | |
| Enable selected modules | Support | [ ] | |

**Organization Details:**
- Name: _________________________
- Industry: _________________________
- Tier: [ ] Trial (5 tags) [ ] Starter (30 tags) [ ] Business (100 tags) [ ] Professional (Unlimited)
- Modules: [ ] Water [ ] Energy [ ] Vessel
- Total Tag Data Needed: _________ tags
- Total Locations: _________ (All tiers = Unlimited locations)

---

## 2.2 User Setup

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Create owner account | Support | [ ] | |
| Send invitation email | Support | [ ] | |
| Confirm owner can login | Support | [ ] | |
| Create additional admin accounts | Customer | [ ] | |
| Create operator/viewer accounts | Customer | [ ] | |

**User Accounts:**

| Email | Name | Role | Status |
|-------|------|------|:------:|
| _______________ | _______________ | Owner | [ ] Active |
| _______________ | _______________ | Admin | [ ] Active |
| _______________ | _______________ | Member | [ ] Active |
| _______________ | _______________ | Viewer | [ ] Active |

---

## 2.3 Location Setup

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Add locations/sites | Customer/Support | [ ] | |
| Set location coordinates | Customer/Support | [ ] | |
| Upload site photos/maps | Customer/Support | [ ] | |
| Configure location hierarchy | Customer/Support | [ ] | |

**Locations:**

| Location Name | Address | Coordinates | Status |
|---------------|---------|-------------|:------:|
| _______________ | _______________ | _______, _______ | [ ] Ready |
| _______________ | _______________ | _______, _______ | [ ] Ready |
| _______________ | _______________ | _______, _______ | [ ] Ready |

---

# PHASE 3: HARDWARE INSTALLATION (Day 2-4)

## 3.1 Pre-Installation Check

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Confirm hardware received | Customer | [ ] | |
| Verify all components in box | Technician | [ ] | |
| Site power availability check | Technician | [ ] | |
| Network availability check | Technician | [ ] | |
| Sensor cable length verification | Technician | [ ] | |
| Mounting location identified | Technician | [ ] | |

**Hardware Received:**

| Item | Qty Ordered | Qty Received | Serial Numbers |
|------|:-----------:|:------------:|----------------|
| SRT-MGATE-1210 | _____ | _____ | _________________ |
| SRT-MGATE-1210-POE | _____ | _____ | _________________ |
| Power adapter | _____ | _____ | - |
| Ethernet cable | _____ | _____ | - |
| Antenna | _____ | _____ | - |

---

## 3.2 Gateway Installation

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Mount gateway at location | Technician | [ ] | |
| Connect power supply | Technician | [ ] | |
| Verify power LED on | Technician | [ ] | |
| Connect Ethernet (if used) | Technician | [ ] | |
| Verify network LED on | Technician | [ ] | |
| Connect RS-485 to sensors | Technician | [ ] | |
| Verify RS-485 LEDs blinking | Technician | [ ] | |

---

## 3.3 Gateway Configuration

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Download SURIOTA Config App | Technician | [ ] | |
| Connect to gateway via BLE | Technician | [ ] | |
| Configure WiFi credentials | Technician | [ ] | |
| Configure MQTT broker settings | Technician | [ ] | |
| Configure Modbus slave addresses | Technician | [ ] | |
| Set data interval | Technician | [ ] | |
| Save configuration | Technician | [ ] | |
| Verify gateway connected to cloud | Technician | [ ] | |

**Gateway Configuration:**

| Setting | Value |
|---------|-------|
| WiFi SSID | _________________________ |
| WiFi Password | ************************* |
| MQTT Broker | mqtt.suriota.com |
| MQTT Port | 8883 |
| MQTT Username | [From SURGE] |
| Data Interval | _____ seconds |

---

## 3.4 Sensor Verification

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Verify Modbus communication | Technician | [ ] | |
| Read test values from each sensor | Technician | [ ] | |
| Compare readings with reference | Technician | [ ] | |
| Document Modbus addresses | Technician | [ ] | |
| Label all cables | Technician | [ ] | |

**Sensor Mapping:**

| Sensor | Type | Modbus Address | Register | Status |
|--------|------|:--------------:|----------|:------:|
| _________ | _________ | _____ | _____ | [ ] OK |
| _________ | _________ | _____ | _____ | [ ] OK |
| _________ | _________ | _____ | _____ | [ ] OK |
| _________ | _________ | _____ | _____ | [ ] OK |
| _________ | _________ | _____ | _____ | [ ] OK |

---

# PHASE 4: SURGE CONFIGURATION (Day 5)

## 4.1 Device Registration

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Add gateway to SURGE | Support | [ ] | |
| Enter gateway serial number | Support | [ ] | |
| Assign gateway to location | Support | [ ] | |
| Verify gateway online in SURGE | Support | [ ] | |

---

## 4.2 Parameter Configuration

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Add parameters/data points | Support | [ ] | |
| Set parameter names | Support | [ ] | |
| Configure units (pH, mg/L, kWh) | Support | [ ] | |
| Set decimal places | Support | [ ] | |
| Map to Modbus registers | Support | [ ] | |
| Verify data coming through | Support | [ ] | |

**Parameter Setup:**

| Parameter | Unit | Min | Max | Threshold Low | Threshold High |
|-----------|------|:---:|:---:|:-------------:|:--------------:|
| _________ | _____ | _____ | _____ | _____ | _____ |
| _________ | _____ | _____ | _____ | _____ | _____ |
| _________ | _____ | _____ | _____ | _____ | _____ |
| _________ | _____ | _____ | _____ | _____ | _____ |
| _________ | _____ | _____ | _____ | _____ | _____ |

---

## 4.3 Dashboard Configuration

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Create dashboard layout | Support | [ ] | |
| Add widgets (gauge, chart, table) | Support | [ ] | |
| Configure chart time ranges | Support | [ ] | |
| Set refresh intervals | Support | [ ] | |
| Add location map | Support | [ ] | |
| Configure dashboard permissions | Support | [ ] | |

---

## 4.4 Alert Configuration

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Set threshold values | Customer | [ ] | |
| Configure alert rules | Support | [ ] | |
| Add email recipients | Customer | [ ] | |
| Test alert trigger | Support | [ ] | |
| Verify email received | Customer | [ ] | |

**Alert Recipients:**

| Name | Email | Alerts |
|------|-------|--------|
| _________ | _________________ | [ ] All [ ] Critical only |
| _________ | _________________ | [ ] All [ ] Critical only |
| _________ | _________________ | [ ] All [ ] Critical only |

---

## 4.5 Report Configuration (Water Analytics)

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Configure KLHK parameters | Support | [ ] | |
| Set baku mutu thresholds | Customer | [ ] | |
| Configure report template | Support | [ ] | |
| Test export function | Support | [ ] | |
| Verify format matches SISPEK | Customer | [ ] | |

---

# PHASE 5: GO-LIVE & TRAINING (Day 6-7)

## 5.1 User Training

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Schedule training session | Support | [ ] | |
| Conduct dashboard training | Support | [ ] | |
| Conduct alert management training | Support | [ ] | |
| Conduct report export training | Support | [ ] | |
| Q&A session | Support | [ ] | |
| Distribute training materials | Support | [ ] | |

**Training Attendees:**

| Name | Role | Attended | Quiz Score |
|------|------|:--------:|:----------:|
| _________ | _________ | [ ] | _____% |
| _________ | _________ | [ ] | _____% |
| _________ | _________ | [ ] | _____% |

---

## 5.2 Go-Live Verification

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| All devices online | Support | [ ] | |
| All parameters reading correctly | Support | [ ] | |
| Alerts working | Support | [ ] | |
| Dashboard accessible | Customer | [ ] | |
| Users can login | Customer | [ ] | |
| 24-hour data collected | Support | [ ] | |

---

## 5.3 Handover

| Task | Owner | Status | Notes |
|------|:-----:|:------:|-------|
| Complete handover document | Support | [ ] | |
| Share support contact info | Support | [ ] | |
| Add customer to support channel | Support | [ ] | |
| Collect feedback form | Support | [ ] | |
| Schedule 7-day check-in call | Support | [ ] | |

**Handover Documents:**

| Document | Delivered | Signed |
|----------|:---------:|:------:|
| Installation Report | [ ] | [ ] |
| Configuration Summary | [ ] | [ ] |
| User Guide PDF | [ ] | [ ] |
| Support Contact Card | [ ] | [ ] |
| Gateway Documentation | [ ] | [ ] |

---

# POST-ONBOARDING SUPPORT

## Check-in Schedule

| Timeline | Activity | Owner | Status |
|----------|----------|:-----:|:------:|
| Day 7 | First check-in call | Support | [ ] |
| Day 14 | System health review | Support | [ ] |
| Day 30 | End of trial/first month review | Sales | [ ] |
| Day 60 | Feature usage review | CSM | [ ] |
| Day 90 | Quarterly business review | Sales | [ ] |

---

## Support Escalation Path

```
Level 1: Self-Service
├── Knowledge Base: help.suriota.com
├── FAQ Documents
└── User Guide PDF

Level 2: Standard Support
├── Email: support@suriota.com
├── WhatsApp: +62 858-3567-2476
└── Response: 8-24 hours

Level 3: Priority Support (Business+)
├── Dedicated WhatsApp group
├── Phone call
└── Response: 4-8 hours

Level 4: On-site Support (Professional)
├── Technician dispatch
├── Remote session
└── Response: Same day
```

---

# TROUBLESHOOTING QUICK GUIDE

## Common Issues During Onboarding

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| Gateway not connecting | Wrong WiFi credentials | Reconfigure via BLE app |
| Gateway offline intermittent | Poor WiFi signal | Move closer or use Ethernet |
| No data from sensor | Wrong Modbus address | Check sensor documentation |
| Data values incorrect | Wrong register/scaling | Adjust register mapping |
| Alert not received | Wrong email address | Verify in user settings |
| Cannot login | Invitation expired | Resend invitation email |

---

# COMPLETION SIGN-OFF

## Project Summary

| Item | Value |
|------|-------|
| **Customer** | _________________________ |
| **Project Start Date** | _________________________ |
| **Go-Live Date** | _________________________ |
| **Total Duration** | _____ days |
| **SURGE Tier** | _________________________ |
| **Total Devices** | _____ |
| **Total Parameters** | _____ |
| **Total Users** | _____ |

---

## Sign-Off

### Customer Acceptance

> Saya menyatakan bahwa implementasi SURGE Platform telah selesai dan semua fitur berfungsi sesuai yang dijanjikan.

| | |
|-----|-----|
| **Nama** | _________________________ |
| **Jabatan** | _________________________ |
| **Tanggal** | _________________________ |
| **Tanda Tangan** | _________________________ |

### SURIOTA Project Manager

| | |
|-----|-----|
| **Nama** | _________________________ |
| **Jabatan** | _________________________ |
| **Tanggal** | _________________________ |
| **Tanda Tangan** | _________________________ |

---

---

# PRICING REFERENCE

| Plan | Tag Data | Price/Month | Locations | Retention |
|------|:--------:|-------------|:---------:|:---------:|
| Trial | 5 | Free | Unlimited | 30 hari |
| Starter | 30 | $29 (Rp 464K) | Unlimited | 1 tahun |
| Business | 100 | $99 (Rp 1.58M) | Unlimited | 2 tahun |
| Professional | Unlimited | $299 (Rp 4.78M) | Unlimited | 5 tahun |

**Key Notes:**
- Tag Data = jumlah parameter monitoring (pH, kWh, GPS, dll)
- Semua tier sudah include **Unlimited locations**
- Trial = Private access, harus kontak tim SURIOTA

---

_Document Version: 2.0_
_For Internal Use_
_Last Updated: December 29, 2025_
