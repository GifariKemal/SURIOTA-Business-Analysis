# FAQ & Response Template - SURGE Platform

**Panduan menjawab pertanyaan pelanggan dengan format konsisten dan profesional**

---

## Cara Menggunakan Template Ini

### Prinsip Menjawab

1. **Langsung ke inti** - Tidak bertele-tele, jawab pertanyaan di kalimat pertama
2. **Pakai tabel** - Lebih mudah dibaca daripada paragraf panjang
3. **Bold untuk emphasis** - Highlight poin penting dengan **bold**
4. **Berikan angka konkret** - Bukan "banyak" tapi "50 parameters"
5. **Akhiri dengan aksi** - Rekomendasi atau next step yang jelas

### Format Standar

```markdown
## [PERTANYAAN PELANGGAN]

[Jawaban singkat 1-2 kalimat - langsung menjawab pertanyaan]

| Aspek | Detail | Keterangan |
| ----- | ------ | ---------- |
| ...   | ...    | ...        |

**Kesimpulan:** [Rekomendasi atau next step]
```

---

# CONTOH FAQ LENGKAP

---

## Berapa harga SURGE Platform?

Tersedia 4 tier subscription dengan harga berbeda:

| Plan             | Harga/Bulan         | Parameters | Locations | Retention |
| ---------------- | ------------------- | ---------- | --------- | --------- |
| **Trial**        | Free                | 5          | 1         | 30 hari   |
| **Starter**      | Rp 464.000 ($29)    | 10         | 3         | 90 hari   |
| **Business**     | Rp 1.584.000 ($99)  | 25         | 10        | 1 tahun   |
| **Professional** | Rp 4.784.000 ($299) | Unlimited  | Unlimited | 3 tahun   |

**Diskon 20% untuk pembayaran annual.** Hubungi sales@suriota.com untuk pricing custom.

---

## Apakah ada trial gratis?

Ya, tersedia **Trial Plan gratis selama 30 hari**:

| Fitur Trial    | Limit               |
| -------------- | ------------------- |
| Parameters     | 5 parameters        |
| Locations      | 1 lokasi            |
| Data Retention | 30 hari             |
| Dashboard      | Basic (semua chart) |
| Support        | Community (email)   |
| Data Export    | Ya                  |

**Kesimpulan:** Daftar di surge.suriota.com, tidak perlu kartu kredit.

---

## Apa itu "parameter" dalam limit subscription?

**Parameter** adalah sensor/data point yang Anda monitor, seperti pH, suhu, atau kWh.

| Contoh Use Case             | Parameters Dibutuhkan                      |
| --------------------------- | ------------------------------------------ |
| 1 sensor pH + suhu          | 2 parameters                               |
| 5 meter listrik (kWh saja)  | 5 parameters                               |
| Water treatment plant kecil | 10-15 parameters (pH, COD, TSS, flow, dll) |
| Gedung dengan 10 lantai     | 20-25 parameters                           |

**Kesimpulan:** Starter (10 params) cukup untuk 1 fasilitas kecil. Business (25 params) untuk fasilitas menengah.

---

## SURGE bisa untuk monitoring apa saja?

SURGE punya **3 modul industri terintegrasi**:

| Modul               | Use Case                    | Parameter Contoh        |
| ------------------- | --------------------------- | ----------------------- |
| **Water Analytics** | IPAL, STP, WTP, PDAM        | pH, COD, TSS, NH3, Flow |
| **Energy Mapping**  | Gedung, Pabrik, Data Center | kWh, kVA, Power Factor  |
| **Vessel Tracking** | Kapal, Fleet, Maritim       | GPS, Fuel, RPM, Speed   |

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

**Kesimpulan:** Data setiap organisasi terisolasi, tidak bisa diakses organisasi lain.

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

## Berapa lama data retention?

Retention berbeda per tier:

| Plan         | Retention | Storage Est. |
| ------------ | --------- | ------------ |
| Trial        | 30 hari   | ~100MB       |
| Starter      | 90 hari   | ~500MB       |
| Business     | 1 tahun   | ~2GB         |
| Professional | 3 tahun   | ~10GB        |

**Opsi tambahan:** Extended retention +1 tahun dengan add-on $20/tahun.

**Kesimpulan:** Business plan (1 tahun) cukup untuk mayoritas kebutuhan audit.

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
| 1    | Daftar Trial di surge.suriota.com    | 5 menit    |
| 2    | Setup organization + lokasi          | 10 menit   |
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
| Harga?                 | "Mulai Rp 464rb/bulan (Starter) sampai Rp 4.8jt (Prof)" |
| Ada trial gratis?      | "Ya, 30 hari free dengan 5 parameters"                  |
| Bisa untuk IPAL?       | "Ya, SURGE Water Analytics khusus untuk IPAL/WTP/STP"   |
| KLHK compliance?       | "Ya, format export sudah sesuai SISPEK"                 |
| Sensor apa yg support? | "Semua sensor Modbus/MQTT, kami jual gateway juga"      |
| Beda sama ThingsBoard? | "SURGE lebih murah, ada KLHK compliance, support lokal" |
| Data aman?             | "Ya, encrypted + isolated per organisasi"               |
| Mulai dari mana?       | "Daftar trial di surge.suriota.com, gratis 30 hari"     |
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

_Template Version: 1.0 | Updated: December 28, 2025_
