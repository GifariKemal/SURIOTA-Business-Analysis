# SRT-MGATE-1210 Option A Competitive Analysis
## Analisis Kompetitor di Range Harga Rp 2-4 Juta

**Dokumen Versi**: 1.0
**Tanggal**: 29 November 2025
**Exchange Rate**: 1 USD = Rp 16,000

---

## 1. Pricing Strategy - Option A (Aggressive)

### Harga Jual SURIOTA

| Model | Harga (IDR) | Harga (USD) | COGS | Margin |
|-------|-------------|-------------|------|--------|
| **SRT-MGATE-1210** | Rp 2,500,000 | $156 | Rp 900,000 | **64%** |
| **SRT-MGATE-1210-POE** | Rp 3,500,000 | $219 | Rp 1,096,960 | **68.6%** |

### Alasan Memilih Option A

- **Market Entry Strategy** - Harga kompetitif untuk penetrasi pasar Indonesia
- **Volume Sales** - Target penjualan lebih tinggi dengan harga terjangkau
- **Competitive Edge** - Lebih murah dari Moxa/Advantech dengan fitur lebih lengkap
- **Margin Tetap Sehat** - 64-68% masih sangat profitable

---

## 2. Kompetitor Langsung (Price Range Rp 2-4 Juta)

### 2.1 USR-IOT (China)

| Model | Harga | IDR | RS485 | WiFi | ETH | PoE | BLE | Temp Range |
|-------|-------|-----|-------|------|-----|-----|-----|------------|
| **USR-N510** | $45 | Rp 720,000 | 1x | ❌ | ✅ | ❌ | ❌ | -40~85°C |
| **USR-N520** | $58 | Rp 928,000 | 2x | ❌ | ✅ | ❌ | ❌ | -40~85°C |
| **USR-W610** | $42 | Rp 672,000 | 1x | ✅ | ✅ | ❌ | ❌ | -40~85°C |
| **USR-M100** | $65 | Rp 1,040,000 | 1x | ✅ | ✅ | ❌ | ❌ | -40~85°C |

**Kelebihan USR-IOT:**
- Harga sangat murah
- Industrial temperature range
- Kualitas cukup baik untuk produk China

**Kekurangan USR-IOT:**
- Tidak ada BLE configuration
- WiFi model hanya 1x RS485
- Tidak ada PoE support
- Tidak ada auto failover WiFi ↔ Ethernet

---

### 2.2 Waveshare (China)

| Model | Harga | IDR | RS485 | WiFi | ETH | PoE | Isolation |
|-------|-------|-----|-------|------|-----|-----|-----------|
| **RS485-TO-ETH (B)** | $19.99 | Rp 320,000 | 1x | ❌ | ✅ | ❌ | ❌ |
| **RS485-TO-POE-ETH** | $22.99 | Rp 368,000 | 1x | ❌ | ✅ | ✅ | 2kV |
| **RS485-TO-WIFI-ETH** | $34.99 | Rp 560,000 | 1x | ✅ | ✅ | ❌ | ❌ |

**Kelebihan Waveshare:**
- Harga sangat murah (paling murah di pasaran)
- Dokumentasi lengkap
- Mudah didapat di marketplace

**Kekurangan Waveshare:**
- Hanya 1x RS485 (tidak dual)
- Tidak ada BLE configuration
- Kualitas untuk hobi/prototipe, bukan industrial-grade
- Tidak ada auto failover
- Support terbatas

---

### 2.3 Elfin/Hi-Flying (China)

| Model | Harga | IDR | RS485 | WiFi | ETH | PoE | BLE |
|-------|-------|-----|-------|------|-----|-----|-----|
| **Elfin EW10** | $13-20 | Rp 208,000-320,000 | 1x | ✅ | ❌ | ❌ | ❌ |
| **Elfin EW11** | $15-25 | Rp 240,000-400,000 | 1x | ✅ | ❌ | ❌ | ❌ |
| **HF2211** | $25-40 | Rp 400,000-640,000 | 1x | ✅ | ✅ | ❌ | ❌ |

**Kelebihan Elfin/Hi-Flying:**
- Harga paling murah di kategori WiFi
- Ukuran compact
- Populer untuk DIY project

**Kekurangan Elfin/Hi-Flying:**
- Tidak ada Ethernet (EW10/EW11)
- Hanya 1x RS485
- Kualitas consumer-grade
- Tidak ada BLE configuration
- Dokumentasi terbatas (Bahasa China)

---

### 2.4 Ebyte (China)

| Model | Harga | IDR | RS485 | WiFi | ETH | PoE | Protokol |
|-------|-------|-----|-------|------|-----|-----|----------|
| **NE2-D11** | $11 | Rp 176,000 | 1x | ❌ | ✅ | ❌ | Modbus, MQTT |
| **NE2-D11P** | $12.55 | Rp 201,000 | 1x | ❌ | ✅ | ✅ | Modbus, MQTT |
| **NE2-D14** | $14.30 | Rp 229,000 | 1x | ❌ | ✅ | ❌ | RS485/232/422 |

