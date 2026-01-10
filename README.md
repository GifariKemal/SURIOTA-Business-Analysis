# SURIOTA Business Analysis

**Business Analysis Repository for PT Surya Inovasi Prioritas (SURIOTA)**

---

## Overview

This repository contains comprehensive business analysis documentation for **SURIOTA**, covering:

- **Company Profile** - About Us page recommendations and scoring
- **Products** - Business analysis for SURIOTA products:
  - **SRT-MGATE-1210** - Industrial Modbus-to-MQTT Gateway (Hardware)
  - **SURGE Platform** - Multi-tenant SaaS IoT Monitoring (Software)
  - **SRICARE** - Patient Companion & Home Care Mobile App (Software)
- **Services** - Industrial IoT service offerings

---

## Company Information

**PT Surya Inovasi Prioritas (SURIOTA)** is a technology-based company specializing in Industrial IoT Services and System Integration, headquartered in Batam, Riau Islands, Indonesia.

### Core Values (CIPTA)

| Value         | Description               |
| ------------- | ------------------------- |
| **C**ommitted | Committed outcomes        |
| **I**ntegrity | Integrity in innovation   |
| **P**recision | Precision in execution    |
| **T**rust     | Trust through reliability |
| **A**daptive  | Adaptive growth           |

### Key Metrics

| Metric                       | Value               |
| ---------------------------- | ------------------- |
| Established                  | 2023                |
| Projects Delivered           | 55+                 |
| Team Members                 | 25+                 |
| Products Developed           | 6+                  |
| Market Size (Indonesia IIoT) | $2.7 billion (2025) |

---

## Repository Structure

```
SURIOTA-Business-Analysis/
├── README.md                                    # This file
├── CLAUDE.md                                    # AI context file
│
├── company-profile/                             # Company Profile documentation
│   ├── MARKET_RESEARCH_FINDINGS.md              # Market research data
│   ├── page3/                                   # About Us page (v1-v3)
│   ├── page4/                                   # Vision & Mission page (v1-v3)
│   └── page5/                                   # Services page
│
├── products/                                    # Product business analysis
│   ├── SRT-MGATE-1210/                          # Modbus Gateway (Hardware)
│   │   ├── README.md                            # Documentation index
│   │   ├── BUSINESS_ANALYSIS.md                 # Main business document
│   │   ├── sales/                               # Sales documents
│   │   ├── onboarding/                          # Onboarding guides
│   │   └── technical/                           # Technical docs
│   │
│   ├── SURGE/                                   # SURGE Platform (SaaS)
│   │   ├── README.md                            # Documentation index
│   │   ├── BUSINESS_ANALYSIS.md                 # Main business document
│   │   ├── sales/                               # Sales documents
│   │   ├── onboarding/                          # Onboarding guides
│   │   └── technical/                           # Technical docs
│   │
│   └── SRICARE/                                 # SRICARE App (Mobile)
│       ├── README.md                            # Documentation index
│       ├── PRD.md                               # Product Requirements Document
│       ├── BUSINESS_ANALYSIS.md                 # Market analysis & financials
│       ├── PITCH_DECK.md                        # Investor pitch deck
│       ├── UI_MOCKUPS.md                        # UI/UX design system
│       ├── BRAND_GUIDELINES.md                  # Brand identity
│       └── assets/                              # Logo & brand assets
│
├── data/                                        # Supporting data files
│   ├── SRT-MGATE-1210/                          # Hardware BOM & costs
│   └── SURGE/                                   # Platform documentation
│
└── .claude/                                     # Claude Code config
```

---

## Products

### 1. SRT-MGATE-1210 - Industrial Modbus Gateway

Industrial Modbus-to-MQTT Gateway with advanced connectivity features.

| Model              | Description                        | Price (IDR)  | Price (USD) | Margin |
| ------------------ | ---------------------------------- | ------------ | ----------- | :----: |
| SRT-MGATE-1210     | Standard - 2xRS485, ETH, WiFi, BLE | Rp 2,700,000 | ~$169       |  40%   |
| SRT-MGATE-1210-POE | PoE - 2xRS485, ETH+PoE, WiFi, BLE  | Rp 3,100,000 | ~$194       |  41%   |

**Key Features:**

- Dual RS-485 with ESD protection
- WiFi 2.4GHz with auto-failover
- BLE 5.0 mobile configuration
- RTC DS3231 with battery backup
- MQTT Output JSON to any cloud
- Industrial Grade -40C to +75C

**USP:** ONLY Modbus-to-MQTT gateway in Indonesia with WiFi + BLE + RTC

[View Full Documentation →](./products/SRT-MGATE-1210/)

---

