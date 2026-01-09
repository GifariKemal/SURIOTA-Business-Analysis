# FAQ & Template Respons - SRT-MGATE-1210
# *FAQ & Response Template - SRT-MGATE-1210*

**Panduan menjawab pertanyaan pelanggan dengan format konsisten dan profesional**
***Guide for answering customer questions with consistent and professional format***

**Versi / *Version***: 1.2 | **Terakhir Diperbarui / *Last Updated***: 9 Januari 2026 (Kamis) / *January 9, 2026 (Thursday)*

---

## Cara Menggunakan Template Ini
## *How to Use This Template*

### Prinsip Menjawab / *Response Principles*

1. **Langsung ke inti** - Tidak bertele-tele, jawab pertanyaan di kalimat pertama
   *Get to the point - No rambling, answer the question in the first sentence*
2. **Pakai tabel** - Lebih mudah dibaca daripada paragraf panjang
   *Use tables - Easier to read than long paragraphs*
3. **Bold untuk emphasis** - Highlight poin penting dengan **bold**
   *Bold for emphasis - Highlight key points with **bold***
4. **Berikan angka konkret** - Bukan "banyak" tapi "50 unit"
   *Give concrete numbers - Not "many" but "50 units"*
5. **Akhiri dengan aksi** - Rekomendasi atau next step yang jelas
   *End with action - Clear recommendation or next step*

### Format Standar / *Standard Format*

```markdown
## [PERTANYAAN PELANGGAN / CUSTOMER QUESTION]

[Jawaban singkat 1-2 kalimat - langsung menjawab pertanyaan]
[Short answer 1-2 sentences - directly answering the question]

| Aspek / Aspect | Detail | Keterangan / Notes |
| -------------- | ------ | ------------------ |
| ...            | ...    | ...                |

**Kesimpulan / Conclusion:** [Rekomendasi atau next step / Recommendation or next step]
```

---

# CONTOH FAQ LENGKAP
# *COMPLETE FAQ EXAMPLES*

---

## Berapa harga SRT-MGATE-1210?
## *What is the price of SRT-MGATE-1210?*

Tersedia 2 varian dengan harga berbeda:
*Available in 2 variants with different prices:*

| Model | Harga / *Price* | Fitur Tambahan / *Additional Features* |
| ----- | --------------- | -------------------------------------- |
| **SRT-MGATE-1210** | Rp 2,700,000 | Standard - 2xRS485, WiFi, BLE, ETH |
| **SRT-MGATE-1210-POE** | Rp 3,100,000 | + PoE IEEE 802.3af/at support |

**Diskon volume tersedia** untuk pembelian 10+ unit.
***Volume discount available** for purchases of 10+ units.*

---

## Apakah ada diskon untuk pembelian banyak?
## *Are there discounts for bulk purchases?*

Ya, tersedia diskon volume:
*Yes, volume discounts are available:*

| Kuantitas / *Quantity* | Diskon / *Discount* | Harga/Unit (Standard) / *Price/Unit (Standard)* |
| ---------------------- | ------------------- | ----------------------------------------------- |
| 1-9 unit | 0% | Rp 2,700,000 |
| 10-24 unit | 5% | Rp 2,565,000 |
| 25-49 unit | 10% | Rp 2,430,000 |
| 50+ unit | 15% | Rp 2,295,000 |

**Kesimpulan / *Conclusion*:** Hubungi sales@suriota.com untuk negosiasi harga proyek besar. / *Contact sales@suriota.com to negotiate pricing for large projects.*

---

## Apa bedanya dengan gateway China yang lebih murah?
## *What's the difference from cheaper China gateways?*

SURIOTA memiliki fitur yang tidak ada di kompetitor China:
*SURIOTA has features not found in China competitors:*

| Fitur / *Feature* | SURIOTA | USR-IOT | BLIIoT |
| ----------------- | ------- | ------- | ------ |
| WiFi Built-in | Ya / *Yes* | Tidak / *No* | Ya / *Yes* |
| BLE Configuration | Ya / *Yes* | Tidak / *No* | Tidak / *No* |
| RTC Battery Backup | Ya / *Yes* | Tidak / *No* | Tidak / *No* |
| 9 LED Indicator | Ya / *Yes* | 4 LED | 5 LED |
| Support Lokal Indonesia / *Local Indonesia Support* | Ya / *Yes* | Tidak / *No* | Tidak / *No* |
| Garansi / *Warranty* | 1.5 Tahun / *1.5 Years* | 1 Tahun / *1 Year* | 1 Tahun / *1 Year* |

**Kesimpulan / *Conclusion*:** Harga mirip, tapi fitur SURIOTA lebih lengkap + support lokal. / *Similar price, but SURIOTA features more complete + local support.*

---

