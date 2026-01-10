# SRICARE - Business Analysis

## Analisis Bisnis Lengkap | Complete Business Analysis

> Version 1.0 | January 2026

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Market Background](#2-market-background)
3. [Problem Statement](#3-problem-statement)
4. [Solution Overview](#4-solution-overview)
5. [Target Market Analysis](#5-target-market-analysis)
6. [Market Size & Opportunity](#6-market-size--opportunity)
7. [SWOT Analysis](#7-swot-analysis)
8. [Business Model](#8-business-model)
9. [Go-to-Market Strategy](#9-go-to-market-strategy)
10. [Financial Projections](#10-financial-projections)
11. [Risk Analysis](#11-risk-analysis)
12. [Implementation Roadmap](#12-implementation-roadmap)

---

## 1. Executive Summary

### EN | English

**SRICARE** is a location-based on-demand mobile application that connects users with professional caregivers for patient companion services in hospitals, dialysis accompaniment, medical appointment assistance, and home care services.

**Key Highlights:**

- **First-mover advantage** in Batam market (no dedicated competitor)
- **Target**: Perantau/migrant workers who need care support for family
- **Model**: Gojek-style marketplace with GPS-based matching
- **Integration**: Potential integration with SURGE Platform ecosystem

### ID | Bahasa Indonesia

**SRICARE** adalah aplikasi mobile berbasis lokasi yang menghubungkan pengguna dengan Caregiver profesional untuk layanan pendampingan pasien di rumah sakit, menemani cuci darah, menemani berobat, dan perawatan di rumah.

**Highlight Utama:**

- **First-mover advantage** di pasar Batam (belum ada kompetitor dedicated)
- **Target**: Perantau/anak rantau yang butuh support care untuk keluarga
- **Model**: Marketplace ala Gojek dengan GPS-based matching
- **Integrasi**: Potensi integrasi dengan ekosistem SURGE Platform

---

## 2. Market Background

### 2.1 Indonesia Healthcare Landscape

| Metric                        | Value                       | Source              |
| ----------------------------- | --------------------------- | ------------------- |
| Healthcare Providers Market   | $36.62 Billion (2025)       | Statista            |
| Connected Healthcare Market   | $0.89B → $3.09B (2025-2030) | Mordor Intelligence |
| Home Healthcare Growth (CAGR) | 28.13%                      | Mordor Intelligence |
| Elderly Care Market           | $15 Billion (2023)          | Ken Research        |
| Elderly Population            | 28 Million+ (2023)          | Ken Research        |
| BPJS Coverage Target          | 98% population              | World Bank          |

### 2.2 Batam Strategic Context

**Mengapa Batam?**

| Factor                 | Description                                                |
| ---------------------- | ---------------------------------------------------------- |
| **Populasi**           | 1.29 juta jiwa (57% dari Kepulauan Riau)                   |
| **Bonus Demografi**    | 70.31% usia produktif (15-64 tahun)                        |
| **Dominasi Perantau**  | Mayoritas penduduk adalah pendatang dari seluruh Indonesia |
| **Miniatur Indonesia** | Multietnis: Melayu (27%), Jawa (18%), Batak (14%), dll     |
| **Healthcare Growth**  | RS Mayapada International (investasi Rp 1 Triliun)         |
| **KEK Kesehatan**      | KEK Pariwisata & Kesehatan Internasional Batam             |
| **Proximity**          | Dekat Singapura (medical tourism hub)                      |
| **FTZ Status**         | Free Trade Zone - business-friendly environment            |

### 2.3 Healthcare Infrastructure Growth in Batam

**Mayapada Apollo Batam International Hospital (MABIH)**

- Investment: **Rp 1+ Triliun**
- Capacity: **250 beds** (Phase 1)
- Area: **2.9 hectares**
- Target completion: **End 2027**
- Centers of Excellence: Cardiovascular, Oncology, Neurology, Gastrohepatology, Orthopedics

**KEK Target:**

- Investment: **Rp 6.91 Triliun** (through 2032)
- Jobs: **105,406** positions (over 80 years)

### 2.4 The Perantau Challenge

**Problem unik perantau di kota industri seperti Batam:**

```
┌─────────────────────────────────────────────────────────────────┐
│                      PERANTAU DILEMMA                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   🏠 Orang tua di kampung                                       │
│       ↓                                                         │
│   📞 Orang tua sakit, butuh dibawa ke RS                        │
│       ↓                                                         │
│   ✈️  Tidak bisa pulang (kerja, biaya, waktu)                   │
│       ↓                                                         │
│   😰 Stres, khawatir, tidak ada yang bisa membantu              │
│                                                                 │
│   ATAU                                                          │
│                                                                 │
│   👴 Orang tua ikut ke Batam (mengikuti anak)                   │
│       ↓                                                         │
│   🏥 Orang tua perlu ke RS/cuci darah rutin                     │
│       ↓                                                         │
│   👷 Anak kerja pabrik (shift/lembur)                           │
│       ↓                                                         │
│   😰 Tidak ada yang menemani orang tua ke RS                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Statistik Migrasi Indonesia:**

- Migrasi didominasi usia **20-39 tahun** (usia produktif)
- Jawa Tengah: **5.99 juta** perantau (2020-2022)
- Tren: Populasi urban terus meningkat (66% by 2050)

---

## 3. Problem Statement

### 3.1 Pain Points - User Perspective

| User Segment               | Pain Points                                                                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Perantau/Anak Rantau**   | • Tidak bisa menemani orang tua sakit<br>• Khawatir saat orang tua operasi/cuci darah<br>• Tidak ada keluarga di Batam untuk membantu    |
| **Keluarga dengan Lansia** | • Sibuk kerja, tidak bisa menemani 24/7<br>• Cuci darah 2-3x seminggu, butuh pendamping<br>• Tidak percaya meninggalkan lansia sendirian |
| **Pasien Kronis**          | • Perlu pendampingan rutin ke RS<br>• Butuh bantuan aktivitas sehari-hari<br>• Administrasi RS yang rumit                                |
| **Pasien Pasca Operasi**   | • Butuh perawatan di rumah<br>• Keluarga tidak punya keahlian merawat<br>• Mahal jika harus rawat inap terus                             |

### 3.2 Current Solutions & Gaps

| Current Solution           | Limitations                                      |
| -------------------------- | ------------------------------------------------ |
| **Keluarga/Tetangga**      | Tidak selalu tersedia, bukan profesional         |
| **Panti Jompo**            | Stigma negatif, biaya tinggi, jauh dari keluarga |
| **Perawat RS**             | Fokus pada tindakan medis, bukan pendampingan    |
| **Jasa Informal**          | Tidak terverifikasi, tidak ada jaminan kualitas  |
| **Aplikasi Jakarta-based** | Tidak cover Batam (Medi-Call, Kavacare, CarePro) |

### 3.3 Gap Analysis

```
┌────────────────────────────────────────────────────────────────┐
│                     MARKET GAP: BATAM                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│   Existing Apps (Jakarta/Jabodetabek):                         │
│   ✓ Medi-Call     → Jakarta, Bandung, Surabaya                 │
│   ✓ Kavacare      → Jakarta, Tangerang, Bekasi, Depok          │
│   ✓ CarePro       → Jabodetabek, Bandung                       │
│   ✓ LoveCare      → 50+ cities (limited coverage)              │
│                                                                │
│   Batam Coverage:                                              │
│   ✗ NO dedicated patient companion app                         │
│   ✗ Only informal/word-of-mouth services                       │
│   ✗ No GPS-based on-demand booking                             │
│                                                                │
│   OPPORTUNITY: FIRST MOVER in Batam healthcare tech            │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 4. Solution Overview

### 4.1 SRICARE - Core Concept

**SRICARE** adalah platform marketplace yang menghubungkan:

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│    USER      │◄───────►│   SRICARE    │◄───────►│  CAREGIVER   │
│  (Customer)  │   App   │  (Platform)  │   App   │  (Partner)   │
└──────────────┘         └──────────────┘         └──────────────┘
      │                         │                        │
      ▼                         ▼                        ▼
  • Perantau              • GPS Matching            • Perawat
  • Keluarga              • Booking System          • Caregiver
  • Pasien                • Payment Gateway         • Pendamping
                          • Rating/Review           • Terapis
```

### 4.2 Service Categories

| Category                  | Description                                          | Duration Options            |
| ------------------------- | ---------------------------------------------------- | --------------------------- |
| **🏥 Hospital Companion** | Menemani pasien di RS (rawat inap, IGD, pemeriksaan) | Per jam / Per shift         |
| **💉 Dialysis Support**   | Menemani cuci darah (antar-jemput + tunggu)          | Per sesi (4-5 jam)          |
| **👨‍⚕️ Medical Escort**     | Menemani berobat ke dokter/klinik                    | Per kunjungan               |
| **🏠 Home Care**          | Perawatan di rumah (lansia, pasca operasi)           | Harian / Mingguan / Bulanan |
| **🚗 Medical Transport**  | Antar-jemput pasien ke faskes                        | Per trip                    |

### 4.3 User Flows

**Flow 1: Booking Pendamping Cuci Darah**

```
1. User buka app → Pilih "Cuci Darah"
2. Input lokasi jemput, RS tujuan, jadwal
3. App tampilkan caregiver terdekat + rating
4. User pilih caregiver → Konfirmasi booking
5. Caregiver dapat notifikasi → Accept
6. Real-time tracking → Caregiver ke lokasi
7. Caregiver jemput user/pasien
8. Antar ke RS → Tunggu selama proses HD
9. Antar pulang → Selesai
10. User bayar via app → Beri rating
```

**Flow 2: Booking Jaga Pasien di RS**

```
1. User buka app → Pilih "Jaga di RS"
2. Input nama RS, ruangan, durasi jaga
3. App tampilkan caregiver available
4. User pilih → Input detail pasien
5. Caregiver datang ke RS
6. Check-in via app (GPS verification)
7. Jaga pasien sesuai durasi
8. Report aktivitas via app
9. Check-out → Selesai
10. Payment → Rating
```

---

## 5. Target Market Analysis

### 5.1 Primary Target Segments

| Segment                       | Size Estimate (Batam) | Characteristics                                                   |
| ----------------------------- | --------------------- | ----------------------------------------------------------------- |
| **Perantau dengan Orang Tua** | ~200,000 households   | Usia 25-45, kerja pabrik/industri, orang tua ikut atau di kampung |
| **Keluarga dengan Lansia**    | ~50,000 households    | Ada anggota keluarga 60+, butuh bantuan rutin                     |
| **Pasien Hemodialisis**       | ~3,000-5,000 pasien   | Cuci darah 2-3x/minggu, butuh pendamping rutin                    |
| **Pasien Pasca Operasi**      | ~10,000/tahun         | Recovery di rumah, butuh home care sementara                      |

### 5.2 User Personas

**Persona 1: Andi - Pekerja Pabrik**

```
Usia: 32 tahun
Pekerjaan: Operator Produksi di pabrik elektronik
Penghasilan: Rp 5-7 juta/bulan
Situasi: Ibunya (63 tahun) ikut tinggal di Batam
Masalah: Ibu perlu ke RS untuk kontrol diabetes, tapi Andi kerja shift
Kebutuhan: Pendamping untuk antar ibu ke RS + tunggu selesai
Budget: Rp 150-200rb per kunjungan
```

**Persona 2: Sari - Profesional**

```
Usia: 38 tahun
Pekerjaan: Manager di perusahaan shipping
Penghasilan: Rp 15-20 juta/bulan
Situasi: Ayahnya (68 tahun) gagal ginjal, cuci darah 2x/minggu
Masalah: Sari sibuk meeting, tidak bisa antar ayah setiap kali HD
Kebutuhan: Pendamping tetap untuk cuci darah rutin
Budget: Rp 300-500rb per sesi HD
```

**Persona 3: Budi - Perantau Jauh**

```
Usia: 28 tahun
Pekerjaan: Teknisi di shipyard
Penghasilan: Rp 8-10 juta/bulan
Situasi: Orang tua di Jawa, ayah baru operasi jantung
Masalah: Tidak bisa pulang, tapi ingin ada yang bantu jaga ayah
Kebutuhan: Jasa pendamping pasien di RS kampung (future expansion)
Budget: Rp 200-300rb per shift
```

### 5.3 Market Sizing (Batam)

**TAM (Total Addressable Market)**

```
Populasi Batam: 1,290,000 jiwa
Households: ~400,000 (asumsi 3.2/household)
% dengan kebutuhan care: 15%
TAM = 60,000 households
Average spend/year: Rp 3,600,000 (Rp 300k x 12)
TAM Value = Rp 216 Miliar/tahun (~$13.5M)
```

**SAM (Serviceable Addressable Market)**

```
Digital-savvy households: 50% of TAM
SAM = 30,000 households
SAM Value = Rp 108 Miliar/tahun (~$6.75M)
```

**SOM (Serviceable Obtainable Market) - Year 1**

```
Realistic capture: 5% of SAM
SOM = 1,500 households
Average transactions: 6/year
Transaction value: Rp 250,000
SOM Value = Rp 2.25 Miliar/tahun (~$140K)
```

---

## 6. Market Size & Opportunity

### 6.1 Indonesia Caregiving Market

| Segment               | Market Size    | Growth      |
| --------------------- | -------------- | ----------- |
| Elderly Care Services | $15 Billion    | 8.2% CAGR   |
| Home Healthcare       | $4.6 Billion   | 28.13% CAGR |
| Healthcare Providers  | $36.62 Billion | 6.96% CAGR  |

### 6.2 Digital Health Opportunity

| Metric                           | 2025    | 2030     | CAGR   |
| -------------------------------- | ------- | -------- | ------ |
| Connected Healthcare (Indonesia) | $0.89B  | $3.09B   | 28.13% |
| Elderly Care Apps (Global)       | $2.1B   | $3.4B    | 10%    |
| AI in Elderly Care (Global)      | $43.76B | $122.88B | 29.5%  |

### 6.3 Competitive Landscape Summary

| Competitor    | Coverage                       | Users           | Funding                    |
| ------------- | ------------------------------ | --------------- | -------------------------- |
| **Medi-Call** | Jakarta, Bandung, Surabaya     | 100K+ downloads | Undisclosed                |
| **Kavacare**  | Jabodetabek                    | Growing         | Undisclosed                |
| **CarePro**   | Jabodetabek, Bandung           | Growing         | Top 3 DTO Accelerator 2024 |
| **LoveCare**  | 50+ cities                     | 200+ partners   | $10K (Pre-seed)            |
| **Homage**    | Singapore, Malaysia, Australia | 1M+ care hours  | Series C funded            |

**Gap:** None of the above have strong presence in **Batam**.

---

## 7. SWOT Analysis

### Strengths (Kekuatan)

| #   | Strength                                                                 |
| --- | ------------------------------------------------------------------------ |
| 1   | **First-mover advantage** di Batam - belum ada kompetitor dedicated      |
| 2   | **Local presence** - SURIOTA berbasis di Batam, paham pasar lokal        |
| 3   | **Tech capability** - Tim sudah develop SURGE Platform & SRT-MGATE       |
| 4   | **Ecosystem integration** - Bisa integrate dengan SURGE untuk monitoring |
| 5   | **Low cost structure** - Tidak perlu bersaing dengan Jakarta-based apps  |

### Weaknesses (Kelemahan)

| #   | Weakness                                      | Mitigation                                          |
| --- | --------------------------------------------- | --------------------------------------------------- |
| 1   | Belum punya experience di healthcare services | Partner dengan RS/klinik untuk training caregiver   |
| 2   | Supply caregiver terbatas di awal             | Start dengan recruitment campaign + training        |
| 3   | Brand awareness rendah                        | Leverage existing SURIOTA network + local marketing |
| 4   | Cash flow intensive (pay caregivers)          | Implement escrow system + fast payout               |

### Opportunities (Peluang)

| #   | Opportunity                                                     |
| --- | --------------------------------------------------------------- |
| 1   | **Healthcare infrastructure boom** - RS Mayapada, KEK Kesehatan |
| 2   | **Aging population** - Indonesia projected 28M+ elderly         |
| 3   | **Digital adoption surge** - 92% using e-wallets                |
| 4   | **Remote care trend** - Post-COVID preference for home care     |
| 5   | **Government support** - BPJS integration potential, JKN Mobile |
| 6   | **Regional expansion** - Kepri islands, then Sumatera           |

### Threats (Ancaman)

| #   | Threat                             | Mitigation                                            |
| --- | ---------------------------------- | ----------------------------------------------------- |
| 1   | Jakarta-based apps expand to Batam | Build loyal user base + local caregiver network first |
| 2   | Informal services (cheaper)        | Emphasize quality, verification, insurance            |
| 3   | Regulatory changes                 | Stay compliant, engage with health authorities        |
| 4   | Economic downturn                  | Focus on essential services (HD, hospital care)       |

---

## 8. Business Model

### 8.1 Revenue Streams

| Revenue Stream               | Description                         | % of Revenue |
| ---------------------------- | ----------------------------------- | ------------ |
| **Service Commission**       | 15-20% dari setiap transaksi        | 70%          |
| **Subscription (Caregiver)** | Monthly fee untuk premium listing   | 15%          |
| **Partnership Fee**          | RS/Klinik partnership program       | 10%          |
| **Value-Added Services**     | Insurance, medical equipment rental | 5%           |

### 8.2 Commission Structure

| Service Type                 | User Pays  | Caregiver Gets | Platform Commission |
| ---------------------------- | ---------- | -------------- | ------------------- |
| Hospital Companion (per jam) | Rp 50,000  | Rp 42,500      | Rp 7,500 (15%)      |
| Dialysis Support (per sesi)  | Rp 300,000 | Rp 255,000     | Rp 45,000 (15%)     |
| Medical Escort (per trip)    | Rp 150,000 | Rp 127,500     | Rp 22,500 (15%)     |
| Home Care (per hari)         | Rp 400,000 | Rp 340,000     | Rp 60,000 (15%)     |

### 8.3 Unit Economics

**Per Transaction (Average)**

```
Average Order Value (AOV): Rp 200,000
Commission Rate: 15%
Gross Revenue per Transaction: Rp 30,000
Payment Gateway Fee (2%): Rp 4,000
Net Revenue per Transaction: Rp 26,000
```

**Monthly Target (Year 1 - Month 12)**

```
Transactions/month: 500
Gross Revenue: Rp 15,000,000
Net Revenue (after payment fees): Rp 13,000,000
Operating Costs: Rp 10,000,000
Net Profit: Rp 3,000,000
```

### 8.4 Cost Structure

| Cost Category               | Monthly Estimate  | % of Revenue |
| --------------------------- | ----------------- | ------------ |
| **Tech Infrastructure**     | Rp 3,000,000      | 20%          |
| **Marketing & Acquisition** | Rp 5,000,000      | 33%          |
| **Operations & Support**    | Rp 4,000,000      | 27%          |
| **Caregiver Training**      | Rp 2,000,000      | 13%          |
| **Miscellaneous**           | Rp 1,000,000      | 7%           |
| **Total**                   | **Rp 15,000,000** | **100%**     |

---

## 9. Go-to-Market Strategy

### 9.1 Phase 1: Pre-Launch (Month 1-2)

| Activity                  | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **Caregiver Recruitment** | Recruit 50 initial caregivers di Batam           |
| **Training Program**      | Basic care training, app usage, customer service |
| **Partnership**           | MoU dengan 3-5 RS/Klinik di Batam                |
| **Beta Testing**          | Internal testing + 50 beta users                 |

### 9.2 Phase 2: Soft Launch (Month 3-4)

| Activity                 | Description                        |
| ------------------------ | ---------------------------------- |
| **Limited Launch**       | Launch untuk 500 users pertama     |
| **Promo Campaign**       | Diskon 50% untuk 5 booking pertama |
| **Feedback Loop**        | Collect user feedback, iterate     |
| **Caregiver Onboarding** | Scale to 100 active caregivers     |

### 9.3 Phase 3: Full Launch (Month 5-6)

| Activity                   | Description                        |
| -------------------------- | ---------------------------------- |
| **Public Launch**          | Full marketing campaign            |
| **Referral Program**       | "Ajak Teman" bonus Rp 50,000       |
| **Partnership Activation** | RS promotion, community events     |
| **PR & Media**             | Local media coverage, social proof |

### 9.4 Marketing Channels

| Channel           | Strategy                               | Budget Allocation |
| ----------------- | -------------------------------------- | ----------------- |
| **Social Media**  | Facebook/Instagram ads targeting Batam | 30%               |
| **Community**     | Komunitas RT/RW, perkumpulan perantau  | 20%               |
| **Partnership**   | RS/Klinik referral program             | 20%               |
| **Word of Mouth** | Referral incentives                    | 15%               |
| **Local Events**  | Health bazaar, community events        | 10%               |
| **Digital PR**    | Local news, health blogs               | 5%                |

---

## 10. Financial Projections

### 10.1 Year 1 Projections

| Month     | Users     | Caregivers | Transactions | GMV      | Revenue (15%) |
| --------- | --------- | ---------- | ------------ | -------- | ------------- |
| M1        | 0         | 50         | 0            | 0        | 0             |
| M2        | 0         | 75         | 0            | 0        | 0             |
| M3        | 100       | 100        | 50           | 10M      | 1.5M          |
| M4        | 250       | 100        | 100          | 20M      | 3M            |
| M5        | 500       | 150        | 200          | 40M      | 6M            |
| M6        | 750       | 150        | 300          | 60M      | 9M            |
| M7        | 1,000     | 200        | 400          | 80M      | 12M           |
| M8        | 1,250     | 200        | 450          | 90M      | 13.5M         |
| M9        | 1,500     | 250        | 500          | 100M     | 15M           |
| M10       | 1,750     | 250        | 550          | 110M     | 16.5M         |
| M11       | 2,000     | 300        | 600          | 120M     | 18M           |
| M12       | 2,500     | 300        | 700          | 140M     | 21M           |
| **Total** | **2,500** | **300**    | **3,850**    | **770M** | **115.5M**    |

_GMV = Gross Merchandise Value (in Rp)_
_Revenue = Platform commission at 15%_

### 10.2 3-Year Financial Summary

| Metric           | Year 1    | Year 2  | Year 3   |
| ---------------- | --------- | ------- | -------- |
| **Users**        | 2,500     | 10,000  | 30,000   |
| **Caregivers**   | 300       | 800     | 1,500    |
| **Transactions** | 3,850     | 25,000  | 75,000   |
| **GMV**          | Rp 770M   | Rp 5B   | Rp 15B   |
| **Revenue**      | Rp 115.5M | Rp 750M | Rp 2.25B |
| **Gross Margin** | 65%       | 70%     | 75%      |
| **Net Profit**   | -Rp 64.5M | Rp 150M | Rp 675M  |

### 10.3 Funding Requirements

**Seed Funding: Rp 500 Juta (~$31,000)**

| Allocation             | Amount  | %   |
| ---------------------- | ------- | --- |
| Tech Development (MVP) | Rp 200M | 40% |
| Marketing & Launch     | Rp 150M | 30% |
| Operations (6 months)  | Rp 100M | 20% |
| Contingency            | Rp 50M  | 10% |

---

## 11. Risk Analysis

### 11.1 Risk Matrix

| Risk                     | Probability | Impact | Mitigation                                     |
| ------------------------ | ----------- | ------ | ---------------------------------------------- |
| **Low caregiver supply** | High        | High   | Aggressive recruitment, competitive commission |
| **User adoption slow**   | Medium      | High   | Heavy marketing, referral incentives           |
| **Competitor entry**     | Medium      | Medium | Build moat with local network + quality        |
| **Regulatory changes**   | Low         | High   | Stay compliant, legal counsel                  |
| **Tech failures**        | Low         | High   | Redundancy, monitoring, backup systems         |
| **Payment fraud**        | Medium      | Medium | Escrow system, verification                    |

### 11.2 Contingency Plans

**If caregiver supply is low:**

- Partner with nursing schools for internship program
- Offer sign-up bonus for early caregivers
- Implement "refer a caregiver" program

**If user adoption is slow:**

- Pivot to B2B (corporate employee benefits)
- Partner exclusively with 1 hospital for patient referrals
- Reduce commission to attract more users

---

## 12. Implementation Roadmap

### 12.1 Development Timeline

```
                    2026
    Q1              Q2              Q3              Q4
    ├───────────────┼───────────────┼───────────────┤
    │               │               │               │
M1  │ Research      │               │               │
M2  │ Design/UI     │               │               │
M3  │ MVP Dev       │               │               │
M4  │               │ Beta Test     │               │
M5  │               │ Soft Launch   │               │
M6  │               │ Full Launch   │               │
M7  │               │               │ Scale Batam   │
M8  │               │               │ Add Features  │
M9  │               │               │ Optimize      │
M10 │               │               │               │ Expansion Plan
M11 │               │               │               │ Kepri Islands
M12 │               │               │               │ Year 1 Review
```

### 12.2 MVP Features (Month 1-4)

| Priority | Feature                | Description                            |
| -------- | ---------------------- | -------------------------------------- |
| P0       | User Registration      | Phone OTP verification                 |
| P0       | Caregiver Registration | Profile, verification, documents       |
| P0       | Service Booking        | Select service, date, time, location   |
| P0       | GPS Matching           | Find nearest available caregiver       |
| P0       | Payment Integration    | QRIS, e-wallet, VA                     |
| P1       | Real-time Tracking     | Track caregiver location               |
| P1       | In-app Chat            | Communication between user & caregiver |
| P1       | Rating & Review        | Post-service feedback                  |
| P2       | Booking History        | View past transactions                 |
| P2       | Push Notifications     | Booking updates, reminders             |

### 12.3 Success Metrics

| Phase        | Metric               | Target        |
| ------------ | -------------------- | ------------- |
| **Month 3**  | Beta Users           | 50            |
| **Month 3**  | Active Caregivers    | 100           |
| **Month 6**  | Monthly Active Users | 750           |
| **Month 6**  | Monthly Transactions | 300           |
| **Month 6**  | Average Rating       | 4.5+          |
| **Month 12** | Total Users          | 2,500         |
| **Month 12** | Monthly Transactions | 700           |
| **Month 12** | GMV                  | Rp 140M/month |

---

## Appendix

### A. Glossary

| Term                  | Definition                                      |
| --------------------- | ----------------------------------------------- |
| **Caregiver**         | Tenaga pendamping non-medis yang terlatih       |
| **Hemodialisis (HD)** | Proses cuci darah untuk pasien gagal ginjal     |
| **GMV**               | Gross Merchandise Value - total nilai transaksi |
| **MAU**               | Monthly Active Users                            |
| **QRIS**              | Quick Response Code Indonesian Standard         |
| **FTZ**               | Free Trade Zone                                 |
| **KEK**               | Kawasan Ekonomi Khusus                          |

### B. References

- [Statista - Healthcare Providers Indonesia](https://www.statista.com/outlook/hmo/healthcare-providers/indonesia)
- [Mordor Intelligence - Indonesia Connected Healthcare](https://www.mordorintelligence.com/industry-reports/indonesia-connected-healthcare-market)
- [BP Batam - Population Data](https://bpbatam.go.id/en/jumlah-penduduk-kota-batam/)
- [Mayapada Hospital - MABIH Project](https://mayapadahospital.com/news/mayapada-healthcare-lakukan-peletakan-batu-pertama-untuk-rs-internasional-di-kek-pariwisata-dan-kesehatan-internasional-batam)
- [Databoks - Batam Demographics](https://databoks.katadata.co.id/en/demographics/statistics/eb5ed9eb58c51d7/57-of-riau-islands-population-will-be-in-batam-city-by-mid-2024)

---

_Document Version: 1.0_
_Last Updated: January 2026_
_Author: SURIOTA Team_
