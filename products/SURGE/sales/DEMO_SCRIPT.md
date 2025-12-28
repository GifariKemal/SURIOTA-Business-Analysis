# SURGE Platform - Demo Script

## Panduan Presentasi Demo untuk Sales Team

**Document Version**: 1.0
**Last Updated**: December 28, 2025
**Duration**: 30-45 menit
**Audience**: Prospect customer (Ops Manager, Environment Manager, IT Manager)

---

# PERSIAPAN SEBELUM DEMO

## Checklist Teknis

| Item | Status | Notes |
|------|:------:|-------|
| Internet stabil (>10 Mbps) | [ ] | Test sebelum meeting |
| Login SURGE demo account | [ ] | admin@suriota.com |
| Browser Chrome/Firefox terbaru | [ ] | Clear cache jika perlu |
| Screen sharing ready | [ ] | Test audio + video |
| Backup: Screenshots/video | [ ] | Jika internet bermasalah |

## Informasi yang Harus Dikumpulkan Sebelum Demo

| Pertanyaan | Jawaban Customer | Impact |
|------------|------------------|--------|
| Industri apa? | _____________ | Pilih modul yang relevan |
| Berapa lokasi? | _____________ | Tentukan tier yang cocok |
| Sensor/device apa yang dipakai? | _____________ | Tunjukkan integrasi |
| Masalah utama saat ini? | _____________ | Focus pain point |
| Budget range? | _____________ | Sesuaikan pricing discussion |
| Timeline decision? | _____________ | Urgency level |

---

# STRUKTUR DEMO (30 Menit)

## Timeline Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  0-3 min    │  Opening & Rapport Building                          │
│  3-8 min    │  Pain Point Discovery & Confirmation                 │
│  8-20 min   │  Platform Demo (sesuai modul)                        │
│  20-25 min  │  Pricing & ROI Discussion                            │
│  25-30 min  │  Q&A & Next Steps                                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

# SCRIPT DETAIL

## BAGIAN 1: Opening (3 menit)

### Salam & Intro (1 menit)

> "Selamat [pagi/siang/sore] Pak/Bu [Nama]. Terima kasih sudah meluangkan waktu untuk demo SURGE hari ini.
>
> Saya [Nama Anda] dari SURIOTA. Sebelum kita mulai, boleh saya konfirmasi - apakah ada peserta lain yang akan join, atau kita bisa mulai sekarang?"

*[Tunggu konfirmasi]*

### Set Expectations (1 menit)

> "Oke, untuk demo hari ini saya akan:
> 1. Konfirmasi kebutuhan Bapak/Ibu terlebih dahulu
> 2. Tunjukkan bagaimana SURGE bisa membantu
> 3. Diskusi pricing dan next steps
>
> Total sekitar 30 menit. Apakah ada agenda atau pertanyaan spesifik yang ingin dibahas?"

*[Catat jika ada request khusus]*

### Quick Company Intro (1 menit)

> "Sedikit tentang kami - SURIOTA adalah perusahaan IoT lokal yang fokus di industrial monitoring. SURGE adalah platform SaaS kami yang sudah dipakai untuk monitoring kualitas air, energi, dan armada kapal.
>
> Yang membedakan kami: support lokal dalam Bahasa Indonesia, dan untuk Water Analytics - sudah siap untuk compliance KLHK."

---

## BAGIAN 2: Pain Point Discovery (5 menit)

### Opening Questions

> "Sebelum saya tunjukkan platform-nya, saya ingin memahami situasi Bapak/Ibu dulu.
>
> **Pertanyaan 1:** Saat ini monitoring [kualitas air/energi/armada] dilakukan bagaimana?"

*[Dengarkan, catat pain points]*

Kemungkinan jawaban & follow-up:

| Jawaban Customer | Follow-up Question |
|------------------|-------------------|
| "Manual, pakai Excel" | "Berapa lama waktu yang dibutuhkan untuk compile data setiap bulan?" |
| "Sudah ada SCADA" | "Apakah bisa diakses dari luar site? Atau harus di control room?" |
| "Pakai platform X" | "Apa yang kurang dari platform tersebut?" |
| "Belum ada monitoring" | "Apa yang memotivasi untuk mulai monitoring sekarang?" |

### Confirm Pain Points

> "Jadi kalau saya rangkum, tantangan utama saat ini adalah:
> 1. [Pain point 1]
> 2. [Pain point 2]
> 3. [Pain point 3]
>
> Betul seperti itu, Pak/Bu?"

*[Tunggu konfirmasi sebelum lanjut demo]*

---

## BAGIAN 3: Platform Demo (12 menit)

### 3A. Login & Dashboard Overview (2 menit)

*[Share screen, buka SURGE]*

> "Ini adalah SURGE Platform. Saya login dengan akun demo..."