### 2. SURGE Platform - IoT Monitoring SaaS

Multi-Tenant SaaS Platform for industrial IoT monitoring with 3 integrated modules.

| Module              | Target               | Key Parameters          |
| ------------------- | -------------------- | ----------------------- |
| **Water Analytics** | IPAL, STP, WTP, PDAM | pH, COD, TSS, NH3, Flow |
| **Energy Mapping**  | Buildings, Factories | kWh, kVA, Power Factor  |
| **Vessel Tracking** | Maritime, Fleet      | GPS, Fuel, RPM, Speed   |

**Pricing:**

| Plan         | Price/Month     | Tag Data  | Locations | Retention |
| ------------ | --------------- | :-------: | :-------: | :-------: |
| Trial        | Free            |     5     | Unlimited |  30 days  |
| Starter      | $29 (Rp 464K)   |    30     | Unlimited |  1 year   |
| Business     | $99 (Rp 1.58M)  |    100    | Unlimited |  2 years  |
| Professional | $299 (Rp 4.78M) | Unlimited | Unlimited |  5 years  |

**USP:** Unlimited locations in ALL tiers + KLHK Compliance + 70% cheaper than ThingsBoard

[View Full Documentation →](./products/SURGE/)

---

### 3. SRICARE - Patient Companion & Home Care App

<div align="center">
<img src="./products/SRICARE/assets/sricare-logo.png" alt="SRICARE Logo" width="250">

_"Caring hands, always near"_

</div>

On-demand mobile app connecting users with professional Caregivers for patient companion and home care services.

| Service            | Minimum       | Standard               | Premium           |
| ------------------ | ------------- | ---------------------- | ----------------- |
| Hospital Companion | Rp 50K/jam    | Rp 250K/6jam           | Rp 600K/24jam     |
| Dialysis Support   | Rp 200K/sesi  | Rp 300K/sesi+transport | Rp 2M/12sesi      |
| Medical Escort     | Rp 100K/visit | Rp 200K/full           | Rp 300K+transport |
| Home Care          | Rp 350K/day   | Rp 5.5M/month          | Rp 6.5M/live-in   |

**Target Market:** Batam first (pilot), Indonesia expansion

**USP:** First-mover in Batam + GPS-based matching + Hospital companion (unique)

[View Full Documentation →](./products/SRICARE/)

---

## Company Profile

### Market Research

Comprehensive market research compiled in `MARKET_RESEARCH_FINDINGS.md`:

- Indonesia IIoT Market ($2.7B, 15% CAGR)
- Digital Economy Overview ($130B by 2025)
- Batam Strategic Advantages (FTZ, Singapore proximity)
- Healthcare Market ($15B elderly care, 28% CAGR home healthcare)

### Page Documentation

| Page   | Content          | Final Version    |   Score    |
| ------ | ---------------- | ---------------- | :--------: |
| Page 3 | About Us         | `v3-final.md`    | **8.5/10** |
| Page 4 | Vision & Mission | `v3-final.md`    | **8.5/10** |
| Page 5 | Services         | `v1-services.md` | **8.5/10** |

**Vision (Recommended):**

> "Transforming industries through smart, connected solutions."

---

## Supplier Program (SRT-MGATE-1210)

SURIOTA offers supplier/distributor partnership with MAP policy:

| Tier       | Min Order | Discount | Non-PoE Price    | PoE Price        |
| ---------- | --------- | -------- | ---------------- | ---------------- |
| Tier 1     | 5 unit    | 20%      | Rp 2,160,000     | Rp 2,480,000     |
| **Tier 2** | 10 unit   | **25%**  | **Rp 2,025,000** | **Rp 2,325,000** |
| Tier 3     | 25 unit   | 30%      | Rp 1,890,000     | Rp 2,170,000     |

Contact sales@suriota.com for supplier registration.

---

## Contact

**PT Surya Inovasi Prioritas (SURIOTA)**

|         |                   |
| ------- | ----------------- |
| Website | www.suriota.com   |
| Email   | sales@suriota.com |
| Phone   | +62 858-3567-2476 |

---

## Related Repositories

**Hardware (SRT-MGATE-1210):**

- [GatewaySuriotaPOC](https://github.com/GifariKemal/GatewaySuriotaPOC) - Firmware source code
- [GatewaySuriotaOTA](https://github.com/GifariKemal/GatewaySuriotaOTA) - OTA releases

**Software (SURGE Platform):**

- `surge-energy-map-frontend` - Frontend Next.js application
- `surge--water-analytics-backend` - Backend NestJS application

---

## License

This documentation is proprietary to PT Surya Inovasi Prioritas. All rights reserved.

---

_Last Updated: January 2026_