**Kelebihan Ebyte:**
- Harga sangat murah
- Industrial temp range (-40~85°C)
- Support MQTT built-in
- Tersedia versi PoE

**Kekurangan Ebyte:**
- Hanya 1x RS485
- Tidak ada WiFi
- Tidak ada BLE configuration
- Support dan dokumentasi terbatas

---

### 2.5 ICP DAS (Taiwan) - Mid-Range

| Model | Harga | IDR | RS485 | WiFi | ETH | PoE | BLE |
|-------|-------|-----|-------|------|-----|-----|-----|
| **GW-7472** | $200-250 | Rp 3,200,000-4,000,000 | 4x | ❌ | ✅ | ❌ | ❌ |
| **tGW-724** | $150-200 | Rp 2,400,000-3,200,000 | 2x | ❌ | ✅ | ❌ | ❌ |

**Kelebihan ICP DAS:**
- Brand Taiwan dengan reputasi baik
- Kualitas industrial-grade
- Banyak port RS485

**Kekurangan ICP DAS:**
- Tidak ada WiFi
- Tidak ada BLE
- Harga lebih mahal dari SURIOTA
- Fitur lebih sedikit

---

## 3. Feature Comparison Matrix

### Perbandingan Fitur Lengkap

| Feature | SURIOTA | USR-N520 | Waveshare WiFi-ETH | HF2211 | Ebyte NE2-D11P | ICP DAS |
|---------|---------|----------|-------------------|--------|----------------|---------|
| **Harga** | Rp 2.5M | Rp 928K | Rp 560K | Rp 640K | Rp 201K | Rp 3.2M |
| **RS485 Ports** | **2x** | 2x | 1x | 1x | 1x | 2-4x |
| **RS485 Isolation** | **2kV** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **WiFi** | **✅** | ❌ | ✅ | ✅ | ❌ | ❌ |
| **WiFi WPA3** | **✅** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Ethernet** | **✅** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **BLE Config** | **✅** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **PoE Support** | **✅*** | ❌ | ❌ | ❌ | ✅ | ❌ |
| **Auto Failover** | **✅** | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Modbus RTU/TCP** | **✅** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **MQTT** | **✅** | ✅ | ✅ | ❌ | ✅ | ❌ |
| **Industrial Temp** | **-40~75°C** | -40~85°C | 0~70°C | 0~70°C | -40~85°C | -25~75°C |
| **Local Support** | **Indonesia** | China | China | China | China | Taiwan |

*PoE pada versi SRT-MGATE-1210-POE (Rp 3.5M)

---

## 4. Positioning Analysis

### 4.1 SURIOTA vs Budget Options (< Rp 1 Juta)

```
┌─────────────────────────────────────────────────────────────────┐
│     SURIOTA vs BUDGET OPTIONS (Ebyte, Waveshare, Elfin)        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Harga SURIOTA        : Rp 2,500,000                           │
│  Harga Budget         : Rp 200,000 - 600,000                   │
│  Price Premium        : 4-12x lebih mahal                      │
│                                                                 │
│  JUSTIFIKASI PREMIUM:                                          │
│  ─────────────────────                                         │
│  ✅ Dual RS-485 (vs single)           = Rp 500,000 value       │
│  ✅ 2kV Isolation (vs none)           = Rp 300,000 value       │
│  ✅ WiFi + Ethernet combo             = Rp 400,000 value       │
│  ✅ BLE Mobile Config (unique!)       = Rp 500,000 value       │
│  ✅ Auto Failover (unique!)           = Rp 400,000 value       │
│  ✅ Industrial-grade build            = Rp 300,000 value       │
│  ✅ Local Indonesia support           = Rp 200,000 value       │
│  ─────────────────────────────────────────────────────────────  │
│  Total Value Added                    = Rp 2,600,000           │
│                                                                 │
│  KESIMPULAN: Worth the premium untuk industrial application    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 SURIOTA vs Mid-Range Options (Rp 1-3 Juta)

```
┌─────────────────────────────────────────────────────────────────┐
│       SURIOTA vs MID-RANGE (USR-IOT, ICP DAS Entry)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Harga SURIOTA        : Rp 2,500,000                           │
│  Harga USR-N520       : Rp 928,000 (dual RS485, no WiFi)       │
│  Harga ICP DAS tGW    : Rp 2,400,000 (no WiFi, no BLE)         │
│                                                                 │
│  vs USR-N520 (Rp 1.6M lebih mahal):                            │
│  ✅ WiFi connectivity                                          │
│  ✅ BLE configuration                                          │
│  ✅ 2kV RS485 isolation                                        │
│  ✅ Auto failover                                              │
│  ✅ Local support                                              │
│                                                                 │
│  vs ICP DAS (Rp 100K lebih murah!):                            │
│  ✅ Lebih murah                                                │
│  ✅ WiFi connectivity                                          │
│  ✅ BLE configuration                                          │
│  ✅ Auto failover                                              │
│  ✅ Local Indonesia support                                    │
│                                                                 │
│  KESIMPULAN: Best value di segmen ini!                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Target Market Analysis