*[Login: admin@suriota.com]*

> "Setelah login, Bapak/Ibu langsung melihat dashboard overview.
>
> Di sini terlihat:
> - **Status semua device** - mana yang online, mana yang offline
> - **Alert terbaru** - jika ada parameter yang melewati threshold
> - **Quick stats** - summary dari semua lokasi"

**Key Points to Highlight:**
- Real-time data (tunjukkan timestamp)
- Clean, modern interface
- Bahasa Indonesia option

---

### 3B. Demo Sesuai Modul (8 menit)

#### OPSI A: Water Analytics Demo

*[Untuk customer IPAL/STP/WTP]*

> "Karena Bapak/Ibu dari [IPAL/industri], saya fokuskan ke Water Analytics module..."

**Step 1: Location Map (1 menit)**
> "Di sini terlihat peta semua outlet monitoring. Klik salah satu untuk lihat detail..."

*[Klik lokasi di map]*

**Step 2: Real-time Parameters (2 menit)**
> "Ini parameter real-time dari outlet ini:
> - pH: [nilai] - threshold kami set di 6-9 sesuai baku mutu
> - COD: [nilai] mg/L
> - TSS: [nilai] mg/L
>
> Lihat, data update setiap [interval]. Kalau ada yang melewati threshold, langsung alert."

**Step 3: Historical Chart (2 menit)**
> "Untuk melihat trend, kita bisa pilih range waktu...
>
> *[Pilih last 7 days]*
>
> Di sini terlihat pattern pH selama seminggu terakhir. Kalau ada anomaly, bisa langsung terdeteksi."

**Step 4: KLHK Export (2 menit)**
> "Yang paling penting untuk compliance - export data...
>
> *[Klik Export]*
>
> Format sudah sesuai standar KLHK, tinggal download dan submit ke SISPEK. Tidak perlu reformat lagi di Excel."

**Step 5: Alert Configuration (1 menit)**
> "Untuk setup alert, tinggal masukkan threshold sesuai baku mutu...
>
> *[Tunjukkan alert settings]*
>
> Ketika parameter melewati batas, notifikasi otomatis via email. WhatsApp notification coming soon."

---

#### OPSI B: Energy Mapping Demo

*[Untuk customer Building/Factory]*

> "Karena fokus di energy management, saya tunjukkan Energy Mapping module..."

**Step 1: Building/Floor Map (1 menit)**
> "Ini peta gedung dengan semua meter yang terpasang. Warna menunjukkan status - hijau normal, merah high consumption..."

**Step 2: Real-time kWh (2 menit)**
> "Untuk setiap meter, kita bisa lihat:
> - Konsumsi real-time dalam kWh
> - Power factor
> - Peak demand"

**Step 3: Comparison Chart (2 menit)**
> "Yang powerful - comparison antar zona atau antar periode...
>
> *[Tunjukkan comparison chart]*
>
> Di sini bisa lihat lantai mana yang paling boros, atau bandingkan weekday vs weekend."

**Step 4: Cost Analysis (2 menit)**
> "Kita juga bisa masukkan tarif PLN untuk lihat estimated cost...
>
> *[Tunjukkan cost breakdown]*
>
> Ini membantu untuk billing per tenant atau cost allocation per department."

**Step 5: Alert for Peak (1 menit)**
> "Alert bisa diset untuk peak demand, jadi sebelum kena penalty PLN, sudah ada warning."

---

#### OPSI C: Vessel Tracking Demo

*[Untuk customer Maritime/Fleet]*

> "Untuk fleet management, ini Vessel Tracking module..."

**Step 1: Fleet Map (2 menit)**
> "Semua kapal terlihat di peta maritim. Posisi update setiap [interval].
>
> *[Klik salah satu vessel]*
>
> Detail vessel: posisi, speed, heading, dan status engine."

**Step 2: Fuel Monitoring (2 menit)**
> "Yang critical untuk operasional - fuel monitoring...
>
> Lihat fuel level dan consumption rate. Bisa detect kalau ada anomaly consumption yang menunjukkan masalah engine atau... kebocoran."

**Step 3: Route History (2 menit)**
> "Untuk audit, kita bisa lihat route history...
>
> *[Playback route]*
>
> Kapan berangkat, rute yang diambil, berapa lama di setiap port."

**Step 4: Engine Performance (2 menit)**
> "RPM dan engine parameters untuk preventive maintenance. Kalau ada pattern abnormal, bisa schedule maintenance sebelum breakdown di tengah laut."

---

### 3C. Multi-tenant & Admin Features (2 menit)

> "Satu lagi yang penting - SURGE adalah multi-tenant platform.
>
> Artinya:
> - Setiap organisasi punya data terpisah dan terisolasi
> - Bisa invite team member dengan role berbeda (viewer, member, admin)
> - Owner bisa manage semua settings
>
> *[Tunjukkan organization settings]*
>
> Jadi kalau Bapak/Ibu punya beberapa site, semua bisa dikelola dari satu dashboard."

