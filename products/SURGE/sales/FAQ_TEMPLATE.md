# FAQ & Response Template - SURGE Platform

**Panduan menjawab pertanyaan pelanggan dengan format konsisten dan profesional**

**Version**: 2.0 | **Last Updated**: December 29, 2025

---

## Cara Menggunakan Template Ini

### Prinsip Menjawab

1. **Langsung ke inti** - Tidak bertele-tele, jawab pertanyaan di kalimat pertama
2. **Pakai tabel** - Lebih mudah dibaca daripada paragraf panjang
3. **Bold untuk emphasis** - Highlight poin penting dengan **bold**
4. **Berikan angka konkret** - Bukan "banyak" tapi "100 tag data"
5. **Akhiri dengan aksi** - Rekomendasi atau next step yang jelas

---

# FAQ LENGKAP - PRICING & SUBSCRIPTION

---

## Berapa harga SURGE Platform?

Tersedia 4 tier subscription dengan harga berbeda:

| Plan             | Harga/Bulan         | Tag Data   | Lokasi    | Retention |
| ---------------- | ------------------- | ---------- | --------- | --------- |
| **Trial**        | Free                | 5          | Unlimited | 30 hari   |
| **Starter**      | Rp 464.000 ($29)    | 30         | Unlimited | 1 tahun   |
| **Business**     | Rp 1.584.000 ($99)  | 100        | Unlimited | 2 tahun   |
| **Professional** | Rp 4.784.000 ($299) | Unlimited  | Unlimited | 5 tahun   |

**Diskon 20% untuk pembayaran annual.** Hubungi sales@suriota.com untuk pricing custom.

---

## Apakah ada trial gratis?

Ya, tersedia **Trial Plan gratis selama 30 hari**, namun bersifat **private/invitation only**:

| Fitur Trial    | Limit               |
| -------------- | ------------------- |
| Tag Data       | 5 tag               |
| Lokasi         | Unlimited           |
| Logging Interval| 2 menit            |
| Data Retention | 30 hari             |
| Dashboard      | Basic (semua chart) |
| Support        | Email only          |
| Data Export    | Limited             |

**Cara Mendapatkan Trial:**
1. Hubungi tim SURIOTA via sales@suriota.com atau WhatsApp
2. Tim akan melakukan discovery call untuk memahami kebutuhan Anda
3. Akun trial akan dibuatkan khusus untuk Anda
4. Data Anda terisolasi penuh (tidak bisa dilihat organisasi lain)

**Kesimpulan:** Trial tidak publik untuk memastikan onboarding yang proper.

---

## Apa itu "tag data/parameter" dalam limit subscription?

**Tag data/parameter** adalah sensor/data point yang Anda monitor, seperti pH, suhu, atau kWh.

| Contoh Use Case             | Tag Data Dibutuhkan                        |
| --------------------------- | ------------------------------------------ |
| 1 sensor pH + suhu          | 2 tag                                      |
| 5 meter listrik (kWh saja)  | 5 tag                                      |
| Water treatment plant kecil | 10-15 tag (pH, COD, TSS, flow, dll)        |
| Gedung dengan 10 lantai     | 20-30 tag                                  |
| Pabrik menengah             | 50-100 tag                                 |

**Kesimpulan:**
- Starter (30 tags) cukup untuk 1 fasilitas kecil-menengah
- Business (100 tags) untuk multi-facility atau pabrik menengah

---

## Apa bedanya lokasi dengan tag data?

| Konsep    | Definisi                                    | Contoh                      |
| --------- | ------------------------------------------- | --------------------------- |
| **Lokasi**| Tempat fisik perangkat dipasang             | Pabrik A, Gedung B, Kapal C |
| **Tag Data**| Parameter yang dimonitor per lokasi       | pH, kWh, GPS, suhu          |

**Contoh:**
- Anda punya 3 lokasi (Pabrik A, B, C)
- Setiap lokasi monitor 10 parameter
- Total = 30 tag data

**SURGE unik:** Lokasi **UNLIMITED di semua tier**. Kompetitor biasanya batasi lokasi.

---

## Berapa interval penyimpanan data ke database?

| Tier         | Logging Interval | Keterangan                    |
| ------------ | :--------------: | ----------------------------- |
| Trial        | 2 menit          | Fixed                         |
| Starter      | 1 menit          | Fixed                         |
| Business     | 1 menit          | Fixed                         |
| Professional | Customizable     | Bisa 30 detik, 1, 2, 5 menit  |

