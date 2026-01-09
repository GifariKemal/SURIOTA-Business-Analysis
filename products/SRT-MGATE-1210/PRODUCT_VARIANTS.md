# Varian Produk SRT-MGATE-1210

# *SRT-MGATE-1210 Product Variants*

**Versi Dokumen:** 1.1
**Terakhir Diperbarui:** Januari 2026
**Lini Produk:** Industrial Modbus Gateway

---

## Daftar Isi / *Table of Contents*

1. [Ringkasan Eksekutif](#1-ringkasan-eksekutif)
2. [Konvensi Penamaan](#2-konvensi-penamaan)
3. [Gambaran Varian](#3-gambaran-varian)
4. [Matriks Fitur Detail](#4-matriks-fitur-detail)
5. [Strategi Harga](#5-strategi-harga)
6. [Analisis Kompetitor](#6-analisis-kompetitor)
7. [Varian Campuran (Mix)](#7-varian-campuran-mix)
8. [Implementasi Teknis](#8-implementasi-teknis)

---

## 1. Ringkasan Eksekutif

## *1. Executive Summary*

SRT-MGATE-1210 tersedia dalam **8 varian** yang terdiri dari:

*SRT-MGATE-1210 is available in **8 variants** consisting of:*

- **4 Tipe Fungsi / *Function Types*:** C (Converter), D (Concentrator), G (IoT Gateway), X (All-in-One)
- **2 Tipe Daya / *Power Types*:** Non-POE dan POE

Strategi ini memungkinkan pelanggan memilih fitur sesuai kebutuhan dan anggaran, dari converter dasar hingga IoT gateway lengkap.

*This strategy allows customers to choose features according to their needs and budget, from basic converter to full-featured IoT gateway.*

### Referensi Cepat / *Quick Reference*

| Varian | Nama | Kasus Penggunaan | Harga (Non-POE / POE) |
|:------:|------|------------------|----------------------:|
| **C** | Converter | Jembatan Modbus RTU ↔ TCP | Rp 1.900.000 / Rp 2.300.000 |
| **D** | Concentrator | Agregasi Multi-Perangkat | Rp 2.500.000 / Rp 2.900.000 |
| **G** | IoT Gateway | Konektivitas Cloud (MQTT) | Rp 2.700.000 / Rp 3.100.000 |
| **X** | All-in-One | Solusi Lengkap | Rp 5.000.000 / Rp 5.500.000 |

---

## 2. Konvensi Penamaan

## *2. Naming Convention*

### 2.1 Format Nama Produk / *Product Name Format*

```
SRT-MGATE-1210[FUNGSI][(P)]
     │    │     │    │     │
     │    │     │    │     └─ Varian Daya: (P) = POE, kosong = Non-POE
     │    │     │    └─────── Fungsi: C, D, G, atau X
     │    │     └──────────── Nomor Model: 1210
     │    └────────────────── Tipe Produk: MGATE (Modbus Gateway)
     └─────────────────────── Kode Merek: SRT (Suriota)
```

### 2.2 Format Nama Perangkat BLE / *BLE Device Name Format*

```
MGate-1210[FUNGSI][(P)]XXXX
    │    │     │     │    │
    │    │     │     │    └─ ID Unik (4 karakter hex dari MAC)
    │    │     │     └────── Daya: (P) = POE, kosong = Non-POE
    │    │     └──────────── Fungsi: C, D, G, atau X
    │    └────────────────── Nomor Model: 1210
    └─────────────────────── Merek: MGate
```

**Contoh / *Examples*:**
- `MGate-1210CA3F2` - Converter, Non-POE
- `MGate-1210D(P)B847` - Concentrator, POE
- `MGate-1210GA716` - IoT Gateway, Non-POE
- `MGate-1210X(P)C825` - All-in-One, POE

### 2.3 Format Nomor Seri / *Serial Number Format*

```
SRT-MGATE1210[FUNGSI][P]-YYYYMMDD-XXXXXX
    │      │      │      │      │       │
    │      │      │      │      │       └─ ID Unik (6 hex dari MAC)
    │      │      │      │      └───────── Tanggal Produksi
    │      │      │      └──────────────── P = POE, kosong = Non-POE
    │      │      └─────────────────────── Fungsi: C, D, G, atau X
    │      └────────────────────────────── Model (tanpa strip)
    └───────────────────────────────────── Prefiks Merek
```

**Contoh / *Examples*:**
- `SRT-MGATE1210C-20260115-3AC9A7` - Converter, Non-POE
- `SRT-MGATE1210DP-20260115-7D8E2B` - Concentrator, POE
- `SRT-MGATE1210G-20260115-A716F8` - IoT Gateway, Non-POE
- `SRT-MGATE1210XP-20260115-B827E4` - All-in-One, POE

### 2.4 Penamaan Binary Firmware / *Firmware Binary Naming*

```
MGATE-1210_[FUNGSI][P]_v[VERSI].bin

Contoh / Examples:
- MGATE-1210_C_v1.0.6.bin      (Converter, Non-POE)
- MGATE-1210_DP_v1.0.6.bin     (Concentrator, POE)
- MGATE-1210_G_v1.0.6.bin      (IoT Gateway, Non-POE)
- MGATE-1210_XP_v1.0.6.bin     (All-in-One, POE)
```

---

## 3. Gambaran Varian

## *3. Variant Overview*

### 3.1 Varian Fungsi / *Function Variants*

#### **C - Converter (Pengkonversi Data / *Data Converter*)**

**Target:** Kebutuhan konversi protokol dasar
***Target:** Basic protocol conversion needs*

```
┌─────────────────────────────────────────────────────────────┐
│  MGate-1210C - Pengkonversi Protokol Modbus                 │
│  MGate-1210C - Modbus Protocol Converter                    │
│                                                             │
│  Port RS-485 1 ─────┐                                       │
│                     │    ┌──────────────┐                   │
│                     ├───►│  Modbus      │◄──► Ethernet      │
│                     │    │  RTU ↔ TCP   │◄──► WiFi          │
│  Port RS-485 2 ─────┘    │  Bridge      │                   │
│                          └──────────────┘                   │
│                                                             │
│  Konfigurasi: Aplikasi Mobile BLE                           │
└─────────────────────────────────────────────────────────────┘
```

**Fitur Utama / *Key Features*:**
- Konversi bidireksional Modbus RTU ↔ Modbus TCP
- Dual port RS-485 (independen atau gabungan)
- Konektivitas WiFi dengan auto-failover ke Ethernet
- Konfigurasi via aplikasi mobile BLE 5.0
- 9 indikator LED status
- RTC dengan backup baterai

**Kasus Penggunaan / *Use Cases*:**
- Integrasi PLC/sensor lama ke SCADA
- Jembatan serial-to-Ethernet
- Akses Modbus TCP jarak jauh

---

#### **D - Concentrator (Pengumpul Data / *Data Concentrator*)**

**Target:** Agregasi data multi-perangkat dan re-mapping
***Target:** Multi-device data aggregation and re-mapping*

```
┌─────────────────────────────────────────────────────────────┐
│  MGate-1210D - Pengumpul Data Modbus                        │
│  MGate-1210D - Modbus Data Concentrator                     │
│                                                             │
│  Port RS-485 1 ─────┐                                       │
│  (Master/Slave)     │    ┌──────────────┐                   │
│                     ├───►│  Register    │◄──► Ethernet      │
│                     │    │  Re-Mapping  │◄──► WiFi          │
│  Port RS-485 2 ─────┘    │  & Agregasi  │                   │
│  (Master/Slave)          └──────────────┘                   │
│                                 │                           │
│                          ┌──────▼──────┐                    │
│                          │ Tabel Slave │                    │
│                          │ Virtual     │                    │
│                          └─────────────┘                    │
│                                                             │
│  Mode: Master-Master-Slave, Master-Slave-Slave              │
└─────────────────────────────────────────────────────────────┘
```

**Fitur Utama (termasuk semua fitur C, plus):**
***Key Features (includes all C features, plus):***

- Re-mapping register & translasi alamat
- Topologi Master-Master-Slave
- Topologi Master-Slave-Slave
- Dukungan Dual TCP Master (WiFi + Ethernet)
- Agregasi tabel slave virtual
- Optimisasi batch polling
- Caching & buffering data

**Kasus Penggunaan / *Use Cases*:**
- Konsolidasi beberapa PLC/meter
- Virtualisasi register SCADA
- Translasi protokol untuk perangkat heterogen
- Sistem multi-master

---

#### **G - IoT Gateway (Konektivitas Cloud / *Cloud Connectivity*)**

**Target:** Integrasi platform cloud dengan MQTT/HTTP
***Target:** Cloud platform integration with MQTT/HTTP*

```
┌─────────────────────────────────────────────────────────────┐
│  MGate-1210G - Gateway IoT Industri                         │
│  MGate-1210G - Industrial IoT Gateway                       │
│                                                             │
│  Port RS-485 1 ─────┐                                       │
│                     │    ┌──────────────┐    ┌────────────┐ │
│                     ├───►│  Mesin       │───►│  Platform  │ │
│                     │    │  Protokol    │    │  Cloud     │ │
│  Port RS-485 2 ─────┘    └──────────────┘    └────────────┘ │
│                                 │                           │
│                    ┌────────────┼────────────┐              │
│                    ▼            ▼            ▼              │
│               ┌────────┐  ┌────────┐  ┌────────┐            │
│               │  MQTT  │  │  HTTP  │  │  JSON  │            │
│               │ Broker │  │  REST  │  │ Format │            │
│               └────────┘  └────────┘  └────────┘            │
│                                                             │
│  Didukung: AWS IoT, Azure, SURGE, ThingsBoard, Datacake     │
└─────────────────────────────────────────────────────────────┘
```

**Fitur Utama (termasuk semua fitur C, plus):**
***Key Features (includes all C features, plus):***

- Klien MQTT v3.1.1/v5.0
- HTTP/HTTPS REST API
- Enkripsi TLS 1.2/1.3
- Pemformatan data JSON
- Integrasi platform cloud:
  - AWS IoT Core
  - Azure IoT Hub
  - Platform SURGE (SURIOTA)
  - ThingsBoard
  - Datacake
  - Grafana
  - Broker MQTT kustom
- Pembaruan firmware OTA
- Store-and-forward data
- Edge computing (aturan dasar)

**Kasus Penggunaan / *Use Cases*:**
- Pemantauan jarak jauh via dashboard cloud
- Pengumpulan data predictive maintenance
- Integrasi pemantauan energi
- Kepatuhan lingkungan (KLHK)

---

#### **X - All-in-One (Solusi Lengkap / *Complete Solution*)**

**Target:** Gateway IoT industri dengan fitur lengkap
***Target:** Full-featured industrial IoT gateway*

```
┌─────────────────────────────────────────────────────────────┐
│  MGate-1210X - Gateway Industri All-in-One                  │
│  MGate-1210X - All-in-One Industrial Gateway                │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │                    SEMUA FITUR / ALL FEATURES           ││
│  │                                                         ││
│  │  ✓ Converter (RTU ↔ TCP)                               ││
│  │  ✓ Concentrator (Re-mapping, Multi-master)             ││
│  │  ✓ IoT Gateway (MQTT, HTTP, Cloud)                     ││
│  │  ✓ Edge Computing (Aturan lanjutan)                    ││
│  │  ✓ Diagnostik & Logging Lengkap                        ││
│  │                                                         ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│  RS-485 ×2 ◄──► WiFi ◄──► Ethernet ◄──► Cloud              │
│                    │                                        │
│                    └── Konfigurasi BLE + OTA                │
└─────────────────────────────────────────────────────────────┘
```

**Fitur Utama (SEMUA fitur digabung):**
***Key Features (ALL features combined):***

- **Semua fitur Converter (C) / *All Converter (C) features***
- **Semua fitur Concentrator (D) / *All Concentrator (D) features***
- **Semua fitur IoT Gateway (G) / *All IoT Gateway (G) features***
- Edge computing lanjutan
- Diagnostik perangkat lengkap
- Logging diperluas dengan dukungan SD card (mendatang)
- Dukungan teknis prioritas

**Kasus Penggunaan / *Use Cases*:**
- Deployment kelas enterprise
- Lingkungan multi-protokol kompleks
- Instalasi tahan masa depan
- Aplikasi mission-critical

---

### 3.2 Varian Daya / *Power Variants*

| Tipe Daya | Sufiks | Tegangan Input | Fitur |
|-----------|:------:|----------------|-------|
| **Non-POE** | (kosong) | 12-48V DC | Daya DC standar |
| **POE** | (P) | 12-48V DC + 36-57V POE | Daya ganda dengan auto-failover |

**Manfaat POE / *POE Benefits*:**
- Instalasi kabel tunggal (Daya + Data)
- Pergantian sumber daya otomatis
- Integrasi UPS via switch POE
- Pengurangan kompleksitas pengkabelan

---

## 4. Matriks Fitur Detail

## *4. Detailed Feature Matrix*

### 4.1 Perbandingan Fitur Lengkap / *Complete Feature Comparison*

| Fitur / *Feature* | C (Converter) | D (Concentrator) | G (IoT Gateway) | X (All-in-One) |
|-------------------|:-------------:|:----------------:|:---------------:|:--------------:|
| **PERANGKAT KERAS / *HARDWARE*** |||||
| ESP32-S3 (8MB PSRAM) | ✓ | ✓ | ✓ | ✓ |
| RS-485 ×2 | ✓ | ✓ | ✓ | ✓ |
| Ethernet (W5500) | ✓ | ✓ | ✓ | ✓ |
| WiFi 2.4GHz | ✓ | ✓ | ✓ | ✓ |
| BLE 5.0 | ✓ | ✓ | ✓ | ✓ |
| RTC (DS3231) | ✓ | ✓ | ✓ | ✓ |
| 9 Indikator LED | ✓ | ✓ | ✓ | ✓ |
| Proteksi ESD | ✓ | ✓ | ✓ | ✓ |
| Opsi POE | ✓ | ✓ | ✓ | ✓ |
| **MODBUS** |||||
| Modbus RTU | ✓ | ✓ | ✓ | ✓ |
| Modbus TCP | ✓ | ✓ | ✓ | ✓ |
| Jembatan RTU ↔ TCP | ✓ | ✓ | ✓ | ✓ |
| Operasi Dual Port | ✓ | ✓ | ✓ | ✓ |
| Re-mapping Register | - | ✓ | - | ✓ |
| Master-Master-Slave | - | ✓ | - | ✓ |
| Master-Slave-Slave | - | ✓ | - | ✓ |
| Tabel Slave Virtual | - | ✓ | - | ✓ |
| Dual TCP Master | - | ✓ | - | ✓ |
| **CLOUD/IoT** |||||
| Klien MQTT | - | - | ✓ | ✓ |
| HTTP/REST API | - | - | ✓ | ✓ |
| Enkripsi TLS | - | - | ✓ | ✓ |
| Pemformatan JSON | - | - | ✓ | ✓ |
| AWS IoT Core | - | - | ✓ | ✓ |
| Azure IoT Hub | - | - | ✓ | ✓ |
| Platform SURGE | - | - | ✓ | ✓ |
| ThingsBoard | - | - | ✓ | ✓ |
| Store-and-Forward | - | - | ✓ | ✓ |
| Edge Computing (Dasar) | - | - | ✓ | ✓ |
| **KONEKTIVITAS / *CONNECTIVITY*** |||||
| WiFi Auto-Failover | ✓ | ✓ | ✓ | ✓ |
| Pembaruan OTA | ✓ | ✓ | ✓ | ✓ |
| Konfigurasi Mobile BLE | ✓ | ✓ | ✓ | ✓ |
| **LANJUTAN / *ADVANCED*** |||||
| Edge Computing (Lanjutan) | - | - | - | ✓ |
| Diagnostik Diperluas | - | - | - | ✓ |
| Dukungan Prioritas | - | - | - | ✓ |

### 4.2 Kapasitas Slave/Perangkat / *Slave/Device Capacity*

| Varian | Slave RS-485 (per port) | Slave TCP | Maks Register |
|:------:|:-----------------------:|:---------:|:-------------:|
| C | 32 | 16 | 256 |
| D | 48 | 32 | 512 |
| G | 32 | 16 | 256 |
| X | 64 | 64 | 1024 |

---

## 5. Strategi Harga

## *5. Pricing Strategy*

### 5.1 Analisis COGS / *COGS Analysis*

**COGS Dasar (Produksi Saat Ini):**
***Base COGS (Current Production):***

| Komponen | Non-POE | POE |
|----------|--------:|----:|
| PCB & Komponen | Rp 1.100.000 | Rp 1.200.000 |
| Enclosure | Rp 150.000 | Rp 150.000 |
| Perakitan & Pengujian | Rp 180.000 | Rp 280.000 |
| **COGS Dasar** | **Rp 1.430.000** | **Rp 1.630.000** |
| Amortisasi R&D (14%) | Rp 200.000 | Rp 200.000 |
| **COGS Terbeban Penuh** | **Rp 1.630.000** | **Rp 1.830.000** |

### 5.2 Harga Retail / *Retail Pricing*

| Varian | Non-POE | POE | Gross Margin |
|:------:|--------:|----:|:------------:|
| **C (Converter)** | Rp 1.900.000 | Rp 2.300.000 | 14-21% |
| **D (Concentrator)** | Rp 2.500.000 | Rp 2.900.000 | 35-37% |
| **G (IoT Gateway)** | Rp 2.700.000 | Rp 3.100.000 | 40-41% |
| **X (All-in-One)** | Rp 5.000.000 | Rp 5.500.000 | 67-67% |

**Ekuivalen USD (@ Rp 16.000/USD):**
***USD Equivalent (@ Rp 16,000/USD):***

| Varian | Non-POE | POE |
|:------:|--------:|----:|
| **C (Converter)** | $119 | $144 |
| **D (Concentrator)** | $156 | $181 |
| **G (IoT Gateway)** | $169 | $194 |
| **X (All-in-One)** | $313 | $344 |

### 5.3 Rasionalisasi Harga / *Pricing Rationale*

**Strategi Harga Berbasis Nilai:**
***Value-Based Pricing Strategy:***

1. **Varian C (Rp 1,9M)** - Entry level
   - Harga lebih rendah untuk menarik pelanggan entry-level
   - Kompetitor (Moxa MB3180) di Rp 2,6M tapi TANPA WiFi/BLE
   - SURIOTA C lebih murah tapi LEBIH BANYAK fitur

2. **Varian D (Rp 2,5M)** - Mid-range concentrator
   - Fitur re-mapping register adalah nilai tambah
   - Topologi multi-master untuk pengguna lanjutan
   - Kompetitor (ICP DAS tGW-725) di Rp 3,5M

3. **Varian G (Rp 2,7M)** - BASELINE IoT Gateway
   - Ini adalah harga produk saat ini (produksi aktual)
   - MQTT + konektivitas Cloud sangat diminati
   - 20% lebih murah dari BLIIoT BL101L (Rp 3,3M)

4. **Varian X (Rp 5,0M)** - Premium All-in-One
   - Semua fitur dalam satu perangkat
   - 47% lebih murah dari Moxa AIG-101 (Rp 9,3M)
   - Target pelanggan enterprise

---

## 6. Analisis Kompetitor

## *6. Competitor Analysis*

### 6.1 Harga Kompetitor Terverifikasi (Januari 2026)

### *6.1 Verified Competitor Pricing (January 2026)*

#### **Kategori 1: Converter Serial-ke-Ethernet Dasar**
#### ***Category 1: Basic Serial-to-Ethernet Converters***
*Tanpa MQTT, tanpa konektivitas cloud*

| Pabrikan | Model | Harga (IDR) | Fitur | Sumber |
|----------|-------|------------:|-------|--------|
| Elfin | EW11 | Rp 300.000 - 500.000 | WiFi, 1x RS-485, Modbus | [CNX Software](https://www.cnx-software.com/2023/03/06/elfin-ew11-is-a-compact-wifi-to-rs485-unit-with-modbus-tcp-support/) |
| Waveshare | RS485-WiFi-ETH | Rp 480.000 - 550.000 | WiFi+ETH, Modbus dasar | [Waveshare](https://www.waveshare.com/rs232-485-to-wifi-eth-b.htm) |
| USR-IOT | DR302 | Rp 430.000 - 800.000 | DIN Rail, RS485-ETH | [Tokopedia](https://www.tokopedia.com/ptc1/industrial-rs485-to-ethernet-converter-modbus-gateway-usr-dr302) |
| Generik | RTU-TCP Basic | Rp 260.000 - 430.000 | Konversi dasar saja | Berbagai marketplace |

**Analisis:** Converter entry-level sangat murah (Rp 300K-800K) tapi:
- Tidak industrial-grade
- Tidak ada proteksi ESD
- Tidak ada RTC
- Tidak ada konfigurasi BLE
- Kualitas tidak konsisten

---

#### **Kategori 2: Converter Modbus Industri (RTU ↔ TCP)**
#### ***Category 2: Industrial Modbus Converters (RTU ↔ TCP)***
*Konversi protokol saja, tanpa MQTT/cloud*

| Pabrikan | Model | Harga (IDR) | Fitur | Sumber |
|----------|-------|------------:|-------|--------|
| **Moxa** | MGate MB3180 | Rp 2.657.658 | 1x RS-485, Ethernet | [Moxa Alvasta](https://moxa-alvasta.co.id/product/mgate-mb3180/) |
| **Moxa** | MGate MB3170 | Rp 4.474.000 | + Web Management | [Moxa Alvasta](https://moxa-alvasta.co.id/) |
| **Moxa** | MGate MB3280 | Rp 6.138.000 | 2x RS-485 | [Moxa Alvasta](https://moxa-alvasta.co.id/product/mgate-mb3280/) |
| **Moxa** | MGate MB3480 | Rp 8.876.000 | 4x RS-485 | [Moxa Alvasta](https://moxa-alvasta.co.id/product/mgate-mb3480/) |
| **ICP DAS** | tGW-715 | Rp 2.500.000 - 3.000.000 | 1x RS-485, Ethernet | [RS Online](https://www.rs-online.id/p/gateway-modbus-tcp-rtu-ascii-gateway/) |
| **ICP DAS** | tGW-725 | Rp 3.530.000 | 2x RS-485, POE | [Lazada](https://www.lazada.co.id/products/icpdas-tgw-725-modbustcp-to-rtu-gateway-with-poe-and-2-port-rs-485-i7628196301.html) |

**Analisis:** Converter industrial-grade ada di range Rp 2,5M-9M:
- Moxa MB3180 (Rp 2,6M) TIDAK punya WiFi, TIDAK punya BLE
- ICP DAS tGW-725 (Rp 3,5M) punya POE tapi TIDAK punya WiFi/BLE
- **SURIOTA C (Rp 1,9M)** lebih murah dan punya WiFi + BLE + 2x RS-485

---

#### **Kategori 3: IoT Gateway (Modbus ke MQTT/Cloud)**
#### ***Category 3: IoT Gateways (Modbus to MQTT/Cloud)***
*Dengan koneksi cloud/MQTT*

| Pabrikan | Model | Harga (IDR) | Fitur | Sumber |
|----------|-------|------------:|-------|--------|
| **BLIIoT** | BL101L | Rp 3.373.000 | 1x RS-485, 4G, MQTT | [Microthings.id](https://www.microthings.id/product/modbus-to-mqtt-gateway/) |
| **BLIIoT** | BL102 | Rp 4.012.000 | + Dukungan PLC, Linux | [Microthings.id](https://www.microthings.id/product/plc-industrial-iot-gateway-bl102/) |
| **BLIIoT** | BL110 | Rp 4.984.000 | Multi-protokol, OPC UA | [Microthings.id](https://www.microthings.id/product/industrial-iot-gateway-bl110/) |
| **BLIIoT** | BA113 | Rp 5.667.000 | + Dukungan BACnet | [Microthings.id](https://www.microthings.id/product/bacnet-iot-gateway-ba113/) |
| **USR-IOT** | M100 | Rp 3.200.000 | Remote I/O, Modbus | [Tokopedia](https://www.tokopedia.com/mandala-tech/usr-m100-iot-gateway-industrial-ethernet-remote-io-modbus-gateway-best) |
| **Moxa** | AIG-101 | Rp 9.340.000 | LTE, MQTT, Edge Computing | [Moxa Store](https://moxastore.express-inc.com/AIG_101_T_EU_p/aig-101-t-eu.htm) |
| **Moxa** | AIG-301 | Rp 26.400.000+ | Advanced IIoT Gateway | [Melchioni](https://www.melchionielectronics.com/en/advanced-iiot-gateway-aig-300-azure-iot-edge-moxa-aig-301-t-ap-azu-lx.html) |

**Analisis:** IoT gateway dengan MQTT ada di range Rp 3,2M-26M:
- BLIIoT BL101L (Rp 3,3M) punya 4G tapi TIDAK punya combo Ethernet+WiFi
- BLIIoT BL110 (Rp 4,9M) multi-protokol tapi lebih mahal
- Moxa AIG-101 (Rp 9,3M) enterprise-grade, sangat mahal
- **SURIOTA G (Rp 2,7M)** lebih murah dari semua dengan WiFi+ETH+BLE

---

### 6.2 Matriks Posisi Kompetitif / *Competitive Positioning Matrix*

```
                        HARGA (IDR) / PRICE (IDR)
                    ↑
      Rp 10.000.000 │                              ★ Moxa AIG-101 ($584)
                    │
       Rp 8.000.000 │                       ★ Moxa MB3480
                    │
       Rp 6.000.000 │                  ★ Moxa MB3280    ★ BLIIoT BA113
                    │             ★ BLIIoT BL110
       Rp 5.000.000 │     ┌────────────────────────────────────┐
                    │     │  ★ SRT-MGATE-1210X                 │ ← ALL-IN-ONE
                    │     │     (Rp 5,0M / $313)               │
       Rp 4.000.000 │     │         ★ Moxa MB3170  ★ BL102     │
                    │     │              ★ ICP DAS tGW-725     │
                    │     │     ★ BLIIoT BL101L   ★ USR-M100   │
       Rp 3.000.000 │     │  ★ SRT-MGATE-1210G ◄─── IoT GATEWAY│
                    │     │     (Rp 2,7M / $169)               │
                    │     │  ★ SRT-MGATE-1210D ◄─── CONCENTRATOR
                    │     │     (Rp 2,5M / $156)   ★ Moxa MB3180
       Rp 2.000.000 │     │  ★ SRT-MGATE-1210C ◄─── CONVERTER  │
                    │     │     (Rp 1,9M / $119)               │
                    │     └────────────────────────────────────┘
       Rp 1.000.000 │  ★ Entry-level (Waveshare, Elfin, USR-DR)
                    │
                    └──────────────────────────────────────────►
                        DASAR         FITUR          LANJUTAN
                        Converter   Concentrator   IoT Gateway
```

### 6.3 Perbandingan Fitur vs Kompetitor / *Feature Comparison vs Competitors*

| Fitur | SURIOTA | Moxa MB3180 | BLIIoT BL101L | Moxa AIG-101 |
|-------|:-------:|:-----------:|:-------------:|:------------:|
| **Harga** | Rp 1,9-5,0M | Rp 2,6M | Rp 3,3M | Rp 9,3M |
| Port RS-485 | 2 | 1 | 1 | 2 |
| Ethernet | ✓ | ✓ | - | ✓ |
| WiFi | ✓ | - | - | - |
| 4G/LTE | - | - | ✓ | ✓ |
| Konfigurasi BLE | ✓ | - | - | - |
| Baterai RTC | ✓ | - | - | ✓ |
| MQTT | G/X saja | - | ✓ | ✓ |
| WiFi Auto-Failover | ✓ | - | - | - |
| Proteksi ESD | ✓ | ✓ | ✓ | ✓ |
| **Dukungan Lokal (ID)** | ✓ | Distributor | Distributor | Distributor |

### 6.4 Poin Penjualan Unik vs Kompetisi / *Unique Selling Points vs Competition*

| USP | Deskripsi | vs Moxa | vs BLIIoT |
|-----|-----------|---------|-----------|
| **Konfigurasi Mobile BLE** | Setup via smartphone 5 menit | EKSKLUSIF | EKSKLUSIF |
| **WiFi + Ethernet** | Konektivitas ganda | EKSKLUSIF | +Ethernet (BL101L hanya 4G) |
| **WiFi Auto-Failover** | Pergantian jaringan otomatis | EKSKLUSIF | EKSKLUSIF |
| **2x RS-485** | Dual serial port standar | +1 port vs MB3180 | +1 port vs BL101L |
| **Backup Baterai RTC** | Timestamp akurat | +Fitur | +Fitur |
| **Dukungan Lokal** | Bahasa Indonesia, dukungan WA | Lebih Baik | Lebih Baik |
| **Harga** | Harga kompetitif | 28% lebih murah (C vs MB3180) | 20% lebih murah (G vs BL101L) |

---

## 7. Varian Campuran (Mix)

## *7. Mix Variants*

### 7.1 Gambaran Umum / *Overview*

Varian Mix memungkinkan kombinasi fitur dari beberapa varian untuk kebutuhan spesifik.

*Mix Variants allow combining features from multiple variants for specific needs.*

### 7.2 Opsi Mix Tersedia / *Available Mix Options*

| Kode Mix | Kombinasi | Fitur | Harga (Non-POE / POE) |
|:--------:|-----------|-------|-----------------------:|
| **CD** | Converter + Concentrator | RTU↔TCP + Re-mapping + Multi-master | Rp 2.900.000 / Rp 3.300.000 |
| **CG** | Converter + IoT Gateway | RTU↔TCP + MQTT + Cloud | Rp 3.200.000 / Rp 3.600.000 |
| **DG** | Concentrator + IoT Gateway | Re-mapping + MQTT + Cloud | Rp 3.800.000 / Rp 4.300.000 |

### 7.3 Matriks Fitur Varian Mix / *Mix Variant Feature Matrix*

| Fitur | CD Mix | CG Mix | DG Mix |
|-------|:------:|:------:|:------:|
| Modbus RTU/TCP | ✓ | ✓ | ✓ |
| Re-mapping Register | ✓ | - | ✓ |
| Topologi Multi-master | ✓ | - | ✓ |
| Tabel Slave Virtual | ✓ | - | ✓ |
| Klien MQTT | - | ✓ | ✓ |
| HTTP REST API | - | ✓ | ✓ |
| Platform Cloud | - | ✓ | ✓ |
| Edge Computing | - | Dasar | Dasar |

### 7.4 Kasus Penggunaan Varian Mix / *Mix Variant Use Cases*

**CD Mix (Converter + Concentrator):**
- Sistem SCADA besar yang membutuhkan agregasi data
- Integrasi PLC multi-vendor
- Virtualisasi register tanpa cloud

**CG Mix (Converter + IoT Gateway):**
- Kebutuhan konektivitas cloud sederhana
- Pemantauan jarak jauh tanpa topologi kompleks
- Retrofit sistem lama ke cloud

**DG Mix (Concentrator + IoT Gateway):**
- Lingkungan industri kompleks
- Agregasi cloud multi-perangkat
- Deployment IoT enterprise

### 7.5 Memesan Varian Mix / *Ordering Mix Variants*

Varian Mix adalah **build kustom** dan memerlukan:

*Mix variants are **custom builds** and require:*

1. Kuantitas pesanan minimum: 10 unit
2. Lead time: 2-3 minggu
3. Komitmen pre-order

Hubungi sales@suriota.com untuk pesanan Varian Mix.

*Contact sales@suriota.com for Mix Variant orders.*

---

## 8. Implementasi Teknis

## *8. Technical Implementation*

### 8.1 Struktur ProductConfig.h / *ProductConfig.h Structure*

```cpp
// ============================================================================
// KONFIGURASI VARIAN PRODUK / PRODUCT VARIANT CONFIGURATION
// ============================================================================

// Pemilihan Varian Fungsi (uncomment SATU)
// Function Variant Selection (uncomment ONE)
#define PRODUCT_FUNCTION_C      // Converter
// #define PRODUCT_FUNCTION_D   // Concentrator
// #define PRODUCT_FUNCTION_G   // IoT Gateway
// #define PRODUCT_FUNCTION_X   // All-in-One

// Pemilihan Varian Daya (uncomment SATU)
// Power Variant Selection (uncomment ONE)
// #define PRODUCT_VARIANT ""   // Non-POE
#define PRODUCT_VARIANT "P"     // POE
#define PRODUCT_IS_POE 1

// Kode Fungsi / Function Codes
#ifdef PRODUCT_FUNCTION_C
  #define PRODUCT_FUNCTION_CODE "C"
  #define FEATURE_CONVERTER 1
  #define FEATURE_CONCENTRATOR 0
  #define FEATURE_IOT_GATEWAY 0
#endif

#ifdef PRODUCT_FUNCTION_D
  #define PRODUCT_FUNCTION_CODE "D"
  #define FEATURE_CONVERTER 1
  #define FEATURE_CONCENTRATOR 1
  #define FEATURE_IOT_GATEWAY 0
#endif

#ifdef PRODUCT_FUNCTION_G
  #define PRODUCT_FUNCTION_CODE "G"
  #define FEATURE_CONVERTER 1
  #define FEATURE_CONCENTRATOR 0
  #define FEATURE_IOT_GATEWAY 1
#endif

#ifdef PRODUCT_FUNCTION_X
  #define PRODUCT_FUNCTION_CODE "X"
  #define FEATURE_CONVERTER 1
  #define FEATURE_CONCENTRATOR 1
  #define FEATURE_IOT_GATEWAY 1
#endif

// Nama yang Dihasilkan / Generated Names
#if PRODUCT_IS_POE
  #define PRODUCT_FULL_MODEL "MGate-1210" PRODUCT_FUNCTION_CODE "(P)"
#else
  #define PRODUCT_FULL_MODEL "MGate-1210" PRODUCT_FUNCTION_CODE
#endif
```

### 8.2 Flag Fitur / *Feature Flags*

```cpp
// Ketersediaan fitur berdasarkan varian
// Feature availability based on variant
#if FEATURE_CONCENTRATOR
  // Kode re-mapping register
  // Kode topologi multi-master
  // Kode tabel slave virtual
#endif

#if FEATURE_IOT_GATEWAY
  // Kode klien MQTT
  // Kode klien HTTP REST
  // Kode integrasi cloud
  // Kode enkripsi TLS
#endif
```

### 8.3 Matriks Build Firmware / *Firmware Build Matrix*

| Target Build | Fungsi | Daya | Nama Binary |
|--------------|--------|------|-------------|
| MGATE1210C | Converter | Non-POE | MGATE-1210_C_v1.0.6.bin |
| MGATE1210CP | Converter | POE | MGATE-1210_CP_v1.0.6.bin |
| MGATE1210D | Concentrator | Non-POE | MGATE-1210_D_v1.0.6.bin |
| MGATE1210DP | Concentrator | POE | MGATE-1210_DP_v1.0.6.bin |
| MGATE1210G | IoT Gateway | Non-POE | MGATE-1210_G_v1.0.6.bin |
| MGATE1210GP | IoT Gateway | POE | MGATE-1210_GP_v1.0.6.bin |
| MGATE1210X | All-in-One | Non-POE | MGATE-1210_X_v1.0.6.bin |
| MGATE1210XP | All-in-One | POE | MGATE-1210_XP_v1.0.6.bin |

---

## Lampiran A: Daftar Lengkap SKU Produk

## *Appendix A: Complete Product SKU List*

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

---

## Lampiran B: Sumber Data & Referensi

## *Appendix B: Data Sources & References*

### Harga Kompetitor Diverifikasi Dari: / *Competitor Pricing Verified From:*

1. **Moxa Official Indonesia**
   - Sumber: [moxa-alvasta.co.id](https://moxa-alvasta.co.id/)
   - Produk: MGate MB3180, MB3170, MB3280, MB3480
   - Tanggal verifikasi: Januari 2026

2. **BLIIoT Indonesia (Microthings)**
   - Sumber: [microthings.id](https://www.microthings.id/)
   - Produk: BL101L, BL102, BL110, BA113
   - Tanggal verifikasi: Januari 2026

3. **ICP DAS**
   - Sumber: [Lazada Indonesia](https://www.lazada.co.id/), [RS Online Indonesia](https://www.rs-online.id/)
   - Produk: tGW-715, tGW-725
   - Tanggal verifikasi: Januari 2026

4. **USR-IOT**
   - Sumber: [Tokopedia](https://www.tokopedia.com/)
   - Produk: M100, DR302
   - Tanggal verifikasi: Januari 2026

5. **Produk Entry-Level**
   - Sumber: Tokopedia, Shopee, website pabrikan
   - Produk: Elfin EW11, Waveshare RS485-WiFi-ETH
   - Tanggal verifikasi: Januari 2026

### Kurs yang Digunakan: / *Exchange Rate Used:*
- USD ke IDR: Rp 16.000
- EUR ke IDR: Rp 17.400

---

*Dokumen dipelihara oleh SURIOTA Product Management*
*Document maintained by SURIOTA Product Management*

*Terakhir Diperbarui: Januari 2026*
*Last Updated: January 2026*