### 5.1 Segmen yang Cocok untuk Option A

| Segmen | Kebutuhan | Kenapa Pilih SURIOTA |
|--------|-----------|---------------------|
| **UMKM Manufaktur** | Monitoring mesin sederhana | Harga terjangkau, setup mudah via BLE |
| **Smart Building** | Integrasi HVAC, meter | WiFi + Ethernet redundancy |
| **Pertanian** | IoT sensor, remote monitoring | WiFi coverage area luas |
| **Startup IoT** | Prototipe ke production | Fitur lengkap, harga kompetitif |
| **System Integrator** | Project kecil-menengah | Margin bagus, support lokal |

### 5.2 Kompetitor per Segmen

| Segmen | Budget Option | SURIOTA Advantage |
|--------|---------------|-------------------|
| **Basic Monitoring** | Ebyte NE2-D11 (Rp 176K) | +BLE config, +WiFi, +dual port |
| **WiFi Required** | Waveshare WiFi-ETH (Rp 560K) | +dual RS485, +isolation, +failover |
| **Dual Port** | USR-N520 (Rp 928K) | +WiFi, +BLE, +isolation |
| **Industrial** | ICP DAS (Rp 2.4M) | -Rp 100K, +WiFi, +BLE |

---

## 6. Sales Talking Points

### Menghadapi Keberatan Harga

**"Kenapa lebih mahal dari Ebyte/Waveshare?"**
> "Benar, harga kami lebih tinggi. Tapi dengan Rp 2.5 juta Anda dapat:
> - 2x RS485 port (bukan 1)
> - Isolasi 2kV (perlindungan surge)
> - WiFi + Ethernet (redundancy)
> - Konfigurasi via HP (hemat waktu)
> - Support Indonesia (respon cepat)
>
> Kalau beli Ebyte + butuh WiFi terpisah + isolator + support = lebih mahal"

**"USR-IOT lebih murah dengan 2 port RS485"**
> "USR-N520 memang dual port, tapi:
> - Tidak ada WiFi (harus kabel terus)
> - Tidak ada BLE config (setup ribet)
> - Tidak ada isolation (rentan rusak)
> - Support dari China (respon lama)
>
> Selisih Rp 1.6 juta untuk fitur yang jauh lebih lengkap"

**"ICP DAS lebih terpercaya"**
> "ICP DAS memang brand Taiwan bagus, tapi:
> - Harga hampir sama (Rp 2.4M vs Rp 2.5M)
> - Tidak ada WiFi
> - Tidak ada BLE configuration
> - Support harus ke Taiwan/distributor
>
> Kami lebih lengkap dengan harga sama dan support lokal"

---

## 7. Financial Analysis - Option A

### 7.1 Per Unit Profitability

| Metric | Standard | PoE |
|--------|----------|-----|
| **Selling Price** | Rp 2,500,000 | Rp 3,500,000 |
| **COGS** | Rp 900,000 | Rp 1,096,960 |
| **Gross Profit** | Rp 1,600,000 | Rp 2,403,040 |
| **Gross Margin** | 64% | 68.6% |

### 7.2 Production Run Analysis (200 pcs)

**Asumsi Mix: 120 Standard + 80 PoE**

