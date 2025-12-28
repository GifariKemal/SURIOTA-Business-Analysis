# SRT-MGATE-1210 - Demo Script

## Panduan Demo Produk untuk Sales Team

**Document Version**: 1.0
**Last Updated**: December 28, 2025
**Duration**: 20-30 menit
**Audience**: System Integrator, IT Manager, Maintenance Engineer

---

# PERSIAPAN SEBELUM DEMO

## Checklist Hardware

| Item | Status | Notes |
|------|:------:|-------|
| Gateway SRT-MGATE-1210 | [ ] | Unit demo, charged |
| Power adapter 12V DC | [ ] | Atau power supply |
| Ethernet cable | [ ] | Untuk demo koneksi |
| RS-485 dummy device (optional) | [ ] | Sensor atau simulator |
| Laptop dengan browser | [ ] | Untuk SURGE dashboard |
| Smartphone Android/iOS | [ ] | Untuk demo BLE config |
| SURIOTA Config App installed | [ ] | Versi terbaru |

## Checklist Network

| Item | Status | Notes |
|------|:------:|-------|
| WiFi hotspot ready | [ ] | Dari HP atau portable WiFi |
| SURGE demo account | [ ] | Login ready |
| Internet untuk demo dashboard | [ ] | Minimal 4G |

---

# STRUKTUR DEMO (20 Menit)

