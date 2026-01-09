# SRT-MGATE-1210 Panduan Roasting & Respons
# *SRT-MGATE-1210 Roasting & Response Guide*

## Panduan Menghadapi Kritik Keras dari Customer
## *Guide for Handling Tough Customer Criticism*

**Versi Dokumen / *Document Version***: 1.2
**Terakhir Diperbarui / *Last Updated***: 9 Januari 2026 (Kamis) / *January 9, 2026 (Thursday)*
**Tujuan / *Purpose***: Mempersiapkan tim sales menghadapi pertanyaan/kritik tajam / *Preparing sales team for tough questions/criticism*

---

# DAFTAR ISI / *TABLE OF CONTENTS*

1. [Brand & Kredibilitas / *Brand & Credibility*](#1-brand--kredibilitas)
2. [Teknis & Kualitas / *Technical & Quality*](#2-teknis--kualitas)
3. [Harga & Nilai / *Price & Value*](#3-harga--nilai)
4. [Support & Garansi / *Support & Warranty*](#4-support--garansi)
5. [Perbandingan Fitur / *Feature Comparison*](#5-perbandingan-fitur)
6. [Bisnis & Perusahaan / *Business & Company*](#6-bisnis--perusahaan)
7. [Spesifik Use Case / *Use Case Specific*](#7-spesifik-use-case)
8. [Supplier & Distributor](#8-supplier--distributor)

---

# 1. BRAND & KREDIBILITAS
# *1. BRAND & CREDIBILITY*

## ROASTING 1.1: "SURIOTA? Siapa itu? Belum pernah dengar!"
## *ROASTING 1.1: "SURIOTA? Who's that? Never heard of them!"*

**Kritik / *Criticism*:**

> "Brand tidak dikenal, tidak ada track record. Kami tidak mau jadi kelinci percobaan untuk produk baru yang belum teruji."

*> "Unknown brand, no track record. We don't want to be guinea pigs for an untested new product."*

**Respons / *Response*:**

> Terima kasih atas kejujurannya. Memang benar SURIOTA adalah brand baru di pasar Indonesia. Tapi izinkan saya jelaskan:
>
> **Fakta:**
> - Kami menggunakan komponen yang SAMA dengan brand besar:
>   - ESP32-S3 (sama seperti di banyak IoT device international)
>   - W5500 Ethernet dari Wiznet Korea (dipakai Moxa juga)
>   - DS3231 RTC (industry standard)
>
> **Keuntungan Brand Baru:**
> - Kami LEBIH HUNGRY untuk membuktikan diri
> - Customer service lebih responsif karena setiap customer sangat berharga
> - Harga lebih kompetitif karena belum ada "brand tax"
>
> **Mitigasi Risiko:**
> - Garansi 1.5 tahun (lebih lama dari standar 1 tahun)
> - Trial/PoC available sebelum bulk order
> - Replacement unit ready jika ada masalah
>
> **Pertanyaan balik:** Moxa dan Siemens juga pernah jadi brand baru. Apakah Bapak/Ibu bersedia mencoba 1-2 unit dulu untuk membuktikan kualitas kami?

*> "Thank you for your honesty. It's true that SURIOTA is a new brand in the Indonesian market. But let me explain:*
*>*
*> **Facts:***
*> - We use the SAME components as major brands:*
*>   - ESP32-S3 (same as many international IoT devices)*
*>   - W5500 Ethernet from Wiznet Korea (also used by Moxa)*
*>   - DS3231 RTC (industry standard)*
*>*
*> **Advantages of Being New:***
*> - We're MORE HUNGRY to prove ourselves*
*> - Customer service more responsive because every customer matters*
*> - More competitive pricing since no "brand tax"*
*>*
*> **Risk Mitigation:***
*> - 1.5 year warranty (longer than standard 1 year)*
*> - Trial/PoC available before bulk order*
*> - Replacement unit ready if issues arise*
*>*
*> **Counter question:** Moxa and Siemens were also new brands once. Would you be willing to try 1-2 units first to prove our quality?"*

---

## ROASTING 1.2: "Produk China rebrand ya? Cuma tempel stiker SURIOTA?"
## *ROASTING 1.2: "Just a China rebrand? Just slapping SURIOTA sticker?"*

**Kritik / *Criticism*:**

> "Pasti ini cuma produk ODM China yang ditempel logo sendiri. Sama seperti brand lokal lainnya yang cuma jadi reseller."

*> "This must be just a China ODM product with your own logo. Same as other local brands that are just resellers."*

**Respons / *Response*:**

> Pertanyaan yang sangat valid, dan saya senang Bapak/Ibu kritis. Jawabannya: **TIDAK, ini bukan rebrand.**
>
> **Bukti Desain Original:**
> - PCB di-design sendiri menggunakan EasyEDA/Altium
> - Firmware dikembangkan in-house (bukan SDK vendor)
> - Mechanical enclosure custom design
> - Schematic dan BOM bisa kami tunjukkan jika diperlukan
>
> **Yang Kami Beli dari Luar:**
> - Komponen elektronik (wajar, semua manufacturer juga begitu)
> - PCB fabrication (dari manufacturer Indonesia/China)
> - Enclosure injection molding
>
> **Yang Kami Kerjakan Sendiri:**
> - Circuit design & PCB layout
> - Firmware development (Modbus, MQTT, BLE, WiFi stack)
> - Mobile app development
> - Assembly & QC
> - Customer support
>
> **Tantangan:** Silakan buka casing dan bandingkan PCB kami dengan produk China manapun. Layout-nya berbeda karena memang desain sendiri.

*> "Very valid question, and I'm glad you're critical. The answer: **NO, this is NOT a rebrand.***
*>*
*> **Proof of Original Design:***
*> - PCB designed in-house using EasyEDA/Altium*
*> - Firmware developed in-house (not vendor SDK)*
*> - Custom mechanical enclosure design*
*> - Schematic and BOM can be shown if needed*
*>*
*> **What We Source Externally:***
*> - Electronic components (normal, all manufacturers do this)*
*> - PCB fabrication (from Indonesia/China manufacturers)*
*> - Enclosure injection molding*
*>*
*> **What We Do Ourselves:***
*> - Circuit design & PCB layout*
*> - Firmware development (Modbus, MQTT, BLE, WiFi stack)*
*> - Mobile app development*
*> - Assembly & QC*
*> - Customer support*
*>*
*> **Challenge:** Feel free to open the casing and compare our PCB with any China product. The layout is different because it's our own design."*

---

## ROASTING 1.3: "Kalau perusahaan tutup, produk kami jadi sampah elektronik dong?"
## *ROASTING 1.3: "If the company closes, our products become e-waste?"*

**Kritik / *Criticism*:**

> "Startup banyak yang gagal dalam 2-3 tahun. Kalau SURIOTA bangkrut, siapa yang support produk kami?"

*> "Many startups fail within 2-3 years. If SURIOTA goes bankrupt, who supports our products?"*

**Respons / *Response*:**

> Kekhawatiran yang sangat masuk akal. Ini jawaban jujur kami:
>
> **Mitigasi Risiko Bisnis:**
> 1. **Open Documentation** - Kami akan release technical documentation jika diminta
> 2. **Standard Protocol** - Produk pakai MQTT standard, tidak proprietary
> 3. **Common Components** - Semua komponen available di pasaran
> 4. **Firmware Update** - Bisa OTA, tidak tergantung kami untuk basic operation
>
> **Business Sustainability:**
> - PT Surya Inovasi Prioritas adalah PT resmi terdaftar
> - Fokus di niche market (Industrial IoT) dengan demand growing
> - Margin sehat (40-41%) untuk sustainability
> - Tidak burn money untuk growth, fokus profitability
>
> **Worst Case Scenario:**
> - Produk tetap bisa dipakai karena protocol standard (MQTT)
> - Komponen replacement tersedia di pasaran
> - Komunitas/third party bisa maintain jika open source
>
> **Komitmen:** Kami bersedia sign agreement untuk provide technical documentation dan source code escrow jika volume order signifikan.

*> "A very reasonable concern. Here's our honest answer:*
*>*
*> **Business Risk Mitigation:***
*> 1. **Open Documentation** - We will release technical documentation if requested*
*> 2. **Standard Protocol** - Product uses standard MQTT, not proprietary*
*> 3. **Common Components** - All components available in market*
*> 4. **Firmware Update** - OTA capable, not dependent on us for basic operation*
*>*
*> **Business Sustainability:***
*> - PT Surya Inovasi Prioritas is a registered legal entity*
*> - Focus on niche market (Industrial IoT) with growing demand*
*> - Healthy margin (40-41%) for sustainability*
*> - Not burning money for growth, focus on profitability*
*>*
*> **Worst Case Scenario:***
*> - Product continues to work because of standard protocol (MQTT)*
*> - Replacement components available in market*
*> - Community/third party can maintain if open sourced*
*>*
*> **Commitment:** We're willing to sign agreement for technical documentation and source code escrow for significant order volumes."*

---

# 2. TEKNIS & KUALITAS
# *2. TECHNICAL & QUALITY*

## ROASTING 2.1: "ESP32? Itu kan chip mainan, bukan industrial grade!"
## *ROASTING 2.1: "ESP32? That's a toy chip, not industrial grade!"*

**Kritik / *Criticism*:**

> "ESP32 itu chip untuk hobby project dan Arduino. Tidak cocok untuk industrial deployment yang butuh reliability tinggi."

*> "ESP32 is a chip for hobby projects and Arduino. Not suitable for industrial deployment that needs high reliability."*

**Respons / *Response*:**

> Persepsi yang umum tapi tidak sepenuhnya akurat. Mari kita bahas:
>
> **Fakta ESP32-S3:**
> - **Manufacturer**: Espressif Systems (listed company, bukan startup)
> - **Certifications**: FCC, CE, IC, TELEC, KCC, NCC, SRRC certified
> - **Operating Temp**: -40°C to +85°C (Industrial grade)
> - **Reliability**: MTBF data available dari Espressif
> - **Adoption**: Digunakan di ribuan commercial products globally
>
> **Industrial Deployments ESP32:**
> - Smart meters (jutaan unit deployed)
> - Industrial sensors
> - Building automation
> - Agricultural IoT
> - Automotive (Tesla menggunakan Espressif chips)
>
> **Kenapa ESP32 untuk SURIOTA:**
> - WiFi + BLE integrated (tidak perlu module terpisah)
> - Dual-core untuk real-time processing
> - FreeRTOS untuk deterministic behavior
> - OTA update capability
> - Cost effective tanpa mengorbankan quality
>
> **Perbandingan:**
> - Moxa AIG-101 pakai ARM processor - bagus tapi **3x lebih mahal**
> - Untuk 80% use case, ESP32 MORE THAN ENOUGH
>
> **Challenge:** Coba jalankan stress test 30 hari. Kalau fail, kami ganti unit baru.

*> "A common perception but not entirely accurate. Let's discuss:*
*>*
*> **ESP32-S3 Facts:***
*> - **Manufacturer**: Espressif Systems (listed company, not startup)*
*> - **Certifications**: FCC, CE, IC, TELEC, KCC, NCC, SRRC certified*
*> - **Operating Temp**: -40°C to +85°C (Industrial grade)*
*> - **Reliability**: MTBF data available from Espressif*
*> - **Adoption**: Used in thousands of commercial products globally*
*>*
*> **ESP32 Industrial Deployments:***
*> - Smart meters (millions of units deployed)*
*> - Industrial sensors*
*> - Building automation*
*> - Agricultural IoT*
*> - Automotive (Tesla uses Espressif chips)*
*>*
*> **Why ESP32 for SURIOTA:***
*> - WiFi + BLE integrated (no separate module needed)*
*> - Dual-core for real-time processing*
*> - FreeRTOS for deterministic behavior*
*> - OTA update capability*
*> - Cost effective without sacrificing quality*
*>*
*> **Comparison:***
*> - Moxa AIG-101 uses ARM processor - great but **3x more expensive***
*> - For 80% of use cases, ESP32 is MORE THAN ENOUGH*
*>*
*> **Challenge:** Run a 30-day stress test. If it fails, we replace it with a new unit."*

---

## ROASTING 2.2: "Tidak ada galvanic isolation 2kV? Nanti kena surge langsung rusak!"
## *ROASTING 2.2: "No 2kV galvanic isolation? Surge will damage it instantly!"*

**Kritik / *Criticism*:**

> "RS-485 tanpa isolation itu berbahaya di environment industrial. Surge dari motor atau lightning bisa merusak semua device."

*> "RS-485 without isolation is dangerous in industrial environments. Surge from motors or lightning can damage all devices."*

**Respons / *Response*:**

> Terima kasih sudah detail secara teknis. Mari saya jelaskan design choice kami:
>
> **Apa yang Kami Punya:**
> - **ESD Protection** via TVS diodes (SMCJ60CA-M3/9AT)
> - Rating: **60V standoff, 600W surge**
> - Response time: **< 1ns** (sangat cepat)
>
> **Kapan Butuh Galvanic Isolation:**
> - Ground loop issues di long cable runs (>1km)
> - Different ground potential antar building
> - Direct exposure ke lightning strike zone
> - High voltage equipment nearby
>
> **Kapan ESD Protection Cukup:**
> - Cable run < 500m (mayoritas factory)
> - Same building/ground reference
> - Behind proper surge protection di panel
> - Normal industrial environment
>
> **Solusi untuk High-Risk Environment:**
> - Tambah external RS-485 isolator (Rp 200-500K)
> - Total masih lebih murah dari Moxa
>
> **Data:**
> - 90% instalasi industrial tidak butuh galvanic isolation
> - TVS protection sudah cukup untuk ESD dan transient surge
>
> **Rekomendasi:** Kalau environment memang extreme, kami bisa rekomendasikan isolator tambahan. Tapi untuk mayoritas use case, built-in ESD protection sudah sufficient.

*> "Thank you for the technical detail. Let me explain our design choice:*
*>*
*> **What We Have:***
*> - **ESD Protection** via TVS diodes (SMCJ60CA-M3/9AT)*
*> - Rating: **60V standoff, 600W surge***
*> - Response time: **< 1ns** (very fast)*
*>*
*> **When Galvanic Isolation is Needed:***
*> - Ground loop issues on long cable runs (>1km)*
*> - Different ground potential between buildings*
*> - Direct exposure to lightning strike zone*
*> - High voltage equipment nearby*
*>*
*> **When ESD Protection is Sufficient:***
*> - Cable run < 500m (majority of factories)*
*> - Same building/ground reference*
*> - Behind proper surge protection in panel*
*> - Normal industrial environment*
*>*
*> **Solution for High-Risk Environment:***
*> - Add external RS-485 isolator (Rp 200-500K)*
*> - Total still cheaper than Moxa*
*>*
*> **Data:***
*> - 90% of industrial installations don't need galvanic isolation*
*> - TVS protection is sufficient for ESD and transient surge*
*>*
*> **Recommendation:** If environment is truly extreme, we can recommend additional isolator. But for majority of use cases, built-in ESD protection is sufficient."*

---

## ROASTING 2.3: "Casing plastik? Nanti retak kena panas matahari!"
## *ROASTING 2.3: "Plastic casing? It'll crack in the sun!"*

**Kritik / *Criticism*:**

> "Industrial equipment harusnya pakai metal casing. Plastik itu murahan dan tidak tahan lama."

*> "Industrial equipment should use metal casing. Plastic is cheap and won't last."*

**Respons / *Response*:**

> Valid concern. Mari kita bahas material choice:
>
> **Material Kami: PLA+ Industrial Grade**
> - Operating temp: -40°C to +75°C
> - UV resistant (outdoor capable)
> - Flame retardant (UL94 V-0 rating)
> - Impact resistant
>
> **Kenapa Bukan Metal:**
>
> | Aspek / *Aspect* | Plastik / *Plastic* | Metal |
> |------------------|---------------------|-------|
> | Sinyal WiFi/BLE / *WiFi/BLE signal* | **Excellent** | Blocked/reduced |
> | Berat / *Weight* | Ringan / *Light* | Berat / *Heavy* |
> | Biaya / *Cost* | Lebih murah / *Lower* | Lebih mahal / *Higher* |
> | Korosi / *Corrosion* | Tidak ada / *None* | Mungkin / *Possible* |
> | Disipasi panas / *Heat dissipation* | Cukup / *Adequate* | Lebih baik / *Better* |
>
> **Key Point:** Metal casing akan BLOCK WiFi dan BLE signal! / *Metal casing would BLOCK WiFi and BLE signal!*
>
> **Kompetitor dengan Plastic Casing:**
> - USR-IOT N720: Plastic
> - BLIIoT BL100: Plastic
> - ICP DAS tGW-725: Plastic
> - Bahkan beberapa Moxa series: Plastic / *Even some Moxa series: Plastic*
>
> **Untuk Harsh Environment:**
> - Install di dalam panel/enclosure / *Install inside panel/enclosure*
> - Kami punya IP65 enclosure option (coming soon)
>
> **Real World:** Produk sudah ditest outdoor (tidak langsung kena hujan) selama 6 bulan tanpa degradation. / *Product has been tested outdoor (not direct rain) for 6 months without degradation.*

---

## ROASTING 2.4: "Firmware buatan sendiri? Pasti banyak bug!"
## *ROASTING 2.4: "Self-made firmware? Must be full of bugs!"*

**Kritik / *Criticism*:**

> "Moxa dan Siemens punya tim ratusan engineer. Firmware SURIOTA pasti tidak mature dan penuh bug."

*> "Moxa and Siemens have hundreds of engineers. SURIOTA firmware must not be mature and full of bugs."*

**Respons / *Response*:**

> Kekhawatiran yang wajar. Ini transparansi kami:
>
> **Status Firmware:**
> - Development time: 18+ bulan / *18+ months*
> - Sudah melalui beberapa pilot deployment / *Already through several pilot deployments*
> - Core libraries menggunakan proven open source (ESP-IDF, MQTT lib)
> - Modbus stack: tested dengan 20+ jenis device / *tested with 20+ device types*
>
> **Yang Sudah Tested / *What's Been Tested*:**
> - [x] Modbus RTU read/write (tested dengan 15+ device brands)
> - [x] Modbus TCP server/client
> - [x] MQTT publish ke ThingsBoard, AWS, Datacake
> - [x] WiFi reconnection logic
> - [x] Ethernet failover
> - [x] BLE configuration
> - [x] OTA firmware update
>
> **Yang Kami Akui / *What We Acknowledge*:**
> - Mungkin ada edge case yang belum ketemu / *There may be edge cases we haven't found*
> - Fitur masih lebih sedikit dari Moxa / *Features still fewer than Moxa*
> - Documentation belum selengkap brand besar / *Documentation not as complete as big brands*
>
> **Mitigasi / *Mitigation*:**
> - OTA update untuk bug fix (tidak perlu ke site) / *OTA update for bug fix (no site visit needed)*
> - Responsive support untuk issue resolution
> - Firmware changelog transparent
>
> **Komitmen / *Commitment*:** Kalau ada bug critical, fix dalam 48 jam dan push OTA. / *If there's a critical bug, fix within 48 hours and push OTA.*

---

# 3. HARGA & NILAI
# *3. PRICE & VALUE*

## ROASTING 3.1: "Murah pasti murahan. Ada udang di balik batu!"
## *ROASTING 3.1: "Cheap means low quality. There must be a catch!"*

**Kritik / *Criticism*:**

> "Harga segitu pasti ada yang di-cut. Mungkin pakai komponen KW atau QC tidak ketat."

*> "At that price, something must be cut. Maybe using counterfeit components or loose QC."*

**Respons / *Response*:**

> Skeptisisme yang sehat! Ini breakdown kenapa kami bisa lebih murah:
>
> **Perbandingan Struktur Biaya / *Cost Structure Comparison*:**
>
> | Item Biaya / *Cost Item* | Brand Import | SURIOTA | Penghematan / *Savings* |
> | ------------------------ | ------------ | ------- | ----------------------- |
> | Manufacturing | China/Taiwan | Indonesia | Sama / *Same* |
> | R&D overhead | Tim besar / *Huge team* | Tim ramping / *Lean team* | -60% |
> | Marketing | Global campaign | Targeted | -80% |
> | Distribusi / *Distribution* | Multi-layer | Direct | -30% |
> | Brand premium | High / *Tinggi* | None / *Tidak ada* | -40% |
> | Margin | 60-70% | 40-41% | Lower / *Lebih rendah* |
>
> **Yang TIDAK Kami Potong / *What We DON'T Cut*:**
> - Komponen kualitas (genuine, bukan KW) / *Quality components (genuine, not counterfeit)*
> - QC process (100% tested)
> - Safety features (ESD protection, proper power design)
>
> **Yang Kami Efisienkan / *What We Optimize*:**
> - No fancy marketing campaign
> - No distributor margin (direct sales)
> - No global office overhead
> - Lean team (tapi expert di bidangnya) / *(but experts in their fields)*
>
> **Transparansi HPP / *COGS Transparency*:**
> - COGS (Fully Loaded): Rp 1,630,000 (Non-PoE) / Rp 1,830,000 (PoE)
> - Selling price: Rp 2,700,000 (Non-PoE) / Rp 3,100,000 (PoE)
> - Margin: 40-41% (reasonable, bukan excessive)
>
> **Challenge:** Kami bisa provide component list dan datasheets. Silakan verify sendiri semua genuine. / *We can provide component list and datasheets. Feel free to verify all are genuine.*

---

## ROASTING 3.2: "Rp 2.7 juta masih kemahalan untuk produk lokal!"
## *ROASTING 3.2: "Rp 2.7 million is still too expensive for a local product!"*

**Kritik / *Criticism*:**

> "Produk China di AliExpress harganya $30-50. Kenapa SURIOTA hampir $170?"

*> "China products on AliExpress cost $30-50. Why is SURIOTA almost $170?"*

**Respons / *Response*:**

> Perbandingan yang tidak apple-to-apple. Mari kita breakdown:
>
> **$30-50 AliExpress Product:**
> - Basic serial to ethernet converter
> - Tidak ada MQTT / *No MQTT*
> - Tidak ada WiFi / *No WiFi*
> - Tidak ada BLE / *No BLE*
> - Tidak ada RTC / *No RTC*
> - No warranty di Indonesia
> - No technical support
> - Shipping 2-4 minggu / *Shipping 2-4 weeks*
>
> **SURIOTA Rp 2.7M ($169):**
> - Modbus to MQTT gateway (lengkap / *complete*)
> - WiFi + Ethernet + BLE
> - RTC dengan battery backup / *RTC with battery backup*
> - 9 LED indicators
> - Garansi 1.5 tahun Indonesia / *1.5 year Indonesia warranty*
> - Technical support Bahasa Indonesia
> - Ready stock / 1-2 minggu / *Ready stock / 1-2 weeks*
>
> **Total Cost of Ownership:**
>
> | Item | AliExpress + DIY | SURIOTA |
> | ---- | ---------------- | ------- |
> | Hardware | $50 | $169 |
> | Additional modules | $30-50 | $0 |
> | Development time | 40-80 jam/*hrs* | 0 |
> | Testing/debugging | 20 jam/*hrs* | 0 |
> | Support cost | Tinggi (self) / *High (self)* | Included |
> | **Total** | **$200-400+** | **$169** |
>
> **Kesimpulan / *Conclusion*:** SURIOTA bukan murah atau mahal, tapi **VALUE FOR MONEY**.

---

## ROASTING 3.3: "Kompetitor kasih diskon 40%, SURIOTA cuma 20%!"
## *ROASTING 3.3: "Competitors give 40% discount, SURIOTA only 20%!"*

**Kritik / *Criticism*:**

> "Distributor Moxa kasih diskon besar untuk project. SURIOTA pelit banget diskonnya."

*> "Moxa distributors give big discounts for projects. SURIOTA is stingy with discounts."*

**Respons / *Response*:**

> Ini games yang sering dimainkan brand besar. Mari kita bongkar:
>
> **Trik "Diskon Besar" / *"Big Discount" Trick*:**
>
> ```
> Moxa AIG-101:
> - "List price": Rp 12,000,000 (inflated)
> - "Special discount": 40%
> - "Your price": Rp 7,200,000
> - Actual market price: Rp 8-9 juta
>
> SURIOTA:
> - List price: Rp 2,700,000 (real price / harga sebenarnya)
> - Volume discount: 15-20%
> - Your price: Rp 2,160,000 - 2,295,000
> ```
>
> **Perbandingan Final / *Final Comparison*:**
> - Moxa setelah "diskon 40%": **Rp 7,200,000**
> - SURIOTA setelah diskon 20%: **Rp 2,160,000**
> - **Selisih / Difference: Rp 5,040,000 per unit!**
>
> **Filosofi Pricing Kami / *Our Pricing Philosophy*:**
> - Harga jujur dari awal (no games) / *Honest pricing from start (no games)*
> - Diskon reasonable untuk volume / *Reasonable discount for volume*
> - Tidak mark-up tinggi lalu diskon besar / *No high markup then big discount*
>
> **Untuk 10 unit / *For 10 units*:**
> - Moxa: 10 x Rp 7.2M = Rp 72,000,000
> - SURIOTA: 10 x Rp 2.43M = Rp 24,300,000 (diskon 10%)
> - **Hemat / Save: Rp 47,700,000!**

---

# 4. SUPPORT & GARANSI
# *4. SUPPORT & WARRANTY*

## ROASTING 4.1: "Support lokal? Paling cuma 1-2 orang, nanti lama responsenya!"
## *ROASTING 4.1: "Local support? Probably just 1-2 people, response will be slow!"*

**Kritik / *Criticism*:**

> "Tim kecil pasti overwhelmed kalau banyak customer. Response time pasti lambat."

*> "Small team will be overwhelmed with many customers. Response time will definitely be slow."*

**Respons / *Response*:**

> Concern yang valid. Ini realitanya:
>
> **Current Capacity:**
> - Target customer: 200 units dalam 2 tahun / *200 units in 2 years*
> - Bukan mass market, tapi focused industrial / *Not mass market, but focused industrial*
> - Setiap customer sangat berharga bagi kami / *Every customer is very valuable to us*
>
> **Support Commitment:**
>
> | Prioritas / *Priority* | Response Time | Resolution Time |
> |------------------------|---------------|-----------------|
> | Critical (down) | < 4 jam / *hrs* | < 24 jam / *hrs* |
> | High / Tinggi | < 8 jam / *hrs* | < 48 jam / *hrs* |
> | Medium / Sedang | < 24 jam / *hrs* | < 1 minggu / *week* |
> | Low / Rendah | < 48 jam / *hrs* | Best effort |
>
> **Support Channels:**
> - WhatsApp direct (fastest)
> - Email: support@suriota.com
> - Phone: +62 858-3567-2476
> - Remote access untuk troubleshooting
>
> **Advantage Tim Kecil / *Small Team Advantage*:**
> - Langsung bicara dengan engineer, bukan call center / *Talk directly with engineer, not call center*
> - No ticket queue yang panjang / *No long ticket queue*
> - Relationship based, bukan transactional / *Relationship based, not transactional*
>
> **Comparison dengan Brand Besar / *Comparison with Big Brands*:**
> - Moxa support: Email ke Taiwan, response 2-3 hari / *Email to Taiwan, 2-3 day response*
> - Distributor lokal: Sering tidak paham teknis / *Local distributor: Often don't understand technical*
>
> **SLA Agreement:** Untuk customer dengan volume signifikan, kami bersedia sign SLA dengan penalty jika tidak terpenuhi. / *For customers with significant volume, we're willing to sign SLA with penalty if not fulfilled.*

---

## ROASTING 4.2: "Garansi 1.5 tahun? Moxa 5 tahun! Berarti produk tidak awet!"
## *ROASTING 4.2: "1.5 year warranty? Moxa has 5 years! Means product won't last!"*

**Kritik / *Criticism*:**

> "Kalau yakin produk bagus, kenapa garansinya pendek? Moxa berani kasih 5 tahun."

*> "If you're confident the product is good, why short warranty? Moxa dares to give 5 years."*

**Respons / *Response*:**

> Pertanyaan bagus. Ini penjelasannya:
>
> **Realita Garansi di Industri / *Industry Warranty Reality*:**
> - Garansi adalah **business decision**, bukan quality indicator
> - Perusahaan besar bisa absorb warranty cost / *Big companies can absorb warranty cost*
> - Startup harus lebih conservative dengan liability / *Startups must be more conservative with liability*
>
> **Kenapa 1.5 Tahun (Bukan 1 Tahun Standard) / *Why 1.5 Years (Not 1 Year Standard)*:**
> - Lebih lama dari standar industri (1 tahun) / *Longer than industry standard (1 year)*
> - Menunjukkan confidence kami / *Shows our confidence*
> - Balance antara coverage dan business sustainability
>
> **Yang Mempengaruhi Lifetime Produk / *What Affects Product Lifetime*:**
>
> | Faktor / *Factor* | Dampak / *Impact* | Mitigasi / *Mitigation* |
> |-------------------|-------------------|-------------------------|
> | Kualitas komponen / *Component quality* | Tinggi / *High* | Genuine parts |
> | Kondisi operasi / *Operating condition* | Tinggi / *High* | Spec compliance |
> | Kualitas power / *Power quality* | Sedang / *Medium* | Proper supply |
> | Lingkungan / *Environmental* | Sedang / *Medium* | Enclosure |
>
> **Extended Warranty Option:**
> - Available untuk tambahan Rp 300,000/tahun / *Available for additional Rp 300,000/year*
> - Cover sampai 3 tahun total / *Coverage up to 3 years total*
>
> **Perspective:**
> - 95% issues muncul dalam 6 bulan pertama (infant mortality)
> - Setelah itu, produk biasanya reliable untuk tahun-tahun berikutnya / *After that, product usually reliable for years to come*
> - Garansi 1.5 tahun sudah cover critical period

---

## ROASTING 4.3: "Kalau rusak, harus kirim ke mana? Nanti berminggu-minggu!"
## *ROASTING 4.3: "If broken, where to send? Will take weeks!"*

**Kritik / *Criticism*:**

> "Produk import kalau rusak harus kirim ke service center di Jakarta atau bahkan ke luar negeri. Downtime bisa berminggu-minggu."

*> "Imported products when broken must be sent to service centers in Jakarta or even abroad. Downtime can be weeks."*

**Respons / *Response*:**

> Ini justru **KEUNGGULAN KAMI** sebagai produk lokal:
> *This is actually **OUR ADVANTAGE** as a local product:*
>
> **SURIOTA Warranty Process:**
>
> ```
> Hari 1 / Day 1: Report issue via WhatsApp
> Hari 1-2 / Day 1-2: Remote troubleshooting attempt
> Hari 2-3 / Day 2-3: If hardware issue confirmed:
>          - Replacement unit shipped immediately
>          - Defective unit picked up later
> Hari 3-5 / Day 3-5: Replacement arrives
>
> Total downtime: 3-5 hari MAX / 3-5 days MAX
> ```
>
> **Moxa/Brand Import Process:**
>
> ```
> Hari 1 / Day 1: Report to distributor
> Hari 2-3 / Day 2-3: Distributor contact principal
> Hari 3-5 / Day 3-5: RMA approval process
> Hari 5-7 / Day 5-7: Ship defective unit to service center
> Hari 7-14 / Day 7-14: Repair/evaluation
> Hari 14-21 / Day 14-21: Ship back repaired unit
>
> Total downtime: 2-3 minggu MINIMUM / 2-3 weeks MINIMUM
> ```
>
> **Advance Replacement Policy:**
> - Untuk customer dengan support contract / *For customers with support contract*
> - Kami kirim replacement DULU / *We ship replacement FIRST*
> - Anda kirim defective unit setelah replacement tiba / *You ship defective unit after replacement arrives*
> - Zero downtime!
>
> **Spare Unit Program:**
> - Beli 10 unit, dapat 1 spare dengan diskon 50% / *Buy 10 units, get 1 spare at 50% discount*
> - Spare siap pakai jika ada issue / *Spare ready to use if issues arise*

---

# 5. PERBANDINGAN FITUR
# *5. FEATURE COMPARISON*

## ROASTING 5.1: "Tidak ada 4G/LTE? Bagaimana untuk remote site?"
## *ROASTING 5.1: "No 4G/LTE? How for remote sites?"*

**Kritik / *Criticism*:**

> "Site kami di remote area tidak ada WiFi atau Ethernet. Tanpa cellular, produk ini tidak berguna."

*> "Our site in remote area has no WiFi or Ethernet. Without cellular, this product is useless."*

**Respons / *Response*:**

> Fair point. Ini honest assessment kami:
>
> **Kenapa Tidak Ada 4G Built-in / *Why No Built-in 4G*:**
> - Menambah cost Rp 500K-1M per unit / *Adds Rp 500K-1M cost per unit*
> - Menambah monthly cost (SIM card) / *Adds monthly cost (SIM card)*
> - Mayoritas (80%) industrial site sudah ada network / *Majority (80%) industrial sites already have network*
> - Kami fokus ke use case terbesar dulu / *We focus on largest use case first*
>
> **Solusi untuk Remote Site / *Solution for Remote Sites*:**
>
> | Option | Cost | Pros | Cons |
> | ------ | ---- | ---- | ---- |
> | SURIOTA + 4G Router | Rp 3.2-3.7M | Flexibility, BLE config | 2 devices |
> | BLIIoT BL100 | Rp 3.37M | All-in-one | No BLE, complex setup |
> | Moxa AIG-101 | Rp 8.96M | Enterprise grade | Sangat mahal / *Very expensive* |
>
> **SURIOTA + 4G Router:**
> - Total: Rp 2.7M + Rp 500K-1M = Rp 3.2-3.7M
> - Masih lebih murah dari BLIIoT / *Still cheaper than BLIIoT*
> - Tetap punya advantage BLE config / *Still has BLE config advantage*
> - Router bisa di-share untuk keperluan lain / *Router can be shared for other uses*
>
> **Roadmap:**
> - SRT-MGATE-1210-LTE dalam development / *in development*
> - Target release: Q2 2026
> - Akan ada cellular option / *Will have cellular option*
>
> **Rekomendasi Jujur / *Honest Recommendation*:**
> - Kalau 100% remote tanpa network sama sekali → BLIIoT atau Moxa mungkin lebih cocok
> - Kalau remote tapi ada WiFi (dari 4G router) → SURIOTA still best value

---

## ROASTING 5.2: "Cuma 2 port RS-485? USR-N540 punya 4 port!"
## *ROASTING 5.2: "Only 2 RS-485 ports? USR-N540 has 4 ports!"*

**Kritik / *Criticism*:**

> "Kami punya banyak device Modbus. 2 port tidak cukup. USR-N540 lebih value dengan 4 port."

*> "We have many Modbus devices. 2 ports not enough. USR-N540 is better value with 4 ports."*

**Respons / *Response*:**

> Benar, USR-N540 punya 4 port dengan harga lebih murah. Tapi mari kita analisis:
>
> **Kapan Butuh 4+ Port / *When 4+ Ports Needed*:**
> - Lebih dari 64 Modbus devices (32 per port x 2)
> - Device dengan address conflict
> - Different baud rate requirements
>
> **2 Port SURIOTA Capacity:**
> - 2 x 32 devices = **64 Modbus devices**
> - Untuk mayoritas instalasi, ini LEBIH DARI CUKUP / *For majority of installations, this is MORE THAN ENOUGH*
>
> **Trade-off USR-N540:**
>
> | Fitur / *Feature* | USR-N540 | SURIOTA |
> |-------------------|----------|---------|
> | RS-485 ports | 4 | 2 |
> | Max devices | 128 | 64 |
> | WiFi | **TIDAK / NO** | **YA / YES** |
> | BLE config | **TIDAK / NO** | **YA / YES** |
> | ESD protection | **TIDAK / NO** | **YA / YES** |
> | RTC battery | **TIDAK / NO** | **YA / YES** |
> | Auto failover | **TIDAK / NO** | **YA / YES** |
>
> **Pertanyaan Kunci / *Key Question*:**
> > Apakah Bapak/Ibu benar-benar butuh lebih dari 64 device di satu gateway?
> > *Do you really need more than 64 devices on one gateway?*
>
> **Kalau Butuh Lebih dari 64 Devices / *If Need More Than 64 Devices*:**
> - Gunakan 2 unit SURIOTA (4 port total) / *Use 2 SURIOTA units (4 ports total)*
> - 2 x Rp 2.7M = Rp 5.4M
> - Total 128 devices + redundancy + WiFi + BLE

---

## ROASTING 5.3: "Tidak ada data logging/historian? Data hilang kalau network down!"
## *ROASTING 5.3: "No data logging/historian? Data lost if network down!"*

**Kritik / *Criticism*:**

> "Gateway profesional harus ada local storage untuk buffering data saat network down. SURIOTA tidak punya SD card."

*> "Professional gateways should have local storage for data buffering when network is down. SURIOTA doesn't have SD card."*

**Respons / *Response*:**

> Kritik yang sangat teknis dan valid. Ini design decision kami:
>
> **Current Implementation:**
> - RAM buffer untuk short-term storage
> - MQTT QoS 1/2 untuk guaranteed delivery
> - Automatic retry mechanism
>
> **Kenapa Tidak Ada SD Card (Untuk Sekarang) / *Why No SD Card (For Now)*:**
> - SD card di industrial environment: high failure rate
> - Adds complexity dan potential failure point
> - Mayoritas use case: real-time monitoring, bukan historian
>
> **Data Loss Scenario Analysis:**
>
> | Network Outage | RAM Buffer | Risiko Kehilangan Data / *Data Loss Risk* |
> | -------------- | ---------- | ----------------------------------------- |
> | < 5 menit / *min* | 1000+ messages | Zero |
> | 5-30 menit / *min* | Overflow possible | Rendah / *Low* |
> | > 30 menit / *min* | Likely overflow | Sedang / *Medium* |
> | > 1 jam / *hr* | Overflow certain | Tinggi / *High* |
>
> **Mitigasi / *Mitigation*:**
> 1. **WiFi Failover** - Network down di Ethernet? Auto switch ke WiFi
> 2. **Dual Connection** - Bisa connect ke 2 MQTT broker simultaneously
> 3. **Timestamp dari RTC** - Data tetap punya accurate timestamp
>
> **Solusi untuk Critical Data / *Solution for Critical Data*:**
> - Deploy edge historian (Rp 2-5M) untuk buffering
> - Atau gunakan gateway dengan SD card (Moxa AIG-101: Rp 9M)
>
> **Roadmap:**
> - SD card support dalam evaluation / *under evaluation*
> - Flash-based logging lebih reliable dari SD
> - Target: firmware update Q1 2026
>
> **Honest Assessment:**
> - Untuk real-time monitoring: SURIOTA cukup / *SURIOTA is sufficient*
> - Untuk mission-critical historian: mungkin butuh additional edge device

---

# 6. BISNIS & PERUSAHAAN
# *6. BUSINESS & COMPANY*

## ROASTING 6.1: "PT Surya Inovasi Prioritas? Company profile-nya mana?"
## *ROASTING 6.1: "PT Surya Inovasi Prioritas? Where's the company profile?"*

**Kritik / *Criticism*:**

> "Tidak ada website proper, tidak ada company profile, tidak ada portfolio. Bagaimana kami bisa trust?"

*> "No proper website, no company profile, no portfolio. How can we trust?"*

**Respons / *Response*:**

> Kritik yang sangat fair. Ini kondisi kami saat ini:
>
> **Yang Sudah Ada / *What's Already Available*:**
> - PT terdaftar resmi di Indonesia / *Officially registered company in Indonesia*
> - NPWP dan legalitas lengkap / *Complete tax ID and legality*
> - Kantor operasional (bukan virtual office) / *Operational office (not virtual)*
> - Tim engineer dedicated
>
> **Yang Masih Dalam Pengembangan / *Still In Development*:**
> - Website sudah ada di www.suriota.com
> - Company profile ada dalam draft final / *Company profile in final draft*
> - Technical documentation sedang disusun / *Technical documentation being prepared*
> - Product brochures dalam proses desain / *Product brochures in design process*
> - Case studies sedang dikumpulkan / *Case studies being collected*
>
> **Kenapa Belum Lengkap / *Why Not Complete Yet*:**
> - Fokus ke product development dulu / *Focus on product development first*
> - Bootstrap company, prioritas ke R&D
> - Marketing collateral menyusul setelah product stable
>
> **Yang Bisa Kami Provide / *What We Can Provide*:**
> - Company registration documents
> - NPWP
> - Product datasheets
> - Technical documentation
> - Reference dari pilot customers (dengan izin) / *with permission*
> - Factory/office visit invitation
>
> **Komitmen / *Commitment*:**
> - Website live dalam 2 bulan / *Website live in 2 months*
> - Company profile available dalam 1 bulan / *Company profile in 1 month*
> - Happy to arrange company visit
>
> **Pertanyaan / *Question*:** Informasi spesifik apa yang Bapak/Ibu butuhkan untuk proceed? Kami akan prioritaskan. / *What specific information do you need to proceed? We'll prioritize it.*

---

## ROASTING 6.2: "Sertifikasi CE/FCC belum ada? Berarti belum tested properly!"
## *ROASTING 6.2: "No CE/FCC certification? Means not properly tested!"*

**Kritik / *Criticism*:**

> "Produk industrial harus ada sertifikasi. Tanpa CE/FCC, ini produk tidak compliant dan berisiko."

*> "Industrial products must have certifications. Without CE/FCC, this product is non-compliant and risky."*

**Respons / *Response*:**

> Benar, sertifikasi full product belum complete. Ini statusnya:
>
> **Current Certification Status:**
>
> | Sertifikasi / *Certification* | Status | Timeline |
> | ----------------------------- | ------ | -------- |
> | RoHS | Compliant | Selesai / *Done* |
> | CE | Planned | Q1 2026 |
> | FCC | Planned | Q1 2026 |
> | TKDN | Dalam proses / *In process* | Q4 2025 |
>
> **Component-Level Certifications:**
> - ESP32-S3: FCC, CE, IC, TELEC, KCC certified
> - W5500: Industrial grade certified
> - Power components: UL certified
>
> **Apa Artinya Ini / *What This Means*:**
> - Core components sudah certified / *Core components already certified*
> - Full product certification = testing + documentation
> - Bukan masalah quality, tapi masalah process / *Not quality issue, but process issue*
>
> **Untuk Customer yang Butuh Segera / *For Customers Who Need It Now*:**
> - Declaration of Conformity (DoC) available
> - Component certificates available
> - Internal test reports available
>
> **Rekomendasi / *Recommendation*:**
> - Untuk pilot/internal project: bisa proceed dengan DoC / *can proceed with DoC*
> - Untuk project dengan compliance requirement strict: tunggu Q1 2026 / *wait for Q1 2026*
>
> **Transparansi:** Kami tidak mau bohong soal sertifikasi. Prosesnya sedang berjalan dan akan complete sesuai timeline. / *We don't want to lie about certification. Process is ongoing and will complete per timeline.*

---

# 7. SPESIFIK USE CASE
# *7. USE CASE SPECIFIC*

## ROASTING 7.1: "Di pabrik kami banyak noise. ESP32 pasti interference!"
## *ROASTING 7.1: "Our factory has lots of noise. ESP32 will definitely have interference!"*

**Kritik / *Criticism*:**

> "Environment pabrik penuh dengan motor, VFD, welding. WiFi dan BLE pasti tidak reliable."

*> "Factory environment is full of motors, VFDs, welding. WiFi and BLE definitely not reliable."*

**Respons / *Response*:**

> Concern yang sangat valid untuk industrial environment. Ini mitigasinya:
>
> **Built-in Protection:**
> - ESP32-S3 antenna design dengan filtering
> - WiFi: 2.4GHz dengan channel hopping
> - BLE: Adaptive frequency hopping (AFH)
> - Power supply filtering untuk conducted noise
>
> **Installation Best Practices:**
>
> | Sumber Noise / *Noise Source* | Mitigasi / *Mitigation* |
> | ----------------------------- | ----------------------- |
> | VFD | Install > 2m dari VFD, gunakan shielded cable / *Install > 2m from VFD, use shielded cable* |
> | Motor | Proper grounding, jarak dari motor / *Proper grounding, distance from motor* |
> | Welding | Tidak install di area welding aktif / *Don't install in active welding area* |
> | RF interference | Survey spectrum sebelum install / *Survey spectrum before install* |
>
> **Ethernet Backup:**
> - Kalau WiFi unreliable → gunakan Ethernet sebagai primary / *If WiFi unreliable → use Ethernet as primary*
> - WiFi tetap available sebagai backup / *WiFi still available as backup*
> - Best of both worlds!
>
> **Site Survey Service:**
> - Kami bisa bantu site survey sebelum deployment / *We can help with site survey before deployment*
> - Identify potential interference sources
> - Recommend optimal installation location
>
> **Guarantee:**
> - Kalau setelah proper installation WiFi tidak reliable / *If after proper installation WiFi not reliable*
> - Gunakan Ethernet saja, WiFi sebagai backup only / *Use Ethernet only, WiFi as backup only*
> - BLE untuk config tetap bisa dipakai (short range, less affected)

---

## ROASTING 7.2: "Kami pakai Schneider PLC, pasti tidak compatible!"
## *ROASTING 7.2: "We use Schneider PLC, definitely not compatible!"*

**Kritik / *Criticism*:**

> "Kami sudah invest di ekosistem Schneider/Siemens/Allen-Bradley. Produk luar ekosistem pasti bermasalah."

*> "We already invested in Schneider/Siemens/Allen-Bradley ecosystem. Products outside ecosystem will be problematic."*

**Respons / *Response*:**

> Justru sebaliknya! SURIOTA adalah **protocol converter**, bukan bagian dari ekosistem tertentu.
> *Actually the opposite! SURIOTA is a **protocol converter**, not part of any specific ecosystem.*
>
> **Compatibility Matrix:**
>
> | PLC Brand | Modbus Support | Tested |
> | --------- | -------------- | ------ |
> | Schneider | Modbus RTU/TCP native | Ya / *Yes* |
> | Siemens S7 | Via Modbus module | Ya / *Yes* |
> | Allen-Bradley | Via Modbus module | Partial |
> | Mitsubishi | Modbus RTU/TCP | Ya / *Yes* |
> | Omron | Via Modbus module | Ya / *Yes* |
> | Delta | Modbus RTU/TCP native | Ya / *Yes* |
>
> **Kenapa SURIOTA Compatible / *Why SURIOTA is Compatible*:**
> - Modbus adalah **OPEN STANDARD** protocol
> - Tidak proprietary ke vendor manapun / *Not proprietary to any vendor*
> - Selama device support Modbus → compatible
>
> **Tested Devices:**
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
>              (tidak proprietary / not proprietary)
> ```
>
> **Support:** Kami bisa bantu testing dengan specific device Anda sebelum purchase. / *We can help test with your specific device before purchase.*

---

## ROASTING 7.3: "Sudah ada SCADA, ngapain butuh IoT gateway?"
## *ROASTING 7.3: "Already have SCADA, why need IoT gateway?"*

**Kritik / *Criticism*:**

> "Kami sudah invest mahal di SCADA system. IoT gateway cuma duplikasi dan waste of money."

*> "We already invested heavily in SCADA system. IoT gateway is just duplication and waste of money."*

**Respons / *Response*:**

> SCADA dan IoT Gateway punya fungsi berbeda dan **COMPLEMENTARY**, bukan replacement.
> *SCADA and IoT Gateway have different functions and are **COMPLEMENTARY**, not replacement.*
>
> **SCADA vs IoT Gateway:**
>
> | Aspek / *Aspect* | SCADA | IoT Gateway (SURIOTA) |
> | ---------------- | ----- | --------------------- |
> | Fungsi utama / *Primary function* | Control | Monitoring + Cloud |
> | Akses / *Access* | Lokal (control room) | Remote (anywhere) |
> | Pengguna / *Users* | Operators | Management, analysts |
> | Data | Real-time display | Historical + analytics |
> | Alert | Local alarm | Push notification |
> | Investasi / *Investment* | Tinggi (Rp 50-500M) | Rendah (Rp 2.7M) / *Low* |
>
> **Parallel Operation:**
>
> ```
>                     ┌──→ SCADA (Local Control)
> Modbus Device ──────┤
>                     └──→ SURIOTA ──→ Cloud (Remote Monitoring)
> ```
>
> **Use Cases yang SCADA Tidak Cover / *Use Cases SCADA Doesn't Cover*:**
> 1. Management mau lihat production dari rumah / *Management wants to see production from home*
> 2. Predictive maintenance dengan cloud AI
> 3. Multi-site comparison dashboard
> 4. Long-term data analytics
> 5. Integration dengan ERP/MES
>
> **ROI Story:**
> - SCADA: Rp 100M investment
> - SURIOTA: Rp 2.7M addition
> - Remote access capability: +2.7% cost untuk 100% remote visibility
>
> **Not Replacement, Enhancement:**
> > "SURIOTA tidak mengganti SCADA Anda. SURIOTA membuat investment SCADA Anda lebih valuable dengan menambah remote capability."
> > *"SURIOTA doesn't replace your SCADA. SURIOTA makes your SCADA investment more valuable by adding remote capability."*

---

# 8. SUPPLIER & DISTRIBUTOR

## ROASTING 8.1: "Saya mau jadi reseller, tapi margin terlalu kecil!"
## *ROASTING 8.1: "I want to be a reseller, but margin is too small!"*

**Kritik / *Criticism*:**

> "Diskon 20-25% tidak cukup untuk cover operasional toko saya. Brand lain kasih margin lebih besar."

*> "20-25% discount is not enough to cover my store operations. Other brands give bigger margins."*

**Respons / *Response*:**

> Mari kita hitung bersama dengan transparan:
> *Let's calculate together transparently:*
>
> **Skema Supplier SURIOTA (Tier 2 - 10 unit min):**
>
> | Varian / *Variant* | Harga Supplier / *Supplier Price* | Harga Jual (MAP) / *Selling Price (MAP)* | Margin |
> | ------------------ | --------------------------------- | ---------------------------------------- | ------ |
> | Non-PoE | Rp 2,025,000 | Rp 2,700,000 | **Rp 675,000 (33%)** |
> | PoE | Rp 2,325,000 | Rp 3,100,000 | **Rp 775,000 (33%)** |
>
> **Perbandingan dengan Brand Lain / *Comparison with Other Brands*:**
> - Brand China: Margin 10-15%, tapi produk komoditas, perang harga / *but commodity product, price war*
> - Brand Enterprise: Margin 20-30%, tapi modal besar, slow moving / *but large capital, slow moving*
> - SURIOTA: Margin 25-33%, produk unik, no price war (MAP policy)
>
> **Keuntungan MAP Policy / *MAP Policy Benefits*:**
> - Tidak ada supplier lain yang jual lebih murah / *No other supplier sells cheaper*
> - Compete di service dan expertise, bukan harga / *Compete on service and expertise, not price*
> - Customer tidak bisa tawar "di tempat lain lebih murah" / *Customer can't bargain "cheaper elsewhere"*
>
> **Support untuk Supplier / *Support for Suppliers*:**
> - Marketing material (brosur, datasheet)
> - Technical training
> - Priority stock allocation
> - Lead referral untuk area Anda / *Lead referral for your area*
>
> **Kesimpulan / *Conclusion*:** Margin lebih sehat karena tidak ada perang harga. Rp 675K per unit x 10 unit = Rp 6.75M profit. / *Healthier margin because no price war.*

---

## ROASTING 8.2: "Takut supplier lain jual lebih murah dan rusak market!"
## *ROASTING 8.2: "Afraid other suppliers will sell cheaper and ruin the market!"*

**Kritik / *Criticism*:**

> "Bagaimana kalau ada supplier nakal yang jual dibawah harga? Nanti kami yang rugi."

*> "What if there's a rogue supplier selling below price? We'll be the ones losing."*

**Respons / *Response*:**

> Kami menerapkan **MAP Policy** (Minimum Advertised Price) yang ketat:
> *We apply strict **MAP Policy** (Minimum Advertised Price):*
>
> **Aturan MAP / *MAP Rules*:**
> - Non-PoE: MIN Rp 2,700,000 (sama dengan harga direct SURIOTA)
> - PoE: MIN Rp 3,100,000 (sama dengan harga direct SURIOTA)
>
> **Enforcement:**
>
> | Pelanggaran / *Violation* | Sanksi / *Penalty* |
> | ------------------------- | ------------------ |
> | Pertama / *First* | Warning + 1 bulan monitoring / *1 month monitoring* |
> | Kedua / *Second* | Suspend supply 3 bulan / *Suspend supply 3 months* |
> | Ketiga / *Third* | Terminasi kerjasama permanen / *Permanent partnership termination* |
>
> **Monitoring:**
> - Mystery shopper berkala / *Periodic mystery shopper*
> - Monitor marketplace listings
> - Report dari sesama supplier / *Reports from fellow suppliers*
>
> **Komitmen SURIOTA / *SURIOTA Commitment*:**
> - Kami TIDAK akan undercut supplier / *We will NOT undercut suppliers*
> - Direct sales SURIOTA di harga MAP
> - Supplier compete di service, bukan harga / *Suppliers compete on service, not price*
>
> **Perlindungan / *Protection*:** Jika ada bukti supplier lain melanggar MAP, lapor ke kami untuk enforcement. / *If there's evidence of another supplier violating MAP, report to us for enforcement.*

---

## ROASTING 8.3: "Kalau saya beli 5 unit, nanti ada yang beli 50 unit dapat harga lebih murah?"
## *ROASTING 8.3: "If I buy 5 units, someone buying 50 gets cheaper price?"*

**Kritik / *Criticism*:**

> "Tidak fair kalau supplier besar dapat harga jauh lebih murah. Kami tidak bisa compete."

*> "Not fair if big suppliers get much cheaper prices. We can't compete."*

**Respons / *Response*:**

> Sistem tier kami didesain fair untuk semua ukuran supplier:
> *Our tier system is designed to be fair for all supplier sizes:*
>
> **Tier Pricing:**
>
> | Tier | Min Order | Diskon / *Discount* | Gap |
> | ---- | --------- | ------------------- | --- |
> | Tier 1 | 5 unit | 20% | - |
> | Tier 2 | 10 unit | 25% | 5% |
> | Tier 3 | 25 unit | 30% | 5% |
>
> **Kenapa Gap Hanya 5% / *Why Only 5% Gap*:**
> - Supplier kecil tetap kompetitif / *Small suppliers stay competitive*
> - Tidak ada monopoli oleh 1-2 supplier besar / *No monopoly by 1-2 big suppliers*
> - Gap 5% = selisih harga ~Rp 135K/unit / *5% gap = ~Rp 135K/unit price difference*
>
> **Level Playing Field:**
> - Semua supplier terikat MAP yang sama / *All suppliers bound by same MAP*
> - Service dan expertise jadi differentiator / *Service and expertise become differentiator*
> - Area/regional exclusivity bisa dinegosiasi / *Area/regional exclusivity negotiable*
>
> **Contoh / *Example*:**
>
> | Supplier | Tier | Beli / *Buy* | Jual / *Sell* | Margin/unit |
> | -------- | ---- | ------------ | ------------- | ----------- |
> | A (kecil/small) | Tier 1 | Rp 2,160,000 | Rp 2,700,000 | Rp 540,000 |
> | B (besar/big) | Tier 3 | Rp 1,890,000 | Rp 2,700,000 | Rp 810,000 |
>
> **Realita / *Reality*:** Supplier besar dapat margin lebih banyak per unit, tapi supplier kecil masih punya margin yang sehat (25%). / *Big suppliers get more margin per unit, but small suppliers still have healthy margin (25%).*

---

# KARTU REFERENSI CEPAT
# *QUICK REFERENCE CARD*

## Keberatan → Respons Satu Baris
## *Objection → One-Liner Response*

| Keberatan / *Objection* | Respons Cepat / *Quick Response* |
| ----------------------- | -------------------------------- |
| "Brand tidak dikenal" / *"Unknown brand"* | "Semua brand besar juga pernah baru. Kami buktikan dengan garansi dan support." / *"All big brands were once new. We prove ourselves with warranty and support."* |
| "Produk rebrand China" / *"China rebrand product"* | "Design original, bisa kami tunjukkan schematic dan source code." / *"Original design, we can show schematic and source code."* |
| "ESP32 bukan industrial" / *"ESP32 not industrial"* | "ESP32 certified -40 to +85°C, dipakai di jutaan industrial devices globally." / *"ESP32 certified -40 to +85°C, used in millions of industrial devices globally."* |
| "Tidak ada isolation" / *"No isolation"* | "ESD protection 600W sudah cukup untuk 90% use case. Isolator eksternal available." / *"600W ESD protection sufficient for 90% use cases. External isolator available."* |
| "Casing plastik murahan" / *"Cheap plastic casing"* | "Metal akan block WiFi/BLE. Kompetitor juga pakai plastic." / *"Metal would block WiFi/BLE. Competitors also use plastic."* |
| "Murah pasti murahan" / *"Cheap means low quality"* | "Murah karena direct sales dan lean operation, bukan karena potong quality." / *"Cheap due to direct sales and lean operation, not cutting quality."* |
| "Support pasti lambat" / *"Support will be slow"* | "Tim kecil = bicara langsung dengan engineer, bukan antri di call center." / *"Small team = talk directly with engineer, not queue at call center."* |
| "Garansi pendek" / *"Short warranty"* | "1.5 tahun lebih lama dari standard 1 tahun. Extended warranty available." / *"1.5 years longer than standard 1 year. Extended warranty available."* |
| "Tidak ada 4G" / *"No 4G"* | "80% site sudah ada network. Untuk remote, tambah 4G router masih lebih murah." / *"80% sites already have network. For remote, adding 4G router still cheaper."* |
| "Sertifikasi belum ada" / *"No certifications yet"* | "Component certified, product certification Q1 2026. DoC available sekarang." / *"Component certified, product certification Q1 2026. DoC available now."* |
| "Margin supplier kecil" / *"Small supplier margin"* | "25-33% margin + MAP policy = tidak ada perang harga, compete di service." / *"25-33% margin + MAP policy = no price war, compete on service."* |
| "Takut supplier lain undercut" / *"Afraid other suppliers undercut"* | "MAP policy ketat dengan enforcement. Semua jual di harga sama." / *"Strict MAP policy with enforcement. Everyone sells at same price."* |

---

# PERNYATAAN PENUTUP
# *CLOSING STATEMENT*

Ketika customer masih ragu setelah semua penjelasan:
*When customer is still hesitant after all explanations:*

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

*> "Sir/Ma'am, I understand your concerns. As a new brand, we have to work harder to prove ourselves.*
*>*
*> What I can offer:*
*>*
*> 1. **Trial 1 unit** at normal price - test in your real environment*
*> 2. **1.5 year warranty** with replacement policy*
*> 3. **Direct support** from the engineer who developed this product*
*> 4. **Money back** if it doesn't meet expectations within 30 days*
*>*
*> Your risk is minimal, but potential savings are huge. For just 10 units, you can save Rp 50 million compared to Moxa.*
*>*
*> Can I arrange a demo or send a sample unit for testing?"*

---

_Versi Dokumen / Document Version: 1.2_
_Hanya Untuk Penggunaan Tim Sales Internal / For Internal Sales Team Use Only_
_Terakhir Diperbarui / Last Updated: 9 Januari 2026 (Kamis) / January 9, 2026 (Thursday)_
_Changelog: Bilingual ID/EN format, updated pricing (Rp 2.7M/3.1M, 40% margin), added Section 8 Supplier & Distributor_
