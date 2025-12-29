# SURGE Business Analysis & Pricing Strategy

## Dokumen Analisis Bisnis untuk Finance & Marketing

**Document Version**: 2.0
**Last Updated**: December 29, 2025
**Prepared by**: Product Development Team
**Exchange Rate**: 1 USD = Rp 16,000 (rounded for calculation)

---

# REKOMENDASI HARGA FINAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    HARGA JUAL RESMI SURGE PLATFORM                          │
│                        (Updated: December 29, 2025)                         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  PLAN                │  HARGA/BULAN     │  TAG DATA   │  LOKASI    │   │
│   ├──────────────────────┼──────────────────┼─────────────┼────────────┤   │
│   │  Trial (Free)        │  Rp 0            │  5 tags     │  Unlimited │   │
│   │  (Private/Invitation)│                  │             │            │   │
│   │                      │                  │             │            │   │
│   │  Starter             │  Rp 464.000      │  30 tags    │  Unlimited │   │
│   │                      │  ($29/month)     │             │            │   │
│   │                      │                  │             │            │   │
│   │  Business            │  Rp 1.584.000    │  100 tags   │  Unlimited │   │
│   │                      │  ($99/month)     │             │            │   │
│   │                      │                  │             │            │   │
│   │  Professional        │  Rp 4.784.000    │  Unlimited  │  Unlimited │   │
│   │                      │  ($299/month)    │             │            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   POSITIONING:                                                              │
│   • 75% lebih murah dari ThingsBoard PE ($399/mo vs $99/mo)                │
│   • 34% lebih murah dari ThingsBoard Prototype ($149/mo vs $99/mo)         │
│   • Same price as Ubidots Launch tapi 2x lebih banyak tags (100 vs 50)     │
│   • Lokasi UNLIMITED di semua tier (kompetitor biasanya limited)           │
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
3. [Platform Features](#platform-features)
4. [Module Details](#module-details)
5. [Competitor Analysis](#competitor-analysis)
6. [Feature Comparison](#feature-comparison)
7. [Pricing Strategy](#pricing-strategy)
8. [Unique Selling Proposition (USP)](#unique-selling-proposition-usp)
9. [Target Market & Segmentation](#target-market--segmentation)
10. [Cost Structure](#cost-structure)
11. [Sales & Marketing Guide](#sales--marketing-guide)
12. [Financial Projections](#financial-projections)

---

# Executive Summary

## Ringkasan Eksekutif

**SURGE (Suriota Governance Ecosystem)** adalah platform **Multi-Tenant SaaS** produksi lokal PT Surya Inovasi Prioritas (SURIOTA) yang dirancang untuk monitoring IoT industri dengan **3 modul terintegrasi**:

1. **Water Analytics** - Monitoring kualitas air (IPAL/STP/WTP/PDAM)
2. **Energy Mapping** - Monitoring konsumsi energi gedung/industri
3. **Vessel Tracking** - Monitoring armada kapal maritim
4. **Custom Use Cases** - Dapat disesuaikan untuk kebutuhan monitoring lainnya

### Key Highlights:

| Metric                     | Value                                   |
| -------------------------- | --------------------------------------- |
| **Target Market**          | Industrial IoT Indonesia                |
| **Competitive Position**   | Mid-range dengan fitur enterprise       |
| **Price Point**            | $29 - $299/month                        |
| **Target ARR**             | $100,000 dalam 12 bulan                 |
| **Target Organizations**   | 50+ organisasi aktif tahun pertama      |
| **Data Retention**         | 30 hari - 5 tahun (per tier)            |

### Keunggulan Kompetitif:

- **SATU-SATUNYA** platform IoT Indonesia dengan **3 modul industri terintegrasi**
- **KLHK Compliance Ready** untuk monitoring lingkungan
- **Produksi Lokal** = Support Bahasa Indonesia, timezone WIB, regulasi lokal
- **75% lebih murah** dari ThingsBoard Professional dengan fitur setara
- **Multi-tenant architecture** dengan full data isolation
- **Unlimited lokasi** di semua tier (kompetitor biasanya limited)

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

# Platform Features

## Fitur-Fitur Utama SURGE

### 1. Live Monitoring / Real-time Dashboard

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Real-time Data**       | Data sensor terupdate secara real-time via MQTT     |
| **Live Reading Interval**| Tergantung sensor/user - SURGE menyesuaikan         |
| **Auto-refresh**         | Dashboard auto-refresh tanpa reload halaman         |
| **Device Status**        | Tampilan online/offline status perangkat            |

### 2. Interactive Charts & Analytics

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Line Charts**          | Trend data historis dengan zoom & pan               |
| **Bar Charts**           | Perbandingan data antar periode/lokasi              |
| **Gauge Charts**         | Visualisasi real-time untuk single parameter        |
| **Scatter Plots**        | Korelasi antar parameter                            |
| **Heatmap**              | Visualisasi data spasial (planned)                  |
| **Date Range Filter**    | Filter data berdasarkan rentang waktu               |
| **Export Chart**         | Download chart sebagai image                        |

### 3. Database Logging & Retention

| Tier         | Logging Interval | Data Retention | Storage Est. |
| ------------ | :--------------: | :------------: | :----------: |
| Trial        | 2 menit          | 30 hari        | ~100MB       |
| Starter      | 1 menit          | 1 tahun        | ~1GB         |
| Business     | 1 menit          | 2 tahun        | ~5GB         |
| Professional | Customizable     | 5 tahun        | ~20GB        |

> **Catatan:**
> - Interval logging ke database berbeda dengan interval live monitoring
> - Live monitoring: real-time sesuai kiriman sensor
> - Database logging: interval tetap untuk penyimpanan historis

### 4. Role Access Management (RBAC)

| Role         | Permissions                                         |
| ------------ | --------------------------------------------------- |
| **Viewer**   | View dashboard & data only                          |
| **Member**   | View + Export data                                  |
| **Admin**    | View + Export + Manage devices & alerts             |
| **Owner**    | Full access + Manage users & organization settings  |

### 5. Map View & Location Management

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Interactive Map**      | Mapbox GL JS dengan satellite/street view           |
| **Device Markers**       | Pin lokasi perangkat dengan status indicator        |
| **Cluster View**         | Grouping untuk banyak device dalam satu area        |
| **Geofencing**           | Alert ketika device keluar/masuk area (Vessel)      |
| **Route Playback**       | Replay rute historis (Vessel)                       |

### 6. Alert & Notification System

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Threshold Alerts**     | Alert ketika parameter melebihi batas               |
| **Email Notification**   | Notifikasi via email                                |
| **WhatsApp Alerts**      | Notifikasi via WhatsApp (planned)                   |
| **Alert History**        | Log semua alert yang pernah terjadi                 |
| **Escalation**           | Multi-level escalation (planned)                    |

### 7. Data Export & Reporting

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Excel Export**         | Download data dalam format .xlsx                    |
| **CSV Export**           | Download data dalam format .csv                     |
| **KLHK Format**          | Export sesuai format SISPEK (Water Analytics)       |
| **Custom Report**        | Report builder (planned)                            |
| **Scheduled Report**     | Auto-export report berkala (planned)                |

### 8. API & Integration

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **REST API**             | Full API access untuk integrasi                     |
| **MQTT Broker**          | Direct MQTT publish/subscribe                       |
| **Webhook**              | Push data ke sistem eksternal                       |
| **API Documentation**    | Swagger/OpenAPI documentation                       |

### 9. Multi-tenant Architecture

| Feature                  | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Data Isolation**       | Setiap organisasi data terisolasi penuh             |
| **Custom Branding**      | Logo & warna organisasi (Professional)              |
| **Separate Login**       | Akun terpisah per organisasi                        |
| **Resource Allocation**  | Quota management per organisasi                     |

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

## 4. Custom Use Cases

SURGE platform dapat digunakan untuk berbagai kebutuhan monitoring lainnya:

| Use Case                  | Parameters                                          |
| ------------------------- | --------------------------------------------------- |
| **Cold Chain**            | Temperature, Humidity, Door status                  |
| **Agriculture**           | Soil moisture, Temperature, Humidity                |
| **HVAC Monitoring**       | Temperature, Pressure, Airflow                      |
| **Tank Level**            | Level, Temperature, Pressure                        |
| **Machine Monitoring**    | Vibration, Temperature, Runtime                     |

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

#### Harga (Cloud)

| Plan              | Price                | Features                         |
| ----------------- | -------------------- | -------------------------------- |
| **Community**     | Free (Open Source)   | Self-hosted, basic features      |
| **Maker**         | $10/month            | 30 devices, cloud hosted         |
| **Prototype**     | $149/month           | 100 devices, rule engine         |
| **Startup**       | $399/month           | 500 devices, white-label         |
| **Business**      | Custom               | Unlimited, enterprise features   |

#### vs SURGE

| Aspek             | ThingsBoard Startup | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $399/month          | $99/month      | **SURGE (-75%)**|
| Local Support     | No                  | Yes            | **SURGE**       |
| KLHK Integration  | No                  | Yes            | **SURGE**       |
| Setup Complexity  | High                | Low            | **SURGE**       |
| Lokasi            | Limited             | Unlimited      | **SURGE**       |

---

### 2. Ubidots

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

#### vs SURGE

| Aspek             | Ubidots Launch      | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $99/month           | $99/month      | **TIE**         |
| Tags/Devices      | 50 devices          | 100 tags       | **SURGE (2x)**  |
| Lokasi            | 5 organizations     | Unlimited      | **SURGE**       |
| Industry Modules  | Generic             | 3 specialized  | **SURGE**       |
| Local Support     | No                  | Yes            | **SURGE**       |
| Retention         | 2 years             | 2 years        | **TIE**         |

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
| **Free**          | €0                   | 5 devices, 7-day retention       |
| **Pay-as-you-go** | €2-5/device/month    | Per device pricing               |
| **Light**         | €150/month           | 50 devices, 1-month retention    |
| **Standard**      | €375/month           | 200 devices, 12-month retention  |
| **Plus**          | €625/month           | 1000 devices, 12-month retention |

#### vs SURGE

| Aspek             | Datacake Standard   | SURGE Business | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | €375/mo (~$400)     | $99/month      | **SURGE (-75%)**|
| Devices/Tags      | 200 devices         | 100 tags       | Datacake        |
| Retention         | 12 months           | 24 months      | **SURGE (2x)**  |
| Lokasi            | Limited             | Unlimited      | **SURGE**       |
| Local Support     | No                  | Yes            | **SURGE**       |
| Industry Modules  | Generic             | 3 specialized  | **SURGE**       |

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
| **Maker**         | $6.99/month          | 5 devices, automations           |
| **Pro**           | $49/month            | 40 devices, OTA                  |
| **Business**      | $999/year            | 100+ devices, white-label        |

#### vs SURGE

| Aspek             | Blynk Pro           | SURGE Starter  | Winner          |
| ----------------- | ------------------- | -------------- | --------------- |
| Harga             | $49/month           | $29/month      | **SURGE (-41%)**|
| Web Dashboard     | Limited             | Full-featured  | **SURGE**       |
| Tags              | 40 devices          | 30 tags        | Blynk           |
| Industrial Focus  | No                  | Yes            | **SURGE**       |
| Local Support     | No                  | Yes            | **SURGE**       |

---

# Feature Comparison

## Matriks Perbandingan Fitur - IoT Platform

| Feature             | ThingsBoard | Ubidots   | Datacake  | Blynk     | **SURGE**      |
| ------------------- | ----------- | --------- | --------- | --------- | -------------- |
| **Harga/bulan**     | $10-$399    | $49-$99   | €150-€625 | $7-$83    | **$29-$299**   |
| **Type**            | Open+Cloud  | AEP       | Low-code  | Mobile    | **SaaS**       |
|                     |             |           |           |           |                |
| **Multi-tenant**    | Yes         | Yes       | Limited   | No        | **Yes**        |
| **RBAC**            | Yes         | Yes       | Limited   | Basic     | **Yes**        |
| **Device Mgmt**     | Yes         | Yes       | Yes       | Yes       | **Yes**        |
| **MQTT Native**     | Yes         | Yes       | Yes       | Yes       | **Yes**        |
| **REST API**        | Yes         | Yes       | Yes       | Yes       | **Yes**        |
|                     |             |           |           |           |                |
| **Water Module**    | No          | No        | No        | No        | **Yes**        |
| **Energy Module**   | Generic     | Generic   | No        | No        | **Yes**        |
| **Maritime Module** | No          | No        | No        | No        | **Yes**        |
| **KLHK Compliance** | No          | No        | No        | No        | **Yes**        |
|                     |             |           |           |           |                |
| **Interactive Map** | Yes         | Yes       | Yes       | No        | **Yes**        |
| **Charts**          | Yes         | Yes       | Yes       | Yes       | **Yes**        |
| **Alerting**        | Yes         | Yes       | Yes       | Yes       | **Yes**        |
| **Data Export**     | Yes         | Yes       | Limited   | No        | **Yes**        |
|                     |             |           |           |           |                |
| **Unlimited Lokasi**| No          | No        | No        | No        | **Yes**        |
| **Bahasa Indo**     | No          | No        | No        | No        | **Yes**        |
| **Local Support**   | No          | No        | No        | No        | **Yes**        |
| **Indonesia TZ**    | Manual      | Manual    | Manual    | Manual    | **Auto**       |

---

# Pricing Strategy

## Strategi Penetapan Harga

### Subscription Tiers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SURGE PRICING TIERS v2.0                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TRIAL (Free) - PRIVATE ACCESS                                              │
│  ─────────────────────────────────                                          │
│  • 5 tag data/parameter    • UNLIMITED lokasi   • 30-day retention          │
│  • 2-minute logging        • Basic dashboard    • Email support only        │
│  • Akses via invitation dari tim SURIOTA (tidak publik)                     │
│  IDEAL FOR: Demo, Proof of Concept, Evaluasi produk                         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  STARTER ($29/month = Rp 464.000)                                           │
│  ─────────────────────────────────                                          │
│  • 30 tag data/parameter   • UNLIMITED lokasi   • 1-year retention          │
│  • 1-minute logging        • Full dashboard     • Email + WA support        │
│  • Data export             • All modules        • API access (limited)      │
│  IDEAL FOR: Small business, single facility, pilot project                  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BUSINESS ($99/month = Rp 1.584.000) ★ MOST POPULAR                        │
│  ─────────────────────────────────────────────────                          │
│  • 100 tag data/parameter  • UNLIMITED lokasi   • 2-year retention          │
│  • 1-minute logging        • Advanced dashboard • Priority support          │
│  • Full API access         • All modules        • Custom alerts             │
│  • Team management         • Advanced analytics • Dedicated training        │
│  IDEAL FOR: Medium business, multi-facility, growing organizations         │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PROFESSIONAL ($299/month = Rp 4.784.000)                                   │
│  ─────────────────────────────────────────                                  │
│  • UNLIMITED tag data      • UNLIMITED lokasi   • 5-year retention          │
│  • Customizable logging    • White-label        • Dedicated support         │
│  • Custom integration      • SLA agreement      • Training included         │
│  • Priority features       • On-site support    • Custom reports            │
│  IDEAL FOR: Enterprise, System Integrator, Government                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Perbandingan Detail per Tier

| Feature                    | Trial    | Starter  | Business | Professional |
| -------------------------- | :------: | :------: | :------: | :----------: |
| **Harga/bulan**            | Free     | $29      | $99      | $299         |
| **Tag Data/Parameter**     | 5        | 30       | 100      | Unlimited    |
| **Lokasi**                 | Unlimited| Unlimited| Unlimited| Unlimited    |
| **Logging Interval**       | 2 menit  | 1 menit  | 1 menit  | Custom       |
| **Data Retention**         | 30 hari  | 1 tahun  | 2 tahun  | 5 tahun      |
|                            |          |          |          |              |
| **Live Monitoring**        | ✓        | ✓        | ✓        | ✓            |
| **Interactive Charts**     | ✓        | ✓        | ✓        | ✓            |
| **Map View**               | ✓        | ✓        | ✓        | ✓            |
| **Alert/Notification**     | Basic    | Full     | Full     | Custom       |
| **Data Export**            | Limited  | ✓        | ✓        | ✓            |
|                            |          |          |          |              |
| **All Modules (Water/Energy/Vessel)** | ✓ | ✓   | ✓        | ✓            |
| **KLHK Compliance Export** | ✓        | ✓        | ✓        | ✓            |
| **API Access**             | -        | Limited  | Full     | Full         |
| **White-label**            | -        | -        | -        | ✓            |
|                            |          |          |          |              |
| **Role Management**        | 1 user   | 3 users  | 10 users | Unlimited    |
| **Support Response**       | 48 jam   | 24 jam   | 8 jam    | 4 jam        |
| **Support Channel**        | Email    | Email+WA | +Phone   | +On-site     |

### Akses Trial - Private/Invitation Only

> **PENTING**: Trial tier TIDAK tersedia untuk publik.
>
> Untuk mendapatkan akses trial:
> 1. Customer menghubungi tim SURIOTA via sales@suriota.com atau WhatsApp
> 2. Tim SURIOTA melakukan discovery call untuk memahami kebutuhan
> 3. Tim SURIOTA membuat akun trial khusus untuk customer
> 4. Data setiap organisasi terisolasi (multi-tenant)
>
> **Tujuan**: Memastikan onboarding yang proper dan conversion yang lebih baik.

### Annual Discount

| Plan         | Monthly    | Annual (20% off)  | Savings      |
| ------------ | ---------- | ----------------- | ------------ |
| Starter      | $29/mo     | $278/year         | $70          |
| Business     | $99/mo     | $950/year         | $238         |
| Professional | $299/mo    | $2,870/year       | $718         |

### Add-on Services

| Service                    | Price                | Description                    |
| -------------------------- | -------------------- | ------------------------------ |
| **Extra Tags**             | $2/tag/month         | Beyond tier limit              |
| **Extended Retention**     | $50/year/additional  | +1 year data retention         |
| **Custom Integration**     | $500 one-time        | Custom API/webhook setup       |
| **On-site Training**       | $300/session         | 4-hour training session        |
| **White-label Setup**      | $1,000 one-time      | Custom branding implementation |
| **SMS/WA Alerts**          | $20/month            | Additional notification channel|

---

# Unique Selling Proposition (USP)

## Mengapa SURGE Berbeda

### 1. SATU Platform, 3+ Modul Industri

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

### 2. UNLIMITED Lokasi di Semua Tier

| Tier         | SURGE   | ThingsBoard | Ubidots | Datacake |
| ------------ | :-----: | :---------: | :-----: | :------: |
| Entry        | **∞**   | Limited     | 1       | Limited  |
| Mid-tier     | **∞**   | Limited     | 5       | Limited  |
| Enterprise   | **∞**   | Unlimited   | Custom  | Custom   |

### 3. KLHK Compliance Ready

- Format laporan sesuai PP 22/2021
- Parameter standar KLHK
- Export untuk SISPEK (Sistem Pelaporan Elektronik Kualitas)
- **Tidak ada platform lain yang punya fitur ini!**

### 4. Full Indonesia Localization

| Feature            | Kompetitor          | SURGE              |
| ------------------ | ------------------- | ------------------ |
| Bahasa Indonesia   | Tidak               | **Ya**             |
| Timezone WIB       | Manual setting      | **Otomatis**       |
| Regulasi RI        | Tidak               | **Built-in**       |
| Support Lokal      | Email (Inggris)     | **WA + Phone**     |
| Invoice IDR        | Tidak               | **Ya**             |

### 5. Hardware Integration (SURIOTA Ecosystem)

```
SURIOTA COMPLETE SOLUTION
─────────────────────────────────────────────────────────────────────

    ┌────────────────────┐          ┌────────────────────┐
    │  SRT-MGATE-1210    │          │   SURGE PLATFORM   │
    │  Modbus Gateway    │ ─────────│   Cloud Dashboard  │
    │  (Hardware)        │   MQTT   │   (Software)       │
    └────────────────────┘          └────────────────────┘

    Rp 2.7M hardware + $29/mo software = COMPLETE IoT SOLUTION

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

---

# Cost Structure

## Struktur Biaya SURGE

### Operational Costs (Current)

| Item                       | Cost/Month     | Notes                          |
| -------------------------- | -------------- | ------------------------------ |
| **Server Infrastructure**  | Rp 150.000     | VPS/Cloud hosting              |
| **Domain & SSL**           | ~Rp 50.000     | Annual prorated                |
| **MQTT Broker**            | Included       | Self-hosted                    |
| **Database (TimescaleDB)** | Included       | Self-hosted                    |
| **Total Infra**            | **~Rp 200.000**|                                |

### Gross Margin Calculation

| Plan         | Revenue/Mo  | Est. Cost/Mo | Gross Margin |
| ------------ | ----------- | ------------ | :----------: |
| Starter      | Rp 464.000  | Rp 20.000    | **96%**      |
| Business     | Rp 1.584.000| Rp 50.000    | **97%**      |
| Professional | Rp 4.784.000| Rp 150.000   | **97%**      |

> **Note**: SaaS industry standard gross margin = 80-90%. SURGE > 95% karena infrastructure cost sangat rendah saat ini. Akan adjust seiring scale.

### Break-even Analysis

| Scenario           | Customers Needed | Monthly Revenue |
| ------------------ | :--------------: | --------------- |
| **Cover infra only** | 1 Starter      | Rp 464.000      |
| **1 person salary**  | 10 Starter     | Rp 4.640.000    |
| **Target ARR $100K** | 17 Business    | ~Rp 26.9M/mo    |

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

> "SURGE adalah platform IoT untuk monitoring industri yang punya 3 modul dalam 1 dashboard - Water Analytics untuk IPAL, Energy Mapping untuk gedung, dan Vessel Tracking untuk armada. Bedanya dengan ThingsBoard atau Grafana? Kami sudah siap untuk compliance KLHK, support dalam Bahasa Indonesia, lokasi unlimited di semua paket, dan 75% lebih murah. Mulai dari Rp 464 ribu per bulan untuk 30 tag data."

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
| Starter       | 35%            | $29/mo         | 30%            |
| Business      | 25%            | $99/mo         | 45%            |
| Professional  | 10%            | $299/mo        | 25%            |

---

# Appendix

## A. SURGE Demo Access

| Item          | Value                                           |
| ------------- | ----------------------------------------------- |
| **URL**       | https://surge-nextjs-frontend.cp.suriotadb.com  |
| **Login**     | Contact sales@suriota.com for demo account      |

## B. Contact Information

**PT Surya Inovasi Prioritas (SURIOTA)**

| Channel       | Contact                   |
| ------------- | ------------------------- |
| **Website**   | www.suriota.com           |
| **Email**     | sales@suriota.com         |
| **Phone**     | +62 858-3567-2476         |
| **GitHub**    | github.com/suriota-dev    |

---

_Document Version: 2.0_
_Last Updated: December 29, 2025_
_Prepared by: Product Development Team_