**Penting - 2 Jenis Interval:**
1. **Live Monitoring Interval** = Real-time, tergantung sensor mengirim berapa sering
2. **Database Logging Interval** = Interval penyimpanan ke database untuk data historis

**Kesimpulan:** Live monitoring real-time, database logging sesuai tier untuk efisiensi storage.

---

## Berapa lama data retention?

Retention berbeda per tier:

| Plan         | Retention | Storage Est. |
| ------------ | --------- | ------------ |
| Trial        | 30 hari   | ~100MB       |
| Starter      | 1 tahun   | ~1GB         |
| Business     | 2 tahun   | ~5GB         |
| Professional | 5 tahun   | ~20GB        |

**Opsi tambahan:** Extended retention +1 tahun dengan add-on $50/tahun.

**Kesimpulan:** Business plan (2 tahun) cukup untuk mayoritas kebutuhan audit dan compliance.

---

# FAQ LENGKAP - FITUR PLATFORM

---

## Fitur apa saja yang didapat di SURGE?

SURGE menyediakan fitur lengkap untuk industrial IoT monitoring:

### Fitur Dashboard & Visualization

| Fitur                 | Deskripsi                                    |
| --------------------- | -------------------------------------------- |
| **Live Monitoring**   | Data real-time dari sensor, auto-refresh     |
| **Interactive Charts**| Line, Bar, Gauge, Scatter dengan zoom/pan    |
| **Map View**          | Peta lokasi device dengan status indicator   |
| **Dashboard Builder** | Layout dashboard bisa di-customize           |
| **Heatmap**           | Visualisasi data spasial (planned)           |

### Fitur Data & Analytics

| Fitur                 | Deskripsi                                    |
| --------------------- | -------------------------------------------- |
| **Database Logging**  | Penyimpanan data historis dengan TimescaleDB |
| **Historical Data**   | Akses data historis dengan date range filter |
| **Data Export**       | Export ke Excel/CSV                          |
| **KLHK Export**       | Format sesuai SISPEK untuk Water Analytics   |
| **Trend Analysis**    | Analisis tren parameter over time            |

### Fitur Alert & Notification

| Fitur                 | Deskripsi                                    |
| --------------------- | -------------------------------------------- |
| **Threshold Alerts**  | Notifikasi ketika parameter melebihi batas   |
| **Email Notification**| Alert via email                              |
| **WhatsApp Alerts**   | Notifikasi via WhatsApp (planned)            |
| **Alert History**     | Log semua alert yang pernah terjadi          |

### Fitur User & Access

| Fitur                 | Deskripsi                                    |
| --------------------- | -------------------------------------------- |
| **Role Management**   | RBAC: Viewer, Member, Admin, Owner           |
| **Multi-user**        | Multiple user per organisasi                 |
| **Multi-tenant**      | Data terisolasi per organisasi               |
| **API Access**        | REST API untuk integrasi (Business+)         |

---

## SURGE bisa untuk monitoring apa saja?

SURGE punya **3 modul industri terintegrasi** + support custom use case:

| Modul               | Use Case                    | Parameter Contoh        |
| ------------------- | --------------------------- | ----------------------- |
| **Water Analytics** | IPAL, STP, WTP, PDAM        | pH, COD, TSS, NH3, Flow |
| **Energy Mapping**  | Gedung, Pabrik, Data Center | kWh, kVA, Power Factor  |
| **Vessel Tracking** | Kapal, Fleet, Maritim       | GPS, Fuel, RPM, Speed   |
| **Custom**          | Cold chain, HVAC, Tank, dll | Sesuai kebutuhan        |

**Kesimpulan:** Semua modul termasuk dalam subscription, tidak ada biaya tambahan per modul.

---

## Apakah data saya aman?

Ya, keamanan data adalah prioritas kami:

| Security Layer     | Implementation                    |
| ------------------ | --------------------------------- |
| **Encryption**     | TLS/SSL untuk semua koneksi       |
| **Authentication** | JWT dengan refresh token          |
| **Authorization**  | RBAC (viewer/member/admin/owner)  |
| **Data Isolation** | Multi-tenant dengan isolasi penuh |
| **Backup**         | Daily automated backup            |
| **Uptime**         | Target 99.5% SLA                  |

**Kesimpulan:** Data setiap organisasi terisolasi penuh, tidak bisa diakses organisasi lain.

---

## Bagaimana cara integrasi dengan sensor/device saya?

