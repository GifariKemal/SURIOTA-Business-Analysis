# FAQ & Response Template - SRT-MGATE-1210

**Panduan menjawab pertanyaan pelanggan dengan format konsisten dan profesional**

---

## Cara Menggunakan Template Ini

### Prinsip Menjawab

1. **Langsung ke inti** - Tidak bertele-tele, jawab pertanyaan di kalimat pertama
2. **Pakai tabel** - Lebih mudah dibaca daripada paragraf panjang
3. **Bold untuk emphasis** - Highlight poin penting dengan **bold**
4. **Berikan angka konkret** - Bukan "banyak" tapi "50 unit"
5. **Akhiri dengan aksi** - Rekomendasi atau next step yang jelas

### Format Standar

```markdown
## [PERTANYAAN PELANGGAN]

[Jawaban singkat 1-2 kalimat - langsung menjawab pertanyaan]

| Aspek | Detail | Keterangan |
| ----- | ------ | ---------- |
| ...   | ...    | ...        |

**Kesimpulan:** [Rekomendasi atau next step]
```

---

# CONTOH FAQ LENGKAP

---

## Berapa harga SRT-MGATE-1210?

Tersedia 2 varian dengan harga berbeda:

| Model                  | Harga        | Fitur Tambahan                     |
| ---------------------- | ------------ | ---------------------------------- |
| **SRT-MGATE-1210**     | Rp 2,700,000 | Standard - 2xRS485, WiFi, BLE, ETH |
| **SRT-MGATE-1210-POE** | Rp 3,100,000 | + PoE IEEE 802.3af/at support      |

**Diskon volume tersedia** untuk pembelian 10+ unit.

---

## Apakah ada diskon untuk pembelian banyak?

Ya, tersedia diskon volume:

| Quantity   | Diskon | Harga/Unit (Standard) |
| ---------- | ------ | --------------------- |
| 1-9 unit   | 0%     | Rp 2,700,000          |
| 10-24 unit | 5%     | Rp 2,565,000          |
| 25-49 unit | 10%    | Rp 2,430,000          |
| 50+ unit   | 15%    | Rp 2,295,000          |

**Kesimpulan:** Hubungi sales@suriota.com untuk negosiasi harga proyek besar.

---

## Apa bedanya dengan gateway China yang lebih murah?

SURIOTA memiliki fitur yang tidak ada di kompetitor China:

| Fitur                   | SURIOTA   | USR-IOT | BLIIoT  |
| ----------------------- | --------- | ------- | ------- |
| WiFi Built-in           | Ya        | Tidak   | Ya      |
| BLE Configuration       | Ya        | Tidak   | Tidak   |
| RTC Battery Backup      | Ya        | Tidak   | Tidak   |
| 9 LED Indicator         | Ya        | 4 LED   | 5 LED   |
| Support Lokal Indonesia | Ya        | Tidak   | Tidak   |
| Garansi                 | 1.5 Tahun | 1 Tahun | 1 Tahun |

**Kesimpulan:** Harga mirip, tapi fitur SURIOTA lebih lengkap + support lokal.

---

## Berapa lama garansi?

Garansi **1.5 tahun** (18 bulan) untuk semua unit.

| Cakupan          | Termasuk | Tidak Termasuk |
| ---------------- | -------- | -------------- |
| Defect pabrik    | Ya       | -              |
| Komponen rusak   | Ya       | -              |
| Kerusakan fisik  | -        | Ya             |
| Kebakaran/banjir | -        | Ya             |
| Modifikasi user  | -        | Ya             |

**Proses klaim:** Kirim ke alamat SURIOTA, waktu perbaikan 7-14 hari kerja.

---

## Apakah bisa connect ke cloud platform saya?

Ya, SRT-MGATE-1210 output **MQTT + JSON** yang universal:

| Platform      | Support | Keterangan         |
| ------------- | ------- | ------------------ |
| AWS IoT       | Ya      | MQTT native        |
| Datacake      | Ya      | Template tersedia  |
| Grafana       | Ya      | Via InfluxDB/MQTT  |
| ThingsBoard   | Ya      | MQTT native        |
| SURGE         | Ya      | Sudah terintegrasi |
| Azure IoT     | Ya      | MQTT native        |
| Custom Server | Ya      | Broker MQTT apapun |