---

## BAGIAN 4: Pricing & ROI (5 menit)

### Present Options

> "Untuk pricing, SURGE punya 4 tier..."

*[Tampilkan pricing atau share screen pricing page]*

| Plan | Price | Best For |
|------|-------|----------|
| Trial | Free (30 hari) | Testing, PoC |
| Starter ($29/mo) | Rp 464K | Single facility, <10 params |
| Business ($99/mo) | Rp 1.58M | Multi-location, <25 params |
| Professional ($299/mo) | Rp 4.78M | Enterprise, unlimited |

> "Berdasarkan kebutuhan Bapak/Ibu dengan [X lokasi] dan [Y parameter], saya rekomendasikan **[Plan]**."

### ROI Discussion

> "Untuk ROI, mari kita hitung sederhana:
>
> **Cost of NOT monitoring:**
> - Penalty KLHK jika telat/tidak akurat: Rp 50-500 juta
> - Man-hours untuk manual reporting: [X] jam/bulan × Rp [Y] = Rp [Z]
> - Downtime dari masalah yang tidak terdeteksi: Rp [estimasi]
>
> **Investment SURGE:**
> - [Plan] = Rp [harga]/bulan = Rp [annual]/tahun
>
> **Payback:** Satu incident yang dicegah sudah cover [X] tahun subscription."

---

## BAGIAN 5: Q&A & Next Steps (5 menit)

### Invite Questions

> "Itu overview dari SURGE. Ada pertanyaan tentang fitur, pricing, atau teknis implementasi?"

*[Jawab pertanyaan - gunakan FAQ dan Roasting guide jika perlu]*

### Trial Offer

> "Untuk next step, saya sarankan:
>
> 1. **Trial gratis 30 hari** - Test dengan data real Bapak/Ibu
> 2. Kami bantu setup dan connect device pertama
> 3. Setelah 30 hari, evaluasi dan decide
>
> Tidak ada commitment, tidak perlu kartu kredit untuk trial.
>
> Apakah Bapak/Ibu tertarik untuk mulai trial?"

### Close with Action

**Jika YES:**
> "Bagus! Saya akan kirimkan link registrasi dan jadwalkan call untuk setup. Kapan waktu yang convenient untuk setup call - [opsi 1] atau [opsi 2]?"

**Jika NEED TIME:**
> "Tidak masalah. Saya akan kirimkan:
> 1. Summary demo hari ini
> 2. Proposal pricing
> 3. Link untuk daftar trial jika siap
>
> Kapan saya bisa follow-up untuk discuss lebih lanjut?"

**Jika NO/NOT INTERESTED:**
> "Terima kasih sudah meluangkan waktu. Boleh saya tahu apa concern utama yang membuat belum tertarik?
>
> *[Dengarkan, catat untuk improvement]*
>
> Jika ada perubahan kebutuhan di masa depan, feel free untuk reach out. Saya kirimkan contact info saya."

---

# HANDLING COMMON QUESTIONS DURING DEMO

| Question | Quick Answer |
|----------|--------------|
| "Bisa connect ke sensor merk X?" | "Kalau support Modbus atau MQTT, pasti bisa. Kami juga jual gateway untuk konversi." |
| "Data di-host di mana?" | "Cloud server di Singapore. Untuk enterprise, bisa Indonesia hosting atau on-premise." |
| "Bagaimana security-nya?" | "Encrypted, multi-tenant isolated, RBAC. SOC 2 certification dalam proses." |
| "Sudah ada customer lain?" | "Ya, sudah ada beberapa pilot di industri [X]. Referensi bisa diatur jika perlu." |
| "Bisa custom fitur?" | "Professional tier bisa request custom. Atau via API untuk integrasi sendiri." |

---

# POST-DEMO CHECKLIST

| Action | Timeline | Owner |
|--------|----------|-------|
| Send thank you email + summary | Same day | Sales |
| Send proposal/pricing PDF | Same day | Sales |
| Create trial account (if requested) | 1 day | Sales/Support |
| Schedule setup call | 2-3 days | Sales |
| Follow-up if no response | 1 week | Sales |
| Add to CRM pipeline | Same day | Sales |

---

# DEMO ACCOUNT ACCESS

| Item | Value |
|------|-------|
| **URL** | https://surge-nextjs-frontend.cp.suriotadb.com |
| **Email** | admin@suriota.com |
| **Password** | [Contact admin for password] |

**Demo Data Available:**
- Sample IPAL with 30-day history
- Sample building with energy data
- Sample vessel with route history

---

_Document Version: 1.0_
_For Internal Sales Team Use_
_Last Updated: December 28, 2025_