## Berapa lama garansi?
## *How long is the warranty?*

Garansi **1.5 tahun** (18 bulan) untuk semua unit.
*Warranty **1.5 years** (18 months) for all units.*

| Cakupan / *Coverage* | Termasuk / *Included* | Tidak Termasuk / *Not Included* |
| -------------------- | --------------------- | ------------------------------- |
| Defect pabrik / *Factory defect* | Ya / *Yes* | - |
| Komponen rusak / *Damaged component* | Ya / *Yes* | - |
| Kerusakan fisik / *Physical damage* | - | Ya / *Yes* |
| Kebakaran/banjir / *Fire/flood* | - | Ya / *Yes* |
| Modifikasi user / *User modification* | - | Ya / *Yes* |

**Proses klaim / *Claim process*:** Kirim ke alamat SURIOTA, waktu perbaikan 7-14 hari kerja. / *Send to SURIOTA address, repair time 7-14 working days.*

---

## Apakah bisa connect ke cloud platform saya?
## *Can it connect to my cloud platform?*

Ya, SRT-MGATE-1210 output **MQTT + JSON** yang universal:
*Yes, SRT-MGATE-1210 outputs universal **MQTT + JSON**:*

| Platform | Support | Keterangan / *Notes* |
| -------- | ------- | -------------------- |
| AWS IoT | Ya / *Yes* | MQTT native |
| Datacake | Ya / *Yes* | Template tersedia / *Template available* |
| Grafana | Ya / *Yes* | Via InfluxDB/MQTT |
| ThingsBoard | Ya / *Yes* | MQTT native |
| SURGE | Ya / *Yes* | Sudah terintegrasi / *Already integrated* |
| Azure IoT | Ya / *Yes* | MQTT native |
| Custom Server | Ya / *Yes* | Broker MQTT apapun / *Any MQTT broker* |

**Kesimpulan / *Conclusion*:** Selama platform Anda support MQTT, pasti bisa connect. / *As long as your platform supports MQTT, it can definitely connect.*

---

## Bagaimana cara konfigurasi?
## *How to configure?*

Ada 3 metode konfigurasi:
*There are 3 configuration methods:*

| Metode / *Method* | Waktu Setup / *Setup Time* | Kebutuhan / *Requirements* |
| ----------------- | -------------------------- | -------------------------- |
| **BLE Mobile App** | 5 menit / *5 minutes* | Smartphone Android/iOS |
| **Web Interface** | 10 menit / *10 minutes* | Laptop + Ethernet |
| **Serial Console** | 15 menit / *15 minutes* | USB-TTL converter |

**Rekomendasi / *Recommendation*:** Gunakan BLE Mobile App untuk setup tercepat. / *Use BLE Mobile App for fastest setup.*

---

## Apakah tahan untuk outdoor?
## *Is it suitable for outdoor use?*

SRT-MGATE-1210 adalah **indoor device** dengan rating industrial:
*SRT-MGATE-1210 is an **indoor device** with industrial rating:*

| Spesifikasi / *Specification* | Nilai / *Value* | Keterangan / *Notes* |
| ----------------------------- | --------------- | -------------------- |
| Operating Temp | -40°C to +75°C | Industrial grade |
| IP Rating | IP20 | Indoor only |
| Humidity / Kelembaban | 5-95% RH | Non-condensing |

**Untuk outdoor / *For outdoor*:** Pasang dalam enclosure IP65+ dengan ventilasi. / *Install in IP65+ enclosure with ventilation.*

---

## Berapa device Modbus yang bisa diconnect?
## *How many Modbus devices can be connected?*

Maksimal **64 device** (32 per port RS-485):
*Maximum **64 devices** (32 per RS-485 port):*

| Port | Max Device | Catatan / *Notes* |
| ---- | ---------- | ----------------- |
| RS-485 Port 1 | 32 device | Modbus RTU |
| RS-485 Port 2 | 32 device | Modbus RTU |
| **Total** | **64 device** | Bisa campur berbagai merk / *Can mix various brands* |

**Tips:** Gunakan termination resistor 120Ω di ujung kabel untuk jarak >100m. / *Use 120Ω termination resistor at cable end for distances >100m.*

---

## Apakah stock lama bisa rusak?
## *Can old stock get damaged?*

Elektronik **tidak kadaluarsa** seperti makanan, tapi ada pertimbangan:
*Electronics **don't expire** like food, but there are considerations:*

