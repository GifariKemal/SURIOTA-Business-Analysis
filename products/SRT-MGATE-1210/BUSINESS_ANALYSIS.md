# Analisis Bisnis SRT-MGATE-1210

# *SRT-MGATE-1210 Business Analysis*

> Gateway Modbus Industri dengan Sistem Varian
>
> *Industrial Modbus Gateway with Variant System*

**Versi:** 7.1 - Sistem Varian Produk (Bilingual)
**Diperbarui:** Januari 2026
**Disusun oleh:** Tim Pengembangan Produk
**Kurs Tukar:** USD 1 = Rp 16.000

---

## Ringkasan Eksekutif / *Executive Summary*

### Ringkasan Produk / *Product Summary*

**SRT-MGATE-1210** adalah Industrial Modbus Gateway produksi PT Surya Inovasi Prioritas (SURIOTA) yang tersedia dalam **8 varian** untuk memenuhi berbagai kebutuhan pasar.

*SRT-MGATE-1210 is an Industrial Modbus Gateway manufactured by PT Surya Inovasi Prioritas (SURIOTA), available in **8 variants** to meet various market needs.*

### Matriks Varian Produk / *Product Variant Matrix*

| Varian | Nama | Harga (Non-POE) | Harga (POE) | Kasus Penggunaan |
|:------:|------|----------------:|------------:|------------------|
| **C** | Converter | Rp 1.900.000 | Rp 2.300.000 | RTU ↔ TCP dasar |
| **D** | Concentrator | Rp 2.500.000 | Rp 2.900.000 | Agregasi multi-perangkat |
| **G** | IoT Gateway | Rp 2.700.000 | Rp 3.100.000 | Konektivitas cloud |
| **X** | All-in-One | Rp 5.000.000 | Rp 5.500.000 | Solusi lengkap |

### Metrik Utama / *Key Metrics*

| Metrik | Nilai |
|--------|-------|
| Target Pasar | Industrial IoT Indonesia |
| Posisi Kompetitif | Mid-range dengan fitur premium |
| Rentang Harga | Rp 1,9M - 5,5M |
| Gross Margin | 14% - 67% |
| Break-even | 82 unit |

### Keunggulan Kompetitif / *Competitive Advantages*

- **SATU-SATUNYA** gateway dengan **WiFi + BLE + Industrial Grade** di Indonesia
- **Produksi Lokal** dengan dukungan Bahasa Indonesia
- **20-47% lebih murah** dari kompetitor dengan fitur setara

---

## Daftar Isi / *Table of Contents*