SURGE mendukung **MQTT protocol** yang universal:

| Metode Integrasi | Deskripsi                               |
| ---------------- | --------------------------------------- |
| **MQTT Direct**  | Sensor langsung publish ke SURGE broker |
| **Via Gateway**  | Modbus sensor → SURIOTA Gateway → SURGE |
| **REST API**     | POST data via HTTP                      |
| **Webhook**      | SURGE bisa push ke sistem Anda          |

**Device yang Tested:**

- SURIOTA SRT-MGATE-1210 (fully integrated)
- Generic Modbus sensors
- ESP32/ESP8266 devices
- LoRaWAN sensors (via network server)

**Kesimpulan:** Kalau device Anda support MQTT atau Modbus, pasti bisa connect.

---

## Apa bedanya dengan ThingsBoard/Grafana?

SURGE dirancang khusus untuk **industri Indonesia**:

| Fitur            | ThingsBoard | Grafana  | SURGE             |
| ---------------- | ----------- | -------- | ----------------- |
| Bahasa Indonesia | Tidak       | Tidak    | **Ya**            |
| KLHK Compliance  | Tidak       | Tidak    | **Ya**            |
| Modul Water      | Generic     | Tidak    | **Specialized**   |
| Modul Energy     | Generic     | Generic  | **Specialized**   |
| Modul Vessel     | Tidak       | Tidak    | **Ya**            |
| Lokasi           | Limited     | Limited  | **Unlimited**     |
| Setup Complexity | Tinggi      | Tinggi   | **Rendah**        |
| Local Support    | Tidak       | Tidak    | **Ya (WA/Phone)** |
| Harga (mid-tier) | $399/month  | Variable | **$99/month**     |

**Kesimpulan:** SURGE = fitur enterprise dengan harga SMB + localization Indonesia.

---

## Bagaimana compliance dengan KLHK?

SURGE Water Analytics sudah **compliance ready** untuk KLHK:

| Fitur Compliance      | Detail                                  |
| --------------------- | --------------------------------------- |
| **Parameter Standar** | pH, COD, TSS, NH3, BOD sesuai baku mutu |
| **Format Laporan**    | Sesuai format SISPEK                    |
| **Threshold**         | Baku mutu PP 22/2021                    |
| **Export**            | Excel dengan format KLHK                |
| **Audit Trail**       | Log perubahan data                      |

**Regulasi yang Didukung:**

- PP 22/2021 - Baku Mutu Air Limbah
- Permen LHK 5/2014 - Baku Mutu Air Limbah Domestik
- SNI 6989 - Parameter kualitas air

**Kesimpulan:** Export data, format sudah siap untuk SISPEK.

---

## Bisa diakses dari mobile?

Ya, SURGE adalah **responsive web app**:

| Platform    | Support          |
| ----------- | ---------------- |
| Desktop     | Full-featured    |
| Tablet      | Full-featured    |
| Mobile      | Responsive (PWA) |
| iOS App     | Planned (2026)   |
| Android App | Planned (2026)   |

**PWA Features:**

- Add to home screen
- Offline viewing (limited)
- Push notifications (planned)

**Kesimpulan:** Akses dari browser HP, tidak perlu install app.

---

## Apakah bisa white-label untuk reseller?

Ya, tersedia **white-label option** di tier Professional:

| White-label Feature | Detail                                   |
| ------------------- | ---------------------------------------- |
| Custom Logo         | Ganti logo SURGE dengan logo Anda        |
| Custom Domain       | your-brand.com (bukan surge.suriota.com) |
| Custom Colors       | Sesuaikan tema warna                     |
| Remove "Powered by" | Sembunyikan branding SURIOTA             |
| Custom Email        | Notifikasi dari email Anda               |

**Harga:**

- Professional Plan: $299/month (termasuk white-label)
- One-time setup fee: $1,000

**Kesimpulan:** Ideal untuk System Integrator yang mau jual dengan brand sendiri.

---

## Bagaimana support dan SLA?

Support berbeda per tier:

| Tier         | Support Channel     | Response Time |
| ------------ | ------------------- | ------------- |
| Trial        | Email only          | 48 jam        |
| Starter      | Email + WA          | 24 jam        |
| Business     | Email + WA + Phone  | 8 jam         |
| Professional | Dedicated + On-site | 4 jam         |

**SLA Uptime:**

- Standard: 99.5%
- Professional: 99.9% dengan credit jika gagal

**Kesimpulan:** Business plan sudah dapat response 8 jam untuk kebanyakan kebutuhan.