| Komponen / *Component* | Shelf Life | Catatan / *Notes* |
| ---------------------- | ---------- | ----------------- |
| Baterai CR1220 (RTC) / *CR1220 Battery (RTC)* | 5-10 tahun / *years* | Self-discharge ~1%/tahun/*year* |
| IC/Chip | 10+ tahun / *years* | Jika disimpan kering / *If stored dry* |
| Kapasitor / *Capacitor* | 5-10 tahun / *years* | Hindari suhu tinggi / *Avoid high temperature* |
| PCB | 2-5 tahun / *years* | Bisa oksidasi jika tidak disegel / *Can oxidize if not sealed* |

**Rekomendasi penyimpanan / *Storage recommendations*:**
- Tempat kering (kelembaban <60%) / *Dry place (humidity <60%)*
- Suhu ruangan (15-30°C) / *Room temperature (15-30°C)*
- Kemasan anti-statik (ESD bag)

**Kesimpulan / *Conclusion*:** Stock 1-2 tahun aman tanpa masalah. / *Stock 1-2 years is safe without issues.*

---

## Apakah perlu mass production untuk HPP murah?
## *Is mass production needed for lower COGS?*

Ya, volume mempengaruhi HPP:
*Yes, volume affects COGS:*

| Qty Order | Estimasi HPP / *Est. COGS* | Penghematan / *Savings* |
| --------- | -------------------------- | ----------------------- |
| 1-10 unit | Rp 1,630,000 | - |
| 11-50 unit | Rp 1,500,000 | ~8% |
| 51-100 unit | Rp 1,400,000 | ~14% |
| 100+ unit | Rp 1,300,000 | ~20% |

**Penghematan dari / *Savings from*:** Bulk component pricing, efisiensi assembly, shipping per unit lebih murah. / *Bulk component pricing, assembly efficiency, cheaper per-unit shipping.*

---

## Apa kelebihan utama SURIOTA vs kompetitor?
## *What are SURIOTA's main advantages vs competitors?*

SURIOTA adalah **SATU-SATUNYA** gateway di Indonesia dengan kombinasi:
*SURIOTA is the **ONLY** gateway in Indonesia with this combination:*

| Fitur Eksklusif / *Exclusive Feature* | Manfaat / *Benefit* |
| ------------------------------------- | ------------------- |
| **WiFi + Auto Failover** | Backup otomatis jika Ethernet putus / *Auto backup if Ethernet disconnects* |
| **BLE Mobile Config** | Setup 5 menit via smartphone / *5-minute setup via smartphone* |
| **RTC Battery Backup** | Timestamp akurat walau mati listrik / *Accurate timestamp even during power loss* |
| **9 LED Indicator** | Monitoring lengkap tanpa buka casing / *Complete monitoring without opening case* |
| **Support Lokal / *Local Support*** | Bahasa Indonesia, timezone WIB / *Indonesian language, WIB timezone* |

**One-liner:** "Fitur premium, harga mid-range, support lokal." / *"Premium features, mid-range price, local support."*

---

## Saya ragu dengan merk baru, bagaimana?
## *I'm hesitant about a new brand, what should I do?*

Wajar ragu dengan brand baru. Fakta tentang SURIOTA:
*It's normal to be hesitant about a new brand. Facts about SURIOTA:*

| Aspek / *Aspect* | Fakta / *Fact* |
| ---------------- | -------------- |
| **Perusahaan / *Company*** | PT Surya Inovasi Prioritas, legal terdaftar / *PT Surya Inovasi Prioritas, legally registered* |
| **Tim / *Team*** | Engineer ex-multinational dengan 10+ tahun pengalaman / *Ex-multinational engineers with 10+ years experience* |
| **Garansi / *Warranty*** | 1.5 tahun (lebih panjang dari kompetitor) / *1.5 years (longer than competitors)* |
| **Pilot Project** | Tersedia untuk testing sebelum order besar / *Available for testing before large orders* |
| **Referensi / *References*** | Bisa diberikan setelah NDA / *Can be provided after NDA* |

**Penawaran / *Offer*:** Ambil 1 unit untuk pilot project, evaluasi 30 hari. / *Take 1 unit for pilot project, 30-day evaluation.*

---

## Bagaimana cara menjadi supplier/reseller SURIOTA?
## *How to become a SURIOTA supplier/reseller?*

Kami membuka program supplier untuk mitra bisnis:
*We have a supplier program for business partners:*

| Tier | Min Order | Diskon / *Discount* | Harga Non-PoE / *Non-PoE Price* | Harga PoE / *PoE Price* |
| ---- | --------- | ------------------- | ------------------------------- | ----------------------- |
| Tier 1 | 5 unit | 20% | Rp 2,160,000 | Rp 2,480,000 |
| **Tier 2** | 10 unit | **25%** | **Rp 2,025,000** | **Rp 2,325,000** |
| Tier 3 | 25 unit | 30% | Rp 1,890,000 | Rp 2,170,000 |

**Syarat Supplier / *Supplier Requirements*:**
- Memiliki usaha/toko resmi (online/offline) / *Have official business/store (online/offline)*
- Mematuhi MAP (Minimum Advertised Price) = harga retail SURIOTA / *Comply with MAP (Minimum Advertised Price) = SURIOTA retail price*
- Payment: 50% DP, 50% sebelum kirim / *Payment: 50% DP, 50% before shipping*

**Benefit / *Benefits*:**
- Margin supplier 20-30% / *Supplier margin 20-30%*
- Marketing material support
- Technical training
- Priority stock allocation

**Kesimpulan / *Conclusion*:** Hubungi sales@suriota.com dengan subject "Program Supplier" untuk info lebih lanjut. / *Contact sales@suriota.com with subject "Supplier Program" for more info.*

---

## Berapa harga minimum jual untuk reseller?
## *What is the minimum selling price for resellers?*

SURIOTA menerapkan **MAP Policy** (Minimum Advertised Price):
*SURIOTA applies **MAP Policy** (Minimum Advertised Price):*

| Model | MAP (Harga Min Jual) / *MAP (Min Selling Price)* | Keterangan / *Notes* |
| ----- | ------------------------------------------------ | -------------------- |
| SRT-MGATE-1210 | Rp 2,700,000 | Sama dengan harga retail SURIOTA / *Same as SURIOTA retail price* |
| SRT-MGATE-1210-POE | Rp 3,100,000 | Sama dengan harga retail SURIOTA / *Same as SURIOTA retail price* |

**Kenapa Ada MAP / *Why MAP Exists*:**
- Mencegah perang harga antar supplier / *Prevents price wars between suppliers*
- Menjaga value perception produk / *Maintains product value perception*
- Supplier compete di service, bukan harga / *Suppliers compete on service, not price*

**Pelanggaran MAP / *MAP Violation*:**
- Peringatan pertama → kedua → terminasi kerjasama / *First warning → second → partnership termination*

**Kesimpulan / *Conclusion*:** Supplier bebas jual diatas MAP, tapi DILARANG jual dibawah MAP. / *Suppliers free to sell above MAP, but PROHIBITED from selling below MAP.*

---

# TEMPLATE KOSONG
# *BLANK TEMPLATE*

Copy template ini untuk menambah FAQ baru:
*Copy this template to add new FAQ:*

```markdown
## [PERTANYAAN PELANGGAN / CUSTOMER QUESTION]

[Jawaban singkat 1-2 kalimat / Short answer 1-2 sentences]

| Kolom 1 / Column 1 | Kolom 2 / Column 2 | Kolom 3 / Column 3 |
| ------------------ | ------------------ | ------------------ |
| Data               | Data               | Data               |

**Kesimpulan / Conclusion:** [Rekomendasi/next step / Recommendation/next step]
```

---

# KARTU RESPONS CEPAT
# *QUICK RESPONSE CARD*

Untuk jawaban cepat via WhatsApp/Chat:
*For quick answers via WhatsApp/Chat:*

| Pertanyaan / *Question* | Jawaban Singkat / *Short Answer* |
| ----------------------- | -------------------------------- |
| Harga? / *Price?* | "Rp 2.7jt (Standard) / Rp 3.1jt (PoE)" |
| Diskon? / *Discount?* | "5% untuk 10+ unit, hubungi sales untuk volume besar" / *"5% for 10+ units, contact sales for large volume"* |
| Garansi? / *Warranty?* | "1.5 tahun, termasuk defect dan komponen" / *"1.5 years, includes defects and components"* |
| Bisa cloud X? / *Cloud X compatible?* | "Ya, selama support MQTT pasti bisa" / *"Yes, as long as it supports MQTT"* |
| Bedanya sama China? / *Difference from China?* | "WiFi+BLE+RTC built-in, support lokal Indonesia" / *"Built-in WiFi+BLE+RTC, local Indonesia support"* |
| Lead time? | "Ready stock 3-5 hari, indent 2-3 minggu" / *"Ready stock 3-5 days, indent 2-3 weeks"* |
| COD? | "Bisa untuk area Jabodetabek" / *"Available for Jabodetabek area"* |
| Jadi supplier? / *Become supplier?* | "Hubungi sales untuk program supplier dengan diskon 20-30%" / *"Contact sales for supplier program with 20-30% discount"* |

---

## Kontak / *Contact*

**PT Surya Inovasi Prioritas (SURIOTA)**

|         |                   |
| ------- | ----------------- |
| Website | www.suriota.com   |
| Email   | sales@suriota.com |
| Phone   | +62 858-3567-2476 |

---

_Versi Template / Template Version: 1.2_
_Terakhir Diperbarui / Last Updated: 9 Januari 2026 (Kamis) / January 9, 2026 (Thursday)_
_Changelog: Bilingual ID/EN format, updated pricing (Rp 2.7M/3.1M), added supplier FAQ, added MAP policy_
