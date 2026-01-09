# SRT-MGATE-1210 - Panduan Demo Produk
# *SRT-MGATE-1210 - Product Demo Script*

## Panduan Demo untuk Sales Team
## *Demo Guide for Sales Team*

**Versi Dokumen / *Document Version***: 1.1
**Terakhir Diperbarui / *Last Updated***: 9 Januari 2026 (Kamis) / *January 9, 2026 (Thursday)*
**Durasi / *Duration***: 20-30 menit / *20-30 minutes*
**Audiens / *Audience***: System Integrator, IT Manager, Maintenance Engineer

---

# PERSIAPAN SEBELUM DEMO
# *PRE-DEMO PREPARATION*

## Checklist Hardware
## *Hardware Checklist*

| Item | Status | Catatan / *Notes* |
|------|:------:|-------------------|
| Gateway SRT-MGATE-1210 | [ ] | Unit demo, charged |
| Power adapter 12V DC | [ ] | Atau power supply / *Or power supply* |
| Ethernet cable | [ ] | Untuk demo koneksi / *For connection demo* |
| RS-485 dummy device (optional) | [ ] | Sensor atau simulator / *Sensor or simulator* |
| Laptop dengan browser | [ ] | Untuk SURGE dashboard / *For SURGE dashboard* |
| Smartphone Android/iOS | [ ] | Untuk demo BLE config / *For BLE config demo* |
| SURIOTA Config App installed | [ ] | Versi terbaru / *Latest version* |

## Checklist Network
## *Network Checklist*

| Item | Status | Catatan / *Notes* |
|------|:------:|-------------------|
| WiFi hotspot ready | [ ] | Dari HP atau portable WiFi / *From phone or portable WiFi* |
| SURGE demo account | [ ] | Login ready |
| Internet untuk demo dashboard | [ ] | Minimal 4G / *Minimum 4G* |

---

# STRUKTUR DEMO (20 Menit)
# *DEMO STRUCTURE (20 Minutes)*

```
┌─────────────────────────────────────────────────────────────────────┐
│  0-2 min    │  Opening & Overview Produk / Product Overview         │
│  2-5 min    │  Konfirmasi Pain Point / Pain Point Confirmation      │
│  5-12 min   │  Live Demo Konfigurasi BLE / BLE Configuration Demo   │
│  12-17 min  │  Demo Dashboard & Cloud / Dashboard & Cloud Demo      │
│  17-20 min  │  Harga & Langkah Selanjutnya / Pricing & Next Steps   │
└─────────────────────────────────────────────────────────────────────┘
```

---

# SCRIPT DETAIL
# *DETAILED SCRIPT*

## BAGIAN 1: Pembukaan (2 menit)
## *PART 1: Opening (2 minutes)*

### Introduksi Produk / *Product Introduction*

> "Selamat [pagi/siang/sore] Pak/Bu. Hari ini saya akan demo **SRT-MGATE-1210** - Gateway Industrial IoT buatan lokal yang mengkonversi Modbus ke MQTT untuk cloud monitoring."

*> "Good [morning/afternoon/evening]. Today I will demo the **SRT-MGATE-1210** - a locally-made Industrial IoT Gateway that converts Modbus to MQTT for cloud monitoring."*

*[Tunjukkan unit gateway fisik / Show physical gateway unit]*

> "Ini unit-nya. Ukuran compact, mounting DIN Rail atau wall mount. Yang membuat unik:
> 1. **Konfigurasi via HP** - tidak perlu laptop ke site
> 2. **Dual koneksi** - Ethernet + WiFi backup
> 3. **Produk lokal** - support Bahasa Indonesia, harga kompetitif"

*> "This is the unit. Compact size, DIN Rail or wall mount. What makes it unique:*
*> 1. **Phone configuration** - no laptop needed at site*
*> 2. **Dual connection** - Ethernet + WiFi backup*
*> 3. **Local product** - Indonesian language support, competitive price"*

### Highlight Spesifikasi Cepat / *Quick Specs Highlight*

| Fitur / *Feature* | Spesifikasi / *Spec* |
|-------------------|----------------------|
| RS-485 | 2 port, up to 32 device/port |
| Konektivitas / *Connectivity* | Ethernet + WiFi + BLE |
| Protokol / *Protocol* | Modbus RTU/TCP → MQTT |
| Daya / *Power* | 12-48V DC (atau PoE / *or PoE*) |
| Suhu Operasi / *Operating Temp* | -40°C hingga +75°C / *-40°C to +75°C* |

---

## BAGIAN 2: Konfirmasi Pain Point (3 menit)
## *PART 2: Pain Point Confirmation (3 minutes)*