```
┌─────────────────────────────────────────────────────────────────┐
│           FINANCIAL ANALYSIS - OPTION A PRICING                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  REVENUE                                                        │
│  ────────                                                       │
│  Standard: 120 x Rp 2,500,000    = Rp 300,000,000              │
│  PoE:      80  x Rp 3,500,000    = Rp 280,000,000              │
│  ─────────────────────────────────────────────────────          │
│  Total Revenue                   = Rp 580,000,000              │
│                                    ($36,250 USD)                │
│                                                                 │
│  COSTS                                                          │
│  ──────                                                         │
│  Standard: 120 x Rp 900,000      = Rp 108,000,000              │
│  PoE:      80  x Rp 1,096,960    = Rp  87,756,800              │
│  Fixed Costs (Tooling, etc)      = Rp  75,000,000              │
│  ─────────────────────────────────────────────────────          │
│  Total Costs                     = Rp 270,756,800              │
│                                    ($16,922 USD)                │
│                                                                 │
│  PROFIT                                                         │
│  ───────                                                        │
│  Gross Profit                    = Rp 309,243,200              │
│  Net Profit (after fixed)        = Rp 309,243,200              │
│                                    ($19,328 USD)                │
│                                                                 │
│  METRICS                                                        │
│  ────────                                                       │
│  Overall Margin                  = 53.3%                       │
│  ROI                             = 114%                        │
│  Break-even                      = 85 units                    │
│  Payback Period                  = 4-5 months                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 Comparison: Option A vs Original Pricing

| Metric | Original (Rp 5M/6M) | Option A (Rp 2.5M/3.5M) | Difference |
|--------|---------------------|-------------------------|------------|
| Revenue | Rp 1,080,000,000 | Rp 580,000,000 | -46% |
| Net Profit | Rp 809,243,200 | Rp 309,243,200 | -62% |
| ROI | 299% | 114% | -185% |
| Break-even | 60 units | 85 units | +25 units |
| Margin | 82% | 53% | -29% |

**Trade-off Analysis:**
- Profit lebih rendah per batch
- Tapi lebih mudah masuk pasar Indonesia
- Volume sales berpotensi lebih tinggi
- Market share lebih cepat didapat

---

## 8. Competitive Summary

### Price Positioning Chart

```
HARGA (Rp)
│
15M ┤                                    ┌─────────────┐
    │                                    │  Red Lion   │
    │                                    │  DA10D      │
10M ┤                                    └─────────────┘
    │
 8M ┤                     ┌───────────────────────────┐
    │                     │    Moxa MGate MB3280      │
 6M ┤                     └───────────────────────────┘
    │              ┌────────────────────────┐
 5M ┤              │   Moxa MGate MB3180    │
    │              └────────────────────────┘
    │
 4M ┤        ┌──────────────────────────────────────────────────┐
    │        │  ★ SURIOTA POE (Rp 3.5M) - BEST VALUE POE ★      │
3.5M┤        └──────────────────────────────────────────────────┘
    │   ┌────────────────────────┐
 3M ┤   │    ICP DAS tGW-724     │
    │   └────────────────────────┘
    │   ┌──────────────────────────────────────────────────────┐
2.5M┤   │  ★ SURIOTA STANDARD (Rp 2.5M) - BEST VALUE ★         │
    │   └──────────────────────────────────────────────────────┘
    │
 1M ┤   ┌───────────┐
    │   │ USR-N520  │
    │   └───────────┘
    │┌────────────┐
0.5M││ Waveshare  │
    │└────────────┘
    │┌───────┐
0.2M││ Ebyte │
    │└───────┘
────┴──────────────────────────────────────────────────────────
         Budget        Mid-Range        Premium        Enterprise

FITUR: Basic          Dual Port        Full Feature   Mission-Critical
       1x RS485       2x RS485         WiFi+ETH+BLE   Redundancy++
       No WiFi        No WiFi          Failover       Certified
```

---

## 9. Recommended Actions

### Immediate (Bulan 1-2)
1. **Target Segmen UMKM dan Startup** - Harga Rp 2.5M accessible
2. **Demo BLE Configuration** - Unique selling point
3. **Partner dengan System Integrator lokal** - Margin 15-20% untuk SI

### Short-term (Bulan 3-6)
1. **Case Study** - Dokumentasi implementasi sukses
2. **Bundle Packages** - Gateway + sensor + subscription
3. **Volume Pricing** - Diskon untuk order 10+ unit

### Long-term (Bulan 6-12)
1. **Expand ke regional** - Malaysia, Vietnam, Thailand
2. **Certified Partners** - Training program untuk SI
3. **Premium Version** - Fitur tambahan untuk enterprise

---

## 10. Conclusion

### Option A Summary

**Harga:**
- Standard: **Rp 2,500,000** ($156 USD)
- PoE: **Rp 3,500,000** ($219 USD)

**Positioning:**
- **Premium dari Budget** (4-12x Ebyte/Waveshare) dengan justifikasi fitur
- **Sama dengan Mid-Range** (ICP DAS) tapi fitur lebih lengkap
- **Jauh lebih murah dari Premium** (40-60% vs Moxa/Advantech)

**Keunggulan vs Kompetitor:**
1. Satu-satunya dengan BLE Mobile Configuration di price range ini
2. Dual RS-485 + WiFi + Ethernet dalam 1 device
3. Auto failover WiFi ↔ Ethernet
4. 2kV isolation untuk industrial reliability
5. Support Indonesia (Bahasa Indonesia, timezone lokal)

**Financial:**
- Margin 53-68% (masih sangat sehat)
- ROI 114% per production batch
- Break-even 85 unit (achievable dalam 4-5 bulan)

---

*Dokumen ini dibuat untuk internal PT Surya Inovasi Prioritas (SURIOTA)*
*Versi 1.0 - November 2025*
