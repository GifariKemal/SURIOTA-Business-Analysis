# SURGE Business Analysis & Pricing Strategy

## Dokumen Analisis Bisnis untuk Finance & Marketing

**Document Version**: 1.0
**Last Updated**: December 28, 2025
**Prepared by**: Product Development Team
**Exchange Rate**: 1 USD = Rp 16,000 (rounded for calculation)

---

# REKOMENDASI HARGA FINAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    💰 HARGA JUAL RESMI SURGE PLATFORM 💰                   │
│                        (Updated: December 28, 2025)                         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  PLAN                │  HARGA/BULAN     │  PARAMETER  │  LOKASI    │   │
│   ├──────────────────────┼──────────────────┼─────────────┼────────────┤   │
│   │  Trial (Free)        │  Rp 0            │  5 params   │  1 lokasi  │   │
│   │                      │                  │             │            │   │
│   │  Starter             │  Rp 464.000      │  10 params  │  3 lokasi  │   │
│   │                      │  ($29/month)     │             │            │   │
│   │                      │                  │             │            │   │
│   │  Business            │  Rp 1.584.000    │  25 params  │  10 lokasi │   │
│   │                      │  ($99/month)     │             │            │   │
│   │                      │                  │             │            │   │
│   │  Professional        │  Rp 4.784.000    │  Unlimited  │  Unlimited │   │
│   │                      │  ($299/month)    │             │            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   POSITIONING:                                                              │
│   • 75% lebih murah dari ThingsBoard PE ($399/mo vs $99/mo)                │
│   • 60% lebih murah dari Grafana Cloud Enterprise                          │
│   • 50% lebih murah dari Datacake Business                                 │
│   • +3 MODUL TERINTEGRASI: Water, Energy, Vessel dalam 1 platform          │
│                                                                             │
│   USP: SATU-SATUNYA platform IoT lokal dengan 3 modul industri terintegrasi│
│   + KLHK Compliance untuk Water Analytics + Local Bahasa Indonesia Support │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# DAFTAR ISI