### Pertanyaan Discovery / *Discovery Questions*

> "Sebelum demo lebih lanjut, boleh saya konfirmasi setup yang Bapak/Ibu punya sekarang?"

*> "Before we continue, may I confirm your current setup?"*

**Pertanyaan / *Questions*:**

| Pertanyaan / *Question* | Follow-up |
|-------------------------|-----------|
| "Sensor/device apa yang mau dimonitor?" / *"What sensors/devices to monitor?"* | Catat brand, protocol / *Note brand, protocol* |
| "Sekarang datanya diakses bagaimana?" / *"How is data accessed now?"* | SCADA lokal? Manual? / *Local SCADA? Manual?* |
| "Apakah butuh akses remote/cloud?" / *"Need remote/cloud access?"* | Pain point utama / *Main pain point* |
| "Koneksi di site pakai apa?" / *"What connection at site?"* | Ethernet/WiFi/4G? |

### Konfirmasi Pain Points / *Confirm Pain Points*

> "Jadi kalau saya rangkum, tantangan utamanya:
> 1. Data dari sensor Modbus belum bisa diakses remote
> 2. Monitoring masih harus ke site / control room
> 3. Butuh solusi yang simple tanpa programming
>
> Betul seperti itu?"

*> "So to summarize, your main challenges are:*
*> 1. Modbus sensor data cannot be accessed remotely*
*> 2. Monitoring still requires site / control room visit*
*> 3. Need a simple solution without programming*
*>*
*> Is that correct?"*

---

## BAGIAN 3: Live Demo Konfigurasi BLE (7 menit)
## *PART 3: BLE Configuration Live Demo (7 minutes)*

### Langkah 1: Nyalakan Gateway (1 menit)
### *Step 1: Power On Gateway (1 minute)*

*[Colokkan power adapter / Plug in power adapter]*

> "Saya nyalakan gateway-nya dulu..."

*> "Let me power on the gateway first..."*

*[Tunjukkan LED indicators / Show LED indicators]*

> "Lihat LED-nya:
> - **Power** hijau: Power OK
> - **Status** blinking: System running
> - **Config** kuning: Ready for configuration"

*> "Look at the LEDs:*
*> - **Power** green: Power OK*
*> - **Status** blinking: System running*
*> - **Config** yellow: Ready for configuration"*

### Langkah 2: Buka Mobile App (1 menit)
### *Step 2: Open Mobile App (1 minute)*

*[Buka SURIOTA Config App di smartphone / Open SURIOTA Config App on smartphone]*

> "Sekarang saya buka aplikasi konfigurasi. App ini gratis, tersedia di Play Store dan App Store."

*> "Now I open the configuration app. This app is free, available on Play Store and App Store."*

*[Tunjukkan app interface / Show app interface]*

> "Interface-nya simpel. Klik 'Scan' untuk cari gateway via Bluetooth."

*> "The interface is simple. Click 'Scan' to find the gateway via Bluetooth."*

### Langkah 3: Connect via BLE (1 menit)
### *Step 3: Connect via BLE (1 minute)*

*[Klik Scan, pilih gateway / Click Scan, select gateway]*

> "Ini gateway-nya terdeteksi: SRT-MGATE-[serial number]"

*> "The gateway is detected: SRT-MGATE-[serial number]"*

*[Connect ke gateway / Connect to gateway]*

> "Masukkan PIN default: 123456. Ini bisa diganti nanti untuk security."

*> "Enter default PIN: 123456. This can be changed later for security."*

*[Tunjukkan connected state / Show connected state]*

> "Sekarang sudah terkoneksi via Bluetooth. Semua konfigurasi bisa dilakukan dari HP - tidak perlu laptop."

*> "Now connected via Bluetooth. All configuration can be done from phone - no laptop needed."*

### Langkah 4: Configure WiFi (1 menit)
### *Step 4: Configure WiFi (1 minute)*

*[Navigasi ke WiFi settings / Navigate to WiFi settings]*

> "Setting koneksi dulu. Di sini saya masukkan WiFi credentials..."

*> "Configure connection first. Here I enter WiFi credentials..."*

*[Input SSID dan password / Input SSID and password]*

> "Gateway support WPA3 untuk security yang lebih baik."

*> "Gateway supports WPA3 for better security."*

### Langkah 5: Configure MQTT (1.5 menit)
### *Step 5: Configure MQTT (1.5 minutes)*

*[Navigasi ke MQTT settings / Navigate to MQTT settings]*

> "Untuk cloud connection, masukkan MQTT broker details..."

*> "For cloud connection, enter MQTT broker details..."*

