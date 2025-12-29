# SURGE Platform - Roasting & Response Guide

## Panduan Menghadapi Kritik Keras dari Customer

**Document Version**: 2.0
**Last Updated**: December 29, 2025
**Purpose**: Mempersiapkan tim sales menghadapi pertanyaan/kritik tajam

---

# PRICING QUICK REFERENCE

Sebelum masuk ke roasting responses, pastikan hafal struktur pricing:

| Plan | Price | Tag Data | Locations | Logging | Retention | Access |
|------|-------|:--------:|:---------:|:-------:|:---------:|:------:|
| Trial | Free | 5 | Unlimited | 2 min | 30 hari | Private (invitation) |
| Starter | $29/mo | 30 | Unlimited | 1 min | 1 tahun | Public |
| Business | $99/mo | 100 | Unlimited | 1 min | 2 tahun | Public |
| Professional | $299/mo | Unlimited | Unlimited | Custom | 5 tahun | Public |

**Key Differentiators:**
- **Semua tier = Unlimited locations** (unik dibanding kompetitor)
- **Tag data** = jumlah parameter monitoring (pH, suhu, kWh, dll)
- **Trial = Private** = harus kontak SURIOTA untuk demo account

---

# DAFTAR ISI

1. [Brand & Credibility](#1-brand--credibility)
2. [Technical & Platform](#2-technical--platform)
3. [Price & Value](#3-price--value)
4. [Support & Reliability](#4-support--reliability)
5. [Feature Comparison](#5-feature-comparison)
6. [Security & Compliance](#6-security--compliance)
7. [Use Case Specific](#7-use-case-specific)
8. [Trial Access Objections](#8-trial-access-objections)

---

# 1. BRAND & CREDIBILITY

## ROASTING 1.1: "SURGE? Platform baru, belum proven!"

**Kritik:**

> "Kami tidak mau jadi guinea pig untuk platform baru yang belum teruji di production. ThingsBoard sudah dipakai ribuan perusahaan."

**Response:**

> Terima kasih atas kekhawatirannya. Memang benar SURGE adalah platform baru, tapi izinkan saya jelaskan:
>
> **Fakta Platform:**
>
> - Dikembangkan menggunakan tech stack yang sama dengan platform enterprise:
>   - Next.js 15 + React 19 (sama seperti Vercel, Netflix)
>   - NestJS (sama seperti Adidas, Capgemini)
>   - PostgreSQL + TimescaleDB (industry standard untuk IoT)
>
> **Yang Sudah Berjalan:**
>
> - Pilot deployment di beberapa IPAL industri
> - Testing 6+ bulan sebelum production release
> - 99.5% uptime target dengan monitoring 24/7
>
> **Mitigasi Risiko:**
>
> - Demo account untuk evaluasi fitur (kontak tim kami)
> - Trial gratis dengan data Anda sendiri
> - Direct access ke engineering team untuk issue resolution
>
> **Pertanyaan balik:** Boleh kami arrange demo session? Anda bisa test dengan data real di environment kita.

---

## ROASTING 1.2: "Kenapa harus SURGE? ThingsBoard gratis!"

**Kritik:**

> "ThingsBoard Community Edition gratis dan open source. Kenapa saya harus bayar untuk SURGE?"

**Response:**

> Benar, ThingsBoard CE gratis. Tapi mari kita hitung Total Cost of Ownership:
>
> **Hidden Cost ThingsBoard Self-Hosted:**
>
> | Item               | Cost/bulan           | Keterangan               |
> | ------------------ | -------------------- | ------------------------ |
> | Server (VPS/Cloud) | $50-200/bulan        | Minimal 4GB RAM, SSD     |
> | Database           | $30-100/bulan        | PostgreSQL managed       |
> | DevOps Engineer    | $500-1000/bulan      | Part-time maintenance    |
> | Security/SSL       | $20-50/bulan         | Certificates, firewall   |
> | Backup             | $20-50/bulan         | Automated backup service |
> | **TOTAL**          | **$620-1,400/bulan** |                          |
>
> **SURGE Business Plan:**
>
> - $99/bulan = 100 tag data + SEMUA sudah included
> - No server management
> - No DevOps needed
> - Backup + Security included
> - **Unlimited locations** (bisa monitor banyak site)
>
> **Tambahan yang ThingsBoard CE TIDAK punya:**
>
> - KLHK compliance templates
> - Bahasa Indonesia
> - Local support WA/Phone
> - Industry-specific modules (Water, Energy, Vessel)
>
> **Kesimpulan:** ThingsBoard CE "gratis" tapi butuh biaya $600+/bulan untuk operasional. SURGE $99/bulan all-inclusive dengan 100 tag data.

---

## ROASTING 1.3: "SURIOTA siapa? Perusahaan kecil, bisa bangkrut kapan saja!"

**Kritik:**

> "Bagaimana kalau SURIOTA tutup dalam 2-3 tahun? Data kami bagaimana?"

**Response:**

> Kekhawatiran yang sangat valid. Ini mitigasi kami:
>
> **Data Portability:**
>
> - Data Anda selalu bisa di-export (Excel/CSV/API)
> - Format standar yang bisa diimpor ke platform lain
> - Anda OWN data Anda, bukan kami
>
> **Business Sustainability:**
>
> - PT Surya Inovasi Prioritas adalah PT legal terdaftar
> - Bootstrap company, tidak burn investor money
> - Focus pada profitability, bukan unicorn growth
> - Margin sehat (85% SaaS gross margin)
>
> **Worst Case Scenario:**
>
> - 90-day notice sebelum shutdown (if ever)
> - Full data export assistance
> - Source code escrow bisa dinegosiasi untuk enterprise contract
>
> **Komitmen:** Kami bersedia sign data export guarantee dalam kontrak.

---

# 2. TECHNICAL & PLATFORM

## ROASTING 2.1: "Next.js + NestJS? Stack terlalu baru, tidak enterprise!"

**Kritik:**

> "Enterprise pakai Java Spring atau .NET. JavaScript framework tidak cocok untuk production critical."

**Response:**

> Persepsi yang understandable tapi sudah outdated. Ini faktanya:
>
> **Companies Using This Stack:**
>
> | Company  | Stack          | Users/Scale         |
> | -------- | -------------- | ------------------- |
> | Netflix  | Next.js + Node | 200M+ subscribers   |
> | Uber     | NestJS         | 100M+ users         |
> | Adidas   | NestJS         | Global e-commerce   |
> | Twitch   | Node.js        | 140M+ monthly users |
> | LinkedIn | Node.js        | 800M+ members       |
>
> **Why We Chose This Stack:**
>
> - **Performance:** Node.js excellent untuk real-time IoT data
> - **Type Safety:** TypeScript = fewer bugs, better maintainability
> - **Developer Pool:** Easier to find dan train engineers
> - **Modern Tooling:** Better testing, CI/CD, monitoring
>
> **Enterprise Features Kami Punya:**
>
> - RBAC (Role-Based Access Control) - 4 roles: Viewer, Member, Admin, Owner
> - Multi-tenancy dengan complete data isolation
> - JWT authentication dengan refresh token
> - API rate limiting
> - Audit logging
>
> **Challenge:** Kami bisa arrange technical deep-dive dengan tim IT Anda untuk review architecture.

---

## ROASTING 2.2: "Bagaimana dengan scalability? Kalau device kami 10,000?"

**Kritik:**

> "Platform startup biasanya tidak scale. Kami punya rencana 10,000 device dalam 2 tahun."

**Response:**

> Valid concern. Ini arsitektur scalability kami:
>
> **Current Architecture:**
>
> ```
> ┌─────────────────────────────────────────────────────────────┐
> │  MQTT Broker ────> NestJS Backend ────> TimescaleDB        │
> │      │                  │                    │              │
> │   Mosquitto         p-queue              Hypertables        │
> │   (Clusterable)     (Batch 20/2s)       (Auto-partition)   │
> └─────────────────────────────────────────────────────────────┘
> ```
>
> **Scalability Strategy:**
>
> | Scale           | Architecture                 | Status     |
> | --------------- | ---------------------------- | ---------- |
> | 100 devices     | Single instance              | Production |
> | 1,000 devices   | Horizontal scaling           | Tested     |
> | 10,000 devices  | Kubernetes + sharding        | Planned    |
> | 100,000 devices | Enterprise custom deployment | Available  |
>
> **TimescaleDB Advantage:**
>
> - Time-series optimized (designed for IoT)
> - Auto-partitioning by time
> - Compression (10x storage reduction)
> - Proven at billions of rows
>
> **Untuk 10,000 Device:**
>
> - Professional plan ($299/mo) sebagai starting point
> - Custom enterprise deployment jika perlu dedicated infrastructure
> - SLA 99.9%
> - Priority support
>
> **Next Step:** Mari diskusikan requirement spesifik untuk design capacity planning.

---

## ROASTING 2.3: "MQTT saja? Kami pakai OPC UA / Siemens MPI!"

**Kritik:**

> "Industri kami pakai OPC UA dan protokol proprietary. MQTT tidak cukup."

**Response:**

> Fair point. MQTT adalah layer cloud kami, bukan satu-satunya protokol:
>
> **Architecture:**
>
> ```
> Your Devices ──> Protocol Converter ──> MQTT ──> SURGE
>        │
>        └── OPC UA / Modbus / BACnet / etc.
> ```
>
> **Protocol Support:**
>
> | Your Protocol  | Solution                  | Cost          |
> | -------------- | ------------------------- | ------------- |
> | Modbus RTU/TCP | SURIOTA Gateway (Rp 2.7M) | Hardware      |
> | OPC UA         | Node-RED + opc-ua-client  | Free software |
> | Siemens S7     | S7 to MQTT gateway        | Varies        |
> | BACnet         | BACnet gateway            | Varies        |
>
> **SURIOTA Gateway (SRT-MGATE-1210):**
>
> - Modbus RTU/TCP → MQTT
> - Pre-integrated dengan SURGE
> - Rp 2.7 juta, sudah include WiFi + BLE
>
> **OPC UA Integration:**
>
> - Kami bisa bantu setup Node-RED OPC UA bridge
> - Atau rekomendasi third-party OPC UA gateway
>
> **Kesimpulan:** MQTT adalah cloud protocol, bukan constraint. Device edge bisa pakai protokol apapun dengan gateway.

---

# 3. PRICE & VALUE

## ROASTING 3.1: "$99/bulan terlalu mahal untuk SMB!"

**Kritik:**

> "Kami SMB kecil dengan budget terbatas. $99/bulan ($1,200/tahun) itu mahal untuk kami."

**Response:**

> Mari kita hitung value vs cost:
>
> **Starter Plan Available ($29/bulan = Rp 464,000):**
>
> - **30 tag data** (3x lebih banyak dari kompetitor entry-level)
> - **Unlimited lokasi** (bisa monitor banyak site!)
> - 1-year data retention
> - Full dashboard & analytics
> - Email + WhatsApp support
>
> **Cost of NOT Having Monitoring:**
>
> | Risk                      | Potential Cost                  |
> | ------------------------- | ------------------------------- |
> | KLHK penalty              | Rp 50-500 juta                  |
> | Downtime detection late   | Rp 10-100 juta/incident         |
> | Manual reporting time     | 8 jam/bulan x Rp 100K = Rp 800K |
> | Energy waste (no monitor) | 10-15% lebih tinggi             |
>
> **ROI Calculation:**
>
> - Starter: Rp 464,000/bulan
> - Hemat 1 penalty KLHK (Rp 50 juta) = 108 bulan subscription
> - Hemat 8 jam/bulan manual work = Rp 800,000/bulan savings
>
> **Break-even:** Dalam 1 bulan pertama!
>
> **Kesimpulan:** Rp 464K/bulan = asuransi terhadap penalty + produktivitas. Dan dengan 30 tag data + unlimited locations, cukup untuk SMB menengah.

---

## ROASTING 3.2: "Kami sudah invest di sistem lama, tidak mau ganti!"

**Kritik:**

> "Kami sudah pakai SCADA/Excel system selama 10 tahun. Switching cost terlalu tinggi."

**Response:**

> SURGE bukan pengganti, tapi **pelengkap**:
>
> **SURGE + Existing System:**
>
> ```
> ┌───────────────┐     ┌───────────────┐
> │ Your SCADA    │ ──> │   SURGE       │
> │ (tetap pakai) │     │ (tambahan)    │
> └───────────────┘     └───────────────┘
>         │                     │
>    Local Control      Remote Monitoring
>    (existing value)   (new capability)
> ```
>
> **Integration Options:**
>
> | Existing System | Integration Method     |
> | --------------- | ---------------------- |
> | SCADA           | OPC UA gateway → SURGE |
> | PLC             | Modbus gateway → SURGE |
> | Excel reporting | API import ke SURGE    |
>
> **Value Add, Not Replace:**
>
> - SCADA: Local control (keep it)
> - SURGE: Remote monitoring + KLHK compliance (add it)
>
> **Cost Justification:**
>
> - SCADA investment: Rp 100M+ (sunk cost)
> - SURGE addition: Rp 5-15M/tahun
> - Remote capability: +5% cost untuk 100% remote access
>
> **Kesimpulan:** Tidak perlu ganti sistem lama. SURGE menambah value di atas investment yang sudah ada.

---

## ROASTING 3.3: "Kompetitor kasih free tier yang lebih generous!"

**Kritik:**

> "ThingsBoard Community gratis unlimited. Datacake kasih 2 device gratis. SURGE free tier terlalu kecil."

**Response:**

> Mari kita breakdown "free" yang sebenarnya:
>
> **ThingsBoard Community "Free":**
>
> | Item             | Real Cost          |
> | ---------------- | ------------------ |
> | Software         | Free               |
> | Server hosting   | $50-200/bulan      |
> | Database hosting | $30-100/bulan      |
> | Maintenance      | 10 jam/bulan × $50 |
> | Security setup   | 5 jam × $100       |
> | **Total/bulan**  | **$200-800**       |
>
> **Datacake "2 Device Free":**
>
> - 2 devices = meaningless untuk real deployment
> - 30-day retention only
> - No industrial features
> - No local support
>
> **SURGE Trial:**
>
> - **5 tag data** (real testing capability)
> - **Unlimited locations** (tidak dibatasi!)
> - 30-day retention
> - Full dashboard (not crippled)
> - Indonesia localization
> - Upgrade path clear
>
> **Paid Tier Comparison:**
>
> | Platform    | ~30 tags equivalent | Price/month    | Locations |
> | ----------- | ------------------- | -------------- | --------- |
> | ThingsBoard | Custom pricing      | $200+          | Limited   |
> | Datacake    | Light plan          | €150/mo        | Limited   |
> | Ubidots     | Launch plan         | $99/mo         | Limited   |
> | **SURGE**   | **Starter plan**    | **$29/mo**     | **Unlimited** |
>
> **Kesimpulan:** "Free" sering berarti "hidden costs" atau "unusable limits". SURGE transparan dan memberikan unlimited locations di semua tier.

---

## ROASTING 3.4: "Kenapa Starter lebih murah tapi dapat lebih banyak tag dari Trial?"

**Kritik:**

> "Trial 5 tag, Starter 30 tag. Logic-nya apa? Kenapa tidak kasih lebih banyak di Trial?"

**Response:**

> Great question! Ini pertimbangan bisnis kami:
>
> **Trial Purpose:**
>
> - Tujuan: Evaluasi fitur dan UX, bukan production use
> - 5 tag = cukup untuk test 1 sistem lengkap (pH + COD + TSS + Flow + Level)
> - 30 hari = cukup untuk evaluasi
> - **Private access**: Kami butuh qualify customer dulu
>
> **Why Private Trial?**
>
> - Menghindari abuse (mining/spam)
> - Memastikan serious buyer
> - Kami bisa bantu setup yang optimal
> - Personal demo + onboarding
>
> **Starter = Entry Production:**
>
> - 30 tag = 6x lipat dari Trial
> - 1 tahun retention (vs 30 hari)
> - 1-minute logging interval (vs 2-min)
> - Production-ready, bukan evaluasi
>
> **Analogi:**
>
> - Trial = Test drive mobil (30 menit)
> - Starter = Sewa mobil harian (bisa pakai full)
>
> **Kesimpulan:** Trial untuk evaluasi dengan pendampingan, Starter untuk production dengan value lebih.

---

# 4. SUPPORT & RELIABILITY

## ROASTING 4.1: "Startup, pasti support lambat dan tidak reliable!"

**Kritik:**

> "Perusahaan kecil tidak bisa provide support 24/7. Kalau malam ada masalah bagaimana?"

**Response:**

> Concern yang valid. Ini setup support kami:
>
> **Support Tiers:**
>
> | Plan         | Channel            | Response Time | Availability |
> | ------------ | ------------------ | ------------- | ------------ |
> | Trial        | Email              | 48 jam        | Business hrs |
> | Starter      | Email + WA         | 24 jam        | Business hrs |
> | Business     | Email + WA + Phone | 8 jam         | Extended hrs |
> | Professional | Dedicated line     | 4 jam         | 24/7         |
>
> **Advantage Tim Kecil:**
>
> - Direct access ke engineers yang develop platform
> - No tier 1 → tier 2 → tier 3 escalation
> - Personal relationship, bukan ticket number
>
> **For Critical Issues:**
>
> - Platform monitoring 24/7
> - Auto-alert untuk downtime
> - Immediate response dari on-call engineer
>
> **SLA Commitment (Professional):**
>
> - 99.9% uptime guarantee
> - Credit jika SLA tidak terpenuhi
> - Escalation path sampai founder
>
> **Kesimpulan:** Response cepat karena bicara langsung sama yang buat sistem.

---

## ROASTING 4.2: "99.5% uptime? Itu berarti 44 jam downtime per tahun!"

**Kritik:**

> "Industri kami butuh 99.99%. 44 jam downtime per tahun tidak bisa diterima."

**Response:**

> Valid math! Mari kita breakdown:
>
> **Uptime Comparison:**
>
> | SLA    | Downtime/year | Downtime/month | Cost Tier        |
> | ------ | ------------- | -------------- | ---------------- |
> | 99%    | 87.6 jam      | 7.3 jam        | Budget           |
> | 99.5%  | 43.8 jam      | 3.65 jam       | Standard         |
> | 99.9%  | 8.76 jam      | 43.8 menit     | Enterprise       |
> | 99.99% | 52.56 menit   | 4.38 menit     | Mission-critical |
>
> **SURGE SLA by Plan:**
>
> | Plan         | Uptime SLA | Data Retention | Credit if Fail |
> | ------------ | ---------- | -------------- | -------------- |
> | Trial        | Best effort| 30 hari        | No             |
> | Starter      | 99%        | 1 tahun        | No             |
> | Business     | 99.5%      | 2 tahun        | Yes            |
> | Professional | 99.9%      | 5 tahun        | Yes + priority |
> | Enterprise   | 99.99%     | Custom         | Negotiable     |
>
> **Architecture for High Availability:**
>
> - Multi-AZ deployment (dapat diatur)
> - Database replication
> - Load balancing
> - Automated failover
>
> **Realita:**
>
> - Scheduled maintenance: Di luar jam kerja
> - Actual unplanned downtime: Jauh di bawah SLA
>
> **For 99.99% Requirement:**
>
> - Custom enterprise deployment
> - Dedicated infrastructure
> - Harga custom (start dari $1,000/month)
>
> **Kesimpulan:** Professional plan (99.9%) cukup untuk 95% use case industrial.

---

# 5. FEATURE COMPARISON

## ROASTING 5.1: "ThingsBoard punya rule engine, SURGE tidak!"

**Kritik:**

> "ThingsBoard bisa buat complex automation rules. SURGE cuma bisa display data."

**Response:**

> Fair comparison. Ini trade-off yang kami pilih:
>
> **ThingsBoard Rule Engine:**
>
> - Powerful dan flexible
> - Complex to setup dan maintain
> - Steep learning curve
> - Overkill untuk kebanyakan monitoring use case
>
> **SURGE Approach:**
>
> | Feature            | Status    | How                          |
> | ------------------ | --------- | ---------------------------- |
> | Threshold alerts   | Built-in  | Simple UI configuration      |
> | Email notification | Built-in  | Automatic on threshold       |
> | Custom logic       | Via API   | Integrate dengan your system |
> | Webhook            | Available | Push data ke external system |
>
> **80/20 Rule:**
>
> - 80% users hanya butuh: Threshold → Alert → Notification
> - 20% butuh complex rules → Integrate via API/webhook
>
> **Integration for Complex Logic:**
>
> ```
> SURGE ─── Webhook ───> Node-RED ───> Complex Logic ───> Action
>                            │
>                        Your custom rules
> ```
>
> **Planned Features:**
>
> - Simple automation rules (Q2 2026)
> - SMS/WhatsApp alerts (Q1 2026)
> - Escalation workflows (Q2 2026)
>
> **Kesimpulan:** SURGE fokus pada ease-of-use. Complex logic via integration.

---

## ROASTING 5.2: "Grafana visualisasinya jauh lebih bagus!"

**Kritik:**

> "Grafana adalah industry standard untuk dashboards. SURGE tidak bisa tandingi."

**Response:**

> Grafana memang excellent untuk visualization. Tapi apakah Anda butuh Grafana?
>
> **Grafana Strengths:**
>
> - 50+ chart types
> - Extreme customization
> - Plugin ecosystem
> - Beautiful aesthetics
>
> **Grafana Challenges untuk IoT:**
>
> | Gap                  | Impact                         |
> | -------------------- | ------------------------------ |
> | No device management | Harus pakai platform lain      |
> | No MQTT built-in     | Perlu InfluxDB/Prometheus dulu |
> | No alerting (free)   | Perlu Grafana Cloud paid       |
> | No multi-tenant      | Complex setup untuk SaaS       |
>
> **SURGE Visualization:**
>
> - Line, bar, gauge, scatter charts (Recharts)
> - Real-time updates via Socket.IO
> - Interactive maps (Mapbox GL JS)
> - Device-centric view
> - Heatmap (coming soon)
> - Cukup untuk 90% industrial monitoring
>
> **Best of Both Worlds:**
>
> ```
> Devices ───> SURGE ───> API ───> Grafana
>                │
>          Standard dashboard       Custom beautiful dashboard
>          (included)               (if you want)
> ```
>
> **Kesimpulan:** SURGE untuk monitoring + management. Grafana bisa ditambahkan untuk advanced visualization via API.

---

## ROASTING 5.3: "Tidak ada mobile app, kompetitor sudah punya!"

**Kritik:**

> "Blynk punya native mobile app. SURGE harus buka browser?"

**Response:**

> Valid point. Ini roadmap mobile kami:
>
> **Current State:**
>
> - Responsive web app (works on mobile browser)
> - PWA-ready (add to home screen)
> - All features accessible via mobile browser
>
> **PWA Advantages:**
>
> | Feature      | Native App | PWA (SURGE) |
> | ------------ | ---------- | ----------- |
> | Installation | App Store  | Instant     |
> | Updates      | Manual     | Automatic   |
> | Storage      | 50-100MB   | <5MB        |
> | Offline      | Yes        | Partial     |
> | Push notif   | Yes        | Planned     |
>
> **Roadmap:**
>
> | Feature            | Timeline |
> | ------------------ | -------- |
> | PWA improvements   | Q1 2026  |
> | Push notifications | Q1 2026  |
> | React Native app   | Q3 2026  |
>
> **Honest Assessment:**
>
> - Untuk check dashboard: PWA sudah cukup
> - Untuk field data entry: Native app lebih baik (coming soon)
>
> **Kesimpulan:** Current PWA functional untuk monitoring. Native app dalam roadmap.

---

# 6. SECURITY & COMPLIANCE

## ROASTING 6.1: "Data di cloud tidak aman! Kami mau on-premise!"

**Kritik:**

> "Regulasi kami tidak boleh data di luar Indonesia. Cloud tidak compliant."

**Response:**

> Concern yang serius untuk regulated industries. Ini opsi kami:
>
> **Cloud Deployment (Standard):**
>
> - Server di Singapore (closest AWS region)
> - Encrypted at rest dan in transit
> - SOC 2 compliant infrastructure
> - GDPR-ready practices
>
> **Indonesia Hosting Option (Enterprise):**
>
> - Deploy di Indonesia data center (AWS Jakarta, Alibaba Jakarta)
> - Same platform, different location
> - Premium pricing (setup + hosting cost)
>
> **On-Premise Option (Enterprise):**
>
> | Item              | Requirement          |
> | ----------------- | -------------------- |
> | Minimum server    | 8 core, 32GB RAM     |
> | Database          | PostgreSQL + TimescaleDB |
> | Container runtime | Docker/Kubernetes    |
> | Pricing           | $10,000 setup + $2,000/year license |
>
> **Hybrid Option:**
>
> ```
> Your Network ─── SURGE Edge ─── Encrypted ─── SURGE Cloud
>       │                              │
>   Raw data stays local        Aggregated data only
> ```
>
> **For PP PSTE Compliance (Indonesia):**
>
> - Indonesia hosting available
> - Data residency dapat diatur
>
> **Kesimpulan:** Tersedia opsi untuk setiap requirement, dari cloud sampai full on-premise.

---

## ROASTING 6.2: "Sertifikasi security apa yang SURGE punya?"

**Kritik:**

> "Enterprise kami butuh SOC 2, ISO 27001. Apakah SURGE compliant?"

**Response:**

> Ini status sertifikasi kami:
>
> **Current Certifications:**
>
> | Certification   | Status      | Timeline |
> | --------------- | ----------- | -------- |
> | SSL/TLS         | Active      | Done     |
> | OWASP Top 10    | Compliant   | Tested   |
> | Data encryption | Implemented | AES-256  |
> | SOC 2 Type II   | In progress | Q2 2026  |
> | ISO 27001       | Planned     | Q4 2026  |
>
> **Infrastructure Security (AWS/Cloud):**
>
> - AWS security (SOC 1/2/3, ISO 27001)
> - Managed database with encryption
> - VPC isolation
> - WAF protection
>
> **Application Security:**
>
> - JWT authentication
> - RBAC authorization (4 roles)
> - Input validation (Zod)
> - SQL injection protection (Prisma ORM)
> - Rate limiting
> - CSRF protection
>
> **Compliance Assistance:**
>
> - Security questionnaire available
> - Penetration test report (on request)
> - Architecture documentation for audit
>
> **For Enterprise with Strict Requirements:**
>
> - On-premise deployment option
> - Custom security audit
> - SLA with security guarantees
>
> **Kesimpulan:** Praktik security enterprise-grade, sertifikasi formal dalam proses.

---

# 7. USE CASE SPECIFIC

## ROASTING 7.1: "Untuk IPAL, kami butuh akreditasi lab, SURGE bisa?"

**Kritik:**

> "Data monitoring harus dari alat terakreditasi KAN. SURGE bukan lab terakreditasi."

**Response:**

> Important distinction yang perlu diperjelas:
>
> **SURGE adalah platform monitoring, BUKAN lab testing:**
>
> | Aspek     | Lab Akreditasi KAN  | SURGE Platform         |
> | --------- | ------------------- | ---------------------- |
> | Fungsi    | Testing & analysis  | Monitoring & reporting |
> | Frequency | 1x/bulan (sampling) | Real-time (continuous) |
> | Legalitas | Required untuk KLHK | Complementary          |
> | Data      | Official report     | Operational data       |
>
> **How SURGE Complements Lab Testing:**
>
> ```
> ┌─────────────────────┐          ┌─────────────────────┐
> │  Lab Akreditasi     │          │      SURGE          │
> │  (1x/bulan)         │          │   (24/7 real-time)  │
> ├─────────────────────┤          ├─────────────────────┤
> │ - Official KLHK     │          │ - Operational trend │
> │ - Legally binding   │          │ - Early warning     │
> │ - Expensive         │          │ - Affordable        │
> └─────────────────────┘          └─────────────────────┘
>          ↓                                ↓
>     Compliance                      Prevention
> ```
>
> **Value SURGE untuk IPAL:**
>
> - Real-time alerting jika parameter mendekati batas
> - Trend analysis untuk preventive action
> - Data history untuk troubleshooting (hingga 5 tahun di Professional)
> - Reduce surprise saat lab testing bulanan
> - Export format sesuai SISPEK KLHK
>
> **Kesimpulan:** SURGE = operational monitoring, BUKAN pengganti lab akreditasi. Keduanya complementary.

---

## ROASTING 7.2: "Energy monitoring sudah ada di BMS Schneider kami!"

**Kritik:**

> "Gedung kami sudah pakai Schneider EcoStruxure BMS. Kenapa butuh SURGE lagi?"

**Response:**

> EcoStruxure adalah excellent BMS. SURGE bukan replacement:
>
> **EcoStruxure BMS vs SURGE:**
>
> | Capability         | EcoStruxure BMS     | SURGE Energy    |
> | ------------------ | ------------------- | --------------- |
> | HVAC Control       | Yes (core function) | No              |
> | Lighting Control   | Yes                 | No              |
> | Energy Monitoring  | Yes (basic)         | Yes (advanced)  |
> | Multi-site Compare | Limited             | Yes             |
> | Mobile Access      | Via app             | Yes (web + PWA) |
> | Cost Analysis      | Basic               | Detailed        |
> | Integration        | Schneider devices   | Any device      |
>
> **Where SURGE Adds Value:**
>
> ```
> Schneider BMS ─── Data ───> SURGE ───> Advanced Analytics
>       │                          │
>   Control                   Analysis + Reporting
>   (keep it)                 (add this)
> ```
>
> **Use Cases untuk SURGE + BMS:**
>
> - Multi-building comparison (BMS per building, SURGE centralized)
> - Advanced reporting untuk management
> - Integration dengan non-Schneider devices
> - Cost allocation per tenant/department
> - **Unlimited locations** - monitor semua gedung dalam satu dashboard
>
> **Kesimpulan:** BMS untuk control, SURGE untuk analytics dan multi-site visibility.

---

## ROASTING 7.3: "Vessel tracking sudah pakai MarineTraffic, kenapa SURGE?"

**Kritik:**

> "MarineTraffic atau VesselFinder sudah gratis untuk tracking kapal. SURGE mau compete?"

**Response:**

> MarineTraffic adalah excellent untuk AIS tracking. Tapi:
>
> **MarineTraffic (AIS-based):**
>
> | Feature            | Availability     |
> | ------------------ | ---------------- |
> | Position tracking  | Yes (public AIS) |
> | Fuel monitoring    | No               |
> | Engine RPM         | No               |
> | Cargo data         | No               |
> | Custom parameters  | No               |
> | Private fleet only | No (public data) |
>
> **SURGE Vessel Tracking:**
>
> | Feature           | Availability                 |
> | ----------------- | ---------------------------- |
> | Position tracking | Yes (private GPS)            |
> | Fuel monitoring   | Yes                          |
> | Engine RPM        | Yes                          |
> | Custom sensors    | Yes                          |
> | Private data      | Yes (your fleet only)        |
> | Integration       | Combined dengan Energy/Water |
>
> **Different Use Cases:**
>
> - **MarineTraffic:** Track any vessel worldwide (public info)
> - **SURGE:** Operational monitoring MILIK ANDA (private, detailed)
>
> **SURGE Advantage:**
>
> ```
> Your Vessel ─── Your Sensors ─── Private Data ─── SURGE
>      │
>  GPS + Fuel + Engine + Custom
>  (all YOUR data, private)
> ```
>
> **Kesimpulan:** MarineTraffic = public tracking. SURGE = private operational monitoring.

---

# 8. TRIAL ACCESS OBJECTIONS

## ROASTING 8.1: "Kenapa Trial harus kontak dulu? Kompetitor langsung signup!"

**Kritik:**

> "Datacake, Ubidots bisa langsung signup dan pakai. SURGE ribet harus kontak tim dulu."

**Response:**

> Valid concern! Ini alasan kami:
>
> **Why Private Trial?**
>
> | Concern                 | Our Mitigation                     |
> | ----------------------- | ---------------------------------- |
> | Prevent abuse           | Qualify serious prospects          |
> | Better onboarding       | Personal demo + setup assistance   |
> | Optimal configuration   | Kami bantu setup yang benar        |
> | Industry-specific setup | Water/Energy/Vessel needs differ   |
>
> **What You Get with Our Process:**
>
> ```
> ┌──────────────────────────────────────────────────────────────┐
> │  KOMPETITOR                │  SURGE                          │
> ├──────────────────────────────────────────────────────────────┤
> │  Self-signup               │  Guided demo                    │
> │  Figure out yourself       │  Personal onboarding            │
> │  Generic tutorial          │  Industry-specific setup        │
> │  Generic limits            │  Configured for your use case   │
> │  No one to call            │  Direct WA support              │
> └──────────────────────────────────────────────────────────────┘
> ```
>
> **Process Time:**
>
> - Kontak via WA/email: Instantly
> - Demo scheduling: Same day atau next day
> - Account creation: During atau after demo
> - **Total: <24 jam** (bukan berminggu-minggu)
>
> **Honest Admission:**
>
> - Ya, ini friction point
> - Trade-off: Better qualified leads = better support per customer
> - Self-signup dalam roadmap untuk Starter plan (Q2 2026)
>
> **Kesimpulan:** 24 jam extra untuk dapat dedicated support dan optimal setup. Worth it.

---

## ROASTING 8.2: "Trial cuma 5 tag, tidak cukup untuk test proper!"

**Kritik:**

> "5 tag data terlalu sedikit. Kami butuh setidaknya 20 untuk test meaningful."

**Response:**

> Understandable concern. Mari kita breakdown:
>
> **What 5 Tags Can Monitor:**
>
> | Use Case       | Example 5 Tags                          |
> | -------------- | --------------------------------------- |
> | Water (IPAL)   | pH, COD, TSS, NH3, Flow                 |
> | Energy         | kWh, kVA, PF, Volt, Amp                 |
> | Vessel         | GPS Lat, GPS Lon, Fuel, RPM, Speed      |
>
> **5 Tags = 1 Complete System Test:**
>
> - Cukup untuk prove concept bekerja
> - Test semua fitur: dashboard, alerts, export
> - Validate integration dengan device
>
> **If You Need More:**
>
> | Option               | Tags | Price      | Duration |
> | -------------------- | ---- | ---------- | -------- |
> | Trial                | 5    | Free       | 30 days  |
> | Extended Trial       | 15   | By request | 30 days  |
> | Starter (production) | 30   | $29/mo     | Ongoing  |
>
> **Extended Trial untuk Serious Prospects:**
>
> - Jika butuh 15-20 tags untuk proper POC
> - Request via sales team
> - Case-by-case approval
> - Usually untuk enterprise prospects
>
> **Kesimpulan:** 5 tag cukup untuk proof of concept. Extended trial available untuk serious prospects.

---

# QUICK REFERENCE CARD

## Objection → One-Liner Response

| Objection                     | Quick Response                                                          |
| ----------------------------- | ----------------------------------------------------------------------- |
| "Platform baru, tidak proven" | "Tech stack sama dengan Netflix/Uber. Demo gratis untuk buktikan."      |
| "ThingsBoard gratis"          | "Self-hosting $600+/bulan. SURGE $99 all-inclusive + KLHK + unlimited locations." |
| "Terlalu mahal"               | "Starter $29/bulan, 30 tags, unlimited lokasi. Satu penalty KLHK = 10 tahun subscription." |
| "Trial cuma 5 tag"            | "5 tag = 1 sistem lengkap. Extended trial available untuk serious prospects." |
| "Kenapa harus kontak dulu?"   | "24 jam untuk dapat demo + setup optimal. Self-signup coming Q2 2026."  |
| "Tidak ada mobile app"        | "PWA works sekarang. Native app dalam roadmap Q3 2026."                 |
| "Security certification?"     | "AWS infrastructure (SOC 2), SOC 2 app-level in progress Q2 2026."      |
| "Mau on-premise"              | "Available untuk enterprise. $10K setup + $2K/year license."            |
| "Visualization kurang"        | "90% use case covered. Grafana bisa integrate via API kalau mau."       |
| "Sudah ada BMS/SCADA"         | "SURGE complement, bukan replace. Add remote + analytics + unlimited locations." |
| "Retention terlalu pendek"    | "Trial 30d, Starter 1y, Business 2y, Pro 5 tahun. Pick your need."     |

---

## Pricing Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           SURGE PRICING v2.0                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│  TRIAL          STARTER         BUSINESS         PROFESSIONAL                   │
│  Free           $29/mo          $99/mo           $299/mo                        │
│  ──────────     ──────────      ──────────       ──────────                     │
│  5 tags         30 tags         100 tags         Unlimited tags                 │
│  Unlimited loc  Unlimited loc   Unlimited loc    Unlimited loc                  │
│  2-min logging  1-min logging   1-min logging    Custom logging                 │
│  30-day data    1-year data     2-year data      5-year data                    │
│  Private/Demo   Public          Public           Public                         │
│  Email support  WA support      Phone support    24/7 support                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  KEY MESSAGE: Unlimited locations di SEMUA tier = unique vs kompetitor!         │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

# CLOSING STATEMENT

Ketika customer masih ragu setelah semua penjelasan:

> "Pak/Bu, saya mengerti semua kekhawatiran Anda. Sebagai platform baru, kami harus kerja lebih keras untuk membuktikan diri.
>
> Yang bisa kami tawarkan:
>
> 1. **Demo session** - Kami tunjukkan langsung fitur yang Anda butuhkan
> 2. **Trial account** - Test dengan data real Anda (5-15 tags)
> 3. **Technical deep-dive** - Tim IT Anda bisa review architecture kami
> 4. **Reference customer** - Kami arrange call dengan user existing
>
> Risiko Anda: Minimal (trial gratis, no commitment)
> Potential benefit: Compliance terjaga, monitoring real-time, biaya jauh lebih rendah dari alternatif, unlimited locations
>
> Boleh saya arrange demo session? Prosesnya cepat, hari ini WA, besok bisa demo."

---

_Document Version: 2.0_
_For Internal Sales Team Use_
_Last Updated: December 29, 2025_