1. [Executive Summary](#executive-summary)
2. [Product Overview](#product-overview)
3. [Module Details](#module-details)
4. [Competitor Analysis](#competitor-analysis)
5. [Feature Comparison](#feature-comparison)
6. [Pricing Strategy](#pricing-strategy)
7. [Unique Selling Proposition (USP)](#unique-selling-proposition-usp)
8. [Target Market & Segmentation](#target-market--segmentation)
9. [Sales & Marketing Guide](#sales--marketing-guide)
10. [Financial Projections](#financial-projections)

---

# Executive Summary

## Ringkasan Eksekutif

**SURGE (Suriota Governance Ecosystem)** adalah platform **Multi-Tenant SaaS** produksi lokal PT Surya Inovasi Prioritas (SURIOTA) yang dirancang untuk monitoring IoT industri dengan **3 modul terintegrasi**:

1. **Water Analytics** - Monitoring kualitas air (IPAL/STP/WTP/PDAM)
2. **Energy Mapping** - Monitoring konsumsi energi gedung/industri
3. **Vessel Tracking** - Monitoring armada kapal maritim

### Key Highlights:

| Metric                     | Value                                   |
| -------------------------- | --------------------------------------- |
| **Target Market**          | Industrial IoT Indonesia                |
| **Competitive Position**   | Mid-range dengan fitur enterprise       |
| **Price Point**            | $29 - $299/month                        |
| **Target ARR**             | $100,000 dalam 12 bulan                 |
| **Target Organizations**   | 50+ organisasi aktif tahun pertama      |
| **Data Retention**         | 30 hari - 3 tahun (per tier)            |

### Keunggulan Kompetitif:

- **SATU-SATUNYA** platform IoT Indonesia dengan **3 modul industri terintegrasi**
- **KLHK Compliance Ready** untuk monitoring lingkungan
- **Produksi Lokal** = Support Bahasa Indonesia, timezone WIB, regulasi lokal
- **75% lebih murah** dari ThingsBoard Professional dengan fitur setara
- **Multi-tenant architecture** dengan full data isolation

---

# Product Overview

## Platform Overview

### SURGE Platform Architecture

| Specification            | Detail                                              |
| ------------------------ | --------------------------------------------------- |
| **Type**                 | Multi-Tenant SaaS Platform                          |
| **Architecture**         | Frontend-Backend Separation (2-tier)                |
| **Frontend Framework**   | Next.js 15.2.4 + React 19 + TypeScript              |
| **Backend Framework**    | NestJS + PostgreSQL + TimescaleDB                   |
| **Authentication**       | Custom JWT with RBAC (viewer/member/admin/owner)    |
| **UI Library**           | Shadcn UI + Radix UI + Tailwind CSS                 |
| **Maps**                 | Mapbox GL JS 3.14.0                                 |
| **Charts**               | Recharts 2.15.4                                     |
| **Real-time Protocol**   | MQTT + Socket.IO                                    |
| **Data Processing**      | Batch processing (20 msg/2 sec)                     |
| **API Documentation**    | Swagger/OpenAPI                                     |
| **Deployment**           | Docker + Vercel/CapRover                            |

### Performance Specifications

| Metric                   | Target                                  |
| ------------------------ | --------------------------------------- |
| **System Uptime**        | >99.5%                                  |
| **Page Load Time**       | <3 seconds                              |
| **API Response Time**    | <500ms                                  |
| **Real-time Latency**    | <5 seconds                              |
| **Concurrent Users**     | 100+ per organization                   |
| **Data Throughput**      | 1000+ readings per minute               |
| **Storage Capacity**     | 1TB+ data storage                       |

---

# Module Details

## 1. SURGE Water Analytics

### Overview
Platform monitoring kualitas air real-time untuk industri, lingkungan, dan institusi dengan integrasi langsung ke sistem pelaporan KLHK (Kementerian Lingkungan Hidup dan Kehutanan).

### Target Segment
- IPAL (Instalasi Pengolahan Air Limbah)
- STP (Sewage Treatment Plant)
- WTP (Water Treatment Plant)
- PDAM (Perusahaan Daerah Air Minum)
- Industri Manufaktur dengan efluent

### Key Features

| Feature                   | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **Parameter Monitoring**  | pH, COD, TSS, Ammonia, BOD, Temperature, Flow       |
| **Real-time Dashboard**   | Live parameter readings dengan trend charts         |
| **Threshold Alerting**    | Automatic alerts when parameters exceed limits      |
| **KLHK Integration**      | Compliance reporting format untuk regulasi RI       |
| **Multi-location**        | Centralized monitoring multiple outlet points       |
| **Historical Analysis**   | Trend analysis dengan date range filtering          |
| **Data Export**           | Excel/CSV export untuk reporting                    |

### Compliance Standards
- **PP 22/2021** - Baku Mutu Air Limbah
- **Permen LHK 5/2014** - Baku Mutu Air Limbah Domestik
- **SNI 6989** - Parameter kualitas air

---

## 2. SURGE Energy Mapping

### Overview
Platform monitoring konsumsi energi untuk building management dan efisiensi energi industri.

### Target Segment
- Gedung Perkantoran
- Pusat Perbelanjaan
- Fasilitas Manufaktur
- Data Center
- Rumah Sakit

### Key Features

| Feature                   | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **kWh Monitoring**        | Real-time electricity consumption tracking          |
| **Device Map**            | Interactive floor plan dengan device locations      |
| **Meter Integration**     | Connection ke smart meters dan energy analyzers     |
| **Token Management**      | Prepaid electricity token monitoring                |
| **Peak Load Analysis**    | Identify peak consumption periods                   |
| **Carbon Footprint**      | CO2 emission calculation (planned)                  |
| **Billing Integration**   | Cost analysis per zone/device                       |

### Supported Devices
- Schneider PM5xxx Series
- ABB Energy Meters
- Janitza Power Analyzers
- Generic Modbus Energy Meters
- SURIOTA SRT-MGATE-1210 Gateway

---

## 3. SURGE Vessel Tracking

### Overview
Platform monitoring armada maritim untuk pelayaran, logistik, dan perikanan.

### Target Segment
- Perusahaan Pelayaran
- Logistik Maritim
- Kapal Tanker
- Armada Perikanan
- Port Authority

### Key Features

| Feature                   | Description                                         |
| ------------------------- | --------------------------------------------------- |
| **GPS Tracking**          | Real-time vessel position on maritime maps          |
| **Fuel Monitoring**       | Fuel consumption and level tracking                 |
| **RPM Monitoring**        | Engine RPM for performance analysis                 |
| **Route History**         | Historical voyage tracking dan playback             |
| **Geofencing**            | Area alerts for port arrival/departure              |
| **Speed Analysis**        | Speed over ground monitoring                        |
| **Fleet Dashboard**       | Overview of entire fleet status                     |

### Integration
- AIS (Automatic Identification System)
- GPS Trackers
- Marine Engine Sensors
- Fuel Flow Meters

---

# Competitor Analysis

## Analisis Kompetitor - IoT Platform / Dashboard

> **FOKUS**: Platform IoT cloud dengan dashboard visualization dan multi-tenant capability

---

### 1. ThingsBoard (Open Source + Professional)

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | ThingsBoard Inc. (USA)              |
| **Product Type**  | Open Source IoT Platform            |
| **Target Market** | Industrial IoT, Smart Building      |

#### Harga

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **Community**     | Free (Open Source)   | Self-hosted, basic features      |
| **Maker**         | $10/month            | 30 devices, cloud hosted         |
| **Prototype**     | $149/month           | 100 devices, rule engine         |
| **Startup**       | $399/month           | 500 devices, white-label         |
| **Business**      | Custom               | Unlimited, enterprise features   |

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan                         |
| ------------------------- | ---------------------------------- |
| Open source option        | Complex setup untuk self-hosted    |
| Powerful rule engine      | Steep learning curve               |
| White-label support       | No local Indonesia support         |
| Multi-protocol support    | Enterprise = mahal                 |

#### vs SURGE

| Aspek             | ThingsBoard Startup | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $399/month          | $99/month      | **SURGE (-75%)**|
| Local Support     | No                  | Yes            | **SURGE**       |
| KLHK Integration  | No                  | Yes            | **SURGE**       |
| Setup Complexity  | High                | Low            | **SURGE**       |
| Multi-module      | Generic             | 3 specialized  | **SURGE**       |

---

### 2. Grafana Cloud

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | Grafana Labs (USA)                  |
| **Product Type**  | Observability & Dashboarding        |
| **Target Market** | DevOps, IT Monitoring               |

#### Harga

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **Free**          | $0                   | 10K metrics, 3 users             |
| **Pro**           | $19/month + usage    | 10 users, alerting               |
| **Advanced**      | $99/month + usage    | SSO, support                     |
| **Enterprise**    | Custom               | Unlimited, dedicated support     |

*Note: Usage-based pricing dapat menjadi mahal untuk high-volume IoT*

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan                         |
| ------------------------- | ---------------------------------- |
| Powerful visualization    | Not IoT-native (need InfluxDB/etc) |
| Large community           | Usage-based = unpredictable cost   |
| Many data source plugins  | No device management               |
| Industry standard         | Requires technical expertise       |

#### vs SURGE

| Aspek             | Grafana Pro         | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| IoT-native        | No (generic)        | Yes            | **SURGE**       |
| Device Management | No                  | Yes            | **SURGE**       |
| MQTT Built-in     | No (plugin)         | Yes            | **SURGE**       |
| Cost Predictable  | No (usage-based)    | Yes            | **SURGE**       |
| Visualization     | Excellent           | Good           | **Grafana**     |

---

### 3. Datacake

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | Datacake GmbH (Germany)             |
| **Product Type**  | Low-Code IoT Platform               |
| **Target Market** | SMB IoT, LoRaWAN, Sensor Networks   |

#### Harga

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **Free**          | €0                   | 2 devices, 30-day retention      |
| **Lite**          | €5/device/month      | Basic dashboard, 3-month         |
| **Business**      | €375/year (1000 dev) | 12-month retention, API          |
| **Enterprise**    | Custom               | White-label, dedicated           |

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan                         |
| ------------------------- | ---------------------------------- |
| Easy setup, low-code      | Limited customization              |
| LoRaWAN integration       | European-focused                   |
| Good for small scale      | Expensive at scale                 |
| Nice templates            | No local Indonesia support         |

#### vs SURGE

| Aspek             | Datacake Business   | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga (annual)    | €375 (~Rp 6.5M)     | $1,188 (~Rp 19M) | **Datacake**   |
| Local Support     | No                  | Yes            | **SURGE**       |
| Customization     | Low-code            | Full access    | **SURGE**       |
| Multi-module      | Generic             | 3 specialized  | **SURGE**       |
| Indonesia Timezone| No                  | Yes            | **SURGE**       |

---

### 4. Blynk

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | Blynk Inc. (USA)                    |
| **Product Type**  | Mobile IoT Platform                 |
| **Target Market** | Hobbyist, Maker, Small Business     |

#### Harga

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **Free**          | $0                   | 2 devices, limited widgets       |
| **Maker**         | $7/month             | 5 devices, automations           |
| **Pro**           | $49/month            | 40 devices, OTA                  |
| **Business**      | $999/year            | 100+ devices, white-label        |

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan                         |
| ------------------------- | ---------------------------------- |
| Mobile-first              | Limited web dashboard              |
| Easy for makers           | Not for enterprise                 |
| Good Arduino support      | Limited industrial protocols       |
| Affordable starter        | Expensive at scale                 |

#### vs SURGE

| Aspek             | Blynk Pro           | SURGE Starter  | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $49/month           | $29/month      | **SURGE (-41%)**|
| Web Dashboard     | Limited             | Full-featured  | **SURGE**       |
| Industrial        | No                  | Yes            | **SURGE**       |
| Mobile App        | Native              | PWA (planned)  | **Blynk**       |
| Local Support     | No                  | Yes            | **SURGE**       |

---

### 5. Ubidots

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | Ubidots (Colombia/USA)              |
| **Product Type**  | IoT Application Enablement Platform |
| **Target Market** | OEM, System Integrator, Enterprise  |

#### Harga

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **STEM**          | Free                 | Educational only                 |
| **Entrepreneur**  | $49/month            | 25 devices, 2-year retention     |
| **Launch**        | $99/month            | 50 devices, 5 organizations      |
| **Scale**         | Custom               | Unlimited, white-label           |

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan                         |
| ------------------------- | ---------------------------------- |
| Clean UI                  | Per-device pricing gets expensive  |
| Good API                  | Limited widget customization       |
| Multi-org support         | No local support                   |
| Nice documentation        | No specific industry modules       |

#### vs SURGE

| Aspek             | Ubidots Launch      | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $99/month           | $99/month      | **TIE**         |
| Devices           | 50                  | Unlimited*     | **SURGE**       |
| Organizations     | 5                   | Multi-tenant   | **TIE**         |
| Industry Modules  | Generic             | 3 specialized  | **SURGE**       |
| Local Support     | No                  | Yes            | **SURGE**       |

*SURGE limits by parameters, not devices

---

### 6. AVEVA Insight (Enterprise SCADA/Cloud)

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | AVEVA (UK, acquired by Schneider)   |
| **Product Type**  | Industrial Cloud Platform           |
| **Target Market** | Large Enterprise, Oil & Gas, Utility|

#### Harga

| Plan              | Price                               |
| ----------------- | ----------------------------------- |
| **Subscription**  | Custom (typically $10,000+/year)    |
| **Per-point**     | Node/point-based licensing          |

#### vs SURGE

| Aspek             | AVEVA Insight       | SURGE Prof     | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $10,000+/year       | $3,588/year    | **SURGE (-64%)**|
| Setup Time        | Months              | Days           | **SURGE**       |
| Complexity        | Very High           | Medium         | **SURGE**       |
| Local Support     | Via Partner         | Direct         | **SURGE**       |
| Scale             | Enterprise          | SMB-Enterprise | **AVEVA**       |

---

### 7. Schneider EcoStruxure

#### Informasi Produk

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Developer**     | Schneider Electric (France)         |
| **Product Type**  | Industrial IoT Architecture         |
| **Target Market** | Building, Industry, Infrastructure  |

#### Harga

| Plan              | Price                               |
| ----------------- | ----------------------------------- |
| **IT Expert**     | Custom (typically $5,000+/year)     |
| **Building Ops**  | Per-site licensing                  |
| **Resource Adv**  | Per-device/resource                 |

#### vs SURGE

| Aspek             | EcoStruxure         | SURGE Prof     | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $5,000+/year        | $3,588/year    | **SURGE (-28%)**|
| Vendor Lock-in    | High (Schneider)    | Open (MQTT)    | **SURGE**       |
| Setup             | Complex             | Simple         | **SURGE**       |
| Brand Trust       | Global              | Emerging       | **EcoStruxure** |

---

### 8. Weintek cMT Cloud / Haiwell Cloud

#### Informasi Produk (HMI-based Cloud)

| Item              | Detail                              |
| ----------------- | ----------------------------------- |
| **Weintek**       | Taiwan HMI manufacturer             |
| **Haiwell**       | China PLC/HMI manufacturer          |
| **Product Type**  | HMI-integrated cloud service        |
| **Target Market** | Machine OEM, Small Factory          |

#### Harga

| Platform          | Price                               |
| ----------------- | ----------------------------------- |
| **Weintek Cloud** | €60-150/HMI/year (subscription)     |
| **Haiwell Cloud** | Free with Haiwell devices           |

#### vs SURGE

| Aspek             | HMI Cloud           | SURGE          | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Vendor Lock-in    | 100% (their HMI)    | Open (any dev) | **SURGE**       |
| Dashboard         | Basic (HMI mirror)  | Full analytics | **SURGE**       |
| Multi-tenant      | Limited             | Full support   | **SURGE**       |
| Cost              | Low (free/included) | Higher         | **HMI Cloud**   |

---

# Feature Comparison

## Matriks Perbandingan Fitur - IoT Platform

### Tabel Perbandingan Lengkap

| Feature             | ThingsBoard | Grafana   | Datacake  | Blynk     | Ubidots   | **SURGE**      |
| ------------------- | ----------- | --------- | --------- | --------- | --------- | -------------- |
| **Harga/bulan**     | $10-$399    | $19+usage | €31/mo    | $7-$49    | $49-$99   | **$29-$299**   |
| **Type**            | Open+Cloud  | Obs/Dash  | Low-code  | Mobile    | AEP       | **SaaS**       |
|                     |             |           |           |           |           |                |
| **Multi-tenant**    | Yes         | No        | Limited   | No        | Yes       | **Yes**        |
| **RBAC**            | Yes         | Yes       | Limited   | Basic     | Yes       | **Yes**        |
| **Device Mgmt**     | Yes         | No        | Yes       | Yes       | Yes       | **Yes**        |
| **MQTT Native**     | Yes         | No        | Yes       | Yes       | Yes       | **Yes**        |
| **REST API**        | Yes         | Yes       | Yes       | Yes       | Yes       | **Yes**        |
| **WebSocket**       | Yes         | Yes       | Limited   | Yes       | Yes       | **Yes**        |
|                     |             |           |           |           |           |                |
| **Water Module**    | No          | No        | No        | No        | No        | **Yes** ✅     |
| **Energy Module**   | Generic     | Generic   | No        | No        | No        | **Yes** ✅     |
| **Maritime Module** | No          | No        | No        | No        | No        | **Yes** ✅     |
| **KLHK Compliance** | No          | No        | No        | No        | No        | **Yes** ✅     |
|                     |             |           |           |           |           |                |
| **Interactive Map** | Yes         | Plugin    | Yes       | No        | Yes       | **Yes**        |
| **Charts**          | Yes         | Excellent | Yes       | Yes       | Yes       | **Yes**        |
| **Alerting**        | Yes         | Yes       | Yes       | Yes       | Yes       | **Yes**        |
| **Data Export**     | Yes         | Yes       | Limited   | No        | Yes       | **Yes**        |
|                     |             |           |           |           |           |                |
| **White-label**     | Pro         | Ent       | Ent       | Business  | Scale     | **Prof**       |
| **Mobile App**      | Yes         | Yes       | No        | Native    | Yes       | **PWA**        |
| **Bahasa Indo**     | No          | No        | No        | No        | No        | **Yes** ✅     |
| **Local Support**   | No          | No        | No        | No        | No        | **Yes** ✅     |
| **Indonesia TZ**    | Manual      | Manual    | Manual    | Manual    | Manual    | **Auto** ✅    |

### Visual Comparison

```
HARGA vs FITUR (IoT Platform Cloud)
─────────────────────────────────────────────────────────────────────

$10,000+ ┤                                         ● AVEVA Insight
         │                                           (Enterprise only)
         │
         │
$5,000   ┤                                     ● EcoStruxure
         │                                       (Schneider lock-in)
         │
         │
$399     ┤         ● ThingsBoard Startup ───────── Open source option
         │                                         Steep learning curve
$299     ┤ ════════ ★ SURGE Professional ═══════ Unlimited + White-label
         │         ↑ ENTERPRISE VALUE ↑           3 Industry Modules
         │
$99      ┤ ════════ ★ SURGE Business ════════════ 25 params, 10 locations
         │         ↑ BEST VALUE ↑                 KLHK + Local Support
         │
         │         ● Ubidots Launch ─────────────── Good platform, generic
         │
$49      ┤ ● Blynk Pro ──────────────────────────── Mobile-first only
         │
$29      ┤ ════════ ★ SURGE Starter ════════════ Entry-level business
         │
$19      ┤ ● Grafana Pro ────────────────────────── + Usage fees
         │
$10      ┤ ● ThingsBoard Maker ──────────────────── Very limited
         │
Free     ┤ ● Community editions ─────────────────── Self-hosted only
         │
         └─────────────────────────────────────────────────────────────
               FITUR IoT  ─────────────────────────────────────────→

Keterangan:
● = Competitor platforms
★ = SURGE (Best Value - Local + Industry-Specific + KLHK)
```

### Kesimpulan Perbandingan

**SURGE adalah SATU-SATUNYA platform IoT di pasar Indonesia yang memiliki:**

1. ✅ **3 Modul Industri Terintegrasi** (Water, Energy, Vessel)
2. ✅ **KLHK Compliance** untuk monitoring lingkungan Indonesia
3. ✅ **Multi-tenant Architecture** dengan full data isolation
4. ✅ **Support Bahasa Indonesia** dan timezone WIB
5. ✅ **Harga Kompetitif** di mid-range ($29-$299/month)
6. ✅ **Local Support** dari vendor lokal
7. ✅ **Integrasi Hardware SURIOTA** (SRT-MGATE-1210 gateway)

---

# Pricing Strategy

## Strategi Penetapan Harga

### Subscription Tiers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SURGE PRICING TIERS                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TRIAL (Free)                                                               │
│  ─────────────────                                                          │
│  • 5 parameters          • 1 location          • 30-day retention           │
│  • Basic dashboard       • Community support   • No white-label             │
│  IDEAL FOR: Testing, Proof of Concept                                       │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STARTER ($29/month = Rp 464.000)                                           │
│  ─────────────────────────────────                                          │
│  • 10 parameters         • 3 locations         • 90-day retention           │
│  • Standard dashboard    • Email support       • Data export                │
│  IDEAL FOR: Small business, single facility                                 │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BUSINESS ($99/month = Rp 1.584.000) ★ MOST POPULAR                        │
│  ─────────────────────────────────────────────────                          │
│  • 25 parameters         • 10 locations        • 1-year retention           │
│  • Advanced dashboard    • Priority support    • Full API access            │
│  • Custom alerts         • Team management     • Advanced analytics         │
│  IDEAL FOR: Medium business, multi-facility                                 │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PROFESSIONAL ($299/month = Rp 4.784.000)                                   │
│  ─────────────────────────────────────────                                  │
│  • Unlimited parameters  • Unlimited locations • 3-year retention           │
│  • White-label branding  • Dedicated support   • Custom integration         │
│  • SLA agreement         • Training included   • Priority feature requests  │
│  IDEAL FOR: Enterprise, System Integrator, Government                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Annual Discount

| Plan         | Monthly    | Annual (20% off)  | Savings      |
| ------------ | ---------- | ----------------- | ------------ |
| Starter      | $29/mo     | $278/year         | $70          |
| Business     | $99/mo     | $950/year         | $238         |
| Professional | $299/mo    | $2,870/year       | $718         |

### Add-on Services

| Service                    | Price                | Description                    |
| -------------------------- | -------------------- | ------------------------------ |
| **Extra Locations**        | $10/location/month   | Beyond tier limit              |
| **Extra Parameters**       | $5/parameter/month   | Beyond tier limit              |
| **Extended Retention**     | $20/year/additional  | +1 year data retention         |
| **Custom Integration**     | $500 one-time        | Custom API/webhook setup       |
| **On-site Training**       | $300/session         | 4-hour training session        |
| **White-label Setup**      | $1,000 one-time      | Custom branding implementation |

---

# Unique Selling Proposition (USP)

## Mengapa SURGE Berbeda

### 1. SATU Platform, 3 Modul Industri

```
SURGE ONE PLATFORM ADVANTAGE
─────────────────────────────────────────────────────────────────────

    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
    │ WATER ANALYTICS │    │ ENERGY MAPPING  │    │ VESSEL TRACKING │
    ├─────────────────┤    ├─────────────────┤    ├─────────────────┤
    │ • IPAL/STP/WTP  │    │ • Building Mgmt │    │ • Fleet Monitor │
    │ • KLHK Compliant│    │ • Energy Audit  │    │ • Fuel Tracking │
    │ • pH/COD/TSS    │    │ • kWh Analysis  │    │ • GPS/RPM       │
    └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │         SURGE PLATFORM        │
                    │   Single Dashboard, Single    │
                    │   Subscription, Single Login  │
                    └───────────────────────────────┘
```

**Kompetitor** harus beli 3 platform terpisah untuk coverage yang sama!

### 2. KLHK Compliance Ready

- Format laporan sesuai PP 22/2021
- Parameter standar KLHK
- Export untuk SISPEK (Sistem Pelaporan Elektronik Kualitas)
- **Tidak ada platform lain yang punya fitur ini!**

### 3. Full Indonesia Localization

| Feature            | Kompetitor          | SURGE              |
| ------------------ | ------------------- | ------------------ |
| Bahasa Indonesia   | Tidak               | **Ya**             |
| Timezone WIB       | Manual setting      | **Otomatis**       |
| Regulasi RI        | Tidak               | **Built-in**       |
| Support Lokal      | Email (Inggris)     | **WA + Phone**     |
| Invoice IDR        | Tidak               | **Ya**             |

### 4. Hardware Integration (SURIOTA Ecosystem)

```
SURIOTA COMPLETE SOLUTION
─────────────────────────────────────────────────────────────────────

    ┌────────────────────┐          ┌────────────────────┐
    │  SRT-MGATE-1210    │          │   SURGE PLATFORM   │
    │  Modbus Gateway    │ ─────────│   Cloud Dashboard  │
    │  (Hardware)        │   MQTT   │   (Software)       │
    └────────────────────┘          └────────────────────┘

    Rp 2.7M hardware + $99/mo software = COMPLETE IoT SOLUTION

    ✓ Tested & Certified compatible
    ✓ Pre-configured connection
    ✓ Single vendor support
```

---

# Target Market & Segmentation

## Market Segmentation

### Primary Market: Industrial Monitoring

| Segment              | Size (Indonesia)    | Pain Point                      |
| -------------------- | ------------------- | ------------------------------- |
| **IPAL/STP**         | 5,000+ facilities   | Manual reporting to KLHK        |
| **Manufacturing**    | 30,000+ factories   | No real-time monitoring         |
| **Building Mgmt**    | 10,000+ buildings   | Energy waste, no visibility     |

### Secondary Market: Government & Utility

| Segment              | Size (Indonesia)    | Pain Point                      |
| -------------------- | ------------------- | ------------------------------- |
| **PDAM**             | 400+ perusahaan     | Legacy systems, no analytics    |
| **Port Authority**   | 100+ ports          | No vessel tracking integration  |
| **Local Government** | 500+ Pemda          | Environmental compliance        |

### Tertiary Market: System Integrators

| Segment              | Size (Indonesia)    | Pain Point                      |
| -------------------- | ------------------- | ------------------------------- |
| **SI/VAR**           | 200+ companies      | Need white-label platform       |
| **Consulting**       | 100+ firms          | Need monitoring tools           |

## Target Customer Profile

### Ideal Customer Characteristics

| Criteria             | Profile                              |
| -------------------- | ------------------------------------ |
| **Size**             | 10-500 employees                     |
| **IT Capability**    | Basic (not developer-heavy)          |
| **Budget**           | $1,000-10,000/year for IoT           |
| **Pain**             | Manual monitoring, compliance risk   |
| **Decision Maker**   | Ops Manager, Environment Manager     |
| **Industry**         | Manufacturing, Utility, Maritime     |

---

# Sales & Marketing Guide

## Go-to-Market Strategy

### Direct Sales Focus

| Channel              | Target             | Conversion Rate    |
| -------------------- | ------------------ | ------------------ |
| **LinkedIn Outbound**| Ops/Env Managers   | 3-5%               |
| **Trade Shows**      | Industry events    | 5-10%              |
| **Referral**         | Existing customers | 15-20%             |
| **Partner SI**       | System Integrators | 10-15%             |

### Sales Pitch Templates

#### 30-Second Elevator Pitch

> "SURGE adalah platform IoT untuk monitoring industri yang punya 3 modul dalam 1 dashboard - Water Analytics untuk IPAL, Energy Mapping untuk gedung, dan Vessel Tracking untuk armada. Bedanya dengan ThingsBoard atau Grafana? Kami sudah siap untuk compliance KLHK, support dalam Bahasa Indonesia, dan 75% lebih murah. Mulai dari Rp 464 ribu per bulan."

#### Pain-Agitate-Solution

> **Pain**: "Sekarang monitoring IPAL masih manual? Data dikirim ke KLHK pakai Excel?"
>
> **Agitate**: "Kalau telat lapor atau data tidak akurat, sanksinya bisa sampai pencabutan izin operasi. Belum lagi waktu yang terbuang untuk compile data setiap bulan."
>
> **Solution**: "SURGE Water Analytics otomatis mengumpulkan data sensor 24/7, format langsung sesuai standar KLHK, tinggal export dan kirim. Mulai dari Rp 464 ribu per bulan."

### Objection Handling Quick Reference

| Objection                  | Response                                                    |
| -------------------------- | ----------------------------------------------------------- |
| "Sudah pakai platform X"   | "SURGE bisa jalan parallel, atau import data lama Anda"     |
| "Terlalu mahal"            | "Coba hitung biaya manual reporting + risiko compliance"    |
| "Brand baru, tidak yakin"  | "Trial gratis 30 hari, buktikan sendiri"                    |
| "IT kami tidak capable"    | "Setup kami yang handle, Anda tinggal pakai"                |
| "Tidak butuh 3 modul"      | "Bayar hanya yang dipakai, modul lain bonus kalau butuh"    |

---

# Financial Projections

## Year 1 Targets

| Metric               | Q1        | Q2        | Q3        | Q4        | **Total** |
| -------------------- | --------- | --------- | --------- | --------- | --------- |
| **New Customers**    | 5         | 10        | 15        | 20        | **50**    |
| **MRR**              | $1,500    | $4,500    | $9,000    | $15,000   | -         |
| **ARR (End)**        | $18,000   | $54,000   | $108,000  | $180,000  | **$180K** |
| **Churn Rate**       | 5%        | 4%        | 3%        | 2%        | -         |

## Revenue Mix Projection

| Tier          | % of Customers | Avg Revenue    | Contribution   |
| ------------- | -------------- | -------------- | -------------- |
| Trial         | 30%            | $0             | $0             |
| Starter       | 30%            | $29/mo         | 25%            |
| Business      | 30%            | $99/mo         | 50%            |
| Professional  | 10%            | $299/mo        | 25%            |

## Unit Economics

| Metric               | Value              | Calculation                     |
| -------------------- | ------------------ | ------------------------------- |
| **ARPU**             | $60/month          | Weighted average                |
| **CAC**              | $300               | Marketing + Sales cost          |
| **LTV**              | $1,440             | 24 months x $60                 |
| **LTV:CAC Ratio**    | 4.8x               | Target >3x                      |
| **Payback Period**   | 5 months           | CAC / ARPU                      |
| **Gross Margin**     | 85%                | SaaS standard                   |

---

# Appendix

## A. SURGE Demo Access

| Item          | Value                                           |
| ------------- | ----------------------------------------------- |
| **URL**       | https://surge-nextjs-frontend.cp.suriotadb.com  |
| **Login**     | admin@suriota.com                               |
| **Password**  | (Contact sales)                                 |

## B. Technical Documentation

| Document              | Location                           |
| --------------------- | ---------------------------------- |
| **API Documentation** | http://localhost:4000/api (Swagger)|
| **PRD**               | surge-energy-map-frontend/PRD.md   |
| **Frontend Repo**     | surge-energy-map-frontend/         |
| **Backend Repo**      | surge--water-analytics-backend/    |

## C. Contact Information

**PT Surya Inovasi Prioritas (SURIOTA)**

| Channel       | Contact                   |
| ------------- | ------------------------- |
| **Website**   | www.suriota.com           |
| **Email**     | sales@suriota.com         |
| **Phone**     | +62 858-3567-2476         |
| **GitHub**    | github.com/suriota-dev    |

---

_Document Version: 1.0_
_Last Updated: December 28, 2025_
_Prepared by: Product Development Team_
