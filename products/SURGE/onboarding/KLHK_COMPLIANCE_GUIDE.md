# SURGE Water Analytics - KLHK Compliance Guide

## Panduan Lengkap untuk Pemenuhan Regulasi Kementerian Lingkungan Hidup dan Kehutanan

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# DAFTAR ISI

1. [Overview Regulasi KLHK](#1-overview-regulasi-klhk)
2. [Parameter Wajib Monitor](#2-parameter-wajib-monitor)
3. [Baku Mutu Air Limbah](#3-baku-mutu-air-limbah)
4. [Konfigurasi SURGE untuk Compliance](#4-konfigurasi-surge-untuk-compliance)
5. [Pelaporan SISPEK](#5-pelaporan-sispek)
6. [Audit Trail & Dokumentasi](#6-audit-trail--dokumentasi)
7. [FAQ Compliance](#7-faq-compliance)

---

# 1. OVERVIEW REGULASI KLHK

## Regulasi yang Berlaku

| Regulasi | Judul | Relevansi |
|----------|-------|-----------|
| **PP 22/2021** | Penyelenggaraan Perlindungan dan Pengelolaan Lingkungan Hidup | Baku mutu air limbah |
| **Permen LHK 5/2014** | Baku Mutu Air Limbah | Baku mutu domestik |
| **Permen LHK 68/2016** | Baku Mutu Air Limbah Domestik | Update baku mutu |
| **SNI 6989** | Standar Pengukuran Parameter Kualitas Air | Metode pengukuran |
| **PROPER** | Program Penilaian Peringkat Kinerja | Rating kinerja lingkungan |

---

## Kewajiban Pelaporan

### Siapa yang Wajib Lapor?

| Jenis Usaha | Kapasitas | Kewajiban |
|-------------|-----------|-----------|
| Industri manufaktur | Semua kapasitas | Wajib |
| IPAL Komunal | > 50 m³/hari | Wajib |
| Hotel/Resort | > 100 kamar | Wajib |
| Rumah Sakit | Semua | Wajib |
| Mall/Office Building | > 10.000 m² | Wajib |
| Perumahan | > 500 unit | Wajib |

### Frekuensi Pelaporan

| Dokumen | Frekuensi | Deadline |
|---------|-----------|----------|
| Laporan Bulanan | Bulanan | Tanggal 10 bulan berikutnya |
| Laporan Triwulan | 3 bulan | 30 hari setelah akhir triwulan |
| Laporan Semester | 6 bulan | 30 hari setelah akhir semester |
| Laporan Tahunan | Tahunan | 31 Januari tahun berikutnya |

---

# 2. PARAMETER WAJIB MONITOR

## Parameter Standar Kualitas Air Limbah

### Parameter Fisika

| Parameter | Simbol | Satuan | Metode Pengukuran |
|-----------|:------:|:------:|-------------------|
| Suhu | T | °C | Thermometer/Sensor |
| Total Suspended Solids | TSS | mg/L | Gravimetri/Sensor |
| Total Dissolved Solids | TDS | mg/L | Evaporasi/Sensor |
| Warna | - | Pt-Co | Spektrofotometer |
| Bau | - | - | Organoleptik |

### Parameter Kimia

| Parameter | Simbol | Satuan | Metode Pengukuran |
|-----------|:------:|:------:|-------------------|
| pH | pH | - | pH Meter/Sensor |
| Chemical Oxygen Demand | COD | mg/L | Titrimetri/Sensor |
| Biochemical Oxygen Demand | BOD | mg/L | Winkler 5 hari |
| Amonia | NH₃-N | mg/L | Nessler/Sensor |
| Minyak & Lemak | O&G | mg/L | Gravimetri |
| Total Nitrogen | TN | mg/L | Kjeldahl |
| Total Phosphorus | TP | mg/L | Spektrofotometer |
| Sulfida | H₂S | mg/L | Iodometri |
| Fenol | - | mg/L | Spektrofotometer |
| Klorin Bebas | Cl₂ | mg/L | DPD |

### Parameter Biologi

| Parameter | Simbol | Satuan | Metode Pengukuran |
|-----------|:------:|:------:|-------------------|
| Total Coliform | TC | MPN/100mL | Tabung Ganda |
| Fecal Coliform | FC | MPN/100mL | Tabung Ganda |
| E. coli | - | MPN/100mL | Tabung Ganda |

---

## Parameter yang Dapat Dimonitor Online

SURGE Water Analytics mendukung monitoring online untuk:

| Parameter | Online Sensor | Akurasi | Notes |
|-----------|:-------------:|:-------:|-------|
| **pH** | ✅ | ±0.1 | Real-time, most common |
| **COD** | ✅ | ±5% | UV-Vis spectroscopy |
| **TSS** | ✅ | ±5% | Turbidity conversion |
| **NH₃-N** | ✅ | ±5% | Ion-selective electrode |
| **DO** | ✅ | ±0.1 mg/L | Optical sensor |
| **Conductivity** | ✅ | ±1% | For TDS estimation |
| **Flow** | ✅ | ±2% | Ultrasonic/magnetic |
| **Temperature** | ✅ | ±0.5°C | PT100/NTC |
| BOD | ❌ | - | Lab only (5 days) |
| O&G | ❌ | - | Lab only |
| Coliform | ❌ | - | Lab only |

> **Note:** Parameter yang tidak bisa online (BOD, O&G, Coliform) tetap perlu sampling manual untuk lab analysis. SURGE bisa diinput secara manual untuk dokumentasi lengkap.

---

# 3. BAKU MUTU AIR LIMBAH

## Baku Mutu Berdasarkan Jenis Industri

### Industri Tekstil (Lampiran I PP 22/2021)

| Parameter | Satuan | Baku Mutu | Notes |
|-----------|:------:|:---------:|-------|
| pH | - | 6.0 - 9.0 | Range |
| TSS | mg/L | 50 | Max |
| COD | mg/L | 150 | Max |
| BOD | mg/L | 60 | Max |
| Fenol | mg/L | 0.5 | Max |
| Krom Total | mg/L | 1.0 | Max |
| Amonia | mg/L | 8 | Max |
| Sulfida | mg/L | 0.3 | Max |

### Industri Pengolahan Ikan (Lampiran VIII)

| Parameter | Satuan | Baku Mutu |
|-----------|:------:|:---------:|
| pH | - | 6.0 - 9.0 |
| TSS | mg/L | 100 |
| COD | mg/L | 150 |
| BOD | mg/L | 75 |
| NH₃-N | mg/L | 10 |
| O&G | mg/L | 15 |

### Air Limbah Domestik (Permen LHK 68/2016)

| Parameter | Satuan | Baku Mutu |
|-----------|:------:|:---------:|
| pH | - | 6.0 - 9.0 |
| TSS | mg/L | 30 |
| COD | mg/L | 100 |
| BOD | mg/L | 30 |
| O&G | mg/L | 5 |
| Amonia | mg/L | 10 |
| Total Coliform | MPN/100mL | 3000 |

### Kawasan Industri (Lampiran LIV)

| Parameter | Satuan | Baku Mutu |
|-----------|:------:|:---------:|
| pH | - | 6.0 - 9.0 |
| TSS | mg/L | 150 |
| COD | mg/L | 300 |
| BOD | mg/L | 100 |
| NH₃-N | mg/L | 10 |
| Fenol | mg/L | 0.5 |

---

## PROPER Rating Criteria

| Warna | Rating | Kriteria |
|-------|:------:|----------|
| 🥇 **Emas** | Excellent | Beyond compliance + CSR |
| 🟢 **Hijau** | Good | Beyond compliance |
| 🔵 **Biru** | Compliant | Meet requirements |
| 🔴 **Merah** | Non-compliant | Violation |
| ⚫ **Hitam** | Critical | Severe violation |

---

# 4. KONFIGURASI SURGE UNTUK COMPLIANCE

## 4.1 Setup Parameter Sesuai Baku Mutu

### Step 1: Buat Location

1. Login ke SURGE Dashboard
2. Navigasi ke **Settings > Locations**
3. Klik **Add Location**
4. Isi detail:
   - Location Name: "Outlet IPAL"
   - Type: Water Treatment
   - Coordinates: [sesuai GPS site]

### Step 2: Tambah Parameters

1. Navigasi ke **Settings > Parameters**
2. Klik **Add Parameter** untuk setiap parameter
3. Konfigurasi sesuai tabel berikut:

**Contoh Konfigurasi untuk Industri Tekstil:**

| Parameter | Unit | Min | Max | Threshold Low | Threshold High | Alarm |
|-----------|:----:|:---:|:---:|:-------------:|:--------------:|:-----:|
| pH | - | 0 | 14 | 6.0 | 9.0 | ✅ |
| COD | mg/L | 0 | 500 | - | 150 | ✅ |
| TSS | mg/L | 0 | 200 | - | 50 | ✅ |
| NH3-N | mg/L | 0 | 50 | - | 8 | ✅ |
| Flow | m³/h | 0 | 100 | - | - | ❌ |

### Step 3: Configure Alerts

1. Navigasi ke **Settings > Alerts**
2. Create rule untuk setiap threshold violation
3. Set notification recipients
4. Enable email alerts

**Alert Configuration Example:**

```
Rule Name: pH Out of Range
Condition: pH < 6.0 OR pH > 9.0
Severity: Critical
Action: Email to environment@company.com
Message: "ALERT: pH value {value} is out of compliance range (6.0-9.0)"
```

---

## 4.2 Dashboard Compliance View

### Recommended Widgets

| Widget | Purpose | Configuration |
|--------|---------|---------------|
| **Compliance Status** | Overall compliance indicator | Green/Yellow/Red |
| **Parameter Gauge** | Real-time values vs threshold | Show limit lines |
| **Trend Chart** | 24h/7d/30d trend | Highlight violations |
| **Alert Log** | Recent threshold violations | Last 50 alerts |
| **Exceedance Counter** | Count violations per month | Reset monthly |

### Sample Dashboard Layout

```
┌────────────────────────────────────────────────────────────┐
│                    KLHK COMPLIANCE DASHBOARD               │
├────────────────┬───────────────┬───────────────────────────┤
│   COMPLIANCE   │   pH STATUS   │        pH TREND           │
│   ✅ 100%      │    7.2        │   ═══════════════════     │
│   This Month   │   Range: 6-9  │        [Chart]            │
├────────────────┼───────────────┼───────────────────────────┤
│   COD STATUS   │   TSS STATUS  │       COD TREND           │
│    85 mg/L     │   32 mg/L     │   ═══════════════════     │
│   Limit: 150   │  Limit: 50    │        [Chart]            │
├────────────────┴───────────────┴───────────────────────────┤
│                    RECENT ALERTS                           │
│ [12/28 14:30] pH dropped to 5.8 - RESOLVED                 │
│ [12/27 09:15] COD spike to 160 mg/L - RESOLVED             │
└────────────────────────────────────────────────────────────┘
```

---

# 5. PELAPORAN SISPEK

## 5.1 Apa itu SISPEK?

**SISPEK** (Sistem Pelaporan Elektronik Kementerian LHK) adalah platform online KLHK untuk:
- Submit laporan kualitas air limbah
- Submit laporan emisi
- Submit dokumen lingkungan
- Tracking compliance status

**URL:** https://sispek.menlhk.go.id

---

## 5.2 Export Data dari SURGE ke Format SISPEK

### Step-by-Step Export

1. Login ke SURGE Dashboard
2. Navigasi ke **Reports > KLHK Export**
3. Pilih periode pelaporan
4. Pilih location/outlet
5. Pilih parameters
6. Klik **Generate Report**
7. Download file Excel

### Format Output SURGE

SURGE menghasilkan Excel dengan format siap upload ke SISPEK:

| Tanggal | Waktu | pH | COD (mg/L) | TSS (mg/L) | NH3 (mg/L) | Flow (m³/h) |
|---------|-------|:--:|:----------:|:----------:|:----------:|:-----------:|
| 2025-12-01 | 08:00 | 7.2 | 85 | 32 | 4.5 | 25.3 |
| 2025-12-01 | 14:00 | 7.4 | 92 | 35 | 5.1 | 26.1 |
| 2025-12-01 | 20:00 | 7.1 | 78 | 28 | 4.2 | 24.8 |
| ... | ... | ... | ... | ... | ... | ... |

### Summary Statistics (Auto-generated)

| Parameter | Average | Min | Max | Std Dev | Compliance |
|-----------|:-------:|:---:|:---:|:-------:|:----------:|
| pH | 7.23 | 6.8 | 7.8 | 0.21 | 100% |
| COD | 88.5 | 65 | 142 | 15.3 | 100% |
| TSS | 31.2 | 18 | 48 | 6.8 | 100% |

---

## 5.3 Upload ke SISPEK

### Langkah Upload

1. Login ke https://sispek.menlhk.go.id
2. Pilih menu **Pelaporan > Air Limbah**
3. Pilih periode laporan
4. Upload file Excel dari SURGE
5. Review data
6. Submit

### Tips Agar Tidak Ditolak

| Issue | Solution |
|-------|----------|
| Format tanggal salah | Pastikan DD/MM/YYYY |
| Missing data | SURGE auto-fill dengan rata-rata |
| Value out of range | SURGE warning sebelum export |
| Wrong unit | SURGE sudah standard unit |
| File terlalu besar | Pisah per bulan |

---

# 6. AUDIT TRAIL & DOKUMENTASI

## 6.1 Apa yang Di-log SURGE?

| Event | Detail yang Disimpan |
|-------|---------------------|
| Data Reading | Timestamp, value, source device |
| Threshold Violation | Time, parameter, value, limit |
| Alert Sent | Time, recipient, message |
| Config Change | Time, user, before/after value |
| User Login | Time, user, IP address |
| Export | Time, user, date range, parameters |

---

## 6.2 Retention Period

| Plan | Retention | Sufficient For |
|------|:---------:|----------------|
| Trial | 30 hari | Testing |
| Starter | 90 hari | Basic audit |
| Business | 1 tahun | Annual audit ✅ |
| Professional | 3 tahun | Full PROPER cycle ✅ |

> **Recommendation:** Business plan minimum untuk audit compliance.

---

## 6.3 Generating Audit Report

1. Navigasi ke **Reports > Audit Trail**
2. Pilih date range
3. Pilih event types
4. Export to PDF

### Sample Audit Report

```
═══════════════════════════════════════════════════════════════
                    SURGE AUDIT REPORT
═══════════════════════════════════════════════════════════════
Organization: PT ABC Manufacturing
Period: December 2025
Generated: 2025-12-28 15:30:00

COMPLIANCE SUMMARY
──────────────────────────────────────────────────────────────
Total Readings: 8,640
Compliant Readings: 8,592 (99.4%)
Non-compliant Readings: 48 (0.6%)

THRESHOLD VIOLATIONS
──────────────────────────────────────────────────────────────
Date       Time    Parameter  Value   Limit   Duration  Status
2025-12-05 14:32   pH         5.8     6.0     15 min    Resolved
2025-12-12 09:15   COD        162     150     45 min    Resolved
...

ALERT LOG
──────────────────────────────────────────────────────────────
48 alerts generated
48 alerts acknowledged
0 alerts pending

DATA EXPORT LOG
──────────────────────────────────────────────────────────────
2025-12-10 - Monthly report exported by admin@company.com
2025-12-28 - Audit report exported by manager@company.com

═══════════════════════════════════════════════════════════════
```

---

# 7. FAQ COMPLIANCE

## Q: Apakah sensor online bisa menggantikan lab test?

**A:** Tergantung parameter. Untuk pH, COD, TSS - sensor online yang terkalibrasi bisa diterima. Untuk BOD, mikrobiologi - tetap perlu lab test. Rekomendasikan:
- Online monitoring untuk daily compliance
- Lab test bulanan untuk validasi dan parameter non-online

---

## Q: Bagaimana jika sensor error dan tidak ada data?

**A:** SURGE memiliki:
- **Alert offline** - notifikasi jika device tidak mengirim data
- **Gap filling** - opsi interpolasi untuk gap kecil (<2 jam)
- **Manual entry** - input data backup dari alat portable

Untuk KLHK, dokumentasikan alasan data gap dengan surat keterangan.

---

## Q: Apakah data SURGE bisa dijadikan bukti legal?

**A:** Data SURGE memiliki:
- Timestamp dengan RTC battery backup (akurat)
- Audit trail lengkap
- Export dengan hash integrity

Untuk bukti legal, rekomendasikan:
- Kalibrasi sensor terjadwal (sertifikat kalibrasi)
- Backup dengan lab test berkala
- SOP pengoperasian terdokumentasi

---

## Q: Berapa frekuensi data yang diminta KLHK?

**A:** Minimum requirement:
- Data harian: rata-rata atau representatif
- Data bulanan: untuk laporan rutin
- Data insiden: jika ada pelanggaran

SURGE bisa set interval dari 1 menit sampai 1 jam sesuai kebutuhan.

---

## Q: Bagaimana handling jika nilai melebihi baku mutu?

**A:** Workflow recommended:

1. **Immediate:** Alert ke operator
2. **15 menit:** Eskalasi ke supervisor
3. **1 jam:** Dokumentasi di logbook SURGE
4. **24 jam:** Root cause analysis
5. **Report:** Include incident + corrective action di laporan bulanan

---

## Q: Apa yang terjadi jika telat lapor ke SISPEK?

**A:** Sanksi bervariasi:
- Keterlambatan ringan (<7 hari): Warning
- Keterlambatan berat (>7 hari): Potensi denda
- Tidak lapor berulang: PROPER downgrade, potensi pencabutan izin

SURGE membantu dengan:
- Reminder H-5 sebelum deadline
- Auto-generate report
- Quick export format

---

# APPENDIX: CHECKLIST COMPLIANCE

## Monthly Checklist

| Task | Due | Status |
|------|-----|:------:|
| Verify all sensors online | Daily | [ ] |
| Check threshold violations | Daily | [ ] |
| Review alert log | Weekly | [ ] |
| Calibrate pH sensor | Monthly | [ ] |
| Export monthly data | Tanggal 5 | [ ] |
| Submit to SISPEK | Tanggal 10 | [ ] |
| Review SURGE dashboard | Weekly | [ ] |
| Backup data export | Monthly | [ ] |

## Annual Checklist

| Task | Due | Status |
|------|-----|:------:|
| Full sensor calibration | Q1 | [ ] |
| Audit trail review | Q2 | [ ] |
| Lab validation sampling | Quarterly | [ ] |
| PROPER documentation | Q4 | [ ] |
| Annual report submission | January 31 | [ ] |
| Sensor replacement evaluation | Q4 | [ ] |

---

_Document Version: 1.0_
_For Customer and Internal Use_
_Last Updated: December 28, 2025_