| Setting | Value |
|---------|-------|
| Broker | mqtt.suriota.com |
| Port | 8883 (TLS) |
| Username | [dari SURGE / *from SURGE*] |
| Password | [dari SURGE / *from SURGE*] |

> "Credentials ini didapat dari SURGE Platform. Kalau pakai AWS IoT atau platform lain, tinggal ganti broker-nya."

*> "These credentials are from SURGE Platform. If using AWS IoT or other platforms, just change the broker."*

### Langkah 6: Configure Modbus (1.5 menit)
### *Step 6: Configure Modbus (1.5 minutes)*

*[Navigasi ke Modbus settings / Navigate to Modbus settings]*

> "Terakhir, mapping Modbus device..."

*> "Lastly, map the Modbus device..."*

| Setting | Value |
|---------|-------|
| Port | RS485-1 |
| Baud Rate | 9600 |
| Slave Address | 1 |
| Register | 0x0000 |
| Data Type | Float32 |

> "Tinggal masukkan address dan register sesuai datasheet sensor. Bisa tambah multiple device sampai 32 per port."

*> "Just enter address and register according to sensor datasheet. Can add multiple devices up to 32 per port."*

### Langkah 7: Simpan & Verifikasi (30 detik)
### *Step 7: Save & Verify (30 seconds)*

*[Klik Save / Click Save]*

> "Klik Save... Gateway restart... dan sekarang lihat LED-nya:
> - **WiFi** hijau: Connected
> - **NET** hijau: Cloud connected
> - **RS485** blinking: Data flowing"

*> "Click Save... Gateway restarts... and now look at the LEDs:*
*> - **WiFi** green: Connected*
*> - **NET** green: Cloud connected*
*> - **RS485** blinking: Data flowing"*

---

## BAGIAN 4: Demo Dashboard (5 menit)
## *PART 4: Dashboard Demo (5 minutes)*

### Buka SURGE Dashboard / *Open SURGE Dashboard*

*[Buka laptop, login ke SURGE / Open laptop, login to SURGE]*

> "Sekarang kita lihat datanya di cloud..."

*> "Now let's see the data in cloud..."*

*[Navigasi ke device list / Navigate to device list]*

> "Gateway sudah muncul sebagai online. Klik untuk lihat data..."

*> "Gateway appears as online. Click to view data..."*

### Tampilkan Data Real-time / *Show Real-time Data*

*[Tunjukkan real-time values / Show real-time values]*

> "Ini data real-time dari sensor. Update setiap [interval] detik. Kalau pakai sensor pH misalnya, nilai pH langsung terlihat di sini."

*> "This is real-time data from sensor. Updates every [interval] seconds. For pH sensor for example, pH value appears here directly."*

### Tampilkan Chart Historis / *Show Historical Chart*

*[Tunjukkan chart / Show chart]*

> "Untuk historical data, tinggal pilih range waktu. Bisa lihat trend harian, mingguan, bulanan."

*> "For historical data, just select time range. Can view daily, weekly, monthly trends."*

### Tampilkan Konfigurasi Alert / *Show Alert Configuration*

*[Tunjukkan alert settings / Show alert settings]*

> "Yang penting untuk monitoring - alert otomatis. Set threshold, kalau nilai melewati batas langsung dapat notifikasi email."

*> "Important for monitoring - automatic alerts. Set threshold, if value exceeds limit you get email notification immediately."*

---

## BAGIAN 5: Harga & Penutupan (3 menit)
## *PART 5: Pricing & Close (3 minutes)*

### Presentasikan Harga / *Present Pricing*

> "Untuk pricing SRT-MGATE-1210..."

*> "For SRT-MGATE-1210 pricing..."*

| Model | Harga / *Price* | Fitur / *Features* |
|-------|-----------------|---------------------|
| Standard | **Rp 2.700.000** | 2xRS485, WiFi, BLE, Ethernet |
| PoE | **Rp 3.100.000** | + PoE power support |

> "Dibanding kompetitor:
> - **23% lebih murah** dari USR-N720 (Rp 3.5M) - yang tidak ada WiFi & BLE
> - **70% lebih murah** dari Moxa (Rp 9M) - yang tidak ada BLE config"

*> "Compared to competitors:*
*> - **23% cheaper** than USR-N720 (Rp 3.5M) - which has no WiFi & BLE*
*> - **70% cheaper** than Moxa (Rp 9M) - which has no BLE config"*

### Highlight ROI / *ROI Highlight*

> "Untuk ROI, bayangkan:
> - Tidak perlu kirim teknisi ke site untuk konfigurasi - setup via HP
> - Akses data dari mana saja - tidak perlu ke control room
> - Deteksi masalah lebih cepat - alert otomatis"

