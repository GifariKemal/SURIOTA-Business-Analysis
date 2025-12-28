# SRT-MGATE-1210 - Case Study Template

## Template untuk Dokumentasi Customer Success Stories

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# CARA MENGGUNAKAN TEMPLATE INI

1. **Setelah deployment sukses** (minimal 1 bulan running), minta izin dokumentasi
2. **Interview customer** menggunakan pertanyaan di bawah
3. **Isi template** dengan data aktual
4. **Review dengan customer** sebelum publish
5. **Gunakan untuk** sales collateral, website, proposal

---

# TEMPLATE CASE STUDY

## [JUDUL: Industri/Aplikasi + Hasil Utama]

*Contoh: "Pabrik Tekstil Mendigitalisasi 20 Sensor dengan SRT-MGATE-1210"*

---

### Project Overview

| Aspek | Detail |
|-------|--------|
| **Customer** | [Nama Perusahaan] |
| **Industri** | [Manufaktur/IPAL/Building/dll] |
| **Lokasi** | [Kota, Provinsi] |
| **Aplikasi** | [Monitoring kualitas air/energi/mesin/dll] |
| **Unit Deployed** | [X] unit SRT-MGATE-1210 |
| **Sensors Connected** | [X] Modbus devices |
| **Cloud Platform** | [SURGE/AWS/Datacake/dll] |
| **Go-live Date** | [Bulan, Tahun] |

---

### The Challenge (Sebelum SRT-MGATE-1210)

*[Deskripsikan situasi sebelumnya - 2-3 paragraf]*

**Pertanyaan interview:**
- Bagaimana monitoring dilakukan sebelumnya?
- Apa tantangan dengan setup lama?
- Kenapa perlu upgrade ke IoT/cloud?

**Contoh narasi:**

> PT XYZ adalah pabrik tekstil dengan 20 sensor Modbus untuk monitoring kualitas air limbah. Sebelum implementasi:
>
> - Data hanya bisa dilihat dari SCADA lokal di control room
> - Teknisi harus ke site untuk troubleshooting
> - Tidak ada alert otomatis jika ada parameter abnormal
> - Reporting manual memakan waktu 2 hari per minggu

---

### The Solution (Implementasi SRT-MGATE-1210)

*[Deskripsikan deployment - apa yang dipasang, bagaimana konfigurasi]*

**Contoh:**

| Komponen | Detail |
|----------|--------|
| **Gateway** | 2x SRT-MGATE-1210 |
| **Sensors** | 10 sensor pH, 5 flow meter, 5 level sensor |
| **Connection** | Ethernet primary, WiFi backup |
| **Cloud** | SURGE Water Analytics |
| **Config Time** | 2 jam per gateway (via mobile app) |

> Implementasi dilakukan dalam 1 hari kerja:
> - Pagi: Instalasi dan wiring gateway
> - Siang: Konfigurasi via SURIOTA Mobile App
> - Sore: Testing dan handover

---

### The Results (Hasil yang Dicapai)

*[Kuantifikasi hasil dengan angka]*

#### Key Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Time to access data** | 30 min (ke control room) | 0 min (mobile) | **Real-time** |
| **Troubleshooting response** | 4 jam | 15 menit | **-94%** |
| **Manual reporting time** | 16 jam/bulan | 1 jam/bulan | **-94%** |
| **Missed alerts** | 5-10/bulan | 0 | **100% captured** |

#### Highlighted Results

> **Real-time Visibility**
> "Sekarang saya bisa cek status IPAL dari HP, tidak perlu ke pabrik."

> **Faster Response**
> "Alert langsung masuk, tim bisa respond dalam menit bukan jam."

> **Cost Savings**
> "Tidak perlu upgrade SCADA, gateway ini cukup untuk cloud monitoring."

---

### Customer Quote (Testimonial)

> "[Quote 2-3 kalimat tentang pengalaman menggunakan SRT-MGATE-1210]"
>
> **— [Nama], [Jabatan], [Perusahaan]**

**Contoh:**

> "Setup-nya surprisingly mudah. Saya expect butuh vendor IT, ternyata tim maintenance kami bisa konfigurasi sendiri pakai HP. Sekarang monitoring jadi real-time dan responsive."
>
> **— Ir. Ahmad Wijaya, Plant Manager, PT XYZ Textile**

---

### Why SRT-MGATE-1210?

*[Alasan customer memilih SRT-MGATE-1210]*

**Contoh:**

> PT XYZ memilih SRT-MGATE-1210 karena:
>
> 1. **Mobile Configuration** - Setup tanpa laptop, langsung di lapangan
> 2. **Dual Connection** - WiFi backup untuk reliability
> 3. **MQTT Native** - Langsung connect ke SURGE tanpa middleware
> 4. **Local Support** - Response cepat dalam Bahasa Indonesia
> 5. **Price** - 30% lebih murah dari alternatif import

---

### Technical Highlights

| Feature Used | Benefit |
|--------------|---------|
| **BLE Config** | Setup 2 gateway dalam 2 jam |
| **WiFi Failover** | Zero downtime saat maintenance Ethernet |
| **MQTT + JSON** | Seamless integration ke SURGE |
| **RTC Backup** | Timestamp akurat meski power flicker |
| **9 LED Status** | Visual troubleshooting tanpa tools |

---

### About [Company Name]

*[Brief company description - 2-3 kalimat]*

> PT XYZ Textile adalah produsen kain tenun dengan kapasitas 100 ton/bulan, berlokasi di Kawasan Industri Jababeka. Perusahaan ini telah beroperasi sejak 1998 dan mengekspor ke 15 negara.

---

# CHECKLIST SEBELUM PUBLISH

| Item | Status |
|------|:------:|
| Customer approval untuk publish | [ ] |
| Data sudah diverifikasi | [ ] |
| Quote sudah diapprove | [ ] |
| Foto/logo sudah diizinkan | [ ] |
| NDA check (tidak ada info confidential) | [ ] |
| Format untuk website/PDF ready | [ ] |

---

# PERTANYAAN INTERVIEW

### Background
1. Ceritakan tentang fasilitas/pabrik Anda
2. Berapa sensor/device yang dimonitor?
3. Bagaimana monitoring dilakukan sebelumnya?

### Pain Points
4. Apa tantangan terbesar dengan sistem lama?
5. Apakah pernah ada insiden karena tidak real-time?
6. Berapa lama waktu response jika ada masalah?

### Evaluation
7. Kenapa memilih SRT-MGATE-1210?
8. Alternatif apa yang dipertimbangkan?
9. Apa yang membuat akhirnya memilih SURIOTA?

### Implementation
10. Berapa lama proses instalasi?
11. Siapa yang melakukan konfigurasi?
12. Apakah ada kesulitan saat setup?

### Results
13. Apa perubahan paling signifikan setelah implementasi?
14. Berapa waktu yang dihemat?
15. Apakah ada cost savings yang bisa dihitung?
16. Fitur apa yang paling sering digunakan?

### Recommendation
17. Apakah akan merekomendasikan ke perusahaan lain?
18. Satu kalimat untuk mendeskripsikan SRT-MGATE-1210?

---

_Template Version: 1.0_
_For Internal Use_
_Last Updated: December 28, 2025_
