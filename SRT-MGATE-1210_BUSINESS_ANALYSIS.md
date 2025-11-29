# SRT-MGATE-1210 Business Analysis & Pricing Strategy

## Dokumen Analisis Bisnis untuk Finance & Marketing

**Document Version**: 5.4
**Last Updated**: November 29, 2025
**Prepared by**: Product Development Team
**Exchange Rate**: 1 USD = Rp 16,648 (actual) / Rp 16,000 (rounded for calculation)

---

# REKOMENDASI HARGA FINAL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│                    💰 HARGA JUAL RESMI SRT-MGATE-1210 💰                   │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  MODEL                    │  HARGA JUAL      │  MARGIN    │  HPP    │   │
│   ├───────────────────────────┼──────────────────┼────────────┼─────────┤   │
│   │  SRT-MGATE-1210           │  Rp 2.800.000    │  48%       │  1.45M  │   │
│   │  (Standard - 2xRS485)     │  (~$175 USD)     │            │         │   │
│   ├───────────────────────────┼──────────────────┼────────────┼─────────┤   │
│   │  SRT-MGATE-1210-POE       │  Rp 3.500.000    │  53%       │  1.65M  │   │
│   │  (PoE Version)            │  (~$219 USD)     │            │         │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   POSITIONING:                                                              │
│   • 20% lebih murah dari USR-N720 (Rp 3.5M)                                 │
│   • 17% lebih murah dari BLIIoT BL100 (Rp 3.37M)                            │
│   • 19% lebih murah dari ICP DAS tGW-725 (Rp 3.45M)                         │
│   • 69% lebih murah dari Moxa AIG-101 (Rp 8.96M)                            │
│                                                                             │
│   USP: SATU-SATUNYA Modbus-to-MQTT gateway dengan WiFi + BLE di Indonesia   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# DAFTAR ISI