```
┌─────────────────────────────────────────────────────────────────────┐
│  0-2 min    │  Opening & Produk Overview                            │
│  2-5 min    │  Pain Point Confirmation                              │
│  5-12 min   │  Live Demo BLE Configuration                          │
│  12-17 min  │  Dashboard & Cloud Demo                               │
│  17-20 min  │  Pricing & Next Steps                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

# SCRIPT DETAIL

## BAGIAN 1: Opening (2 menit)

### Introduksi Produk

> "Selamat [pagi/siang/sore] Pak/Bu. Hari ini saya akan demo **SRT-MGATE-1210** - Gateway Industrial IoT buatan lokal yang mengkonversi Modbus ke MQTT untuk cloud monitoring."

*[Tunjukkan unit gateway fisik]*

> "Ini unit-nya. Ukuran compact, mounting DIN Rail atau wall mount. Yang membuat unik:
> 1. **Konfigurasi via HP** - tidak perlu laptop ke site
> 2. **Dual koneksi** - Ethernet + WiFi backup
> 3. **Produk lokal** - support Bahasa Indonesia, harga kompetitif"

### Quick Specs Highlight

| Fitur | Spec |
|-------|------|
| RS-485 | 2 port, up to 32 device/port |
| Connectivity | Ethernet + WiFi + BLE |
| Protocol | Modbus RTU/TCP → MQTT |
| Power | 12-48V DC (atau PoE) |
| Operating Temp | -40°C to +75°C |

---

## BAGIAN 2: Pain Point Confirmation (3 menit)

### Discovery Questions

> "Sebelum demo lebih lanjut, boleh saya konfirmasi setup yang Bapak/Ibu punya sekarang?"

**Pertanyaan:**

| Pertanyaan | Follow-up |
|------------|-----------|
| "Sensor/device apa yang mau dimonitor?" | Catat brand, protocol |
| "Sekarang datanya diakses bagaimana?" | SCADA lokal? Manual? |
| "Apakah butuh akses remote/cloud?" | Pain point utama |
| "Koneksi di site pakai apa?" | Ethernet/WiFi/4G? |

### Confirm Pain Points

> "Jadi kalau saya rangkum, tantangan utamanya:
> 1. Data dari sensor Modbus belum bisa diakses remote
> 2. Monitoring masih harus ke site / control room
> 3. Butuh solusi yang simple tanpa programming
>
> Betul seperti itu?"

---

## BAGIAN 3: Live Demo BLE Configuration (7 menit)

### Step 1: Power On Gateway (1 menit)

*[Colokkan power adapter]*

> "Saya nyalakan gateway-nya dulu..."

*[Tunjukkan LED indicators]*

> "Lihat LED-nya:
> - **Power** hijau: Power OK
> - **Status** blinking: System running
> - **Config** kuning: Ready for configuration"

### Step 2: Open Mobile App (1 menit)

*[Buka SURIOTA Config App di smartphone]*

> "Sekarang saya buka aplikasi konfigurasi. App ini gratis, tersedia di Play Store dan App Store."

*[Tunjukkan app interface]*

> "Interface-nya simpel. Klik 'Scan' untuk cari gateway via Bluetooth."

### Step 3: Connect via BLE (1 menit)

*[Klik Scan, pilih gateway]*

> "Ini gateway-nya terdeteksi: SRT-MGATE-[serial number]"

*[Connect ke gateway]*

> "Masukkan PIN default: 123456. Ini bisa diganti nanti untuk security."

*[Tunjukkan connected state]*

> "Sekarang sudah terkoneksi via Bluetooth. Semua konfigurasi bisa dilakukan dari HP - tidak perlu laptop."

### Step 4: Configure WiFi (1 menit)

*[Navigasi ke WiFi settings]*

> "Setting koneksi dulu. Di sini saya masukkan WiFi credentials..."

*[Input SSID dan password]*

> "Gateway support WPA3 untuk security yang lebih baik."

### Step 5: Configure MQTT (1.5 menit)

*[Navigasi ke MQTT settings]*

> "Untuk cloud connection, masukkan MQTT broker details..."

| Setting | Value |
|---------|-------|
| Broker | mqtt.suriota.com |
| Port | 8883 (TLS) |
| Username | [dari SURGE] |
| Password | [dari SURGE] |

> "Credentials ini didapat dari SURGE Platform. Kalau pakai AWS IoT atau platform lain, tinggal ganti broker-nya."

### Step 6: Configure Modbus (1.5 menit)

*[Navigasi ke Modbus settings]*

> "Terakhir, mapping Modbus device..."

| Setting | Value |
|---------|-------|
| Port | RS485-1 |
| Baud Rate | 9600 |
| Slave Address | 1 |
| Register | 0x0000 |
| Data Type | Float32 |

> "Tinggal masukkan address dan register sesuai datasheet sensor. Bisa tambah multiple device sampai 32 per port."

### Step 7: Save & Verify (30 detik)

*[Klik Save]*

> "Klik Save... Gateway restart... dan sekarang lihat LED-nya:
> - **WiFi** hijau: Connected
> - **NET** hijau: Cloud connected
> - **RS485** blinking: Data flowing"

---

## BAGIAN 4: Dashboard Demo (5 menit)

### Open SURGE Dashboard

*[Buka laptop, login ke SURGE]*

> "Sekarang kita lihat datanya di cloud..."

*[Navigasi ke device list]*

> "Gateway sudah muncul sebagai online. Klik untuk lihat data..."

### Show Real-time Data

*[Tunjukkan real-time values]*

> "Ini data real-time dari sensor. Update setiap [interval] detik. Kalau pakai sensor pH misalnya, nilai pH langsung terlihat di sini."

### Show Historical Chart

*[Tunjukkan chart]*

> "Untuk historical data, tinggal pilih range waktu. Bisa lihat trend harian, mingguan, bulanan."

### Show Alert Configuration

*[Tunjukkan alert settings]*

> "Yang penting untuk monitoring - alert otomatis. Set threshold, kalau nilai melewati batas langsung dapat notifikasi email."

---

## BAGIAN 5: Pricing & Close (3 menit)

### Present Pricing

> "Untuk pricing SRT-MGATE-1210..."

| Model | Harga | Features |
|-------|-------|----------|
| Standard | **Rp 2.700.000** | 2xRS485, WiFi, BLE, Ethernet |
| PoE | **Rp 3.100.000** | + PoE power support |

> "Dibanding kompetitor:
> - **23% lebih murah** dari USR-N720 (Rp 3.5M) - yang tidak ada WiFi & BLE
> - **70% lebih murah** dari Moxa (Rp 9M) - yang tidak ada BLE config"

### ROI Highlight

> "Untuk ROI, bayangkan:
> - Tidak perlu kirim teknisi ke site untuk konfigurasi - setup via HP
> - Akses data dari mana saja - tidak perlu ke control room
> - Deteksi masalah lebih cepat - alert otomatis"

### Next Steps

**Jika Tertarik:**

> "Untuk next step:
> 1. Saya bisa siapkan unit untuk testing di site Bapak/Ibu
> 2. Trial dengan sensor existing selama 1 bulan
> 3. Evaluasi dan decide
>
> Mau coba kapan?"

**Jika Butuh Waktu:**

> "Saya kirimkan:
> 1. Brosur dan datasheet
> 2. Quotation resmi
> 3. Contact untuk pertanyaan teknis
>
> Kapan bisa follow-up?"

---

# HANDLING PERTANYAAN UMUM

| Pertanyaan | Jawaban |
|------------|---------|
| "Bisa connect ke sensor merk X?" | "Kalau protokolnya Modbus RTU, pasti bisa. Tinggal set address dan register sesuai datasheet." |
| "Kalau WiFi mati?" | "Ada auto-failover ke Ethernet. Kalau dua-duanya mati, data tersimpan di buffer internal." |
| "Support cloud apa saja?" | "Semua yang support MQTT: AWS, Azure, Datacake, Grafana, ThingsBoard, SURGE. Tinggal ganti broker settings." |
| "Garansi berapa lama?" | "1.5 tahun. Support lokal via WhatsApp." |
| "Bisa beli dimana?" | "Langsung dari SURIOTA atau distributor resmi. PO processing 3-5 hari kerja." |

---

# DEMO TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| Gateway tidak terdeteksi BLE | Pastikan Bluetooth HP aktif, jarak < 10m |
| App tidak connect | Coba restart app, pastikan PIN benar |
| WiFi tidak connect | Cek SSID/password, pastikan 2.4GHz (bukan 5GHz) |
| MQTT tidak connect | Cek credentials, pastikan port 8883 tidak diblock |
| LED tidak nyala | Cek power adapter, voltage 12-48V DC |

---

# POST-DEMO ACTIONS

| Action | Timeline |
|--------|----------|
| Kirim thank you email + datasheet | Same day |
| Kirim quotation | Same day |
| Follow-up jika minta sample | 2-3 hari |
| Follow-up jika butuh proposal | 1 minggu |

---

_Document Version: 1.0_
_For Internal Sales Use_
_Last Updated: December 28, 2025_