1. [Varian Produk](#varian-produk)
2. [Spesifikasi Teknis](#spesifikasi-teknis)
3. [Analisis Biaya (COGS)](#analisis-biaya-cogs)
4. [Strategi Harga](#strategi-harga)
5. [Analisis Kompetitor](#analisis-kompetitor)
6. [Perbandingan Fitur](#perbandingan-fitur)
7. [Proposisi Nilai Unik](#proposisi-nilai-unik)
8. [Strategi Distribusi](#strategi-distribusi)
9. [Panduan Penjualan](#panduan-penjualan)
10. [Proyeksi Keuangan](#proyeksi-keuangan)

---

## Varian Produk

## *Product Variants*

### Gambaran Varian / *Variant Overview*

SRT-MGATE-1210 tersedia dalam 4 tipe fungsi dan 2 opsi daya:

*SRT-MGATE-1210 is available in 4 function types and 2 power options:*

#### Tipe Fungsi / *Function Types*

| Kode | Nama | Deskripsi |
|:----:|------|-----------|
| **C** | Converter | Konversi bidireksional Modbus RTU ↔ TCP |
| **D** | Concentrator | Agregasi multi-perangkat dengan re-mapping register |
| **G** | IoT Gateway | Konektivitas cloud MQTT/HTTP |
| **X** | All-in-One | Semua fitur dalam satu perangkat |

#### Opsi Daya / *Power Options*

| Tipe | Sufiks | Tegangan Input | Fitur |
|------|:------:|----------------|-------|
| Non-POE | (kosong) | 12-48V DC | Daya DC standar |
| POE | (P) | 12-48V DC + 36-57V POE | Daya ganda auto-failover |

### Daftar SKU Lengkap / *Complete SKU List*

| SKU | Deskripsi | Harga (IDR) | Harga (USD) |
|-----|-----------|------------:|------------:|
| SRT-MGATE-1210C | Converter, Non-POE | Rp 1.900.000 | $119 |
| SRT-MGATE-1210C(P) | Converter, POE | Rp 2.300.000 | $144 |
| SRT-MGATE-1210D | Concentrator, Non-POE | Rp 2.500.000 | $156 |
| SRT-MGATE-1210D(P) | Concentrator, POE | Rp 2.900.000 | $181 |
| SRT-MGATE-1210G | IoT Gateway, Non-POE | Rp 2.700.000 | $169 |
| SRT-MGATE-1210G(P) | IoT Gateway, POE | Rp 3.100.000 | $194 |
| SRT-MGATE-1210X | All-in-One, Non-POE | Rp 5.000.000 | $313 |
| SRT-MGATE-1210X(P) | All-in-One, POE | Rp 5.500.000 | $344 |

### Konvensi Penamaan / *Naming Convention*

#### Format Nama Produk / *Product Name Format*

```
SRT-MGATE-1210[FUNGSI][(P)]
```

- `SRT` - Kode merek (Suriota)
- `MGATE` - Tipe produk (Modbus Gateway)
- `1210` - Nomor model
- `[FUNGSI]` - C, D, G, atau X
- `[(P)]` - Varian POE

#### Format Nama Perangkat BLE / *BLE Device Name Format*

```
MGate-1210[FUNGSI][(P)]XXXX
```

- `XXXX` - ID Unik (4 karakter hex dari MAC)

**Contoh / *Examples*:**
- `MGate-1210CA3F2` - Converter, Non-POE
- `MGate-1210G(P)B847` - IoT Gateway, POE

#### Format Nomor Seri / *Serial Number Format*

```
SRT-MGATE1210[FUNGSI][P]-YYYYMMDD-XXXXXX
```

**Contoh / *Examples*:**
- `SRT-MGATE1210C-20260115-3AC9A7`
- `SRT-MGATE1210XP-20260115-B827E4`

---

## Spesifikasi Teknis

## *Technical Specifications*

### Spesifikasi Perangkat Keras / *Hardware Specifications*

| Spesifikasi | Nilai |
|-------------|-------|
| MCU | ESP32-S3-WROOM-1 (Dual-core 240MHz, 8MB PSRAM) |
| RS-485 | 2 port dengan proteksi ESD, hingga 32 perangkat/port |
| Ethernet | W5500 10/100 Mbps dengan isolasi magnetik |
| WiFi | 2.4GHz 802.11 b/g/n, WPA3-PSK |
| Bluetooth | BLE 5.0 untuk konfigurasi mobile |
| RTC | DS3231 dengan backup baterai (CR1220) |
| Indikator LED | 9 LED (Status, Config, WiFi, NET, RS485, Power) |
| Daya (Standar) | 12-48V DC |
| Daya (POE) | 12-48V DC + IEEE 802.3af/at (36-57V) |
| Suhu Operasi | -40°C sampai +75°C (Industrial Grade) |
| Pemasangan | DIN Rail / Wall Mount |
| Dimensi | 110 x 90 x 58 mm |
| Sertifikasi | RoHS & CE |
| Garansi | 1,5 Tahun |

### Matriks Fitur per Varian / *Feature Matrix by Variant*

| Fitur | C | D | G | X |
|-------|:-:|:-:|:-:|:-:|
| **PERANGKAT KERAS** |||||
| ESP32-S3 (8MB PSRAM) | ✓ | ✓ | ✓ | ✓ |
| RS-485 ×2 | ✓ | ✓ | ✓ | ✓ |
| Ethernet + WiFi | ✓ | ✓ | ✓ | ✓ |
| BLE 5.0 | ✓ | ✓ | ✓ | ✓ |
| RTC + Baterai | ✓ | ✓ | ✓ | ✓ |
| 9 Indikator LED | ✓ | ✓ | ✓ | ✓ |
| Proteksi ESD | ✓ | ✓ | ✓ | ✓ |
| **MODBUS** |||||
| Modbus RTU/TCP | ✓ | ✓ | ✓ | ✓ |
| Jembatan RTU ↔ TCP | ✓ | ✓ | ✓ | ✓ |
| Re-mapping Register | - | ✓ | - | ✓ |
| Master-Master-Slave | - | ✓ | - | ✓ |
| Tabel Slave Virtual | - | ✓ | - | ✓ |
| **CLOUD/IoT** |||||
| Klien MQTT | - | - | ✓ | ✓ |
| HTTP REST API | - | - | ✓ | ✓ |
| Enkripsi TLS | - | - | ✓ | ✓ |
| AWS/Azure/SURGE | - | - | ✓ | ✓ |
| Store-and-Forward | - | - | ✓ | ✓ |
| **KONEKTIVITAS** |||||
| WiFi Auto-Failover | ✓ | ✓ | ✓ | ✓ |
| Pembaruan OTA | ✓ | ✓ | ✓ | ✓ |
| Konfigurasi Mobile BLE | ✓ | ✓ | ✓ | ✓ |

### Kapasitas Perangkat / *Device Capacity*

| Varian | Slave RS-485/port | Slave TCP | Maks Register |
|:------:|:-----------------:|:---------:|:-------------:|
| C | 32 | 16 | 256 |
| D | 48 | 32 | 512 |
| G | 32 | 16 | 256 |
| X | 64 | 64 | 1024 |

---

## Analisis Biaya (COGS)

## *Cost Analysis (COGS)*

### Bill of Materials

| Komponen | Biaya/Unit | Catatan |
|----------|----------:|--------|
| PCBA (Elektronik) | Rp 1.480.128 | Komponen LCSC + perakitan |
| Enclosure 3D Print | Rp 56.250 | Housing PLA+ Industri |
| Desain PCB (diamortisasi) | Rp 89.210 | Per 100 unit |
| Desain Enclosure (diamortisasi) | Rp 4.294 | Per 100 unit |
| **Sub-total Hardware** | **Rp 1.629.882** | |

### Biaya Tambahan POE / *POE Additional Cost*

| Item | Biaya |
|------|------:|
| Modul POE + Komponen | +Rp 200.000 |

### Ringkasan COGS / *COGS Summary*

| Model | COGS Hardware | Amortisasi R&D | Biaya Terbeban Penuh |
|-------|-------------:|----------------:|-----------------:|
| Non-POE | Rp 1.430.000 | Rp 200.000 | **Rp 1.630.000** |
| POE | Rp 1.630.000 | Rp 200.000 | **Rp 1.830.000** |

### Investasi R&D / *R&D Investment*

| Proyek | LOC | Estimasi Nilai |
|--------|----:|---------------:|
| Firmware (ESP32-S3) | 25.959 | Rp 180.000.000 |
| Aplikasi Mobile (Flutter) | 20.889 | Rp 90.000.000 |
| **Total** | **46.848** | **Rp 270.000.000** |

> **Catatan:** Aplikasi Mobile tidak dibebankan ke pelanggan (nilai tambah USP).
>
> ***Note:** Mobile App is not charged to customers (value-add USP).*

---

## Strategi Harga

## *Pricing Strategy*

### Harga Retail / *Retail Pricing*

| Varian | Non-POE | POE | Gross Margin |
|:------:|--------:|----:|:------------:|
| **C** | Rp 1.900.000 | Rp 2.300.000 | 14-21% |
| **D** | Rp 2.500.000 | Rp 2.900.000 | 35-37% |
| **G** | Rp 2.700.000 | Rp 3.100.000 | 40-41% |
| **X** | Rp 5.000.000 | Rp 5.500.000 | 67% |

### Rasionalisasi Harga / *Pricing Rationale*

| Varian | Strategi | Referensi Kompetitor |
|--------|----------|---------------------|
| **C** | Entry-level | 28% lebih murah dari Moxa MB3180 (Rp 2,6M) |
| **D** | Mid-range | 29% lebih murah dari ICP DAS tGW-725 (Rp 3,5M) |
| **G** | BASELINE | 20% lebih murah dari BLIIoT BL101L (Rp 3,3M) |
| **X** | Premium | 47% lebih murah dari Moxa AIG-101 (Rp 9,3M) |

### Diskon Volume - Pelanggan Akhir / *Volume Discount - End Customer*

| Kuantitas | Diskon |
|----------:|:------:|
| 1-4 pcs | 0% |
| 5-9 pcs | 5% |
| 10-24 pcs | 10% |
| 25-49 pcs | 15% |
| 50-99 pcs | 18% |
| 100+ pcs | 20% |

### Harga Distributor / *Distributor Pricing*

| Tier | Diskon | Min Order |
|------|:------:|----------:|
| Bronze | 25% | 25 pcs |
| Silver | 30% | 50 pcs |
| Gold | 35% | 100 pcs |

### MAP (Minimum Advertised Price)

> **WAJIB DIPATUHI SEMUA DISTRIBUTOR**
>
> ***MUST BE FOLLOWED BY ALL DISTRIBUTORS***

| Varian | Non-POE | POE |
|--------|--------:|----:|
| C | Rp 1.900.000 | Rp 2.300.000 |
| D | Rp 2.500.000 | Rp 2.900.000 |
| G | Rp 2.700.000 | Rp 3.100.000 |
| X | Rp 5.000.000 | Rp 5.500.000 |

---

## Analisis Kompetitor

## *Competitor Analysis*

### Harga Kompetitor Terverifikasi (Januari 2026)

### *Verified Competitor Pricing (January 2026)*

#### Converter Modbus Industri / *Industrial Modbus Converters*

| Pabrikan | Model | Harga (IDR) | Fitur | Sumber |
|----------|-------|------------:|-------|--------|
| Moxa | MGate MB3180 | Rp 2.657.658 | 1x RS-485, Ethernet | [moxa-alvasta.co.id](https://moxa-alvasta.co.id/product/mgate-mb3180/) |
| Moxa | MGate MB3170 | Rp 4.474.000 | + Web Management | [moxa-alvasta.co.id](https://moxa-alvasta.co.id/) |
| Moxa | MGate MB3280 | Rp 6.138.000 | 2x RS-485 | [moxa-alvasta.co.id](https://moxa-alvasta.co.id/product/mgate-mb3280/) |
| Moxa | MGate MB3480 | Rp 8.876.000 | 4x RS-485 | [moxa-alvasta.co.id](https://moxa-alvasta.co.id/product/mgate-mb3480/) |
| ICP DAS | tGW-725 | Rp 3.530.000 | 2x RS-485, POE | [Lazada](https://www.lazada.co.id/) |

#### IoT Gateway (Modbus ke MQTT) / *IoT Gateways (Modbus to MQTT)*

| Pabrikan | Model | Harga (IDR) | Fitur | Sumber |
|----------|-------|------------:|-------|--------|
| BLIIoT | BL101L | Rp 3.373.000 | 1x RS-485, 4G, MQTT | [microthings.id](https://www.microthings.id/product/modbus-to-mqtt-gateway/) |
| BLIIoT | BL102 | Rp 4.012.000 | + Dukungan PLC | [microthings.id](https://www.microthings.id/product/plc-industrial-iot-gateway-bl102/) |
| BLIIoT | BL110 | Rp 4.984.000 | Multi-protokol, OPC UA | [microthings.id](https://www.microthings.id/product/industrial-iot-gateway-bl110/) |
| Moxa | AIG-101 | Rp 9.340.000 | LTE, MQTT, Edge | [MoxaStore](https://moxastore.express-inc.com/) |
| USR-IOT | M100 | Rp 3.200.000 | Remote I/O, Modbus | [Tokopedia](https://www.tokopedia.com/) |

### Posisi Kompetitif / *Competitive Positioning*

```
                    HARGA (IDR) / PRICE (IDR)
                ↑
   Rp 10.000.000│                          ★ Moxa AIG-101
                │
    Rp 8.000.000│                    ★ Moxa MB3480
                │
    Rp 6.000.000│               ★ Moxa MB3280
                │          ★ BLIIoT BL110
    Rp 5.000.000│  ┌────────────────────────────────┐
                │  │ ★ SURIOTA X (Rp 5,0M)         │
                │  │        ★ Moxa MB3170  ★ BL102 │
    Rp 4.000.000│  │            ★ ICP DAS tGW-725  │
                │  │    ★ BLIIoT BL101L  ★ USR-M100│
    Rp 3.000.000│  │ ★ SURIOTA G (Rp 2,7M)        │
                │  │ ★ SURIOTA D (Rp 2,5M) ★ MB3180│
    Rp 2.000.000│  │ ★ SURIOTA C (Rp 1,9M)        │
                │  └────────────────────────────────┘
    Rp 1.000.000│  ★ Entry-level (Elfin, Waveshare)
                │
                └───────────────────────────────────►
                    DASAR        FITUR       LANJUTAN
                    BASIC       FEATURES     ADVANCED
```

### SURIOTA vs Kompetitor / *SURIOTA vs Competitors*

| Fitur | SURIOTA | Moxa MB3180 | BLIIoT BL101L | Moxa AIG-101 |
|-------|:-------:|:-----------:|:-------------:|:------------:|
| **Harga** | Rp 1,9-5,0M | Rp 2,6M | Rp 3,3M | Rp 9,3M |
| Port RS-485 | 2 | 1 | 1 | 2 |
| Ethernet | ✓ | ✓ | - | ✓ |
| WiFi | ✓ | - | - | - |
| 4G/LTE | - | - | ✓ | ✓ |
| Konfigurasi BLE | ✓ | - | - | - |
| Baterai RTC | ✓ | - | - | ✓ |
| MQTT | G/X | - | ✓ | ✓ |
| WiFi Failover | ✓ | - | - | - |
| Dukungan Lokal | ✓ | Distributor | Distributor | Distributor |

---

## Perbandingan Fitur

## *Feature Comparison*

### Matriks Fitur Lengkap / *Complete Feature Matrix*

| Fitur | USR-N540 | USR-N720 | BLIIoT BL100 | ICP DAS | Moxa AIG-101 | **SURIOTA** |
|-------|:--------:|:--------:|:------------:|:-------:|:------------:|:-----------:|
| **Harga** | Rp 1,82M | Rp 3,5M | Rp 3,37M | Rp 3,45M | Rp 8,96M | **Rp 1,9-5M** |
| **Tipe** | MQTT GW | MQTT GW | MQTT GW | TCP/RTU | MQTT GW | **MQTT GW** |
| Port RS-485 | 4 | 2 | 1 | 2 | 2 | **2** |
| Proteksi ESD | Tidak | Ya | Tidak | Tidak | Ya | **Ya** |
| RTC + Baterai | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya** ✓ |
| Indikator LED | Dasar | Dasar | Dasar | Dasar | Dasar | **9 LED** ✓ |
| Ethernet | Ya | Ya | Ganda | Ya | Ganda | **Ya** |
| WiFi | **Tidak** | **Tidak** | Opsional | **Tidak** | **Tidak** | **Ya** ✓ |
| Konfigurasi BLE | **Tidak** | **Tidak** | **Tidak** | **Tidak** | **Tidak** | **Ya** ✓ |
| MQTT Native | Ya | Ya | Ya | **Tidak** | Ya | **Ya** |
| Suhu Industri | Ya | Ya | Ya | Ya | Ya | **Ya** |
| Opsi POE | Tidak | Tidak | Tidak | Ya | Tidak | **Ya** |
| Auto Failover | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya** ✓ |
| Dukungan Lokal | Tidak | Tidak | Tidak | Tidak | Tidak | **Ya** ✓ |

---

## Proposisi Nilai Unik

## *Unique Selling Proposition*

### Tagline

> **"Satu-satunya Modbus-to-MQTT Gateway dengan WiFi + BLE di Indonesia"**
>
> ***"The only Modbus-to-MQTT Gateway with WiFi + BLE in Indonesia"***

> **"Setup 5 Menit via Smartphone, Langsung Connect ke Cloud"**
>
> ***"5-Minute Setup via Smartphone, Instant Cloud Connection"***

### 5 USP Utama / *5 Main USPs*

#### 1. Konfigurasi Mobile BLE (EKSKLUSIF) / *BLE Mobile Configuration (EXCLUSIVE)*

| Fitur | Manfaat |
|-------|---------|
| Setup via smartphone | Tidak perlu laptop ke lapangan |
| Konfigurasi 5 menit | Hemat waktu instalasi |
| App Android/iOS | Interface ramah pengguna |

> **Talking Point:** "Semua kompetitor harus bawa laptop untuk config. SURIOTA cukup pakai HP - 5 menit selesai!"
>
> ***"All competitors need a laptop for config. SURIOTA only needs a phone - done in 5 minutes!"***

#### 2. WiFi dengan Auto Failover (EKSKLUSIF) / *WiFi with Auto Failover (EXCLUSIVE)*

| Koneksi | Peran |
|---------|-------|
| Ethernet | Primer - koneksi utama |
| WiFi | Backup - auto-switch jika ETH down |
| BLE | Konfigurasi - setup di lokasi |

> **Talking Point:** "Kalau kabel putus, data tetap jalan via WiFi!"
>
> ***"If the cable breaks, data keeps flowing via WiFi!"***

#### 3. MQTT Native ke Semua Platform Cloud / *MQTT Native to All Cloud Platforms*

| Platform | Dukungan |
|----------|----------|
| AWS IoT Core | Koneksi langsung |
| Azure IoT Hub | Koneksi langsung |
| Platform SURGE | Koneksi langsung |
| ThingsBoard | Koneksi langsung |
| Platform Kustom | MQTT Standar |

#### 4. Kualitas Build Industrial Grade / *Industrial Grade Build Quality*

| Spesifikasi | SURIOTA | Kompetitor |
|-------------|---------|------------|
| Suhu | -40°C sampai +75°C | Bervariasi |
| Proteksi RS-485 | Dilindungi ESD | Sering tidak ada |
| RTC + Baterai | DS3231 + CR1220 | Biasanya tidak ada |
| Indikator LED | 9 LED | Dasar |

#### 5. Dukungan Lokal Indonesia / *Local Indonesia Support*

| Layanan | Detail |
|---------|--------|
| Dukungan Teknis | Bahasa Indonesia |
| Waktu Respons | < 24 jam |
| Garansi | 1,5 tahun |
| Pelatihan | Tersedia atas permintaan |

---

## Strategi Distribusi

## *Distribution Strategy*

### Model Distribusi / *Distribution Model*

| Channel | Campuran | Target Unit | Margin |
|---------|:--------:|:-----------:|:------:|
| Penjualan Langsung | 30% | 24 unit | 36% |
| Via Distributor | 50% | 40 unit | 13% |
| Proyek/Tender | 20% | 16 unit | 26% |
| **Total** | **100%** | **80 unit** | **24%** |

### Biaya Siap Distribusi / *Distribution-Ready Cost*

| Komponen | Non-POE | POE |
|----------|--------:|----:|
| COGS Hardware | Rp 1.430.000 | Rp 1.630.000 |
| Amortisasi R&D | Rp 200.000 | Rp 200.000 |
| Packaging | Rp 90.000 | Rp 90.000 |
| Pengiriman | Rp 40.000 | Rp 40.000 |
| Overhead | Rp 20.000 | Rp 20.000 |
| **Total** | **Rp 1.780.000** | **Rp 1.980.000** |

### Harga Tier Distributor (Contoh Varian G) / *Distributor Tier Pricing (G Variant Example)*

| Tier | Min Order | Non-POE | POE | Diskon |
|------|----------:|--------:|----:|:------:|
| Standard | 5 pcs | Rp 2.160.000 | Rp 2.480.000 | 20% |
| Silver | 10 pcs | Rp 2.025.000 | Rp 2.325.000 | 25% |
| Gold | 25 pcs | Rp 1.890.000 | Rp 2.170.000 | 30% |

---

## Panduan Penjualan

## *Sales Guide*

### Kartu Perbandingan Cepat / *Quick Comparison Card*

```
┌────────────────────────────────────────────────────────────────┐
│         SURIOTA vs KOMPETITOR (Modbus Gateway)                 │
│         SURIOTA vs COMPETITORS (Modbus Gateway)                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  vs Moxa MB3180 (Rp 2,6M)     vs BLIIoT BL101L (Rp 3,3M)      │
│  ├─ SURIOTA C: Rp 1,9M (-28%) ├─ SURIOTA G: Rp 2,7M (-20%)    │
│  ├─ Moxa: Tanpa WiFi ❌        ├─ BLIIoT: Tanpa BLE ❌         │
│  └─ SURIOTA: WiFi+BLE ✅       └─ SURIOTA: WiFi+BLE ✅         │
│                                                                │
│  vs ICP DAS tGW-725 (Rp 3,5M)  vs Moxa AIG-101 (Rp 9,3M)      │
│  ├─ SURIOTA D: Rp 2,5M (-29%)  ├─ SURIOTA X: Rp 5M (-47%)     │
│  ├─ ICP: Tanpa MQTT ❌          ├─ Moxa: Tanpa WiFi ❌         │
│  └─ SURIOTA: MQTT+Cloud ✅      └─ SURIOTA: Lengkap ✅         │
│                                                                │
│  KESIMPULAN: SURIOTA = Best Value WiFi+BLE+MQTT+RTC+9LED      │
│  CONCLUSION: SURIOTA = Best Value WiFi+BLE+MQTT+RTC+9LED      │
└────────────────────────────────────────────────────────────────┘
```

### Skrip Penjualan - Skenario Umum / *Sales Script - Common Scenarios*

#### Skenario 1: Pelanggan Mempertimbangkan Moxa / *Customer Considering Moxa*

> "Moxa AIG-101 harganya Rp 9 juta. SURIOTA X dengan fitur lengkap hanya Rp 5 juta - hemat Rp 4 juta per unit. Untuk 10 unit, saving Rp 40 juta!"
>
> *"Moxa AIG-101 costs Rp 9 million. SURIOTA X with full features is only Rp 5 million - save Rp 4 million per unit. For 10 units, that's Rp 40 million in savings!"*

#### Skenario 2: Pelanggan Budget Terbatas / *Budget Customer*

> "Untuk budget terbatas, SURIOTA C hanya Rp 1,9 juta sudah include WiFi + BLE + RTC yang tidak ada di USR-N540 (Rp 1,8M). Selisih Rp 100K tapi dapat fitur premium."
>
> *"For limited budgets, SURIOTA C at only Rp 1.9 million already includes WiFi + BLE + RTC not found in USR-N540 (Rp 1.8M). A Rp 100K difference but you get premium features."*

#### Skenario 3: Pelanggan Butuh Konektivitas Cloud / *Customer Needs Cloud Connectivity*

> "SURIOTA G (Rp 2,7M) langsung connect ke AWS/Azure/SURGE. BLIIoT BL101L (Rp 3,3M) perlu 4G cellular. Kalau ada WiFi, SURIOTA lebih hemat 20%."
>
> *"SURIOTA G (Rp 2.7M) connects directly to AWS/Azure/SURGE. BLIIoT BL101L (Rp 3.3M) requires 4G cellular. If you have WiFi, SURIOTA saves you 20%."*

---

## Proyeksi Keuangan

## *Financial Projections*

### Analisis Break-Even / *Break-Even Analysis*

| Item | Nilai |
|------|------:|
| Biaya Tetap (R&D parsial) | Rp 20.000.000 |
| Rata-rata Contribution Margin | Rp 245.000 |
| **Unit Break-Even** | **82 unit** |

### Proyeksi Tahun 1 (80 unit) / *Year 1 Projection (80 units)*

| Channel | Unit | Pendapatan | Profit |
|---------|-----:|--------:|-------:|
| Penjualan Langsung | 24 | Rp 69M | Rp 25M |
| Distributor | 40 | Rp 86M | Rp 11M |
| Proyek | 16 | Rp 46M | Rp 12M |
| **Total** | **80** | **Rp 201M** | **Rp 48M** |

**Blended Margin:** 24%

### Target Pertumbuhan / *Growth Targets*

| Tahun | Unit | Pendapatan | Catatan |
|-------|-----:|--------:|---------|
| T1 | 80 | Rp 201M | Masuk pasar |
| T2 | 150 | Rp 400M | Ekspansi distribusi |
| T3 | 300 | Rp 800M | Kepemimpinan pasar |

---

## Lampiran / *Appendix*

### Varian Campuran (Pesanan Kustom) / *Mix Variants (Custom Order)*

Varian Mix memungkinkan kombinasi fitur untuk kebutuhan spesifik:

*Mix Variants allow combining features for specific needs:*

| Mix | Kombinasi | Harga (Non-POE) |
|:---:|-----------|----------------:|
| CD | Converter + Concentrator | Rp 2.900.000 |
| CG | Converter + IoT Gateway | Rp 3.200.000 |
| DG | Concentrator + IoT Gateway | Rp 3.800.000 |

**Persyaratan / *Requirements*:**
- Minimum order: 10 unit
- Lead time: 2-3 minggu

### Sumber Data / *Data Sources*

| Sumber | Produk | URL |
|--------|--------|-----|
| Moxa Alvasta | MB3180, MB3280, MB3480 | moxa-alvasta.co.id |
| Microthings.id | BL101L, BL102, BL110 | microthings.id |
| Lazada Indonesia | ICP DAS tGW-725 | lazada.co.id |
| MoxaStore | AIG-101 | moxastore.express-inc.com |
| Tokopedia | USR-M100, USR-DR302 | tokopedia.com |

---

*Dokumen dipelihara oleh SURIOTA Product Management*
*Document maintained by SURIOTA Product Management*

*Terakhir Diperbarui: Januari 2026*
*Last Updated: January 2026*