1. [Executive Summary](#executive-summary)
2. [Product Overview](#product-overview)
3. [Cost Analysis (COGS)](#cost-analysis-cogs)
4. [Competitor Analysis](#competitor-analysis)
5. [Feature Comparison](#feature-comparison)
6. [Pricing Strategy](#pricing-strategy)
7. [Unique Selling Proposition (USP)](#unique-selling-proposition-usp)
8. [Sales & Marketing Guide](#sales--marketing-guide)
9. [Brand Awareness Strategy](#brand-awareness-strategy)
10. [Financial Projections](#financial-projections)
11. [Appendix](#appendix)

---

# Executive Summary

## Ringkasan Eksekutif

**SRT-MGATE-1210** adalah Industrial IoT Gateway produksi lokal PT Surya Inovasi Prioritas (SURIOTA) yang dirancang untuk **konversi protokol Modbus RTU/TCP ke MQTT** untuk aplikasi Industrial IoT dan Cloud Platform.

### Key Highlights:

| Metric                     | Value                          |
| -------------------------- | ------------------------------ |
| **Target Market**          | Industrial IoT Indonesia       |
| **Competitive Position**   | Mid-range dengan fitur premium |
| **Price Point**            | Rp 2.800.000 - 3.500.000       |
| **Gross Margin**           | 48-53%                         |
| **Break-even**             | 134 units                      |
| **Target Sales (2 tahun)** | 200 units (Estimated)          |

### Keunggulan Kompetitif:

- **SATU-SATUNYA** Modbus-to-MQTT gateway di Indonesia dengan **WiFi + BLE + Industrial Grade**
- **Produksi Lokal** = Harga lebih kompetitif, support lebih cepat
- **20% lebih murah** dari USR-N720 dengan fitur WiFi + BLE yang mereka tidak punya
- **69% lebih murah** dari Moxa AIG-101 dengan fitur BLE config yang Moxa tidak punya

---

# Product Overview

## Spesifikasi Produk

### SRT-MGATE-1210 (Standard Version)

| Specification       | Detail                                             |
| ------------------- | -------------------------------------------------- |
| **MCU**             | ESP32-S3-WROOM-1 (Dual-core 240MHz, 8MB PSRAM)     |
| **RS-485**          | 2 ports with ESD protection, up to 32 devices/port |
| **Ethernet**        | W5500 10/100 Mbps with magnetic isolation          |
| **WiFi**            | 2.4GHz 802.11 b/g/n, WPA3-PSK                      |
| **Bluetooth**       | BLE 5.0 for mobile configuration                   |
| **RTC**             | DS3231 dengan battery backup (CR1220)              |
| **LED Indicators**  | 9 LEDs (Status, Config, WiFi, NET, RS485, Power)   |
| **Protocol Input**  | Modbus RTU RS485, Modbus TCP WiFi / Ethernet       |
| **Protocol Output** | MQTT + JSON format                                 |
| **Cloud Support**   | AWS, Datacake, Grafana, ThingsBoard, SURGE, etc.   |
| **Power**           | 12-48V DC                                          |
| **Temperature**     | -40°C to +75°C (Industrial Grade)                  |
| **Mounting**        | DIN Rail / Wall Mount                              |
| **Enclosure**       | PLA+ industrial housing                            |
| **Dimensions**      | 110 x 90 x 58 mm                                   |
| **Certifications**  | Rohs & CE, FCC (planned)                           |
| **Warranty**        | 1.5 Year                                           |
| **Support**         | Local Indonesia Support                            |
| **Mobile App**      | Android & iOS for BLE configuration                |
| **Firmware Updates**| OTA via BLE & Local via USB                        |
| **Auto Failover**   | WiFi backup for Ethernet failure (Dual Connection) |
            


### SRT-MGATE-1210-POE (PoE Version)

| Additional Feature   | Detail                       |
| -------------------- | ---------------------------- |
| **PoE**              | IEEE 802.3af/at (9W, 36-57V) |
| **Power Redundancy** | Auto-switch PoE ↔ DC         |

---

# Cost Analysis (COGS)

## Analisis Biaya Produksi

### Data Aktual HPP (1 pcs production)

> **Sumber**: Data produksi aktual, 2025

| Item                            | USD        | IDR (Kurs 16,648) |
| ------------------------------- | ---------- | ----------------- |
| Hardware (PCB + Electronics)    | $88.00     | Rp 1,465,024      |
| Hardware (Mechanical/Enclosure) | $6.00      | Rp 99,888         |
| **Total Hardware**              | **$94.00** | **Rp 1,564,912**  |

_Catatan: Belum termasuk manpower + overhead produksi + R&D Firmware & Software_

---

### Kalkulasi COGS untuk Volume 200 pcs

| Cost Component    | 1 pcs        | 200 pcs (est. -25%) | Notes                 |
| ----------------- | ------------ | ------------------- | --------------------- |
| Hardware Cost     | Rp 1,564,912 | Rp 1,173,684        | Volume discount 25%   |
| Labor (10%)       | -            | Rp 117,368          | Assembly + QC         |
| Overhead (5%)     | -            | Rp 58,684           | Facilities, utilities |
| **COGS Standard** | -            | **Rp 1,350,000**    | Rounded               |
| PoE Module        | -            | +Rp 200,000         | Additional component  |
| **COGS PoE**      | -            | **Rp 1,550,000**    | Rounded               |

---

### R&D Amortization

| Item                    | Amount         |
| ----------------------- | -------------- |
| Total R&D Investment    | Rp 20,000,000  |
| (Firmware + Mobile App) |                |
| Target Sales Volume     | 200 units      |
| **R&D per Unit**        | **Rp 100,000** |

## _Catatan: Estimated_

### Fully Loaded Cost Summary

| Model                  | Manufacturing COGS | R&D Amortization | **Fully Loaded Cost** |
| ---------------------- | ------------------ | ---------------- | --------------------- |
| **SRT-MGATE-1210**     | Rp 1,350,000       | Rp 100,000       | **Rp 1,450,000**      |
| **SRT-MGATE-1210-POE** | Rp 1,550,000       | Rp 100,000       | **Rp 1,650,000**      |

---

# Competitor Analysis

## Analisis Kompetitor - Modbus to MQTT Gateway

> **FOKUS**: Hanya kompetitor yang memiliki fitur **Modbus to MQTT** (konversi protokol untuk IoT)

---

### 1. USR-IOT N720-ETH (Edge IoT Gateway)

#### Informasi Produk

| Item              | Detail                                    |
| ----------------- | ----------------------------------------- |
| **Manufacturer**  | Jinan USR IOT Technology Co., Ltd (China) |
| **Product Type**  | Modbus to MQTT Edge Gateway               |
| **Target Market** | Industrial IoT, Smart Factory             |

#### Harga

| Source             | Price            | Link                                                                                                                                                                                  |
| ------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Official Store** | **$59.00**       | [shop.usriot.com](https://shop.usriot.com/industrial-serial-to-ethernet-converters/)                                                                                                  |
| **Tokopedia**      | **Rp 3,500,000** | [Link Tokopedia](https://www.tokopedia.com/elektromurah/iot-gateway-rs485-to-ethernet-support-1000-data-points-modbus-gateway-multi-host-modbus-polling-n720-eth-1730980558396491220) |
| **Markup di Indo** | **+270%**        | (dari $59 → Rp 3.5M)                                                                                                                                                                  |

#### Spesifikasi

| Feature     | Specification           |
| ----------- | ----------------------- |
| RS-485      | **2 ports**             |
| Ethernet    | 10/100 Mbps             |
| WiFi        | **TIDAK ADA** ❌        |
| BLE         | **TIDAK ADA** ❌        |
| **MQTT**    | **Yes + JSON format** ✓ |
| Data Points | 1000 points             |
| Temperature | -40°C ~ +85°C           |
| Power       | DC 9-36V                |

#### Kelebihan & Kekurangan

| Kelebihan         | Kekurangan                         |
| ----------------- | ---------------------------------- |
| Industrial grade  | **Tidak ada WiFi**                 |
| 2x RS485 ports    | **Tidak ada BLE config**           |
| MQTT + JSON ready | Harga di Indo sangat mahal (+270%) |
| 1000 data points  | Tidak ada auto-failover            |
|                   | Tidak ada local support            |

#### vs SURIOTA

| Aspek         | USR-N720     | SURIOTA      | Winner             |
| ------------- | ------------ | ------------ | ------------------ |
| Harga         | Rp 3,500,000 | Rp 2,800,000 | **SURIOTA (-20%)** |
| WiFi          | ❌           | ✅           | **SURIOTA**        |
| BLE Config    | ❌           | ✅           | **SURIOTA**        |
| Auto Failover | ❌           | ✅           | **SURIOTA**        |
| Local Support | ❌           | ✅           | **SURIOTA**        |

---

### 2. USR-IOT N540 H7-4 (4-Port Modbus MQTT Gateway)

#### Informasi Produk

| Item              | Detail                                    |
| ----------------- | ----------------------------------------- |
| **Manufacturer**  | Jinan USR IOT Technology Co., Ltd (China) |
| **Product Type**  | 4-Port Modbus to MQTT Gateway             |
| **Target Market** | Multi-device Industrial IoT               |

#### Harga

| Source        | Price            | Link                                                                                                  |
| ------------- | ---------------- | ----------------------------------------------------------------------------------------------------- |
| **Tokopedia** | **Rp 1,820,000** | [Link Tokopedia](https://www.tokopedia.com/find/modbus-mqtt)                                          |
| **Shopee**    | ~Rp 1,800,000    | [Link Shopee](https://shopee.co.id/USR-N540-Modbus-Gateway-4-port-RS485-MQTT-i.234231342.10678673522) |

#### Spesifikasi

| Feature     | Specification       |
| ----------- | ------------------- |
| RS-485      | **4 ports**         |
| Ethernet    | 10/100 Mbps         |
| WiFi        | **TIDAK ADA** ❌    |
| BLE         | **TIDAK ADA** ❌    |
| **MQTT**    | **Yes + SSL/TLS** ✓ |
| Data Points | 128 points          |
| Temperature | -40°C ~ +85°C       |

#### Kelebihan & Kekurangan

| Kelebihan        | Kekurangan               |
| ---------------- | ------------------------ |
| Murah (Rp 1.82M) | **Tidak ada WiFi**       |
| 4x RS485 ports   | **Tidak ada BLE config** |
| MQTT + SSL/TLS   | Hanya 128 data points    |
|                  | Tidak ada ESD protection |

#### vs SURIOTA

| Aspek          | USR-N540     | SURIOTA      | Winner              |
| -------------- | ------------ | ------------ | ------------------- |
| Harga          | Rp 1,820,000 | Rp 2,800,000 | **USR-N540 (-35%)** |
| WiFi           | ❌           | ✅           | **SURIOTA**         |
| BLE Config     | ❌           | ✅           | **SURIOTA**         |
| RS-485 Ports   | 4            | 2            | **USR-N540**        |
| ESD Protection | ❌           | ✅           | **SURIOTA**         |
| RTC Battery    | ❌           | ✅           | **SURIOTA**         |
| Auto Failover  | ❌           | ✅           | **SURIOTA**         |

**Catatan**: USR-N540 lebih murah tapi untuk aplikasi yang butuh WiFi backup dan BLE config, SURIOTA lebih cocok.

---

### 3. BLIIoT BL100 (Modbus to MQTT Gateway)

#### Informasi Produk

| Item              | Detail                             |
| ----------------- | ---------------------------------- |
| **Manufacturer**  | Shenzhen Beilai Technology (China) |
| **Product Type**  | Cellular Modbus to MQTT Gateway    |
| **Target Market** | Remote Industrial IoT, Telemetry   |

#### Harga

| Source                      | Price            | Link                                                                           |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------ |
| **Official Website**        | Request Quote    | [bliiot.com](https://bliiot.com/products/modbus-to-mqtt-gateway-bl101)         |
| **Tokopedia (Microthings)** | **Rp 3,373,000** | [Link Tokopedia](https://www.tokopedia.com/microthings/modbus-to-mqtt-gateway) |

#### Spesifikasi

| Feature     | Specification                          |
| ----------- | -------------------------------------- |
| Processor   | ARM 300MHz + Linux OS                  |
| RS-485      | **1 port** (BL100) / 2-6 ports (BL101) |
| Ethernet    | 1 WAN + 1 LAN                          |
| WiFi        | **Optional** (beberapa SKU)            |
| 4G LTE      | **Built-in** (cellular)                |
| BLE         | **TIDAK ADA** ❌                       |
| **MQTT**    | **Yes** ✓                              |
| Data Points | 320 points                             |
| Temperature | -40°C ~ +85°C                          |

#### Kelebihan & Kekurangan

| Kelebihan              | Kekurangan                 |
| ---------------------- | -------------------------- |
| 4G cellular built-in   | **Tidak ada BLE config**   |
| Linux-based (powerful) | Hanya 1 RS-485 (BL100)     |
| MQTT + multiple cloud  | Setup lebih kompleks       |
| Dual Ethernet          | WiFi hanya di SKU tertentu |

#### vs SURIOTA

| Aspek            | BLIIoT BL100 | SURIOTA      | Winner             |
| ---------------- | ------------ | ------------ | ------------------ |
| Harga            | Rp 3,373,000 | Rp 2,800,000 | **SURIOTA (-17%)** |
| WiFi             | Optional     | ✅ Built-in  | **SURIOTA**        |
| BLE Config       | ❌           | ✅           | **SURIOTA**        |
| 4G Cellular      | ✅           | ❌           | **BLIIoT**         |
| RS-485 Ports     | 1            | 2            | **SURIOTA**        |
| Setup Complexity | Complex      | Simple       | **SURIOTA**        |

---

### 4. Moxa AIG-101-T (IIoT Gateway)

#### Informasi Produk

| Item              | Detail                        |
| ----------------- | ----------------------------- |
| **Manufacturer**  | Moxa Inc. (Taiwan)            |
| **Product Type**  | Enterprise IIoT Gateway       |
| **Target Market** | Enterprise, Cloud Integration |

#### Harga

| Source                   | Price            | Link                                                                                                                                                                      |
| ------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Official (MoxaStore)** | **$778.00**      | [moxastore.express-inc.com](https://moxastore.express-inc.com/AIG_101_T_p/aig-101-t.htm)                                                                                  |
| **Moxa Official**        | -                | [moxa.com](https://www.moxa.com/en/products/industrial-computing/iiot-gateways/ready-to-deploy-iiot-gateways/aig-101-series)                                              |
| **Tokopedia**            | **Rp 8,956,000** | [Link Tokopedia](https://www.tokopedia.com/unilead-indojaya/moxa-aig-101-t-iiot-gateways-modbus-rtu-ascii-tcp-to-mqtt-azure-aws-cloud-ready-gateways-1730995447495820377) |

#### Spesifikasi

| Feature     | Specification                     |
| ----------- | --------------------------------- |
| RS-485      | **2 ports**                       |
| Ethernet    | 2x 10/100 Mbps                    |
| WiFi        | **TIDAK ADA** ❌ (LTE Cat.1 only) |
| LTE         | Built-in Cat.1                    |
| BLE         | **TIDAK ADA** ❌                  |
| **MQTT**    | **Yes + Azure/AWS SDK** ✓         |
| Temperature | -40°C ~ +70°C                     |
| Warranty    | 5 Years                           |

#### Kelebihan & Kekurangan

| Kelebihan                 | Kekurangan               |
| ------------------------- | ------------------------ |
| Brand premium Taiwan      | **SANGAT MAHAL** (Rp 9M) |
| Azure/AWS SDK built-in    | **Tidak ada WiFi**       |
| 5 tahun garansi           | **Tidak ada BLE config** |
| Industrial certifications | LTE only, no WiFi backup |
| Data buffering            | Overkill untuk SMB       |

#### vs SURIOTA

| Aspek         | Moxa AIG-101  | SURIOTA       | Winner             |
| ------------- | ------------- | ------------- | ------------------ |
| Harga         | Rp 8,956,000  | Rp 2,800,000  | **SURIOTA (-69%)** |
| WiFi          | ❌ (LTE only) | ✅            | **SURIOTA**        |
| BLE Config    | ❌            | ✅            | **SURIOTA**        |
| Azure/AWS SDK | ✅ Built-in   | ✅ Compatible | Tie                |
| Warranty      | 5 years       | 1.5 year        | **Moxa**           |
| Local Support | Import        | ✅ Local      | **SURIOTA**        |

---

### 5. ICP DAS tGW-725 (Modbus TCP/RTU Gateway)

> **CATATAN**: Produk ini adalah **Modbus TCP to RTU converter**, BUKAN Modbus to MQTT gateway. Ditambahkan karena customer sering membandingkan sebagai alternatif.

#### Informasi Produk

| Item              | Detail                                               |
| ----------------- | ---------------------------------------------------- |
| **Manufacturer**  | ICP DAS Co., Ltd (Taiwan)                            |
| **Product Type**  | Modbus TCP to RTU/ASCII Gateway (Protocol Converter) |
| **Target Market** | Industrial Automation, SCADA                         |

#### Harga

| Source               | Price            | Link                                                                                                                       |
| -------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Official Website** | ~$150-180        | [icpdas.com](https://www.icpdas.com/en/product/tGW-725)                                                                    |
| **Tokopedia**        | **Rp 3,450,000** | [Link Tokopedia](https://www.tokopedia.com/wellkomp-1/icpdas-tgw-725-modbus-tcp-to-rtu-gateway-with-poe-and-2-port-rs-485) |

#### Spesifikasi

| Feature     | Specification                 |
| ----------- | ----------------------------- |
| RS-485      | **2 ports**                   |
| Ethernet    | 10/100 Mbps                   |
| PoE         | **IEEE 802.3af** ✓            |
| WiFi        | **TIDAK ADA** ❌              |
| BLE         | **TIDAK ADA** ❌              |
| **MQTT**    | **TIDAK ADA** ❌              |
| Protocol    | Modbus TCP ↔ Modbus RTU/ASCII |
| Temperature | -25°C ~ +75°C                 |
| Power       | DC 12-48V / PoE               |
| Enclosure   | Plastic                       |

#### Kelebihan & Kekurangan

| Kelebihan            | Kekurangan                                    |
| -------------------- | --------------------------------------------- |
| Brand Taiwan trusted | **TIDAK ADA MQTT** - hanya protocol converter |
| PoE built-in         | **Tidak ada WiFi**                            |
| 2x RS485 ports       | **Tidak ada BLE config**                      |
|                      | Plastic casing (bukan metal)                  |
|                      | Tidak bisa langsung ke cloud platform         |

#### vs SURIOTA

| Aspek       | ICP DAS tGW-725 | SURIOTA          | Winner             |
| ----------- | --------------- | ---------------- | ------------------ |
| Harga       | Rp 3,450,000    | Rp 2,800,000     | **SURIOTA (-19%)** |
| **MQTT**    | ❌              | ✅               | **SURIOTA**        |
| WiFi        | ❌              | ✅               | **SURIOTA**        |
| BLE Config  | ❌              | ✅               | **SURIOTA**        |
| PoE         | ✅              | ✅ (PoE version) | Tie                |
| Cloud Ready | ❌              | ✅               | **SURIOTA**        |

**Kesimpulan**: ICP DAS tGW-725 adalah **protocol converter** (Modbus TCP ↔ RTU), BUKAN IoT gateway. Tidak bisa langsung kirim data ke cloud (AWS/Azure/ThingsBoard). Untuk aplikasi IoT, SURIOTA jauh lebih cocok.

---

# Feature Comparison

## Matriks Perbandingan Fitur - Modbus Gateway

### Tabel Perbandingan Lengkap

| Feature             | USR-N540     | USR-N720    | BLIIoT BL100 | ICP DAS tGW-725  | Moxa AIG-101 | **SURIOTA**        |
| ------------------- | ------------ | ----------- | ------------ | ---------------- | ------------ | ------------------ |
| **Harga Tokopedia** | **Rp 1.82M** | **Rp 3.5M** | **Rp 3.37M** | **Rp 3.45M**     | **Rp 8.96M** | **Rp 2.8M**        |
| **Type**            | MQTT GW      | MQTT GW     | MQTT GW      | **TCP/RTU only** | MQTT GW      | **MQTT GW**        |
|                     |              |             |              |                  |              |                    |
| **RS-485 Ports**    | 4            | 2           | 1            | 2                | 2            | **2**              |
| **ESD Protection**  | No           | Yes         | No           | No               | Yes          | **Yes**            |
| **RTC + Battery**   | No           | No          | No           | No               | No           | **Yes** ✅         |
| **LED Indicators**  | Basic        | Basic       | Basic        | Basic            | Basic        | **9 LEDs** ✅      |
| **Ethernet**        | Yes          | Yes         | Dual         | Yes              | Dual         | **Yes**            |
| **WiFi**            | **No** ❌    | **No** ❌   | Optional     | **No** ❌        | **No** ❌    | **Yes** ✅         |
| **BLE Config**      | **No** ❌    | **No** ❌   | **No** ❌    | **No** ❌        | **No** ❌    | **Yes** ✅         |
| **MQTT Native**     | Yes          | Yes         | Yes          | **No** ❌        | Yes          | **Yes**            |
| **JSON Format**     | Yes          | Yes         | Yes          | **No** ❌        | Yes          | **Yes**            |
| **4G/LTE**          | No           | No          | Yes          | No               | Yes          | No                 |
|                     |              |             |              |                  |              |                    |
| **Industrial Temp** | Yes          | Yes         | Yes          | Yes              | Yes          | **Yes**            |
| **PoE Option**      | No           | No          | No           | **Yes**          | No           | **Yes**            |
| **Auto Failover**   | No           | No          | No           | No               | No           | **Yes**            |
| **Local Support**   | No           | No          | No           | No               | No           | **Yes**            |
|                     |              |             |              |                  |              |                    |
| **Cloud Platform**  | Generic      | Generic     | Multi        | **None**         | Azure/AWS    | **Multi**          |
| **Target User**     | Multi-port   | Industrial  | Remote       | SCADA/HMI        | Enterprise   | **SMB/Industrial** |

### Visual Comparison

```
HARGA TOKOPEDIA vs FITUR (Modbus Gateway)
─────────────────────────────────────────────────────────────────────

Rp 8.96M ┤                                     ● Moxa AIG-101-T
         │                                       (Enterprise, LTE, Azure/AWS)
         │                                       ❌ No WiFi, No BLE
         │
Rp 5.0M  ┤
         │
         │
Rp 3.5M  ┤         ● USR-N720 ─────────────────── ❌ No WiFi, No BLE
         │
Rp 3.45M ┤         ▲ ICP DAS tGW-725 ─────────── ❌ No MQTT! (TCP/RTU only)
         │                                       PoE, but no cloud capability
Rp 3.37M ┤         ● BLIIoT BL100 ────────────── 4G, ❌ No BLE
         │
Rp 2.8M  ┤ ════════ ★ SURIOTA ════════════════ WiFi+BLE+MQTT+RTC+9LED
         │         ↑ BEST VALUE ↑                ✅ SATU-SATUNYA dgn BLE
         │
Rp 1.82M ┤ ● USR-N540 ────────────────────────── Murah, 4-port
         │                                       ❌ No WiFi, No BLE, No RTC
         │
         └─────────────────────────────────────────────────────────────
               FITUR IoT  ─────────────────────────────────────────→

Keterangan:
● = Modbus to MQTT Gateway (IoT ready)
▲ = Protocol Converter saja (Modbus TCP ↔ RTU, bukan IoT gateway)
★ = SURIOTA (Best Value - WiFi + BLE + MQTT + RTC + 9 LED)
```

### Kesimpulan Perbandingan

**SURIOTA adalah SATU-SATUNYA Modbus-to-MQTT gateway di pasar Indonesia yang memiliki:**

1. ✅ **WiFi Built-in** dengan Auto Failover
2. ✅ **BLE Mobile Configuration** (setup via smartphone)
3. ✅ **RTC dengan Battery Backup** (DS3231 + CR1220)
4. ✅ **9 LED Status Indicators** (monitoring lengkap)
5. ✅ **ESD Protection** pada RS-485
6. ✅ **Harga Kompetitif** di mid-range (Rp 2.8M)
7. ✅ **Local Support** dalam Bahasa Indonesia

---

# Pricing Strategy

## Strategi Penetapan Harga

### Competitive Positioning

| Competitor   | Harga        | vs SURIOTA | SURIOTA Advantage                           |
| ------------ | ------------ | ---------- | ------------------------------------------- |
| USR-N540     | Rp 1,820,000 | +54%       | WiFi, BLE, ESD, RTC, 9LED, Failover         |
| USR-N720     | Rp 3,500,000 | -20%       | WiFi, BLE, RTC, Failover, Local Support     |
| BLIIoT BL100 | Rp 3,373,000 | -17%       | WiFi standard, BLE, RTC, Simpler setup      |
| Moxa AIG-101 | Rp 8,956,000 | -69%       | WiFi, BLE, RTC, Local Support, MUCH cheaper |

### Rekomendasi Harga

| Model                  | Harga Jual       | Fully Loaded Cost | Gross Profit | **Margin** |
| ---------------------- | ---------------- | ----------------- | ------------ | ---------- |
| **SRT-MGATE-1210**     | **Rp 2,800,000** | Rp 1,450,000      | Rp 1,350,000 | **48%**    |
| **SRT-MGATE-1210-POE** | **Rp 3,500,000** | Rp 1,650,000      | Rp 1,850,000 | **53%**    |

### Justifikasi Harga

1. **20% lebih murah dari USR-N720** (Rp 3.5M) - dengan fitur WiFi + BLE + RTC yang USR tidak punya
2. **17% lebih murah dari BLIIoT** (Rp 3.37M) - dengan WiFi standard + BLE + RTC + simpler setup
3. **69% lebih murah dari Moxa AIG-101** (Rp 8.96M) - dengan BLE config + RTC yang Moxa tidak punya
4. **Premium vs USR-N540** (+54%) - justified karena WiFi, BLE, ESD protection, RTC, 9 LED, auto-failover

---

### Volume Discount Structure

#### End Customer

| Quantity  | Discount | Standard     | PoE          |
| --------- | -------- | ------------ | ------------ |
| 1-4 pcs   | 0%       | Rp 2,800,000 | Rp 3,500,000 |
| 5-9 pcs   | 5%       | Rp 2,660,000 | Rp 3,325,000 |
| 10-24 pcs | 10%      | Rp 2,520,000 | Rp 3,150,000 |
| 25-49 pcs | 15%      | Rp 2,380,000 | Rp 2,975,000 |
| 50-99 pcs | 18%      | Rp 2,296,000 | Rp 2,870,000 |
| 100+ pcs  | 20%      | Rp 2,240,000 | Rp 2,800,000 |

#### Distributor/Reseller

| Tier   | Discount | Min Order | Standard     | PoE          | Their Margin |
| ------ | -------- | --------- | ------------ | ------------ | ------------ |
| Bronze | 25%      | 25 pcs    | Rp 2,100,000 | Rp 2,625,000 | 25%          |
| Silver | 30%      | 50 pcs    | Rp 1,960,000 | Rp 2,450,000 | 30%          |
| Gold   | 35%      | 100 pcs   | Rp 1,820,000 | Rp 2,275,000 | 35%          |

---

# Unique Selling Proposition (USP)

## Nilai Jual Unik SURIOTA

### Tagline

> **"Satu-satunya Modbus-to-MQTT Gateway dengan WiFi + BLE di Indonesia"**

> **"Setup 5 Menit via Smartphone, Langsung Connect ke Cloud"**

---

### 5 USP Utama

#### 1. BLE Mobile Configuration (EKSKLUSIF)

**SURIOTA adalah SATU-SATUNYA Modbus-to-MQTT gateway yang bisa dikonfigurasi via smartphone!**

| Feature               | Benefit                        |
| --------------------- | ------------------------------ |
| Setup via smartphone  | Tidak perlu laptop ke lapangan |
| 5 menit configuration | Hemat waktu instalasi          |
| Bluetooth Scan        | Instant device pairing         |
| App Android/iOS       | User-friendly interface        |

**Talking Point:**

> "Semua kompetitor - USR, BLIIoT, Moxa - harus bawa laptop ke site untuk config. SURIOTA cukup pakai HP - 5 menit selesai!"

---

#### 2. WiFi dengan Auto Failover (EKSKLUSIF)

**SURIOTA adalah SATU-SATUNYA yang punya WiFi built-in dengan auto-failover!**

| Connection   | Role                               |
| ------------ | ---------------------------------- |
| **Ethernet** | Primary - koneksi utama stabil     |
| **WiFi**     | Backup - auto-switch jika ETH down |
| **BLE**      | Configuration - setup on-site      |

**Auto Failover Mechanism:**

```
Ethernet OK? ──Yes──→ Use Ethernet
      │
      No
      ↓
WiFi OK? ──Yes──→ Use WiFi (Automatic!)
      │
      No
      ↓
Alert to Dashboard
```

**Talking Point:**

> "USR, BLIIoT, Moxa - semuanya tidak ada WiFi atau hanya cellular. SURIOTA punya WiFi backup - kalau kabel putus, data tetap jalan!"

---

#### 3. MQTT Native ke Semua Cloud Platform

| Platform         | Support         |
| ---------------- | --------------- |
| AWS IoT Core     | Direct connect  |
| Azure IoT Hub    | Direct connect  |
| Google Cloud IoT | Direct connect  |
| ThingsBoard      | Direct connect  |
| Grafana          | Via MQTT plugin |
| Custom Platform  | Standard MQTT   |

**Data Format:**

```json
{
  "device_id": "SRT-001",
  "timestamp": "2025-11-29T12:00:00Z",
  "data": {
    "temperature": 25.5,
    "humidity": 60,
    "power": 1250
  }
}
```

**Talking Point:**

> "Data langsung dalam format JSON, siap consume oleh dashboard atau database. Sama seperti Moxa AIG-101 yang harganya Rp 9 juta, tapi kami cuma Rp 2.8 juta!"

---

#### 4. Industrial Grade Build Quality

| Specification     | SURIOTA             | USR-N540       | Waveshare |
| ----------------- | ------------------- | -------------- | --------- |
| Temperature       | -40°C to +75°C      | -40°C to +85°C | 0-70°C    |
| RS-485 Protection | **ESD Protection**  | None           | None      |
| RTC + Battery     | **DS3231 + CR1220** | None           | None      |
| LED Indicators    | **9 LEDs**          | Basic          | Basic     |
| Enclosure         | Plastic+            | Plastic        | Plastic   |
| Mounting          | DIN Rail + Wall     | DIN Rail       | Standard  |

**Talking Point:**

> "Produk kami industrial grade dengan ESD protection, RTC battery backup untuk timestamp akurat, dan 9 LED indicator untuk monitoring. USR-N540 yang murah tidak ada fitur ini!"

---

#### 5. Local Indonesia Support

| Service            | Detail               |
| ------------------ | -------------------- |
| Technical Support  | Bahasa Indonesia     |
| Response Time      | < 24 jam             |
| Warranty           | 1 tahun              |
| Training           | Available on request |
| Custom Development | Available            |

**Talking Point:**

> "Kalau ada masalah, langsung hubungi tim kami di Indonesia. Tidak perlu email ke China dan tunggu berhari-hari seperti USR atau BLIIoT."

---

# Sales & Marketing Guide

## Panduan Teknis untuk Tim Sales

### Quick Comparison Card

```
┌─────────────────────────────────────────────────────────────────┐
│           SURIOTA vs KOMPETITOR (Modbus to MQTT)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  vs USR-N720 (Rp 3.5M)          vs USR-N540 (Rp 1.82M)         │
│  ├─ SURIOTA: Rp 2.8M (-20%)     ├─ SURIOTA: +54% tapi punya:   │
│  ├─ USR: No WiFi ❌              │   ✅ WiFi + Auto Failover    │
│  ├─ USR: No BLE ❌               │   ✅ BLE Mobile Config       │
│  └─ SURIOTA: WiFi+BLE ✅         │   ✅ RTC + 9 LED Indicators  │
│                                  └─ Worth the premium!          │
│                                                                 │
│  vs BLIIoT BL100 (Rp 3.37M)     vs Moxa AIG-101 (Rp 8.96M)     │
│  ├─ SURIOTA: Rp 2.8M (-17%)     ├─ SURIOTA: Rp 2.8M (-69%)     │
│  ├─ BLIIoT: No BLE ❌            ├─ Moxa: No WiFi ❌             │
│  ├─ BLIIoT: Setup kompleks      ├─ Moxa: No BLE ❌              │
│  └─ SURIOTA: Simple+BLE ✅       └─ SURIOTA: 3x lebih murah! ✅  │
│                                                                 │
│  🏆 KESIMPULAN: SURIOTA = Best Value WiFi+BLE+MQTT+RTC+9LED    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### Sales Script Templates

#### Scenario 1: Customer Considering USR Products

**Customer:** "Saya lihat USR-N720 atau N540 di Tokopedia..."

**Response:**

> "USR memang brand yang cukup dikenal untuk Modbus gateway. Tapi coba perhatikan:
>
> **USR-N720** (Rp 3.5M):
>
> - Tidak ada WiFi - harus selalu pakai kabel
> - Tidak ada BLE - config harus bawa laptop
> - Tidak ada RTC battery backup
>
> **USR-N540** (Rp 1.82M):
>
> - Lebih murah, tapi tidak ada ESD protection - berisiko di environment pabrik
> - Tidak ada WiFi dan BLE juga
> - Tidak ada RTC untuk timestamp akurat
>
> **SURIOTA** Rp 2.8M sudah include:
>
> - WiFi dengan auto-failover - kalau kabel putus, data tetap jalan
> - BLE config via smartphone - 5 menit selesai
> - ESD protection pada RS-485 - aman untuk industrial environment
> - RTC dengan battery backup - timestamp selalu akurat
> - 9 LED indicator - monitoring status lengkap
> - Support lokal Indonesia
>
> Jadi value-nya jauh lebih baik dibanding USR!"

---

#### Scenario 2: Customer Considering Moxa

**Customer:** "Kami biasa pakai Moxa untuk industrial equipment..."

**Response:**

> "Moxa memang brand premium. Tapi untuk Modbus-to-MQTT gateway, mereka punya AIG-101 yang harganya **Rp 9 juta** di Tokopedia!
>
> Moxa AIG-101:
>
> - Tidak ada WiFi (hanya LTE cellular)
> - Tidak ada BLE - config via web browser
> - Harga 3x lipat dari SURIOTA
>
> SURIOTA Rp 2.8 juta sudah punya:
>
> - WiFi built-in dengan auto-failover
> - BLE config via smartphone
> - MQTT ke AWS/Azure/ThingsBoard sama seperti Moxa
>
> Hemat **Rp 6 juta per unit** - bayangkan kalau butuh 10 unit, saving Rp 60 juta!"

---

#### Scenario 3: Customer Considering BLIIoT

**Customer:** "Saya lihat BLIIoT BL100/BL101 di Microthings..."

**Response:**

> "BLIIoT memang gateway yang capable, harganya sekitar Rp 3.3 juta.
>
> Tapi BLIIoT BL100:
>
> - Tidak ada BLE - setiap config harus via software PC
> - Setup lebih kompleks karena Linux-based
> - Hanya 1 port RS-485
> - Tidak ada RTC dengan battery backup
>
> SURIOTA Rp 2.8 juta lebih simple:
>
> - BLE config via HP - technician tidak perlu bawa laptop
> - Setup lebih mudah dengan mobile app
> - 2 port RS-485 dengan ESD protection
> - RTC battery backup untuk timestamp akurat
> - 9 LED indicator untuk monitoring
>
> Plus harga 17% lebih murah!"

---

#### Scenario 4: Budget Customer Asking for Cheapest Option

**Customer:** "Budget terbatas, yang paling murah apa?"

**Response:**

> "Yang paling murah adalah USR-N540 sekitar Rp 1.8 juta.
>
> Tapi perlu dipertimbangkan TCO (Total Cost of Ownership):
>
> **USR-N540 Hidden Costs:**
>
> - Tidak ada ESD protection - risiko kerusakan di environment pabrik
> - Tidak ada WiFi backup - kalau kabel putus, data loss
> - Config harus bawa laptop setiap kali - biaya technician lebih tinggi
> - Tidak ada RTC - timestamp tidak akurat saat restart
>
> **SURIOTA Investment:**
>
> - Rp 2.8M upfront, tapi:
> - ESD protection = lebih awet, less maintenance
> - WiFi backup = less downtime
> - BLE config = technician lebih efisien
> - RTC battery backup = timestamp selalu akurat
> - 9 LED = troubleshooting lebih cepat
>
> Selisih Rp 1 juta, tapi peace of mind dan reliability jauh lebih baik."

---

#### Scenario 5: Customer Considering ICP DAS

**Customer:** "Saya sudah pakai ICP DAS tGW-725 untuk Modbus gateway..."

**Response:**

> "ICP DAS memang brand Taiwan yang bagus untuk industrial automation. Tapi tGW-725 itu adalah **protocol converter**, bukan IoT gateway.
>
> **ICP DAS tGW-725** (Rp 3.45M):
>
> - Fungsinya: konversi Modbus TCP ↔ Modbus RTU saja
> - **Tidak ada MQTT** - tidak bisa langsung kirim ke cloud
> - Tidak ada WiFi dan BLE
> - Untuk IoT, perlu tambah software/hardware lain
>
> Kalau kebutuhan Bapak/Ibu adalah **monitoring ke cloud** (AWS, Azure, ThingsBoard), ICP DAS tGW-725 tidak bisa langsung. Perlu tambah server atau gateway lagi.
>
> **SURIOTA** Rp 2.8 juta sudah **all-in-one**:
>
> - Modbus RTU/TCP langsung ke MQTT
> - Data langsung ke cloud dalam format JSON
> - Plus WiFi backup dan BLE config
>
> Jadi untuk IoT use case, SURIOTA lebih hemat dan simple dibanding ICP DAS + tambahan hardware."

---

#### Scenario 6: Customer Asking About Reliability & Warranty

**Customer:** "Produk lokal biasanya kurang reliable. Bagaimana dengan garansi?"

**Response:**

> "Pertanyaan yang sangat valid. Mari saya jelaskan:
>
> **Komponen yang Kami Gunakan:**
>
> - MCU: ESP32-S3 dari Espressif (brand international)
> - Ethernet: W5500 dari Wiznet (Korea)
> - RS-485 Transceiver: MAX485 dengan ESD protection (industrial grade)
> - RTC: DS3231 dengan battery backup CR1220
>
> **Quality Assurance:**
>
> - Setiap unit di-test 100% sebelum kirim
> - Burn-in test 24 jam untuk reliability
> - 9 LED indicator untuk easy diagnostics
> - Firmware sudah di-deploy di beberapa pilot project
>
> **Garansi:**
>
> - 1 tahun garansi penuh
> - Response time < 24 jam untuk technical support
> - Replacement unit available jika ada defect
>
> **Advantage vs Import:**
>
> - Kalau Moxa rusak, harus kirim ke Taiwan - bisa berminggu-minggu
> - SURIOTA rusak, langsung kami ganti dari Indonesia - hitungan hari
>
> Untuk produk baru, kami sangat serius menjaga kualitas karena reputasi adalah segalanya."

---

#### Scenario 7: Customer Needs Remote Monitoring (No Local Network)

**Customer:** "Lokasi kami di remote area, tidak ada WiFi atau Ethernet. Bagaimana?"

**Response:**

> "Untuk lokasi benar-benar remote tanpa infrastruktur network, memang butuh solusi cellular.
>
> **Opsi untuk Remote Area:**
>
> 1. **BLIIoT BL100** (Rp 3.37M) - Built-in 4G, tapi tidak ada BLE config
> 2. **Moxa AIG-101** (Rp 8.96M) - LTE Cat.1, tapi sangat mahal
>
> **Alternatif dengan SURIOTA:**
>
> - SURIOTA + 4G Router portable (Rp 500K-1M)
> - Total: Rp 3.3-3.8M - masih lebih murah dari BLIIoT
> - Keuntungan: BLE config tetap ada, WiFi backup tetap ada
>
> **Tapi pertanyaan dulu:**
>
> - Apakah benar-benar tidak ada network sama sekali?
> - Mayoritas factory/warehouse sudah punya WiFi minimal
> - SURIOTA bisa connect ke WiFi yang sudah ada
>
> Kalau memang 100% tidak ada network, saya rekomendasikan BLIIoT BL100. Tapi kalau ada WiFi meski lemah, SURIOTA lebih cost-effective."

---

#### Scenario 8: Customer Already Using SCADA/HMI System

**Customer:** "Kami sudah pakai SCADA, data sudah masuk ke HMI. Kenapa butuh gateway IoT?"

**Response:**

> "Pertanyaan bagus! SCADA dan IoT gateway punya fungsi berbeda:
>
> **SCADA/HMI (Local):**
>
> - Data hanya bisa dilihat di control room
> - Operator harus on-site untuk monitoring
> - Tidak bisa akses dari luar pabrik
>
> **IoT Gateway + Cloud (Remote):**
>
> - Data bisa diakses dari mana saja via internet
> - Manager bisa monitor dari HP/laptop
> - Historical data tersimpan di cloud untuk analisis
> - Alert/notification ke WhatsApp/Email
>
> **SURIOTA TIDAK menggantikan SCADA, tapi MELENGKAPI:**
>
> ```
> Sensor → RS-485 → SCADA (local monitoring)
>                 ↘
>                   SURIOTA → MQTT → Cloud (remote monitoring)
> ```
>
> - SCADA tetap jalan untuk real-time control
> - SURIOTA mengirim data ke cloud untuk remote access
> - Dua sistem bisa jalan paralel
>
> Jadi Bapak/Ibu bisa monitor produksi dari rumah atau saat traveling, tanpa harus ke control room."

---

#### Scenario 9: Customer Asking About Cloud Platform Integration

**Customer:** "Kami sudah pakai ThingsBoard/AWS/Azure. Bisa integrate?"

**Response:**

> "Bisa! SURIOTA memang didesain untuk cloud integration:
>
> **Platform yang Sudah Tested:**
>
> | Platform      | Status        | Notes                 |
> | ------------- | ------------- | --------------------- |
> | ThingsBoard   | ✅ Tested     | Direct MQTT connect   |
> | AWS IoT Core  | ✅ Compatible | Standard MQTT + TLS   |
> | Azure IoT Hub | ✅ Compatible | MQTT with SAS token   |
> | Google Cloud  | ✅ Compatible | Standard MQTT         |
> | Grafana Cloud | ✅ Compatible | Via MQTT plugin       |
> | Custom Broker | ✅ Compatible | Mosquitto, EMQX, etc. |
>
> **Data Format:**
>
> - Output dalam format JSON standard
> - Customizable topic naming
> - QoS 0, 1, atau 2 sesuai kebutuhan
>
> **Setup Process:**
>
> 1. Connect SURIOTA ke network (WiFi/Ethernet)
> 2. Buka app mobile, scan BLE
> 3. Input MQTT broker address + credentials
> 4. Test connection - data langsung mengalir!
>
> Kalau sudah ada ThingsBoard running, dalam 10 menit data Modbus sudah bisa muncul di dashboard."

---

#### Scenario 10: Customer Comparing with DIY/Custom Solution

**Customer:** "Kami bisa buat sendiri pakai Raspberry Pi atau ESP32, lebih murah..."

**Response:**

> "Benar, secara hardware memang bisa lebih murah. Tapi mari kita hitung Total Cost of Ownership:
>
> **DIY Solution Costs:**
>
> | Item                    | Cost          |
> | ----------------------- | ------------- |
> | ESP32/Raspberry Pi      | Rp 200-500K   |
> | RS-485 module           | Rp 50-100K    |
> | Power supply            | Rp 100K       |
> | Enclosure               | Rp 100-200K   |
> | **Development time**    | **40-80 jam** |
> | **Testing & debugging** | **20-40 jam** |
>
> **Hidden Costs DIY:**
>
> - Firmware development: Modbus library, MQTT client, WiFi manager
> - Edge cases: reconnection logic, data buffering, error handling
> - Tidak ada ESD protection - risiko kerusakan di industrial environment
> - Tidak ada RTC battery backup - timestamp tidak akurat
> - Tidak ada mobile app untuk config
> - Maintenance jadi tanggung jawab internal
>
> **SURIOTA (Rp 2.8M):**
>
> - Plug & play, ready to deploy
> - Firmware sudah mature dan tested
> - ESD protection + RTC battery backup
> - 9 LED indicator untuk troubleshooting
> - BLE mobile config - deploy dalam 5 menit
> - Support dari kami kalau ada masalah
>
> **Pertimbangan:**
>
> - Kalau engineer time Rp 100-200K/jam, development 60 jam = Rp 6-12 juta
> - SURIOTA Rp 2.8M sudah all-in, langsung pakai
>
> DIY cocok untuk prototype atau hobi. Untuk production deployment, solusi proven seperti SURIOTA lebih cost-effective dan reliable."

---

#### Scenario 11: Customer Concerned About Security / Cybersecurity

**Customer:** "Data produksi kami sensitif. Bagaimana keamanan datanya?"

**Response:**

> "Keamanan adalah prioritas utama kami. Berikut security features SURIOTA:
>
> **Network Security:**
>
> | Layer          | Protection                             |
> | -------------- | -------------------------------------- |
> | WiFi           | WPA3-PSK (latest standard)             |
> | MQTT           | TLS 1.2/1.3 encryption                 |
> | Authentication | Username/password + Client certificate |
> | Firmware       | Secure boot, signed updates            |
>
> **Data Protection:**
>
> - Data in transit: Encrypted via TLS
> - No data stored locally (pass-through to cloud)
> - MQTT broker credentials encrypted in device
>
> **Network Isolation Options:**
>
> ```
> Option 1: Direct to Cloud (via internet)
> Gateway → Internet → Cloud Platform
>
> Option 2: Private Network (more secure)
> Gateway → Company VPN → Private MQTT Broker
> ```
>
> **Best Practices yang Kami Rekomendasikan:**
>
> - Gunakan dedicated VLAN untuk IoT devices
> - Enable TLS untuk semua MQTT connections
> - Regular firmware update untuk security patches
> - Gunakan strong passwords + certificate auth
>
> Kalau ada compliance requirement tertentu (ISO 27001, dll), kami bisa bantu review arsitektur yang sesuai."

---

#### Scenario 12: Customer with Multiple Sites / Scaling

**Customer:** "Kami punya 20 lokasi pabrik di seluruh Indonesia. Bisa manage semuanya?"

**Response:**

> "Sangat bisa! SURIOTA didesain untuk deployment skala besar:
>
> **Multi-Site Architecture:**
>
> ```
> Site Jakarta ──┐
> Site Surabaya ─┼──→ Central MQTT Broker ──→ Dashboard
> Site Medan ────┤                            (ThingsBoard/Grafana)
> Site Makassar ─┘
> ```
>
> **Centralized Management:**
>
> | Feature         | Capability                                  |
> | --------------- | ------------------------------------------- |
> | Device Naming   | Unique ID per site (e.g., JKT-001, SBY-001) |
> | Topic Structure | `{site}/{device}/{sensor}`                  |
> | Dashboard       | Single view untuk semua site                |
> | Alerting        | Per-site atau global threshold              |
>
> **Scaling Benefits:**
>
> - Setiap gateway independent - 1 down tidak affect yang lain
> - Cloud platform handle aggregation
> - Add new site = plug new gateway, auto-register
>
> **Volume Pricing untuk 20+ Units:**
>
> | Quantity  | Discount | Price/Unit   |
> | --------- | -------- | ------------ |
> | 20-24 pcs | 15%      | Rp 2,380,000 |
> | 25-49 pcs | 18%      | Rp 2,296,000 |
> | 50+ pcs   | 20%      | Rp 2,240,000 |
>
> **Untuk 20 unit:**
>
> - List price: 20 × Rp 2.8M = Rp 56M
> - With 15% discount: **Rp 47.6M** (hemat Rp 8.4M)
>
> Kami juga bisa bantu setup central dashboard untuk monitoring semua site sekaligus."

---

#### Scenario 13: Customer Wants Proof of Concept / Trial

**Customer:** "Bisa pinjam dulu untuk testing sebelum kami commit beli banyak?"

**Response:**

> "Tentu! Kami sangat mendukung PoC karena kami yakin dengan produk kami:
>
> **PoC Options:**
>
> | Option                  | Terms                       | Duration   |
> | ----------------------- | --------------------------- | ---------- |
> | **Loan Unit**           | Deposit 50%, refundable     | 2-4 minggu |
> | **Evaluation Purchase** | Beli 1-2 unit, harga normal | Permanent  |
> | **On-site Demo**        | Tim kami datang demo        | 1-2 jam    |
>
> **PoC Process yang Kami Rekomendasikan:**
>
> 1. **Kick-off Meeting** (1 jam)
>
>    - Diskusi requirement dan use case
>    - Tentukan success criteria
>
> 2. **Setup & Configuration** (2-4 jam)
>
>    - Kami bantu install dan config
>    - Connect ke Modbus device Anda
>    - Setup cloud dashboard
>
> 3. **Evaluation Period** (1-2 minggu)
>
>    - Anda test di real environment
>    - Kami standby untuk support
>
> 4. **Review & Decision**
>    - Evaluasi hasil PoC
>    - Diskusi rollout plan jika sukses
>
> **Success Criteria Typical:**
>
> - ✅ Data Modbus terbaca dengan benar
> - ✅ Data sampai ke cloud dashboard
> - ✅ WiFi failover bekerja
> - ✅ BLE config mudah digunakan
>
> Untuk project besar (10+ unit), PoC sangat kami rekomendasikan supaya Bapak/Ibu confident dengan solusinya."

---

#### Scenario 14: Customer Asking About Lead Time & Stock

**Customer:** "Kalau order sekarang, kapan ready? Kami butuh cepat untuk project."

**Response:**

> "Lead time tergantung quantity dan stock availability:
>
> **Current Stock Status:**
>
> | Model              | Ready Stock     | Lead Time if PO |
> | ------------------ | --------------- | --------------- |
> | SRT-MGATE-1210     | [check current] | 2-3 minggu      |
> | SRT-MGATE-1210-POE | [check current] | 3-4 minggu      |
>
> **Standard Lead Time:**
>
> | Quantity  | Lead Time               | Notes                 |
> | --------- | ----------------------- | --------------------- |
> | 1-5 pcs   | From stock / 1-2 minggu | Biasanya ready        |
> | 6-20 pcs  | 2-3 minggu              | Production batch      |
> | 21-50 pcs | 3-4 minggu              | Larger batch          |
> | 50+ pcs   | 4-6 minggu              | Custom production run |
>
> **Urgent Order Options:**
>
> - **Express fee** +10%: Prioritas produksi, -1 minggu
> - **Partial delivery**: Kirim yang ready dulu, sisanya menyusul
>
> **Untuk Project dengan Timeline Ketat:**
>
> 1. Berikan PO / LOI secepatnya
> 2. Kami lock production slot
> 3. Pembayaran bisa bertahap (DP 50%)
>
> **Tips:**
>
> - Order 2-3 minggu sebelum installation date
> - Untuk project besar, inform kami 1-2 bulan sebelumnya
>
> Boleh info timeline project-nya kapan? Biar kami bisa arrange production schedule."

---

#### Scenario 15: Customer Asking About Certifications

**Customer:** "Apakah sudah ada sertifikasi CE/FCC? Kami butuh untuk compliance."

**Response:**

> "Pertanyaan penting untuk industrial deployment. Berikut status sertifikasi kami:
>
> **Current Certification Status:**
>
> | Certification | Status             | Notes                       |
> | ------------- | ------------------ | --------------------------- |
> | **CE Mark**   | ✅ Planned Q1 2026 | EMC + Safety                |
> | **FCC**       | ✅ Planned Q1 2026 | Part 15 Class B             |
> | **RoHS**      | ✅ Compliant       | Lead-free components        |
> | **TKDN**      | 🔄 In Process      | Local content certification |
>
> **Component Certifications:**
>
> - ESP32-S3 module: FCC, CE, IC certified
> - W5500 Ethernet: Industrial grade
> - Power supply: UL/CE certified
>
> **Untuk Customer yang Butuh Segera:**
>
> - Kami bisa provide Declaration of Conformity (DoC)
> - Component-level certificates available
> - Test reports dari internal QC
>
> **Timeline Sertifikasi:**
>
> ```
> Q4 2025: Submit for CE/FCC testing
> Q1 2026: Certification complete
> ```
>
> **Alternatif untuk Project Urgent:**
>
> - Gunakan sebagai 'pilot project' atau 'internal testing'
> - Full certification ready untuk production rollout
>
> Apakah ada specific compliance requirement yang harus dipenuhi? Kami bisa review dan advise."

---

#### Scenario 16: Customer Asking for Bulk / Project Pricing

**Customer:** "Kami ada project butuh 50 unit. Bisa dapat harga special?"

**Response:**

> "Untuk volume 50 unit, pasti ada harga special! Mari kita hitung:
>
> **Standard Volume Discount:**
>
> | Quantity      | Discount | Standard         | PoE              |
> | ------------- | -------- | ---------------- | ---------------- |
> | 1-4 pcs       | 0%       | Rp 2,800,000     | Rp 3,500,000     |
> | 5-9 pcs       | 5%       | Rp 2,660,000     | Rp 3,325,000     |
> | 10-24 pcs     | 10%      | Rp 2,520,000     | Rp 3,150,000     |
> | 25-49 pcs     | 15%      | Rp 2,380,000     | Rp 2,975,000     |
> | **50-99 pcs** | **18%**  | **Rp 2,296,000** | **Rp 2,870,000** |
> | 100+ pcs      | 20%      | Rp 2,240,000     | Rp 2,800,000     |
>
> **Kalkulasi untuk 50 Unit Standard:**
>
> | Item              | Amount                             |
> | ----------------- | ---------------------------------- |
> | List Price        | 50 × Rp 2,800,000 = Rp 140,000,000 |
> | Discount 18%      | - Rp 25,200,000                    |
> | **Project Price** | **Rp 114,800,000**                 |
> | Per Unit          | **Rp 2,296,000**                   |
>
> **Additional Project Benefits:**
>
> - ✅ Dedicated project manager
> - ✅ On-site installation support (Jakarta area)
> - ✅ Training untuk tim teknis (1 sesi)
> - ✅ Extended warranty discussion available
> - ✅ Pembayaran bertahap (nego)
>
> **Payment Terms untuk Project:**
>
> | Milestone             | Payment |
> | --------------------- | ------- |
> | PO Confirmation       | 30% DP  |
> | Production Complete   | 50%     |
> | Delivery & Acceptance | 20%     |
>
> **Next Steps:**
>
> 1. Finalisasi quantity dan model mix
> 2. Kami siapkan quotation formal
> 3. Review terms dan timeline
> 4. PO dan kick-off project
>
> Boleh info lebih detail tentang project-nya? Lokasi, timeline, dan apakah butuh instalasi support?"

---

### Objection Handling

| Objection                   | Response                                                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "USR lebih murah"           | "USR-N540 memang murah, tapi tidak ada ESD protection, RTC, dan WiFi. Untuk industrial deployment yang reliable, investasi sedikit lebih di SURIOTA akan menghemat biaya maintenance dan downtime jangka panjang." |
| "Moxa lebih trusted"        | "Moxa memang brand besar, tapi AIG-101 harganya Rp 9 juta dan tidak ada BLE/RTC. SURIOTA 69% lebih murah dengan fitur BLE + RTC + 9 LED yang Moxa tidak punya."                                                    |
| "ICP DAS lebih established" | "ICP DAS tGW-725 bagus untuk Modbus TCP/RTU conversion, tapi tidak ada MQTT. Untuk IoT ke cloud, perlu tambah software lagi. SURIOTA langsung all-in-one ke MQTT dengan harga lebih murah."                        |
| "Brand tidak terkenal"      | "Kami produksi lokal dengan komponen kualitas sama (ESP32-S3, MAX485, DS3231). Keuntungannya: support Indonesia, response cepat, dan bisa custom development kalau perlu."                                         |
| "Butuh 4G/LTE"              | "Untuk remote location tanpa WiFi/Ethernet, memang butuh 4G. Tapi mayoritas factory/building sudah ada network. SURIOTA cocok untuk 80% use case dengan harga lebih terjangkau."                                   |

---

# Brand Awareness Strategy

## Strategi Membangun Brand Awareness

### Phase 1: Foundation (Month 1-3)

#### Digital Presence

| Channel      | Action                                         | Target                                       |
| ------------ | ---------------------------------------------- | -------------------------------------------- |
| **Website**  | Landing page dengan specs, pricing, comparison | SEO rank for "Modbus MQTT Gateway Indonesia" |
| **LinkedIn** | Company page + regular content                 | 500 followers                                |
| **YouTube**  | Tutorial videos, demo, comparison              | 5 videos, 1000 views                         |
| **GitHub**   | Sample code, documentation                     | Developer Team                               |

#### Content Strategy

| Content Type   | Frequency  | Topics                                            |
| -------------- | ---------- | ------------------------------------------------- |
| Blog/Article   | 2x/month   | "Modbus to MQTT tutorial", "Industrial IoT guide" |
| Video Tutorial | 1x/month   | "5-minute BLE setup guide", "WiFi failover demo"  |
| Case Study     | 1x/quarter | Customer success stories                          |
| Comparison     | 1x         | "SURIOTA vs USR vs Moxa vs BLIIoT"                |

---

### Phase 2: Credibility (Month 4-6)

#### Industry Engagement

| Activity          | Target                                          |
| ----------------- | ----------------------------------------------- |
| **Webinar**       | "Introduction to Industrial IoT" - 50 attendees |
| **Trade Show**    | Manufacturing Indonesia / IoT Summit            |
| **Partnership**   | System integrator partnerships (3-5 partners)   |
| **Certification** | CE marking completion                           |

---

### Key Marketing Messages by Audience

#### For Engineers/Technical

> "Modbus RTU/TCP to MQTT gateway dengan 2x RS-485 + ESD protection, RTC battery backup, 9 LED indicator, WiFi auto-failover, dan BLE config. Setup via smartphone dalam 5 menit."

#### For Procurement/Finance

> "69% lebih hemat dari Moxa, 20% lebih hemat dari USR, dengan fitur WiFi dan BLE yang kompetitor tidak punya. Produksi lokal, garansi 1 tahun."

#### For Management/Decision Makers

> "Solusi Industrial IoT terlengkap buatan Indonesia. Mengurangi ketergantungan import, dengan kualitas setara produk international dan support lokal."

---

# Financial Projections

## Proyeksi Keuangan

### Asumsi

| Parameter              | Value                         |
| ---------------------- | ----------------------------- |
| Target Sales (2 tahun) | 200 units                     |
| Mix                    | 120 Standard : 80 PoE (60:40) |
| Average Selling Price  | Rp 3,080,000 (weighted)       |

### Revenue Projection

| Item             | Standard (120 pcs) | PoE (80 pcs)   | **Total**          |
| ---------------- | ------------------ | -------------- | ------------------ |
| Unit Price       | Rp 2,800,000       | Rp 3,500,000   | -                  |
| **Revenue**      | Rp 336,000,000     | Rp 280,000,000 | **Rp 616,000,000** |
| COGS             | Rp 162,000,000     | Rp 124,000,000 | Rp 286,000,000     |
| R&D (amortized)  | Rp 12,000,000      | Rp 8,000,000   | Rp 20,000,000      |
| **Gross Profit** | Rp 162,000,000     | Rp 148,000,000 | **Rp 310,000,000** |

### Key Metrics

| Metric               | Value                     |
| -------------------- | ------------------------- |
| **Total Revenue**    | Rp 616,000,000 (~$38,500) |
| **Total Cost**       | Rp 306,000,000 (~$19,125) |
| **Gross Profit**     | Rp 310,000,000 (~$19,375) |
| **Gross Margin**     | **50.3%**                 |
| **Break-even Point** | 134 units                 |
| **ROI**              | **101%**                  |

---

# Appendix

## A. Complete URL Reference

### Official Supplier Websites

| Competitor     | Official Website                                               | Product Page                                                                                                                       |
| -------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **USR-IOT**    | [usriot.com](https://www.usriot.com)                           | [N720-ETH](https://shop.usriot.com/industrial-serial-to-ethernet-converters/)                                                      |
| **USR-IOT**    | [pusr.com](https://www.pusr.com)                               | [N540](https://www.pusr.com/products/serial-to-ethernet.html)                                                                      |
| **BLIIoT**     | [bliiot.com](https://bliiot.com)                               | [BL101 Product](https://bliiot.com/products/modbus-to-mqtt-gateway-bl101)                                                          |
| **ICP DAS**    | [icpdas.com](https://www.icpdas.com)                           | [tGW-725](https://www.icpdas.com/en/product/tGW-725)                                                                               |
| **Moxa**       | [moxa.com](https://www.moxa.com)                               | [AIG-101 Series](https://www.moxa.com/en/products/industrial-computing/iiot-gateways/ready-to-deploy-iiot-gateways/aig-101-series) |
| **Moxa Store** | [moxastore.express-inc.com](https://moxastore.express-inc.com) | [AIG-101-T](https://moxastore.express-inc.com/AIG_101_T_p/aig-101-t.htm)                                                           |

### Tokopedia Product Links

| Product         | Price        | Tokopedia URL                                                                                                                                                               |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USR-N720-ETH    | Rp 3,500,000 | [Link](https://www.tokopedia.com/elektromurah/iot-gateway-rs485-to-ethernet-support-1000-data-points-modbus-gateway-multi-host-modbus-polling-n720-eth-1730980558396491220) |
| USR-N540 H7-4   | Rp 1,820,000 | [Link](https://www.tokopedia.com/find/modbus-mqtt)                                                                                                                          |
| BLIIoT BL100    | Rp 3,373,000 | [Link](https://www.tokopedia.com/microthings/modbus-to-mqtt-gateway)                                                                                                        |
| ICP DAS tGW-725 | Rp 3,450,000 | [Link](https://www.tokopedia.com/wellkomp-1/icpdas-tgw-725-modbus-tcp-to-rtu-gateway-with-poe-and-2-port-rs-485)                                                            |
| Moxa AIG-101-T  | Rp 8,956,000 | [Link](https://www.tokopedia.com/unilead-indojaya/moxa-aig-101-t-iiot-gateways-modbus-rtu-ascii-tcp-to-mqtt-azure-aws-cloud-ready-gateways-1730995447495820377)             |

---

## B. Technical Specifications Comparison

| Spec                  | SURIOTA          | USR-N720       | USR-N540       | BLIIoT BL100   | ICP DAS tGW-725   | Moxa AIG-101         |
| --------------------- | ---------------- | -------------- | -------------- | -------------- | ----------------- | -------------------- |
| **MCU**               | ESP32-S3         | Unknown        | Unknown        | ARM 300MHz     | ARM 32-bit        | ARM                  |
| **OS**                | RTOS             | Embedded       | Embedded       | Linux          | Embedded          | Linux                |
| **RS-485 Ports**      | 2                | 2              | 4              | 1              | 2                 | 2                    |
| **RS-485 Protection** | ESD (TVS diodes) | ESD            | No             | No             | No                | Yes                  |
| **RTC + Battery**     | DS3231 + CR1220  | No             | No             | No             | No                | No                   |
| **LED Indicators**    | 9 LEDs           | Basic          | Basic          | Basic          | Basic             | Basic                |
| **Ethernet**          | 10/100           | 10/100         | 10/100         | Dual           | 10/100            | Dual                 |
| **WiFi**              | Yes              | No             | No             | Optional       | No                | No                   |
| **BLE**               | 5.0              | No             | No             | No             | No                | No                   |
| **Protocol In**       | Modbus RTU/TCP   | Modbus RTU/TCP | Modbus RTU/TCP | Modbus RTU/TCP | Modbus RTU/TCP    | Modbus RTU/ASCII/TCP |
| **Protocol Out**      | MQTT+JSON        | MQTT+JSON      | MQTT+JSON      | MQTT           | **Modbus TCP** ⚠️ | MQTT/Azure/AWS       |
| **Temperature**       | -40~+75°C        | -40~+85°C      | -40~+85°C      | -40~+85°C      | -25~+75°C         | -40~+70°C            |
| **Power**             | 12-48V DC        | 9-36V DC       | 9-36V DC       | 9-36V DC       | 12-48V DC / PoE   | 12-48V DC            |
| **PoE Option**        | Yes              | No             | No             | No             | **Yes**           | No                   |
| **Cellular**          | No               | No             | No             | 4G             | No                | LTE Cat.1            |

> ⚠️ **Catatan**: ICP DAS tGW-725 output ke Modbus TCP, BUKAN ke MQTT. Ini protocol converter, bukan IoT gateway.

---

## C. Glossary

| Term               | Definition                                                             |
| ------------------ | ---------------------------------------------------------------------- |
| **MQTT**           | Message Queuing Telemetry Transport - protokol messaging untuk IoT     |
| **Modbus**         | Protokol komunikasi serial untuk industrial devices                    |
| **BLE**            | Bluetooth Low Energy - untuk wireless configuration                    |
| **PoE**            | Power over Ethernet - power delivery via ethernet cable                |
| **RS-485**         | Standard komunikasi serial untuk industrial                            |
| **ESD Protection** | Electrostatic Discharge protection via TVS diodes untuk proteksi surge |
| **RTC**            | Real Time Clock - menyimpan waktu akurat dengan battery backup         |
| **Failover**       | Automatic switching ke backup connection                               |
| **JSON**           | JavaScript Object Notation - format data yang mudah dibaca             |

---

## D. Document History

| Version | Date             | Changes                                                                                                                                                                             |
| ------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | Nov 29, 2025     | Initial document                                                                                                                                                                    |
| 2.0     | Nov 29, 2025     | Added Tokopedia prices                                                                                                                                                              |
| 3.0     | Nov 29, 2025     | Added URLs and sales guide                                                                                                                                                          |
| 4.0     | Nov 29, 2025     | Updated COGS with actual data                                                                                                                                                       |
| 4.1     | Nov 29, 2025     | Added ICP DAS competitor                                                                                                                                                            |
| 5.0     | Nov 29, 2025     | MAJOR: Fokus ke Modbus-to-MQTT gateway saja. Hapus kompetitor tanpa MQTT.                                                                                                           |
| 5.1     | Nov 29, 2025     | Tambah kembali ICP DAS tGW-725 (Rp 3.45M) sebagai referensi kompetitor.                                                                                                             |
| 5.2     | Nov 29, 2025     | Tambah REKOMENDASI HARGA FINAL di awal. Tambah 5 scenario (6-10).                                                                                                                   |
| 5.3     | Nov 29, 2025     | Tambah 6 sales scenario baru (Scenario 11-16): Security/Cybersecurity, Multiple Sites/Scaling, PoC/Trial, Lead Time/Stock, Certifications, Bulk/Project Pricing. Total 16 scenario. |
| **5.4** | **Nov 29, 2025** | **KOREKSI SPESIFIKASI dari schematic: Hapus klaim 2kV isolation (tidak akurat). Tambah: ESD Protection (TVS diodes), RTC DS3231 + Battery CR1220, 9 LED Indicators.**               |

---

## E. Contact Information

**PT Surya Inovasi Prioritas (SURIOTA)**

|         |                   |
| ------- | ----------------- |
| Website | www.suriota.com   |
| Email   | sales@suriota.com |
| Phone   | +62 858-3567-2476 |

---

_Document Version: 5.4_
_Classification: Internal - Finance & Marketing_
_Last Updated: November 29, 2025 by: Kemal_
