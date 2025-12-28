# SRT-MGATE-1210 Roasting & Response Guide

## Panduan Menghadapi Kritik Keras dari Customer

**Document Version**: 1.1
**Last Updated**: December 18, 2025
**Purpose**: Mempersiapkan tim sales menghadapi pertanyaan/kritik tajam

---

# DAFTAR ISI

1. [Brand & Credibility](#1-brand--credibility)
2. [Technical & Quality](#2-technical--quality)
3. [Price & Value](#3-price--value)
4. [Support & Warranty](#4-support--warranty)
5. [Feature Comparison](#5-feature-comparison)
6. [Business & Company](#6-business--company)
7. [Use Case Specific](#7-use-case-specific)
8. [Supplier & Distributor](#8-supplier--distributor) **(NEW)**

---

# 1. BRAND & CREDIBILITY

## ROASTING 1.1: "SURIOTA? Siapa itu? Belum pernah dengar!"

**Kritik:**

> "Brand tidak dikenal, tidak ada track record. Kami tidak mau jadi kelinci percobaan untuk produk baru yang belum teruji."

**Response:**

> Terima kasih atas kejujurannya. Memang benar SURIOTA adalah brand baru di pasar Indonesia. Tapi izinkan saya jelaskan beberapa hal:
>
> **Fakta:**
>
> - Kami menggunakan komponen yang SAMA dengan brand besar:
>   - ESP32-S3 (sama seperti di banyak IoT device international)
>   - W5500 Ethernet dari Wiznet Korea (dipakai Moxa juga)
>   - DS3231 RTC (industry standard)
>
> **Keuntungan Brand Baru:**
>
> - Kami LEBIH HUNGRY untuk membuktikan diri
> - Customer service lebih responsif karena setiap customer sangat berharga
> - Harga lebih kompetitif karena belum ada "brand tax"
>
> **Mitigasi Risiko:**
>
> - Garansi 1.5 tahun (lebih lama dari standar 1 tahun)
> - Trial/PoC available sebelum bulk order
> - Replacement unit ready jika ada masalah
>
> **Pertanyaan balik:** Moxa dan Siemens juga pernah jadi brand baru. Apakah Bapak/Ibu bersedia mencoba 1-2 unit dulu untuk membuktikan kualitas kami?

---

## ROASTING 1.2: "Produk China rebrand ya? Cuma tempel stiker SURIOTA?"

**Kritik:**

> "Pasti ini cuma produk ODM China yang ditempel logo sendiri. Sama seperti brand lokal lainnya yang cuma jadi reseller."

**Response:**

> Pertanyaan yang sangat valid, dan saya senang Bapak/Ibu kritis. Jawabannya: **TIDAK, ini bukan rebrand.**
>
> **Bukti Desain Original:**
>
> - PCB di-design sendiri menggunakan EasyEDA/Altium
> - Firmware dikembangkan in-house (bukan SDK vendor)
> - Mechanical enclosure custom design
> - Schematic dan BOM bisa kami tunjukkan jika diperlukan
>
> **Yang Kami Beli dari Luar:**
>
> - Komponen elektronik (wajar, semua manufacturer juga begitu)
> - PCB fabrication (dari manufacturer Indonesia/China)
> - Enclosure injection molding
>
> **Yang Kami Kerjakan Sendiri:**
>
> - Circuit design & PCB layout
> - Firmware development (Modbus, MQTT, BLE, WiFi stack)
> - Mobile app development
> - Assembly & QC
> - Customer support
>
> **Tantangan:** Silakan buka casing dan bandingkan PCB kami dengan produk China manapun. Layout-nya berbeda karena memang desain sendiri.

---

## ROASTING 1.3: "Kalau perusahaan tutup, produk kami jadi sampah elektronik dong?"

**Kritik:**

> "Startup banyak yang gagal dalam 2-3 tahun. Kalau SURIOTA bangkrut, siapa yang support produk kami?"

**Response:**

> Kekhawatiran yang sangat masuk akal. Ini jawaban jujur kami:
>
> **Mitigasi Risiko Bisnis:**
>
> 1. **Open Documentation** - Kami akan release technical documentation jika diminta
> 2. **Standard Protocol** - Produk pakai MQTT standard, tidak proprietary
> 3. **Common Components** - Semua komponen available di pasaran
> 4. **Firmware Update** - Bisa OTA, tidak tergantung kami untuk basic operation
>
> **Business Sustainability:**
>
> - PT Surya Inovasi Prioritas adalah PT resmi terdaftar
> - Fokus di niche market (Industrial IoT) dengan demand growing
> - Margin sehat (40-41%) untuk sustainability
> - Tidak burn money untuk growth, fokus profitability
>
> **Worst Case Scenario:**
>
> - Produk tetap bisa dipakai karena protocol standard (MQTT)
> - Komponen replacement tersedia di pasaran
> - Komunitas/third party bisa maintain jika open source
>
> **Komitmen:** Kami bersedia sign agreement untuk provide technical documentation dan source code escrow jika volume order signifikan.

---

# 2. TECHNICAL & QUALITY

## ROASTING 2.1: "ESP32? Itu kan chip mainan, bukan industrial grade!"

**Kritik:**

> "ESP32 itu chip untuk hobby project dan Arduino. Tidak cocok untuk industrial deployment yang butuh reliability tinggi."

**Response:**

> Persepsi yang umum tapi tidak sepenuhnya akurat. Mari kita bahas:
>
> **Fakta ESP32-S3:**
>
> - **Manufacturer**: Espressif Systems (listed company, bukan startup)
> - **Certifications**: FCC, CE, IC, TELEC, KCC, NCC, SRRC certified
> - **Operating Temp**: -40°C to +85°C (Industrial grade)
> - **Reliability**: MTBF data available dari Espressif
> - **Adoption**: Digunakan di ribuan commercial products globally
>
> **Industrial Deployments ESP32:**
>
> - Smart meters (jutaan unit deployed)
> - Industrial sensors
> - Building automation
> - Agricultural IoT
> - Automotive (Tesla menggunakan Espressif chips)
>
> **Kenapa ESP32 untuk SURIOTA:**
>
> - WiFi + BLE integrated (tidak perlu module terpisah)
> - Dual-core untuk real-time processing
> - FreeRTOS untuk deterministic behavior
> - OTA update capability
> - Cost effective tanpa mengorbankan quality
>
> **Perbandingan:**
>
> - Moxa AIG-101 pakai ARM processor - bagus tapi **3x lebih mahal**
> - Untuk 80% use case, ESP32 MORE THAN ENOUGH
>
> **Challenge:** Coba jalankan stress test 30 hari. Kalau fail, kami ganti unit baru.

---

## ROASTING 2.2: "Tidak ada galvanic isolation 2kV? Nanti kena surge langsung rusak!"

**Kritik:**

> "RS-485 tanpa isolation itu berbahaya di environment industrial. Surge dari motor atau lightning bisa merusak semua device."

**Response:**

> Terima kasih sudah detail secara teknis. Mari saya jelaskan design choice kami:
>
> **Apa yang Kami Punya:**
>
> - **ESD Protection** via TVS diodes (SMCJ60CA-M3/9AT)
> - Rating: **60V standoff, 600W surge**
> - Response time: **< 1ns** (sangat cepat)
>
> **Kapan Butuh Galvanic Isolation:**
>
> - Ground loop issues di long cable runs (>1km)
> - Different ground potential antar building
> - Direct exposure ke lightning strike zone
> - High voltage equipment nearby
>
> **Kapan ESD Protection Cukup:**
>
> - Cable run < 500m (mayoritas factory)
> - Same building/ground reference
> - Behind proper surge protection di panel
> - Normal industrial environment
>
> **Solusi untuk High-Risk Environment:**
>
> - Tambah external RS-485 isolator (Rp 200-500K)
> - Total masih lebih murah dari Moxa
>
> **Data:**
>
> - 90% instalasi industrial tidak butuh galvanic isolation
> - TVS protection sudah cukup untuk ESD dan transient surge
>
> **Rekomendasi:** Kalau environment memang extreme, kami bisa rekomendasikan isolator tambahan. Tapi untuk mayoritas use case, built-in ESD protection sudah sufficient.

---

## ROASTING 2.3: "Casing plastik? Nanti retak kena panas matahari!"

**Kritik:**

> "Industrial equipment harusnya pakai metal casing. Plastik itu murahan dan tidak tahan lama."

**Response:**

> Valid concern. Mari kita bahas material choice:
>
> **Material Kami: PLA+ Industrial Grade**
>
> - Operating temp: -40°C to +75°C
> - UV resistant (outdoor capable)
> - Flame retardant (UL94 V-0 rating)
> - Impact resistant
>
> **Kenapa Bukan Metal:**
> | Aspek | Plastic | Metal |
> |-------|---------|-------|
> | WiFi/BLE signal | **Excellent** | Blocked/reduced |
> | Weight | Light | Heavy |
> | Cost | Lower | Higher |
> | Corrosion | None | Possible |
> | Heat dissipation | Adequate | Better |
>
> **Key Point:** Metal casing akan BLOCK WiFi dan BLE signal!
>
> **Kompetitor dengan Plastic Casing:**
>
> - USR-IOT N720: Plastic
> - BLIIoT BL100: Plastic
> - ICP DAS tGW-725: Plastic
> - Bahkan beberapa Moxa series: Plastic
>
> **Untuk Harsh Environment:**
>
> - Install di dalam panel/enclosure
> - Kami punya IP65 enclosure option (coming soon)
>
> **Real World:** Produk sudah ditest outdoor (tidak langsung kena hujan) selama 6 bulan tanpa degradation.

---

## ROASTING 2.4: "Firmware buatan sendiri? Pasti banyak bug!"

**Kritik:**

> "Moxa dan Siemens punya tim ratusan engineer. Firmware SURIOTA pasti tidak mature dan penuh bug."

**Response:**

> Kekhawatiran yang wajar. Ini transparansi kami:
>
> **Status Firmware:**
>
> - Development time: 18+ bulan
> - Sudah melalui beberapa pilot deployment
> - Core libraries menggunakan proven open source (ESP-IDF, MQTT lib)
> - Modbus stack: tested dengan 20+ jenis device
>
> **Apa yang Sudah Tested:**
>
> - [x] Modbus RTU read/write (tested dengan 15+ device brands)
> - [x] Modbus TCP server/client
> - [x] MQTT publish ke ThingsBoard, AWS, Datacake
> - [x] WiFi reconnection logic
> - [x] Ethernet failover
> - [x] BLE configuration
> - [x] OTA firmware update
>
> **Yang Kami Akui:**
>
> - Mungkin ada edge case yang belum ketemu
> - Fitur masih lebih sedikit dari Moxa
> - Documentation belum selengkap brand besar
>
> **Mitigasi:**
>
> - OTA update untuk bug fix (tidak perlu ke site)
> - Responsive support untuk issue resolution
> - Firmware changelog transparent
>
> **Komitmen:** Kalau ada bug critical, fix dalam 48 jam dan push OTA.

---

# 3. PRICE & VALUE

## ROASTING 3.1: "Murah pasti murahan. Ada udang di balik batu!"

**Kritik:**

> "Harga segitu pasti ada yang di-cut. Mungkin pakai komponen KW atau QC tidak ketat."

**Response:**

> Skeptisisme yang sehat! Ini breakdown kenapa kami bisa lebih murah:
>
> **Cost Structure Comparison:**
>
> | Cost Item     | Brand Import    | SURIOTA   | Savings |
> | ------------- | --------------- | --------- | ------- |
> | Manufacturing | China/Taiwan    | Indonesia | Same    |
> | R&D overhead  | Huge team       | Lean team | -60%    |
> | Marketing     | Global campaign | Targeted  | -80%    |
> | Distribution  | Multi-layer     | Direct    | -30%    |
> | Brand premium | High            | None      | -40%    |
> | Margin        | 60-70%          | 40-41%    | Lower   |
>
> **Yang TIDAK Kami Potong:**
>
> - Komponen kualitas (genuine, bukan KW)
> - QC process (100% tested)
> - Safety features (ESD protection, proper power design)
>
> **Yang Kami Efisienkan:**
>
> - No fancy marketing campaign
> - No distributor margin (direct sales)
> - No global office overhead
> - Lean team (tapi expert di bidangnya)
>
> **Transparansi HPP:**
>
> - COGS (Fully Loaded): Rp 1,630,000 (Non-PoE) / Rp 1,830,000 (PoE)
> - Selling price: Rp 2,700,000 (Non-PoE) / Rp 3,100,000 (PoE)
> - Margin: 40-41% (reasonable, bukan excessive)
>
> **Challenge:** Kami bisa provide component list dan datasheets. Silakan verify sendiri semua genuine.

---

## ROASTING 3.2: "Rp 2.7 juta masih kemahalan untuk produk lokal!"

**Kritik:**

> "Produk China di AliExpress harganya $30-50. Kenapa SURIOTA hampir $170?"

**Response:**

> Perbandingan yang tidak apple-to-apple. Mari kita breakdown:
>
> **$30-50 AliExpress Product:**
>
> - Basic serial to ethernet converter
> - Tidak ada MQTT
> - Tidak ada WiFi
> - Tidak ada BLE
> - Tidak ada RTC
> - No warranty di Indonesia
> - No technical support
> - Shipping 2-4 minggu
>
> **SURIOTA Rp 2.7M ($169):**
>
> - Modbus to MQTT gateway (lengkap)
> - WiFi + Ethernet + BLE
> - RTC dengan battery backup
> - 9 LED indicators
> - Garansi 1.5 tahun Indonesia
> - Technical support Bahasa Indonesia
> - Ready stock / 1-2 minggu
>
> **Total Cost of Ownership:**
>
> | Item               | AliExpress + DIY | SURIOTA  |
> | ------------------ | ---------------- | -------- |
> | Hardware           | $50              | $169     |
> | Additional modules | $30-50           | $0       |
> | Development time   | 40-80 jam        | 0        |
> | Testing/debugging  | 20 jam           | 0        |
> | Support cost       | High (self)      | Included |
> | **Total**          | **$200-400+**    | **$169** |
>
> **Kesimpulan:** SURIOTA bukan murah atau mahal, tapi **VALUE FOR MONEY**.

---

## ROASTING 3.3: "Kompetitor kasih diskon 40%, SURIOTA cuma 20%!"

**Kritik:**

> "Distributor Moxa kasih diskon besar untuk project. SURIOTA pelit banget diskonnya."

**Response:**

> Ini games yang sering dimainkan brand besar. Mari kita bongkar:
>
> **Trik "Diskon Besar":**
>
> ```
> Moxa AIG-101:
> - "List price": Rp 12,000,000 (inflated)
> - "Special discount": 40%
> - "Your price": Rp 7,200,000
> - Actual market price: Rp 8-9 juta
>
> SURIOTA:
> - List price: Rp 2,700,000 (real price)
> - Volume discount: 15-20%
> - Your price: Rp 2,160,000 - 2,295,000
> ```
>
> **Perbandingan Final:**
>
> - Moxa setelah "diskon 40%": **Rp 7,200,000**
> - SURIOTA setelah diskon 20%: **Rp 2,160,000**
> - **Selisih: Rp 5,040,000 per unit!**
>
> **Filosofi Pricing Kami:**
>
> - Harga jujur dari awal (no games)
> - Diskon reasonable untuk volume
> - Tidak mark-up tinggi lalu diskon besar
>
> **Untuk 10 unit:**
>
> - Moxa: 10 x Rp 7.2M = Rp 72,000,000
> - SURIOTA: 10 x Rp 2.43M = Rp 24,300,000 (diskon 10%)
> - **Hemat: Rp 47,700,000!**

---

# 4. SUPPORT & WARRANTY

## ROASTING 4.1: "Support lokal? Paling cuma 1-2 orang, nanti lama responsenya!"

**Kritik:**

> "Tim kecil pasti overwhelmed kalau banyak customer. Response time pasti lambat."

**Response:**

> Concern yang valid. Ini realitanya:
>
> **Current Capacity:**
>
> - Target customer: 200 units dalam 2 tahun
> - Bukan mass market, tapi focused industrial
> - Setiap customer sangat berharga bagi kami
>
> **Support Commitment:**
> | Priority | Response Time | Resolution Time |
> |----------|---------------|-----------------|
> | Critical (down) | < 4 jam | < 24 jam |
> | High | < 8 jam | < 48 jam |
> | Medium | < 24 jam | < 1 minggu |
> | Low | < 48 jam | Best effort |
>
> **Support Channels:**
>
> - WhatsApp direct (fastest)
> - Email: support@suriota.com
> - Phone: +62 858-3567-2476
> - Remote access untuk troubleshooting
>
> **Advantage Tim Kecil:**
>
> - Langsung bicara dengan engineer, bukan call center
> - No ticket queue yang panjang
> - Relationship based, bukan transactional
>
> **Comparison dengan Brand Besar:**
>
> - Moxa support: Email ke Taiwan, response 2-3 hari
> - Distributor lokal: Sering tidak paham teknis
>
> **SLA Agreement:** Untuk customer dengan volume signifikan, kami bersedia sign SLA dengan penalty jika tidak terpenuhi.

---

## ROASTING 4.2: "Garansi 1.5 tahun? Moxa 5 tahun! Berarti produk tidak awet!"

**Kritik:**

> "Kalau yakin produk bagus, kenapa garansinya pendek? Moxa berani kasih 5 tahun."

**Response:**

> Pertanyaan bagus. Ini penjelasannya:
>
> **Realita Garansi di Industri:**
>
> - Garansi adalah **business decision**, bukan quality indicator
> - Perusahaan besar bisa absorb warranty cost
> - Startup harus lebih conservative dengan liability
>
> **Kenapa 1.5 Tahun (Bukan 1 Tahun Standard):**
>
> - Lebih lama dari standar industri (1 tahun)
> - Menunjukkan confidence kami
> - Balance antara coverage dan business sustainability
>
> **Yang Mempengaruhi Lifetime Produk:**
> | Factor | Impact | Mitigation |
> |--------|--------|------------|
> | Component quality | High | Genuine parts |
> | Operating condition | High | Spec compliance |
> | Power quality | Medium | Proper supply |
> | Environmental | Medium | Enclosure |
>
> **Extended Warranty Option:**
>
> - Available untuk tambahan Rp 300,000/tahun
> - Cover sampai 3 tahun total
>
> **Perspective:**
>
> - 95% issues muncul dalam 6 bulan pertama (infant mortality)
> - Setelah itu, produk biasanya reliable untuk tahun-tahun berikutnya
> - Garansi 1.5 tahun sudah cover critical period
>
> **Fun Fact:** Banyak customer Moxa yang tidak pernah claim garansi 5 tahun mereka karena produk biasanya fail di awal atau last very long.

---

## ROASTING 4.3: "Kalau rusak, harus kirim ke mana? Nanti berminggu-minggu!"

**Kritik:**

> "Produk import kalau rusak harus kirim ke service center di Jakarta atau bahkan ke luar negeri. Downtime bisa berminggu-minggu."

**Response:**

> Ini justru **KEUNGGULAN KAMI** sebagai produk lokal:
>
> **SURIOTA Warranty Process:**
>
> ```
> Day 1: Report issue via WhatsApp
> Day 1-2: Remote troubleshooting attempt
> Day 2-3: If hardware issue confirmed:
>          - Replacement unit shipped immediately
>          - Defective unit picked up later
> Day 3-5: Replacement arrives
>
> Total downtime: 3-5 days MAX
> ```
>
> **Moxa/Brand Import Process:**
>
> ```
> Day 1: Report to distributor
> Day 2-3: Distributor contact principal
> Day 3-5: RMA approval process
> Day 5-7: Ship defective unit to service center
> Day 7-14: Repair/evaluation
> Day 14-21: Ship back repaired unit
>
> Total downtime: 2-3 weeks MINIMUM
> ```
>
> **Advance Replacement Policy:**
>
> - Untuk customer dengan support contract
> - Kami kirim replacement DULU
> - Anda kirim defective unit setelah replacement tiba
> - Zero downtime!
>
> **Spare Unit Program:**
>
> - Beli 10 unit, dapat 1 spare dengan diskon 50%
> - Spare siap pakai jika ada issue

---

# 5. FEATURE COMPARISON

## ROASTING 5.1: "Tidak ada 4G/LTE? Bagaimana untuk remote site?"

**Kritik:**

> "Site kami di remote area tidak ada WiFi atau Ethernet. Tanpa cellular, produk ini tidak berguna."

**Response:**

> Fair point. Ini honest assessment kami:
>
> **Kenapa Tidak Ada 4G Built-in:**
>
> - Menambah cost Rp 500K-1M per unit
> - Menambah monthly cost (SIM card)
> - Mayoritas (80%) industrial site sudah ada network
> - Kami fokus ke use case terbesar dulu
>
> **Solusi untuk Remote Site:**
>
> | Option              | Cost        | Pros                    | Cons                  |
> | ------------------- | ----------- | ----------------------- | --------------------- |
> | SURIOTA + 4G Router | Rp 3.2-3.7M | Flexibility, BLE config | 2 devices             |
> | BLIIoT BL100        | Rp 3.37M    | All-in-one              | No BLE, complex setup |
> | Moxa AIG-101        | Rp 8.96M    | Enterprise grade        | Very expensive        |
>
> **SURIOTA + 4G Router:**
>
> - Total: Rp 2.7M + Rp 500K-1M = Rp 3.2-3.7M
> - Masih lebih murah dari BLIIoT
> - Tetap punya advantage BLE config
> - Router bisa di-share untuk keperluan lain
>
> **Roadmap:**
>
> - SRT-MGATE-1210-LTE dalam development
> - Target release: Q2 2026
> - Akan ada cellular option
>
> **Rekomendasi Jujur:**
>
> - Kalau 100% remote tanpa network sama sekali → BLIIoT atau Moxa mungkin lebih cocok
> - Kalau remote tapi ada WiFi (dari 4G router) → SURIOTA still best value

---

## ROASTING 5.2: "Cuma 2 port RS-485? USR-N540 punya 4 port!"

**Kritik:**

> "Kami punya banyak device Modbus. 2 port tidak cukup. USR-N540 lebih value dengan 4 port."

**Response:**

> Benar, USR-N540 punya 4 port dengan harga lebih murah. Tapi mari kita analisis:
>
> **Kapan Butuh 4+ Port:**
>
> - Lebih dari 64 Modbus devices (32 per port x 2)
> - Device dengan address conflict
> - Different baud rate requirements
>
> **2 Port SURIOTA Capacity:**
>
> - 2 x 32 devices = **64 Modbus devices**
> - Untuk mayoritas instalasi, ini LEBIH DARI CUKUP
>
> **Trade-off USR-N540:**
> | Feature | USR-N540 | SURIOTA |
> |---------|----------|---------|
> | RS-485 ports | 4 | 2 |
> | Max devices | 128 | 64 |
> | WiFi | **NO** | **YES** |
> | BLE config | **NO** | **YES** |
> | ESD protection | **NO** | **YES** |
> | RTC battery | **NO** | **YES** |
> | Auto failover | **NO** | **YES** |
>
> **Pertanyaan Kunci:**
>
> > Apakah Bapak/Ibu benar-benar butuh lebih dari 64 device di satu gateway?
>
> **Kalau Butuh Lebih dari 64 Devices:**
>
> - Gunakan 2 unit SURIOTA (4 port total)
> - 2 x Rp 2.7M = Rp 5.4M
> - Total 128 devices + redundancy + WiFi + BLE
>
> **Versus USR-N540:**
>
> - Rp 1.82M untuk 4 port
> - TAPI: tidak ada backup kalau fail, tidak ada WiFi, tidak ada BLE

---

## ROASTING 5.3: "Tidak ada data logging/historian? Data hilang kalau network down!"

**Kritik:**

> "Gateway profesional harus ada local storage untuk buffering data saat network down. SURIOTA tidak punya SD card."

**Response:**

> Kritik yang sangat teknis dan valid. Ini design decision kami:
>
> **Current Implementation:**
>
> - RAM buffer untuk short-term storage
> - MQTT QoS 1/2 untuk guaranteed delivery
> - Automatic retry mechanism
>
> **Kenapa Tidak Ada SD Card (Untuk Sekarang):**
>
> - SD card di industrial environment: high failure rate
> - Adds complexity dan potential failure point
> - Mayoritas use case: real-time monitoring, bukan historian
>
> **Data Loss Scenario Analysis:**
>
> | Network Outage | RAM Buffer        | Data Loss Risk |
> | -------------- | ----------------- | -------------- |
> | < 5 menit      | 1000+ messages    | Zero           |
> | 5-30 menit     | Overflow possible | Low            |
> | > 30 menit     | Likely overflow   | Medium         |
> | > 1 jam        | Overflow certain  | High           |
>
> **Mitigasi:**
>
> 1. **WiFi Failover** - Network down di Ethernet? Auto switch ke WiFi
> 2. **Dual Connection** - Bisa connect ke 2 MQTT broker simultaneously
> 3. **Timestamp dari RTC** - Data tetap punya accurate timestamp
>
> **Solusi untuk Critical Data:**
>
> - Deploy edge historian (Rp 2-5M) untuk buffering
> - Atau gunakan gateway dengan SD card (Moxa AIG-101: Rp 9M)
>
> **Roadmap:**
>
> - SD card support dalam evaluation
> - Flash-based logging lebih reliable dari SD
> - Target: firmware update Q1 2026
>
> **Honest Assessment:**
>
> - Untuk real-time monitoring: SURIOTA cukup
> - Untuk mission-critical historian: mungkin butuh additional edge device

---

# 6. BUSINESS & COMPANY

## ROASTING 6.1: "PT Surya Inovasi Prioritas? Company profile-nya mana?"

**Kritik:**

> "Tidak ada website proper, tidak ada company profile, tidak ada portfolio. Bagaimana kami bisa trust?"

**Response:**

> Kritik yang sangat fair. Ini kondisi kami saat ini:
>
> **Yang Sudah Ada:**
>
> - PT terdaftar resmi di Indonesia
> - NPWP dan legalitas lengkap
> - Kantor operasional (bukan virtual office)
> - Tim engineer dedicated
>
> **Yang Masih Dalam Pengembangan:**
>
> - Website sudah ada di www.suriota.com
> - Company profile ada dalam draft final
> - Technical documentation sedang disusun
> - Product brochures dalam proses desain
> - Case studies sedang dikumpulkan
> - Case study dari pilot project
>
> **Kenapa Belum Lengkap:**
>
> - Fokus ke product development dulu
> - Bootstrap company, prioritas ke R&D
> - Marketing collateral menyusul setelah product stable
>
> **Yang Bisa Kami Provide:**
>
> - Company registration documents
> - NPWP
> - Product datasheets
> - Technical documentation
> - Reference dari pilot customers (dengan izin)
> - Factory/office visit invitation
>
> **Komitmen:**
>
> - Website live dalam 2 bulan
> - Company profile available dalam 1 bulan
> - Happy to arrange company visit
>
> **Pertanyaan:** Informasi spesifik apa yang Bapak/Ibu butuhkan untuk proceed? Kami akan prioritaskan.

---

## ROASTING 6.2: "Sertifikasi CE/FCC belum ada? Berarti belum tested properly!"

**Kritik:**

> "Produk industrial harus ada sertifikasi. Tanpa CE/FCC, ini produk tidak compliant dan berisiko."

**Response:**

> Benar, sertifikasi full product belum complete. Ini statusnya:
>
> **Current Certification Status:**
>
> | Certification | Status     | Timeline |
> | ------------- | ---------- | -------- |
> | RoHS          | Compliant  | Done     |
> | CE            | Planned    | Q1 2026  |
> | FCC           | Planned    | Q1 2026  |
> | TKDN          | In process | Q4 2025  |
>
> **Component-Level Certifications:**
>
> - ESP32-S3: FCC, CE, IC, TELEC, KCC certified
> - W5500: Industrial grade certified
> - Power components: UL certified
>
> **Apa Artinya Ini:**
>
> - Core components sudah certified
> - Full product certification = testing + documentation
> - Bukan masalah quality, tapi masalah process
>
> **Untuk Customer yang Butuh Segera:**
>
> - Declaration of Conformity (DoC) available
> - Component certificates available
> - Internal test reports available
>
> **Rekomendasi:**
>
> - Untuk pilot/internal project: bisa proceed dengan DoC
> - Untuk project dengan compliance requirement strict: tunggu Q1 2026
>
> **Transparansi:** Kami tidak mau bohong soal sertifikasi. Prosesnya sedang berjalan dan akan complete sesuai timeline.

---

# 7. USE CASE SPECIFIC

## ROASTING 7.1: "Di pabrik kami banyak noise. ESP32 pasti interference!"

**Kritik:**

> "Environment pabrik penuh dengan motor, VFD, welding. WiFi dan BLE pasti tidak reliable."

**Response:**

> Concern yang sangat valid untuk industrial environment. Ini mitigasinya:
>
> **Built-in Protection:**
>
> - ESP32-S3 antenna design dengan filtering
> - WiFi: 2.4GHz dengan channel hopping
> - BLE: Adaptive frequency hopping (AFH)
> - Power supply filtering untuk conducted noise
>
> **Installation Best Practices:**
>
> | Noise Source    | Mitigation                                    |
> | --------------- | --------------------------------------------- |
> | VFD             | Install > 2m dari VFD, gunakan shielded cable |
> | Motor           | Proper grounding, jarak dari motor            |
> | Welding         | Tidak install di area welding aktif           |
> | RF interference | Survey spectrum sebelum install               |
>
> **Ethernet Backup:**
>
> - Kalau WiFi unreliable → gunakan Ethernet sebagai primary
> - WiFi tetap available sebagai backup
> - Best of both worlds!
>
> **Site Survey Service:**
>
> - Kami bisa bantu site survey sebelum deployment
> - Identify potential interference sources
> - Recommend optimal installation location
>
> **Guarantee:**
>
> - Kalau setelah proper installation WiFi tidak reliable
> - Gunakan Ethernet saja, WiFi sebagai backup only
> - BLE untuk config tetap bisa dipakai (short range, less affected)

---

## ROASTING 7.2: "Kami pakai Schneider PLC, pasti tidak compatible!"

**Kritik:**

> "Kami sudah invest di ekosistem Schneider/Siemens/Allen-Bradley. Produk luar ekosistem pasti bermasalah."

**Response:**

> Justru sebaliknya! SURIOTA adalah **protocol converter**, bukan bagian dari ekosistem tertentu.
>
> **Compatibility Matrix:**
>
> | PLC Brand     | Modbus Support        | Tested  |
> | ------------- | --------------------- | ------- |
> | Schneider     | Modbus RTU/TCP native | Yes     |
> | Siemens S7    | Via Modbus module     | Yes     |
> | Allen-Bradley | Via Modbus module     | Partial |
> | Mitsubishi    | Modbus RTU/TCP        | Yes     |
> | Omron         | Via Modbus module     | Yes     |
> | Delta         | Modbus RTU/TCP native | Yes     |
>
> **Kenapa SURIOTA Compatible:**
>
> - Modbus adalah **OPEN STANDARD** protocol
> - Tidak proprietary ke vendor manapun
> - Selama device support Modbus → compatible
>
> **Tested Devices:**
>
> - Schneider PM5xxx series power meters
> - Schneider Altivar VFD
> - Siemens PAC3200
> - ABB energy meters
> - Janitza power analyzers
> - Various Chinese Modbus devices
>
> **Integration Example:**
>
> ```
> Schneider PLC → Modbus RTU → SURIOTA → MQTT → Cloud
>                    |
>              Standard protocol
>              (tidak proprietary)
> ```
>
> **Support:** Kami bisa bantu testing dengan specific device Anda sebelum purchase.

---

## ROASTING 7.3: "Sudah ada SCADA, ngapain butuh IoT gateway?"

**Kritik:**

> "Kami sudah invest mahal di SCADA system. IoT gateway cuma duplikasi dan waste of money."

**Response:**

> SCADA dan IoT Gateway punya fungsi berbeda dan **COMPLEMENTARY**, bukan replacement.
>
> **SCADA vs IoT Gateway:**
>
> | Aspect           | SCADA                | IoT Gateway (SURIOTA)  |
> | ---------------- | -------------------- | ---------------------- |
> | Primary function | Control              | Monitoring + Cloud     |
> | Access           | Local (control room) | Remote (anywhere)      |
> | Users            | Operators            | Management, analysts   |
> | Data             | Real-time display    | Historical + analytics |
> | Alert            | Local alarm          | Push notification      |
> | Investment       | High (Rp 50-500M)    | Low (Rp 2.7M)          |
>
> **Parallel Operation:**
>
> ```
>                     ┌──→ SCADA (Local Control)
> Modbus Device ──────┤
>                     └──→ SURIOTA ──→ Cloud (Remote Monitoring)
> ```
>
> **Use Cases yang SCADA Tidak Cover:**
>
> 1. Management mau lihat production dari rumah
> 2. Predictive maintenance dengan cloud AI
> 3. Multi-site comparison dashboard
> 4. Long-term data analytics
> 5. Integration dengan ERP/MES
>
> **ROI Story:**
>
> - SCADA: Rp 100M investment
> - SURIOTA: Rp 2.7M addition
> - Remote access capability: +2.7% cost untuk 100% remote visibility
>
> **Not Replacement, Enhancement:**
>
> > "SURIOTA tidak mengganti SCADA Anda. SURIOTA membuat investment SCADA Anda lebih valuable dengan menambah remote capability."

---

# QUICK REFERENCE CARD

## Objection → One-Liner Response

| Objection                      | Quick Response                                                                      |
| ------------------------------ | ----------------------------------------------------------------------------------- |
| "Brand tidak dikenal"          | "Semua brand besar juga pernah baru. Kami buktikan dengan garansi dan support."     |
| "Produk rebrand China"         | "Design original, bisa kami tunjukkan schematic dan source code."                   |
| "ESP32 bukan industrial"       | "ESP32 certified -40 to +85°C, dipakai di jutaan industrial devices globally."      |
| "Tidak ada isolation"          | "ESD protection 600W sudah cukup untuk 90% use case. Isolator eksternal available." |
| "Casing plastik murahan"       | "Metal akan block WiFi/BLE. Kompetitor juga pakai plastic."                         |
| "Murah pasti murahan"          | "Murah karena direct sales dan lean operation, bukan karena potong quality."        |
| "Support pasti lambat"         | "Tim kecil = bicara langsung dengan engineer, bukan antri di call center."          |
| "Garansi pendek"               | "1.5 tahun lebih lama dari standard 1 tahun. Extended warranty available."          |
| "Tidak ada 4G"                 | "80% site sudah ada network. Untuk remote, tambah 4G router masih lebih murah."     |
| "Sertifikasi belum ada"        | "Component certified, product certification Q1 2026. DoC available sekarang."       |
| "Margin supplier kecil"        | "25-33% margin + MAP policy = tidak ada perang harga, compete di service."          |
| "Takut supplier lain undercut" | "MAP policy ketat dengan enforcement. Semua jual di harga sama."                    |

---

# 8. SUPPLIER & DISTRIBUTOR

## ROASTING 8.1: "Saya mau jadi reseller, tapi margin terlalu kecil!"

**Kritik:**

> "Diskon 20-25% tidak cukup untuk cover operasional toko saya. Brand lain kasih margin lebih besar."

**Response:**

> Mari kita hitung bersama dengan transparan:
>
> **Skema Supplier SURIOTA (Tier 2 - 10 unit min):**
>
> | Varian  | Harga Supplier | Harga Jual (MAP) | Margin               |
> | ------- | -------------- | ---------------- | -------------------- |
> | Non-PoE | Rp 2,025,000   | Rp 2,700,000     | **Rp 675,000 (33%)** |
> | PoE     | Rp 2,325,000   | Rp 3,100,000     | **Rp 775,000 (33%)** |
>
> **Perbandingan dengan Brand Lain:**
>
> - Brand China: Margin 10-15%, tapi produk komoditas, perang harga
> - Brand Enterprise: Margin 20-30%, tapi modal besar, slow moving
> - SURIOTA: Margin 25-33%, produk unik, no price war (MAP policy)
>
> **Keuntungan MAP Policy:**
>
> - Tidak ada supplier lain yang jual lebih murah
> - Compete di service dan expertise, bukan harga
> - Customer tidak bisa tawar "di tempat lain lebih murah"
>
> **Support untuk Supplier:**
>
> - Marketing material (brosur, datasheet)
> - Technical training
> - Priority stock allocation
> - Lead referral untuk area Anda
>
> **Kesimpulan:** Margin lebih sehat karena tidak ada perang harga. Rp 675K per unit x 10 unit = Rp 6.75M profit.

---

## ROASTING 8.2: "Takut supplier lain jual lebih murah dan rusak market!"

**Kritik:**

> "Bagaimana kalau ada supplier nakal yang jual dibawah harga? Nanti kami yang rugi."

**Response:**

> Kami menerapkan **MAP Policy** (Minimum Advertised Price) yang ketat:
>
> **Aturan MAP:**
>
> - Non-PoE: MIN Rp 2,700,000 (sama dengan harga direct SURIOTA)
> - PoE: MIN Rp 3,100,000 (sama dengan harga direct SURIOTA)
>
> **Enforcement:**
>
> | Pelanggaran | Sanksi                       |
> | ----------- | ---------------------------- |
> | Pertama     | Warning + 1 bulan monitoring |
> | Kedua       | Suspend supply 3 bulan       |
> | Ketiga      | Terminasi kerjasama permanen |
>
> **Monitoring:**
>
> - Mystery shopper berkala
> - Monitor marketplace listings
> - Report dari sesama supplier
>
> **Komitmen SURIOTA:**
>
> - Kami TIDAK akan undercut supplier
> - Direct sales SURIOTA di harga MAP
> - Supplier compete di service, bukan harga
>
> **Perlindungan:** Jika ada bukti supplier lain melanggar MAP, lapor ke kami untuk enforcement.

---

## ROASTING 8.3: "Kalau saya beli 5 unit, nanti ada yang beli 50 unit dapat harga lebih murah?"

**Kritik:**

> "Tidak fair kalau supplier besar dapat harga jauh lebih murah. Kami tidak bisa compete."

**Response:**

> Sistem tier kami didesain fair untuk semua ukuran supplier:
>
> **Tier Pricing:**
>
> | Tier   | Min Order | Diskon | Gap |
> | ------ | --------- | ------ | --- |
> | Tier 1 | 5 unit    | 20%    | -   |
> | Tier 2 | 10 unit   | 25%    | 5%  |
> | Tier 3 | 25 unit   | 30%    | 5%  |
>
> **Kenapa Gap Hanya 5%:**
>
> - Supplier kecil tetap kompetitif
> - Tidak ada monopoli oleh 1-2 supplier besar
> - Gap 5% = selisih harga ~Rp 135K/unit
>
> **Level Playing Field:**
>
> - Semua supplier terikat MAP yang sama
> - Service dan expertise jadi differentiator
> - Area/regional exclusivity bisa dinegosiasi
>
> **Contoh:**
>
> | Supplier  | Tier   | Beli         | Jual         | Margin/unit |
> | --------- | ------ | ------------ | ------------ | ----------- |
> | A (kecil) | Tier 1 | Rp 2,160,000 | Rp 2,700,000 | Rp 540,000  |
> | B (besar) | Tier 3 | Rp 1,890,000 | Rp 2,700,000 | Rp 810,000  |
>
> **Realita:** Supplier besar dapat margin lebih banyak per unit, tapi supplier kecil masih punya margin yang sehat (25%).

---

# CLOSING STATEMENT

Ketika customer masih ragu setelah semua penjelasan:

> "Pak/Bu, saya mengerti kekhawatiran Anda. Sebagai brand baru, kami harus kerja lebih keras untuk membuktikan diri.
>
> Yang bisa saya tawarkan:
>
> 1. **Trial 1 unit** dengan harga normal - uji coba di real environment Anda
> 2. **Garansi 1.5 tahun** dengan replacement policy
> 3. **Direct support** dari engineer yang develop produk ini
> 4. **Money back** jika tidak sesuai expectation dalam 30 hari
>
> Risiko Anda minimal, tapi potential saving sangat besar. Untuk 10 unit saja, bisa hemat Rp 50 juta dibanding Moxa.
>
> Boleh saya arrange demo atau kirim sample unit untuk testing?"

---

_Document Version: 1.1_
_For Internal Sales Team Use_
_Last Updated: December 18, 2025_
_Changelog: Updated pricing (Rp 2.7M/3.1M, 40% margin), added Section 8 Supplier & Distributor_