**Kesimpulan:** Selama platform Anda support MQTT, pasti bisa connect.

---

## Bagaimana cara konfigurasi?

Ada 3 metode konfigurasi:

| Metode             | Waktu Setup | Kebutuhan              |
| ------------------ | ----------- | ---------------------- |
| **BLE Mobile App** | 5 menit     | Smartphone Android/iOS |
| **Web Interface**  | 10 menit    | Laptop + Ethernet      |
| **Serial Console** | 15 menit    | USB-TTL converter      |

**Rekomendasi:** Gunakan BLE Mobile App untuk setup tercepat.

---

## Apakah tahan untuk outdoor?

SRT-MGATE-1210 adalah **indoor device** dengan rating industrial:

| Spesifikasi    | Value          | Keterangan       |
| -------------- | -------------- | ---------------- |
| Operating Temp | -40°C to +75°C | Industrial grade |
| IP Rating      | IP20           | Indoor only      |
| Humidity       | 5-95% RH       | Non-condensing   |

**Untuk outdoor:** Pasang dalam enclosure IP65+ dengan ventilasi.

---

## Berapa device Modbus yang bisa diconnect?

Maksimal **64 device** (32 per port RS-485):

| Port          | Max Device    | Catatan                   |
| ------------- | ------------- | ------------------------- |
| RS-485 Port 1 | 32 device     | Modbus RTU                |
| RS-485 Port 2 | 32 device     | Modbus RTU                |
| **Total**     | **64 device** | Bisa campur berbagai merk |

**Tips:** Gunakan termination resistor 120Ω di ujung kabel untuk jarak >100m.

---

## Apakah stock lama bisa rusak?

Elektronik **tidak kadaluarsa** seperti makanan, tapi ada pertimbangan:

| Komponen             | Shelf Life | Catatan                          |
| -------------------- | ---------- | -------------------------------- |
| Baterai CR1220 (RTC) | 5-10 tahun | Self-discharge ~1%/tahun         |
| IC/Chip              | 10+ tahun  | Jika disimpan kering             |
| Kapasitor            | 5-10 tahun | Hindari suhu tinggi              |
| PCB                  | 2-5 tahun  | Bisa oksidasi jika tidak disegel |

**Rekomendasi penyimpanan:**

- Tempat kering (kelembaban <60%)
- Suhu ruangan (15-30°C)
- Kemasan anti-statik (ESD bag)

**Kesimpulan:** Stock 1-2 tahun aman tanpa masalah.

---

## Apakah perlu mass production untuk HPP murah?

Ya, volume mempengaruhi HPP:

| Qty Order   | Estimasi HPP | Penghematan |
| ----------- | ------------ | ----------- |
| 1-10 unit   | Rp 1,630,000 | -           |
| 11-50 unit  | Rp 1,500,000 | ~8%         |
| 51-100 unit | Rp 1,400,000 | ~14%        |
| 100+ unit   | Rp 1,300,000 | ~20%        |

**Penghematan dari:** Bulk component pricing, efisiensi assembly, shipping per unit lebih murah.

---

## Apa kelebihan utama SURIOTA vs kompetitor?

SURIOTA adalah **SATU-SATUNYA** gateway di Indonesia dengan kombinasi:

| Fitur Eksklusif          | Benefit                              |
| ------------------------ | ------------------------------------ |
| **WiFi + Auto Failover** | Backup otomatis jika Ethernet putus  |
| **BLE Mobile Config**    | Setup 5 menit via smartphone         |
| **RTC Battery Backup**   | Timestamp akurat walau mati listrik  |
| **9 LED Indicator**      | Monitoring lengkap tanpa buka casing |
| **Support Lokal**        | Bahasa Indonesia, timezone WIB       |

**One-liner:** "Fitur premium, harga mid-range, support lokal."

---

## Saya ragu dengan merk baru, bagaimana?

Wajar ragu dengan brand baru. Fakta tentang SURIOTA:

| Aspek             | Fakta                                                 |
| ----------------- | ----------------------------------------------------- |
| **Perusahaan**    | PT Surya Inovasi Prioritas, legal terdaftar           |
| **Tim**           | Engineer ex-multinational dengan 10+ tahun pengalaman |
| **Garansi**       | 1.5 tahun (lebih panjang dari kompetitor)             |
| **Pilot Project** | Tersedia untuk testing sebelum order besar            |
| **Referensi**     | Bisa diberikan setelah NDA                            |

**Penawaran:** Ambil 1 unit untuk pilot project, evaluasi 30 hari.

---

## Bagaimana cara menjadi supplier/reseller SURIOTA?

Kami membuka program supplier untuk mitra bisnis:

| Tier       | Min Order | Diskon  | Harga Non-PoE    | Harga PoE        |
| ---------- | --------- | ------- | ---------------- | ---------------- |
| Tier 1     | 5 unit    | 20%     | Rp 2,160,000     | Rp 2,480,000     |
| **Tier 2** | 10 unit   | **25%** | **Rp 2,025,000** | **Rp 2,325,000** |
| Tier 3     | 25 unit   | 30%     | Rp 1,890,000     | Rp 2,170,000     |

**Syarat Supplier:**

- Memiliki usaha/toko resmi (online/offline)
- Mematuhi MAP (Minimum Advertised Price) = harga retail SURIOTA
- Payment: 50% DP, 50% sebelum kirim

**Benefit:**

- Margin supplier 20-30%
- Marketing material support
- Technical training
- Priority stock allocation

**Kesimpulan:** Hubungi sales@suriota.com dengan subject "Program Supplier" untuk info lebih lanjut.

---

## Berapa harga minimum jual untuk reseller?

SURIOTA menerapkan **MAP Policy** (Minimum Advertised Price):

| Model              | MAP (Harga Min Jual) | Keterangan                       |
| ------------------ | -------------------- | -------------------------------- |
| SRT-MGATE-1210     | Rp 2,700,000         | Sama dengan harga retail SURIOTA |
| SRT-MGATE-1210-POE | Rp 3,100,000         | Sama dengan harga retail SURIOTA |

**Kenapa Ada MAP:**

- Mencegah perang harga antar supplier
- Menjaga value perception produk
- Supplier compete di service, bukan harga

**Pelanggaran MAP:**

- Peringatan pertama → kedua → terminasi kerjasama

**Kesimpulan:** Supplier bebas jual diatas MAP, tapi DILARANG jual dibawah MAP.

---

# TEMPLATE KOSONG

Copy template ini untuk menambah FAQ baru:

```markdown
## [PERTANYAAN PELANGGAN]

[Jawaban singkat 1-2 kalimat]

| Kolom 1 | Kolom 2 | Kolom 3 |
| ------- | ------- | ------- |
| Data    | Data    | Data    |

**Kesimpulan:** [Rekomendasi/next step]
```

---

# QUICK RESPONSE CARD

Untuk jawaban cepat via WhatsApp/Chat:

| Pertanyaan          | Jawaban Singkat                                             |
| ------------------- | ----------------------------------------------------------- |
| Harga?              | "Rp 2.7jt (Standard) / Rp 3.1jt (PoE)"                      |
| Diskon?             | "5% untuk 10+ unit, hubungi sales untuk volume besar"       |
| Garansi?            | "1.5 tahun, termasuk defect dan komponen"                   |
| Bisa cloud X?       | "Ya, selama support MQTT pasti bisa"                        |
| Bedanya sama China? | "WiFi+BLE+RTC built-in, support lokal Indonesia"            |
| Lead time?          | "Ready stock 3-5 hari, indent 2-3 minggu"                   |
| COD?                | "Bisa untuk area Jabodetabek"                               |
| Jadi supplier?      | "Hubungi sales untuk program supplier dengan diskon 20-30%" |

---

## Kontak

**PT Surya Inovasi Prioritas (SURIOTA)**

|         |                   |
| ------- | ----------------- |
| Website | www.suriota.com   |
| Email   | sales@suriota.com |
| Phone   | +62 858-3567-2476 |

---

_Template Version: 1.1 | Updated: December 18, 2025_
_Changelog: Updated pricing (Rp 2.7M/3.1M), added supplier FAQ, added MAP policy_