---

## Saya punya IPAL, mulai dari mana?

Langkah onboarding untuk IPAL baru:

| Step | Aksi                                 | Waktu Est. |
| ---- | ------------------------------------ | ---------- |
| 1    | Hubungi tim SURIOTA untuk trial      | 5 menit    |
| 2    | Discovery call & setup akun          | 30 menit   |
| 3    | Install gateway SURIOTA (jika perlu) | 1-2 hari   |
| 4    | Connect sensor ke gateway            | 1 hari     |
| 5    | Configure parameters di SURGE        | 30 menit   |
| 6    | Training dashboard & reporting       | 1 jam      |

**Kami bantu:**

- Site survey (jika perlu)
- Gateway installation
- Configuration
- Training

**Kesimpulan:** Dari sign-up sampai live monitoring ~3-5 hari dengan bantuan kami.

---

## Apakah bisa integrasi dengan sistem lain (ERP/SAP)?

Ya, SURGE menyediakan **API dan webhook**:

| Integration Type | Capability                     |
| ---------------- | ------------------------------ |
| **REST API**     | Pull data dari SURGE           |
| **Webhook**      | SURGE push data ke sistem Anda |
| **MQTT**         | Real-time stream               |
| **Export**       | Manual Excel/CSV               |

**Contoh Integrasi:**

- SAP/Oracle ERP (via API)
- Power BI/Tableau (via API)
- WhatsApp alerts (via webhook)
- Email notifications (built-in)

**Kesimpulan:** Tier Business keatas dapat full API access.

---

## Hardware apa yang direkomendasikan?

Untuk **Modbus sensors**, kami rekomendasikan gateway SURIOTA:

| Product                | Harga        | Untuk                       |
| ---------------------- | ------------ | --------------------------- |
| **SRT-MGATE-1210**     | Rp 2,700,000 | Standard 2xRS485, WiFi, BLE |
| **SRT-MGATE-1210-POE** | Rp 3,100,000 | + PoE support               |

**Keunggulan SRT-MGATE-1210:**

- Pre-configured untuk SURGE
- WiFi + Ethernet auto-failover
- BLE mobile configuration
- Local support

**Kesimpulan:** Total solution: Gateway Rp 2.7M + Starter $29/mo = lengkap IoT monitoring.

---

# QUICK RESPONSE CARD

Untuk jawaban cepat via WhatsApp/Chat:

| Pertanyaan             | Jawaban Singkat                                         |
| ---------------------- | ------------------------------------------------------- |
| Harga?                 | "Mulai Rp 464rb/bulan (30 tag) sampai Rp 4.8jt (unlimited)" |
| Ada trial gratis?      | "Ya, 30 hari free, hubungi kami untuk dibuatkan akun"   |
| Berapa tag data?       | "Starter 30, Business 100, Professional unlimited"      |
| Lokasi?                | "Unlimited di semua tier"                               |
| Bisa untuk IPAL?       | "Ya, SURGE Water Analytics khusus untuk IPAL/WTP/STP"   |
| KLHK compliance?       | "Ya, format export sudah sesuai SISPEK"                 |
| Sensor apa yg support? | "Semua sensor Modbus/MQTT, kami jual gateway juga"      |
| Beda sama ThingsBoard? | "SURGE lebih murah 75%, KLHK compliance, support lokal" |
| Data aman?             | "Ya, encrypted + isolated per organisasi"               |
| Mulai dari mana?       | "Hubungi kami untuk trial, WA: +62 858-3567-2476"       |
| White-label?           | "Tersedia di Professional tier ($299/bulan)"            |
| Support?               | "WA/Phone untuk Business tier keatas, response <8 jam"  |

---

# TEMPLATE KOSONG

Copy template ini untuk menambah FAQ baru:

```markdown
## [PERTANYAAN PELANGGAN]

[Jawaban singkat 1-2 kalimat]

| Kolom 1 | Kolom 2 | Kolom 3 |
| ------- | ------- | ------- |
| Data    | Data    | Data    |

**Kesimpulan:** [Rekomendasi/next step]
```

---

## Kontak

**PT Surya Inovasi Prioritas (SURIOTA)**

|          |                   |
| -------- | ----------------- |
| Website  | www.suriota.com   |
| Platform | surge.suriota.com |
| Email    | sales@suriota.com |
| Phone    | +62 858-3567-2476 |

---

_Template Version: 2.0 | Updated: December 29, 2025_