*> "For ROI, imagine:*
*> - No need to send technician to site for configuration - setup via phone*
*> - Access data from anywhere - no need to go to control room*
*> - Faster problem detection - automatic alerts"*

### Langkah Selanjutnya / *Next Steps*

**Jika Tertarik / *If Interested*:**

> "Untuk next step:
> 1. Saya bisa siapkan unit untuk testing di site Bapak/Ibu
> 2. Trial dengan sensor existing selama 1 bulan
> 3. Evaluasi dan decide
>
> Mau coba kapan?"

*> "For next steps:*
*> 1. I can prepare a unit for testing at your site*
*> 2. Trial with existing sensors for 1 month*
*> 3. Evaluate and decide*
*>*
*> When would you like to try?"*

**Jika Butuh Waktu / *If Need Time*:**

> "Saya kirimkan:
> 1. Brosur dan datasheet
> 2. Quotation resmi
> 3. Contact untuk pertanyaan teknis
>
> Kapan bisa follow-up?"

*> "I will send:*
*> 1. Brochure and datasheet*
*> 2. Official quotation*
*> 3. Contact for technical questions*
*>*
*> When can I follow up?"*

---

# HANDLING PERTANYAAN UMUM
# *HANDLING COMMON QUESTIONS*

| Pertanyaan / *Question* | Jawaban / *Answer* |
|-------------------------|---------------------|
| "Bisa connect ke sensor merk X?" / *"Can connect to brand X sensor?"* | "Kalau protokolnya Modbus RTU, pasti bisa. Tinggal set address dan register sesuai datasheet." / *"If protocol is Modbus RTU, definitely yes. Just set address and register per datasheet."* |
| "Kalau WiFi mati?" / *"If WiFi goes down?"* | "Ada auto-failover ke Ethernet. Kalau dua-duanya mati, data tersimpan di buffer internal." / *"Auto-failover to Ethernet. If both down, data stored in internal buffer."* |
| "Support cloud apa saja?" / *"What clouds supported?"* | "Semua yang support MQTT: AWS, Azure, Datacake, Grafana, ThingsBoard, SURGE." / *"All MQTT-compatible: AWS, Azure, Datacake, Grafana, ThingsBoard, SURGE."* |
| "Garansi berapa lama?" / *"How long warranty?"* | "1.5 tahun. Support lokal via WhatsApp." / *"1.5 years. Local support via WhatsApp."* |
| "Bisa beli dimana?" / *"Where to buy?"* | "Langsung dari SURIOTA atau distributor resmi. PO processing 3-5 hari kerja." / *"Direct from SURIOTA or authorized distributors. PO processing 3-5 business days."* |

---

# TROUBLESHOOTING DEMO
# *DEMO TROUBLESHOOTING*

| Masalah / *Issue* | Solusi / *Solution* |
|-------------------|----------------------|
| Gateway tidak terdeteksi BLE / *Gateway not detected via BLE* | Pastikan Bluetooth HP aktif, jarak < 10m / *Ensure phone Bluetooth on, distance < 10m* |
| App tidak connect / *App won't connect* | Coba restart app, pastikan PIN benar / *Try restart app, ensure PIN correct* |
| WiFi tidak connect / *WiFi won't connect* | Cek SSID/password, pastikan 2.4GHz (bukan 5GHz) / *Check SSID/password, ensure 2.4GHz (not 5GHz)* |
| MQTT tidak connect / *MQTT won't connect* | Cek credentials, pastikan port 8883 tidak diblock / *Check credentials, ensure port 8883 not blocked* |
| LED tidak nyala / *LED not lit* | Cek power adapter, voltage 12-48V DC / *Check power adapter, voltage 12-48V DC* |

---

# TINDAKAN SETELAH DEMO
# *POST-DEMO ACTIONS*

| Tindakan / *Action* | Timeline |
|---------------------|----------|
| Kirim email terima kasih + datasheet / *Send thank you email + datasheet* | Hari yang sama / *Same day* |
| Kirim quotation / *Send quotation* | Hari yang sama / *Same day* |
| Follow-up jika minta sample / *Follow-up if sample requested* | 2-3 hari / *2-3 days* |
| Follow-up jika butuh proposal / *Follow-up if proposal needed* | 1 minggu / *1 week* |

---

_Versi Dokumen / Document Version: 1.1_
_Untuk Penggunaan Internal Sales / For Internal Sales Use_
_Terakhir Diperbarui / Last Updated: 9 Januari 2026 (Kamis) / January 9, 2026 (Thursday)_
