# SRICARE - Product Requirements Document (PRD)

## Dokumen Spesifikasi Produk

> Version 1.0 | January 2026
> Status: **Ready for Development**

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [User Personas](#2-user-personas)
3. [User Stories & Acceptance Criteria](#3-user-stories--acceptance-criteria)
4. [Functional Requirements](#4-functional-requirements)
5. [Non-Functional Requirements](#5-non-functional-requirements)
6. [Database Schema](#6-database-schema)
7. [API Specifications](#7-api-specifications)
8. [Integration Specifications](#8-integration-specifications)
9. [Security Requirements](#9-security-requirements)
10. [Testing Requirements](#10-testing-requirements)
11. [MVP Definition & Release Criteria](#11-mvp-definition--release-criteria)
12. [Success Metrics](#12-success-metrics)
13. [Risks & Mitigations](#13-risks--mitigations)

---

## 1. Product Overview

### 1.1 Vision Statement

Menjadi platform #1 untuk layanan pendampingan pasien dan home care di Indonesia, dimulai dari Batam.

### 1.2 Product Description

**SRICARE** adalah aplikasi mobile on-demand yang menghubungkan pengguna dengan Caregiver profesional untuk:

- Pendampingan pasien di rumah sakit
- Menemani cuci darah (hemodialisis)
- Menemani berobat ke dokter/klinik
- Perawatan lansia/pasien di rumah
- Antar-jemput medis

### 1.3 Target Users

| User Type     | Description                                     |
| ------------- | ----------------------------------------------- |
| **Customer**  | Perantau, keluarga dengan lansia, pasien kronis |
| **Caregiver** | Perawat, caregiver terlatih, pendamping pasien  |
| **Admin**     | Tim SURIOTA untuk operasional platform          |

### 1.4 Platform

| Platform           | Technology              |
| ------------------ | ----------------------- |
| Mobile (Customer)  | Flutter (iOS & Android) |
| Mobile (Caregiver) | Flutter (iOS & Android) |
| Admin Dashboard    | React.js / Next.js      |
| Backend API        | NestJS + PostgreSQL     |

---

## 2. User Personas

### 2.1 Persona: Customer - "Andi" (Pekerja Pabrik)

```yaml
Nama: Andi Prasetyo
Usia: 32 tahun
Pekerjaan: Operator Produksi di pabrik elektronik
Lokasi: Batam
Penghasilan: Rp 5-7 juta/bulan
Situasi: Ibunya (63 tahun) ikut tinggal di Batam
Status Keluarga: Menikah, 1 anak

Goals:
  - Memastikan ibu tetap sehat dan terawat
  - Tidak perlu izin kerja untuk antar ibu ke RS
  - Mendapat update kondisi ibu secara real-time

Pain Points:
  - Kerja shift, tidak bisa antar ibu ke RS
  - Khawatir saat ibu sendirian di RS
  - Tidak ada keluarga lain di Batam

Tech Savviness: Medium (familiar dengan Gojek, Shopee)
Device: Android mid-range (Xiaomi/Oppo)
Payment Preference: GoPay, OVO, QRIS
```

### 2.2 Persona: Customer - "Sari" (Profesional)

```yaml
Nama: Sari Wulandari
Usia: 38 tahun
Pekerjaan: Manager di perusahaan shipping
Lokasi: Batam
Penghasilan: Rp 15-20 juta/bulan
Situasi: Ayahnya (68 tahun) gagal ginjal, cuci darah 2x/minggu
Status Keluarga: Menikah, 2 anak

Goals:
  - Pendamping tetap untuk ayah cuci darah
  - Caregiver yang bisa dipercaya
  - Scheduling yang fleksibel

Pain Points:
  - Sibuk meeting, tidak bisa antar ayah setiap kali
  - Sulit cari pendamping yang reliable
  - Tidak ada tracking kondisi ayah

Tech Savviness: High (power user mobile apps)
Device: iPhone
Payment Preference: Credit Card, Apple Pay, Bank Transfer
```

### 2.3 Persona: Caregiver - "Dewi"

```yaml
Nama: Dewi Susanti
Usia: 28 tahun
Background: D3 Keperawatan
Pengalaman: 3 tahun di RS, 1 tahun freelance caregiver
Lokasi: Batam
Target Penghasilan: Rp 5-8 juta/bulan

Goals:
  - Penghasilan tambahan yang fleksibel
  - Jadwal kerja yang bisa diatur sendiri
  - Platform yang aman dan terpercaya

Pain Points:
  - Sulit dapat customer baru
  - Pembayaran sering telat (informal)
  - Tidak ada perlindungan/asuransi

Availability: Full-time available
Skills: Basic nursing, elderly care, HD companion
Transport: Motor pribadi
```

---

## 3. User Stories & Acceptance Criteria

### 3.1 Epic: User Registration & Authentication

#### US-001: Customer Registration

```gherkin
AS A new customer
I WANT TO register with my phone number
SO THAT I can book caregiver services

ACCEPTANCE CRITERIA:
  GIVEN I am on the registration screen
  WHEN I enter my phone number (format: 08xxxxxxxxxx)
  THEN I receive an OTP via SMS within 30 seconds

  GIVEN I received the OTP
  WHEN I enter the correct 6-digit OTP
  THEN my account is created
  AND I am prompted to complete my profile

  GIVEN I enter wrong OTP 3 times
  THEN I am blocked for 5 minutes
  AND shown "Too many attempts" message

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

#### US-002: Customer Profile Setup

```gherkin
AS A registered customer
I WANT TO complete my profile
SO THAT caregivers know who they're serving

ACCEPTANCE CRITERIA:
  GIVEN I am logged in for the first time
  WHEN I complete profile setup
  THEN I must provide:
    - Full name (required)
    - Email (optional)
    - Emergency contact name (required)
    - Emergency contact phone (required)
    - Address (optional, can add later)

  GIVEN I skip optional fields
  THEN I can still proceed to home screen
  AND see prompt to complete profile later

PRIORITY: P0 (Must Have)
STORY POINTS: 3
```

#### US-003: Caregiver Registration

```gherkin
AS A prospective caregiver
I WANT TO register and submit my documents
SO THAT I can be verified and start accepting jobs

ACCEPTANCE CRITERIA:
  GIVEN I am on caregiver registration
  WHEN I submit registration
  THEN I must provide:
    - Phone number (OTP verified)
    - Full name (as per KTP)
    - KTP photo (front)
    - Selfie with KTP
    - Certificate/training proof (optional)
    - Bank account details

  GIVEN I submitted all documents
  THEN status shows "Pending Verification"
  AND I receive confirmation SMS
  AND admin is notified for review

  GIVEN admin approves my registration
  THEN I can start accepting bookings
  AND I receive welcome notification

PRIORITY: P0 (Must Have)
STORY POINTS: 8
```

#### US-004: User Login

```gherkin
AS A registered user (customer/caregiver)
I WANT TO login with my phone number
SO THAT I can access my account

ACCEPTANCE CRITERIA:
  GIVEN I have a registered account
  WHEN I enter my phone number
  THEN I receive OTP via SMS

  GIVEN I enter correct OTP
  THEN I am logged in
  AND redirected to home screen
  AND my session is valid for 30 days

  GIVEN I am already logged in on another device
  THEN previous session is invalidated
  AND I am logged in on current device only

PRIORITY: P0 (Must Have)
STORY POINTS: 3
```

---

### 3.2 Epic: Service Booking

#### US-005: Browse Services

```gherkin
AS A customer
I WANT TO see available services
SO THAT I can choose the right service for my needs

ACCEPTANCE CRITERIA:
  GIVEN I am on home screen
  THEN I see service categories:
    - Hospital Companion (Pendamping RS)
    - Dialysis Support (Pendamping Cuci Darah)
    - Medical Escort (Menemani Berobat)
    - Home Care (Perawatan di Rumah)
    - Medical Transport (Antar Jemput Medis)

  GIVEN I tap on a service category
  THEN I see:
    - Service description
    - Price range
    - Duration options
    - "Book Now" button

PRIORITY: P0 (Must Have)
STORY POINTS: 3
```

#### US-006: Create Booking - Hospital Companion

```gherkin
AS A customer
I WANT TO book a hospital companion
SO THAT my family member has someone at the hospital

ACCEPTANCE CRITERIA:
  GIVEN I select "Hospital Companion" service
  WHEN I fill booking form
  THEN I must provide:
    - Hospital name (dropdown + search)
    - Patient name
    - Room/bed number (optional)
    - Start date & time
    - Duration (per jam / 6 jam / 12 jam / 24 jam)
    - Special notes (optional)

  GIVEN I submitted booking form
  THEN I see price calculation
  AND list of available caregivers nearby
  AND estimated arrival time

  GIVEN I select a caregiver
  THEN I proceed to payment screen

PRIORITY: P0 (Must Have)
STORY POINTS: 8
```

#### US-007: Create Booking - Dialysis Support

```gherkin
AS A customer
I WANT TO book dialysis support
SO THAT my family member has companion during hemodialysis

ACCEPTANCE CRITERIA:
  GIVEN I select "Dialysis Support" service
  WHEN I fill booking form
  THEN I must provide:
    - Pickup location (GPS/manual input)
    - Hospital/Clinic for HD
    - Schedule date & time
    - Package type:
      - Basic (HD only, no transport)
      - With Transport (pickup + HD + drop-off)
      - Monthly 8x
      - Monthly 12x
    - Patient name
    - Patient condition notes (optional)

  GIVEN I select monthly package
  THEN I must select all scheduled dates
  AND see total package price

PRIORITY: P0 (Must Have)
STORY POINTS: 8
```

#### US-008: Caregiver Selection

```gherkin
AS A customer
I WANT TO see and choose from available caregivers
SO THAT I can pick the most suitable one

ACCEPTANCE CRITERIA:
  GIVEN I submitted booking details
  THEN I see list of caregivers sorted by:
    - Distance (nearest first)
    - Rating (highest first)
    - Price (can toggle)

  FOR EACH caregiver shown:
    - Profile photo
    - Name
    - Rating (stars + count)
    - Distance from pickup/hospital
    - Experience badge (if any)
    - Price for selected service
    - "View Profile" link

  GIVEN I tap "View Profile"
  THEN I see:
    - Full bio
    - Skills/certifications
    - Reviews (latest 5)
    - Completed jobs count
    - Response rate

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

#### US-009: Booking Payment

```gherkin
AS A customer
I WANT TO pay for my booking
SO THAT the booking is confirmed

ACCEPTANCE CRITERIA:
  GIVEN I selected a caregiver
  WHEN I proceed to payment
  THEN I see:
    - Order summary (service, date, duration)
    - Caregiver details
    - Price breakdown:
      - Base price
      - Platform fee (included)
      - Promo discount (if any)
      - Total amount
    - Payment method options:
      - QRIS
      - GoPay
      - OVO
      - DANA
      - ShopeePay
      - Virtual Account (BCA, Mandiri, BNI, BRI)
    - Promo code input field

  GIVEN I select payment method and confirm
  THEN I am redirected to payment gateway

  GIVEN payment is successful
  THEN:
    - Booking status = "Confirmed"
    - I receive confirmation notification
    - Caregiver receives job notification
    - I see booking details screen

PRIORITY: P0 (Must Have)
STORY POINTS: 8
```

---

### 3.3 Epic: Real-time Tracking & Communication

#### US-010: Track Caregiver Location

```gherkin
AS A customer
I WANT TO track caregiver location in real-time
SO THAT I know when they will arrive

ACCEPTANCE CRITERIA:
  GIVEN booking is confirmed
  AND caregiver has accepted the job
  WHEN caregiver is en route
  THEN I see:
    - Map with caregiver location (live)
    - ETA to pickup/hospital
    - Caregiver status (On the way / Arrived / In Progress)

  GIVEN caregiver location updates
  THEN map refreshes every 10 seconds

  GIVEN caregiver arrives at location
  THEN I receive push notification "Caregiver has arrived"

PRIORITY: P1 (Should Have)
STORY POINTS: 8
```

#### US-011: In-App Chat

```gherkin
AS A customer
I WANT TO chat with my booked caregiver
SO THAT I can coordinate and communicate

ACCEPTANCE CRITERIA:
  GIVEN I have an active booking
  WHEN I open chat
  THEN I can:
    - Send text messages
    - Send photos
    - See message status (sent/delivered/read)
    - See caregiver online status

  GIVEN caregiver sends message
  THEN I receive push notification
  AND message appears in chat

  GIVEN booking is completed
  THEN chat is archived
  AND accessible for 7 days

PRIORITY: P1 (Should Have)
STORY POINTS: 5
```

#### US-012: Activity Updates

```gherkin
AS A customer
I WANT TO receive updates about patient condition
SO THAT I know my family member is okay

ACCEPTANCE CRITERIA:
  GIVEN service is in progress
  WHEN caregiver sends update
  THEN I receive notification with:
    - Update type (Check-in / Activity / Alert)
    - Message text
    - Photo (optional)
    - Timestamp

  GIVEN it's an Alert type update
  THEN notification is HIGH priority
  AND phone vibrates/rings

PRIORITY: P1 (Should Have)
STORY POINTS: 5
```

---

### 3.4 Epic: Caregiver App

#### US-013: View Available Jobs

```gherkin
AS A caregiver
I WANT TO see available job requests near me
SO THAT I can accept work

ACCEPTANCE CRITERIA:
  GIVEN I am online and verified
  WHEN new booking is created near me
  THEN I receive notification
  AND job appears in my "Available Jobs" list

  FOR EACH job shown:
    - Service type
    - Location (hospital/address)
    - Distance from my location
    - Date & time
    - Duration
    - Estimated earnings
    - Time remaining to accept

  GIVEN job is not accepted within 5 minutes
  THEN it's offered to next caregiver

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

#### US-014: Accept/Reject Job

```gherkin
AS A caregiver
I WANT TO accept or reject job requests
SO THAT I can manage my schedule

ACCEPTANCE CRITERIA:
  GIVEN I view a job request
  WHEN I tap "Accept"
  THEN:
    - Job is assigned to me
    - Customer is notified
    - Job moves to "My Jobs" list
    - I see customer contact details

  GIVEN I tap "Reject"
  THEN:
    - Job is removed from my list
    - Job is offered to next caregiver
    - My acceptance rate is updated

  GIVEN I don't respond within timeout
  THEN job auto-expires from my list

PRIORITY: P0 (Must Have)
STORY POINTS: 3
```

#### US-015: Start & Complete Service

```gherkin
AS A caregiver
I WANT TO mark service start and completion
SO THAT the system tracks my work accurately

ACCEPTANCE CRITERIA:
  GIVEN I arrived at location
  WHEN I tap "Start Service"
  THEN:
    - GPS location is verified
    - Service timer starts
    - Customer receives notification
    - Status = "In Progress"

  GIVEN I am not at correct location (>500m)
  THEN I cannot start service
  AND shown error message

  GIVEN service is complete
  WHEN I tap "Complete Service"
  THEN:
    - I must add completion notes
    - I can add photos (optional)
    - Service timer stops
    - Customer receives notification
    - Customer prompted to rate

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

#### US-016: Caregiver Earnings

```gherkin
AS A caregiver
I WANT TO see my earnings and request payout
SO THAT I can manage my income

ACCEPTANCE CRITERIA:
  GIVEN I completed jobs
  THEN I see:
    - Today's earnings
    - This week's earnings
    - This month's earnings
    - Available balance
    - Pending balance (not yet released)
    - Transaction history

  GIVEN I have available balance >= Rp 100,000
  WHEN I request payout
  THEN:
    - I select payout method (Bank/E-wallet)
    - I confirm payout amount
    - Payout is processed within 24 hours (bank) / instant (e-wallet)

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

---

### 3.5 Epic: Rating & Review

#### US-017: Rate Caregiver

```gherkin
AS A customer
I WANT TO rate and review my caregiver
SO THAT others can make informed decisions

ACCEPTANCE CRITERIA:
  GIVEN service is completed
  THEN I am prompted to rate within 24 hours

  WHEN I submit rating
  THEN I must provide:
    - Star rating (1-5, required)
    - Written review (optional, min 10 chars if provided)
    - Tags (optional): Punctual, Professional, Caring, Communicative

  GIVEN I don't rate within 72 hours
  THEN rating window closes
  AND system auto-rates 5 stars

PRIORITY: P1 (Should Have)
STORY POINTS: 3
```

#### US-018: Rate Customer

```gherkin
AS A caregiver
I WANT TO rate the customer
SO THAT I can flag problematic customers

ACCEPTANCE CRITERIA:
  GIVEN service is completed
  THEN I can rate customer:
    - Star rating (1-5)
    - Notes (internal, not shown to customer)

  GIVEN customer has <3.5 average rating
  THEN caregiver sees warning before accepting job

PRIORITY: P2 (Nice to Have)
STORY POINTS: 2
```

---

### 3.6 Epic: Booking Management

#### US-019: View Booking History

```gherkin
AS A customer
I WANT TO see my booking history
SO THAT I can track past services

ACCEPTANCE CRITERIA:
  GIVEN I am logged in
  WHEN I go to "My Bookings"
  THEN I see tabs:
    - Active (ongoing bookings)
    - Scheduled (upcoming)
    - Completed
    - Cancelled

  FOR EACH booking:
    - Service type icon
    - Date & time
    - Caregiver name & photo
    - Status badge
    - Total amount

PRIORITY: P1 (Should Have)
STORY POINTS: 3
```

#### US-020: Cancel Booking

```gherkin
AS A customer
I WANT TO cancel my booking
SO THAT I can change my plans

ACCEPTANCE CRITERIA:
  GIVEN I have a confirmed booking
  WHEN I tap "Cancel Booking"
  THEN I see cancellation policy:
    - >24 hours before: Full refund
    - 12-24 hours before: 50% refund
    - <12 hours before: No refund

  GIVEN I confirm cancellation
  THEN:
    - Booking status = "Cancelled"
    - Refund is processed (if applicable)
    - Caregiver is notified
    - Caregiver's schedule is freed

PRIORITY: P0 (Must Have)
STORY POINTS: 5
```

#### US-021: Reschedule Booking

```gherkin
AS A customer
I WANT TO reschedule my booking
SO THAT I can adjust to changes

ACCEPTANCE CRITERIA:
  GIVEN I have a confirmed booking
  AND booking is >6 hours away
  WHEN I tap "Reschedule"
  THEN I can select new date/time

  GIVEN caregiver is available at new time
  THEN booking is rescheduled
  AND both parties notified

  GIVEN caregiver is NOT available
  THEN I am offered to:
    - Find another caregiver
    - Choose different time
    - Cancel booking

PRIORITY: P1 (Should Have)
STORY POINTS: 5
```

---

## 4. Functional Requirements

### 4.1 Customer App Features

| ID    | Feature                | Priority | Notes                                     |
| ----- | ---------------------- | -------- | ----------------------------------------- |
| F-C01 | Phone OTP Registration | P0       | SMS via Twilio/local provider             |
| F-C02 | Profile Management     | P0       | Name, photo, addresses, emergency contact |
| F-C03 | Service Catalog        | P0       | 5 service categories                      |
| F-C04 | Booking Creation       | P0       | Form varies by service type               |
| F-C05 | Caregiver Selection    | P0       | Sort by distance, rating, price           |
| F-C06 | Payment Integration    | P0       | Midtrans (QRIS, e-wallet, VA)             |
| F-C07 | Real-time Tracking     | P1       | Map with caregiver location               |
| F-C08 | In-app Chat            | P1       | Text + photo                              |
| F-C09 | Push Notifications     | P0       | Booking updates, messages                 |
| F-C10 | Booking History        | P1       | Active, scheduled, completed, cancelled   |
| F-C11 | Cancel/Reschedule      | P0       | With refund policy                        |
| F-C12 | Rating & Review        | P1       | Stars + text + tags                       |
| F-C13 | Promo Code             | P1       | Discount application                      |
| F-C14 | Favorite Caregivers    | P2       | Save preferred caregivers                 |
| F-C15 | Multiple Addresses     | P1       | Home, office, hospital                    |

### 4.2 Caregiver App Features

| ID    | Feature                     | Priority | Notes                            |
| ----- | --------------------------- | -------- | -------------------------------- |
| F-G01 | Registration + Verification | P0       | KTP, selfie, documents           |
| F-G02 | Profile Management          | P0       | Bio, skills, experience          |
| F-G03 | Online/Offline Toggle       | P0       | Control availability             |
| F-G04 | Job Notifications           | P0       | Push + sound                     |
| F-G05 | Accept/Reject Jobs          | P0       | With timeout                     |
| F-G06 | Job Details View            | P0       | Customer info, location, notes   |
| F-G07 | Navigation Integration      | P1       | Open in Google Maps              |
| F-G08 | Start/Complete Service      | P0       | GPS verification                 |
| F-G09 | Activity Updates            | P1       | Send updates to customer         |
| F-G10 | In-app Chat                 | P1       | With customer                    |
| F-G11 | Earnings Dashboard          | P0       | Daily, weekly, monthly           |
| F-G12 | Payout Request              | P0       | Bank + e-wallet                  |
| F-G13 | Schedule Management         | P1       | Set unavailable dates            |
| F-G14 | Rating History              | P1       | View customer ratings            |
| F-G15 | Performance Stats           | P2       | Acceptance rate, completion rate |

### 4.3 Admin Dashboard Features

| ID    | Feature                | Priority | Notes                        |
| ----- | ---------------------- | -------- | ---------------------------- |
| F-A01 | Caregiver Verification | P0       | Approve/reject registration  |
| F-A02 | User Management        | P0       | View, suspend, ban           |
| F-A03 | Booking Management     | P0       | View all bookings, intervene |
| F-A04 | Dispute Resolution     | P0       | Handle complaints            |
| F-A05 | Payout Management      | P0       | Approve, process, track      |
| F-A06 | Analytics Dashboard    | P1       | GMV, transactions, users     |
| F-A07 | Promo Code Management  | P1       | Create, edit, deactivate     |
| F-A08 | Service Configuration  | P1       | Prices, categories, options  |
| F-A09 | Notification Broadcast | P2       | Send to all users            |
| F-A10 | Report Generation      | P2       | Export to Excel/PDF          |

---

## 5. Non-Functional Requirements

### 5.1 Performance

| Metric             | Requirement      | Notes               |
| ------------------ | ---------------- | ------------------- |
| App Launch Time    | < 3 seconds      | Cold start          |
| API Response Time  | < 500ms          | P95                 |
| Map Loading        | < 2 seconds      | Initial load        |
| Location Update    | Every 10 seconds | During tracking     |
| Push Notification  | < 5 seconds      | After event trigger |
| Payment Processing | < 30 seconds     | End-to-end          |

### 5.2 Scalability

| Metric             | MVP Target | Year 1 Target |
| ------------------ | ---------- | ------------- |
| Concurrent Users   | 500        | 5,000         |
| Daily Transactions | 50         | 500           |
| Database Size      | 10 GB      | 100 GB        |
| API Requests/min   | 1,000      | 10,000        |

### 5.3 Availability

| Metric               | Requirement     |
| -------------------- | --------------- |
| Uptime SLA           | 99.5%           |
| Planned Maintenance  | < 4 hours/month |
| Recovery Time (RTO)  | < 4 hours       |
| Recovery Point (RPO) | < 1 hour        |

### 5.4 Compatibility

| Platform    | Minimum Version                     |
| ----------- | ----------------------------------- |
| Android     | 6.0 (API 23)                        |
| iOS         | 12.0                                |
| Web (Admin) | Chrome 90+, Firefox 88+, Safari 14+ |

### 5.5 Localization

| Aspect       | Requirement                                     |
| ------------ | ----------------------------------------------- |
| Language     | Bahasa Indonesia (primary), English (secondary) |
| Timezone     | WIB (UTC+7) default                             |
| Currency     | IDR only                                        |
| Phone Format | +62 / 08xx                                      |
| Date Format  | DD/MM/YYYY                                      |

---

## 6. Database Schema

### 6.1 Entity Relationship Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    USERS    │───────│  BOOKINGS   │───────│  SERVICES   │
└─────────────┘       └─────────────┘       └─────────────┘
      │                     │
      │                     │
      ▼                     ▼
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│  ADDRESSES  │       │  PAYMENTS   │       │  REVIEWS    │
└─────────────┘       └─────────────┘       └─────────────┘
                            │
                            ▼
                      ┌─────────────┐
                      │  PAYOUTS    │
                      └─────────────┘
```

### 6.2 Table Definitions

#### users

```sql
CREATE TABLE users (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  phone           VARCHAR(15) UNIQUE NOT NULL,
  email           VARCHAR(255),
  full_name       VARCHAR(100) NOT NULL,
  profile_photo   VARCHAR(500),
  role            ENUM('customer', 'caregiver', 'admin') NOT NULL,
  status          ENUM('pending', 'active', 'suspended', 'banned') DEFAULT 'pending',
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  last_login      TIMESTAMP,
  fcm_token       VARCHAR(500),

  -- Customer specific
  emergency_contact_name  VARCHAR(100),
  emergency_contact_phone VARCHAR(15),

  -- Caregiver specific
  ktp_number      VARCHAR(20),
  ktp_photo       VARCHAR(500),
  selfie_photo    VARCHAR(500),
  bank_name       VARCHAR(50),
  bank_account    VARCHAR(30),
  bank_holder     VARCHAR(100),
  is_online       BOOLEAN DEFAULT FALSE,
  rating_avg      DECIMAL(2,1) DEFAULT 0,
  rating_count    INT DEFAULT 0,
  completed_jobs  INT DEFAULT 0,
  verification_date TIMESTAMP
);

CREATE INDEX idx_users_phone ON users(phone);
CREATE INDEX idx_users_role_status ON users(role, status);
CREATE INDEX idx_caregiver_online ON users(role, is_online) WHERE role = 'caregiver';
```

#### addresses

```sql
CREATE TABLE addresses (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id         UUID REFERENCES users(id) ON DELETE CASCADE,
  label           VARCHAR(50) NOT NULL, -- 'Home', 'Office', 'Hospital'
  full_address    TEXT NOT NULL,
  latitude        DECIMAL(10, 8) NOT NULL,
  longitude       DECIMAL(11, 8) NOT NULL,
  notes           TEXT,
  is_default      BOOLEAN DEFAULT FALSE,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_addresses_user ON addresses(user_id);
```

#### services

```sql
CREATE TABLE services (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code            VARCHAR(20) UNIQUE NOT NULL, -- 'HOSPITAL', 'DIALYSIS', etc.
  name            VARCHAR(100) NOT NULL,
  name_id         VARCHAR(100) NOT NULL, -- Indonesian name
  description     TEXT,
  description_id  TEXT,
  icon            VARCHAR(50),
  is_active       BOOLEAN DEFAULT TRUE,
  sort_order      INT DEFAULT 0,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Service pricing options
CREATE TABLE service_options (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  service_id      UUID REFERENCES services(id) ON DELETE CASCADE,
  name            VARCHAR(100) NOT NULL,
  name_id         VARCHAR(100) NOT NULL,
  duration_hours  INT,
  price           DECIMAL(12, 2) NOT NULL,
  is_active       BOOLEAN DEFAULT TRUE,
  sort_order      INT DEFAULT 0
);
```

#### bookings

```sql
CREATE TABLE bookings (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  booking_code    VARCHAR(20) UNIQUE NOT NULL, -- 'SRI-20260110-001'
  customer_id     UUID REFERENCES users(id),
  caregiver_id    UUID REFERENCES users(id),
  service_id      UUID REFERENCES services(id),
  service_option_id UUID REFERENCES service_options(id),

  -- Status
  status          ENUM('pending', 'confirmed', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',

  -- Schedule
  scheduled_date  DATE NOT NULL,
  scheduled_time  TIME NOT NULL,
  duration_hours  INT NOT NULL,
  actual_start    TIMESTAMP,
  actual_end      TIMESTAMP,

  -- Location
  pickup_address  TEXT,
  pickup_lat      DECIMAL(10, 8),
  pickup_lng      DECIMAL(11, 8),
  destination_address TEXT, -- Hospital/clinic name
  destination_lat DECIMAL(10, 8),
  destination_lng DECIMAL(11, 8),

  -- Patient Info
  patient_name    VARCHAR(100),
  patient_notes   TEXT,

  -- Pricing
  base_price      DECIMAL(12, 2) NOT NULL,
  platform_fee    DECIMAL(12, 2) NOT NULL,
  discount        DECIMAL(12, 2) DEFAULT 0,
  total_amount    DECIMAL(12, 2) NOT NULL,
  caregiver_earnings DECIMAL(12, 2) NOT NULL,

  -- Promo
  promo_code      VARCHAR(20),

  -- Completion
  completion_notes TEXT,
  completion_photos TEXT[], -- Array of URLs

  -- Cancellation
  cancelled_by    ENUM('customer', 'caregiver', 'admin'),
  cancel_reason   TEXT,
  refund_amount   DECIMAL(12, 2),

  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_bookings_customer ON bookings(customer_id);
CREATE INDEX idx_bookings_caregiver ON bookings(caregiver_id);
CREATE INDEX idx_bookings_status ON bookings(status);
CREATE INDEX idx_bookings_date ON bookings(scheduled_date);
```

#### payments

```sql
CREATE TABLE payments (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  booking_id      UUID REFERENCES bookings(id),

  -- Midtrans
  payment_type    VARCHAR(20) NOT NULL, -- 'qris', 'gopay', 'bca_va', etc.
  transaction_id  VARCHAR(100), -- Midtrans transaction_id
  order_id        VARCHAR(100) UNIQUE NOT NULL, -- Our order ID

  amount          DECIMAL(12, 2) NOT NULL,
  status          ENUM('pending', 'paid', 'failed', 'refunded', 'expired') DEFAULT 'pending',

  -- Timestamps
  paid_at         TIMESTAMP,
  expired_at      TIMESTAMP,
  refunded_at     TIMESTAMP,

  -- Midtrans response
  payment_response JSONB,

  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_payments_booking ON payments(booking_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_order ON payments(order_id);
```

#### payouts

```sql
CREATE TABLE payouts (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  caregiver_id    UUID REFERENCES users(id),

  amount          DECIMAL(12, 2) NOT NULL,
  fee             DECIMAL(12, 2) DEFAULT 0,
  net_amount      DECIMAL(12, 2) NOT NULL,

  method          ENUM('bank_transfer', 'gopay', 'ovo', 'dana') NOT NULL,
  destination     VARCHAR(100) NOT NULL, -- Bank account or e-wallet number

  status          ENUM('pending', 'processing', 'completed', 'failed') DEFAULT 'pending',

  processed_at    TIMESTAMP,
  completed_at    TIMESTAMP,
  failed_reason   TEXT,

  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_payouts_caregiver ON payouts(caregiver_id);
CREATE INDEX idx_payouts_status ON payouts(status);
```

#### reviews

```sql
CREATE TABLE reviews (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  booking_id      UUID REFERENCES bookings(id),
  reviewer_id     UUID REFERENCES users(id), -- Customer
  reviewee_id     UUID REFERENCES users(id), -- Caregiver

  rating          INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
  comment         TEXT,
  tags            VARCHAR(50)[], -- ['Punctual', 'Professional', 'Caring']

  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reviews_reviewee ON reviews(reviewee_id);
```

#### caregiver_locations

```sql
CREATE TABLE caregiver_locations (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  caregiver_id    UUID REFERENCES users(id) ON DELETE CASCADE,
  latitude        DECIMAL(10, 8) NOT NULL,
  longitude       DECIMAL(11, 8) NOT NULL,
  accuracy        INT, -- meters
  updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_location_caregiver ON caregiver_locations(caregiver_id);
CREATE INDEX idx_location_geo ON caregiver_locations USING GIST (
  ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)
);
```

#### chat_messages

```sql
CREATE TABLE chat_messages (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  booking_id      UUID REFERENCES bookings(id) ON DELETE CASCADE,
  sender_id       UUID REFERENCES users(id),

  message_type    ENUM('text', 'image', 'activity_update') DEFAULT 'text',
  content         TEXT NOT NULL,
  image_url       VARCHAR(500),

  is_read         BOOLEAN DEFAULT FALSE,
  read_at         TIMESTAMP,

  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_chat_booking ON chat_messages(booking_id);
CREATE INDEX idx_chat_created ON chat_messages(created_at);
```

#### promo_codes

```sql
CREATE TABLE promo_codes (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  code            VARCHAR(20) UNIQUE NOT NULL,

  discount_type   ENUM('percentage', 'fixed') NOT NULL,
  discount_value  DECIMAL(12, 2) NOT NULL,
  max_discount    DECIMAL(12, 2), -- For percentage type
  min_order       DECIMAL(12, 2) DEFAULT 0,

  usage_limit     INT, -- NULL = unlimited
  usage_count     INT DEFAULT 0,
  per_user_limit  INT DEFAULT 1,

  valid_from      TIMESTAMP NOT NULL,
  valid_until     TIMESTAMP NOT NULL,

  is_active       BOOLEAN DEFAULT TRUE,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_promo_code ON promo_codes(code);
CREATE INDEX idx_promo_active ON promo_codes(is_active, valid_until);
```

---

## 7. API Specifications

### 7.1 API Standards

| Aspect         | Standard                     |
| -------------- | ---------------------------- |
| Protocol       | HTTPS only                   |
| Format         | JSON                         |
| Authentication | JWT Bearer Token             |
| Versioning     | URL path (/api/v1/)          |
| Rate Limiting  | 100 requests/minute per user |

### 7.2 Authentication Endpoints

#### POST /api/v1/auth/request-otp

Request OTP for login/registration.

```json
// Request
{
  "phone": "081234567890",
  "type": "customer" // or "caregiver"
}

// Response 200
{
  "success": true,
  "message": "OTP sent",
  "data": {
    "expires_in": 300,
    "retry_after": 60
  }
}

// Response 429 (Too Many Requests)
{
  "success": false,
  "error": {
    "code": "OTP_RATE_LIMITED",
    "message": "Please wait 5 minutes before requesting another OTP"
  }
}
```

#### POST /api/v1/auth/verify-otp

Verify OTP and get JWT token.

```json
// Request
{
  "phone": "081234567890",
  "otp": "123456",
  "type": "customer"
}

// Response 200
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_in": 2592000, // 30 days
    "user": {
      "id": "uuid",
      "phone": "081234567890",
      "full_name": "John Doe",
      "role": "customer",
      "is_new": false
    }
  }
}

// Response 400 (Invalid OTP)
{
  "success": false,
  "error": {
    "code": "INVALID_OTP",
    "message": "Invalid or expired OTP"
  }
}
```

### 7.3 Booking Endpoints

#### GET /api/v1/services

Get available services.

```json
// Response 200
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "code": "HOSPITAL",
      "name": "Hospital Companion",
      "name_id": "Pendamping RS",
      "description": "Accompany patient at hospital",
      "description_id": "Menemani pasien di rumah sakit",
      "icon": "hospital",
      "options": [
        {
          "id": "uuid",
          "name": "Per Hour",
          "name_id": "Per Jam",
          "duration_hours": 1,
          "price": 50000
        },
        {
          "id": "uuid",
          "name": "6 Hours",
          "name_id": "6 Jam",
          "duration_hours": 6,
          "price": 250000
        }
      ]
    }
  ]
}
```

#### POST /api/v1/bookings

Create new booking.

```json
// Request
{
  "service_id": "uuid",
  "service_option_id": "uuid",
  "scheduled_date": "2026-01-15",
  "scheduled_time": "08:00",
  "pickup_address": "Jl. Sudirman No. 123",
  "pickup_lat": 1.0456,
  "pickup_lng": 104.0302,
  "destination_address": "RS Awal Bros Batam",
  "destination_lat": 1.0512,
  "destination_lng": 104.0356,
  "patient_name": "Ibu Sari",
  "patient_notes": "Butuh kursi roda",
  "promo_code": "SRICARE50"
}

// Response 201
{
  "success": true,
  "data": {
    "booking_id": "uuid",
    "booking_code": "SRI-20260115-001",
    "status": "pending",
    "price_breakdown": {
      "base_price": 250000,
      "platform_fee": 0,
      "discount": 50000,
      "total_amount": 200000
    },
    "available_caregivers": [
      {
        "id": "uuid",
        "name": "Dewi Susanti",
        "photo": "https://...",
        "rating": 4.8,
        "rating_count": 45,
        "distance_km": 2.3,
        "price": 200000
      }
    ]
  }
}
```

#### POST /api/v1/bookings/{id}/select-caregiver

Select caregiver for booking.

```json
// Request
{
  "caregiver_id": "uuid"
}

// Response 200
{
  "success": true,
  "data": {
    "booking_id": "uuid",
    "booking_code": "SRI-20260115-001",
    "status": "pending_payment",
    "caregiver": {
      "id": "uuid",
      "name": "Dewi Susanti",
      "phone": "08123456****" // Masked
    },
    "payment_deadline": "2026-01-15T07:30:00Z",
    "total_amount": 200000
  }
}
```

#### POST /api/v1/bookings/{id}/pay

Initiate payment.

```json
// Request
{
  "payment_method": "gopay"
}

// Response 200
{
  "success": true,
  "data": {
    "payment_id": "uuid",
    "order_id": "SRI-PAY-20260115-001",
    "payment_type": "gopay",
    "amount": 200000,
    "deeplink_url": "gojek://gopay/...", // For e-wallet
    "qr_code_url": "https://...", // For QRIS
    "va_number": "12345678901234", // For VA
    "expires_at": "2026-01-15T08:00:00Z"
  }
}
```

### 7.4 Webhook Endpoints

#### POST /api/v1/webhooks/midtrans

Handle Midtrans payment notifications.

```json
// Midtrans sends
{
  "transaction_status": "settlement",
  "order_id": "SRI-PAY-20260115-001",
  "payment_type": "gopay",
  "gross_amount": "200000.00",
  "signature_key": "..."
}

// Our response
{
  "success": true
}
```

### 7.5 Real-time Events (Socket.IO)

```javascript
// Events emitted by server
'booking:status_changed'    // Booking status update
'caregiver:location'        // Caregiver location update
'chat:new_message'          // New chat message
'activity:update'           // Caregiver activity update

// Events emitted by client (Caregiver)
'location:update'           // Send current location
'job:accept'                // Accept job
'job:reject'                // Reject job
'service:start'             // Start service
'service:complete'          // Complete service

// Event payloads
{
  "event": "booking:status_changed",
  "data": {
    "booking_id": "uuid",
    "status": "in_progress",
    "timestamp": "2026-01-15T08:00:00Z"
  }
}

{
  "event": "caregiver:location",
  "data": {
    "booking_id": "uuid",
    "lat": 1.0456,
    "lng": 104.0302,
    "timestamp": "2026-01-15T08:00:00Z"
  }
}
```

---

## 8. Integration Specifications

### 8.1 Payment Gateway - Midtrans

| Aspect            | Detail                                                                           |
| ----------------- | -------------------------------------------------------------------------------- |
| Mode              | Snap (hosted payment page) + Core API                                            |
| Environment       | Sandbox (dev) → Production                                                       |
| Supported Methods | QRIS, GoPay, OVO, DANA, ShopeePay, LinkAja, VA (BCA, Mandiri, BNI, BRI, Permata) |

**Configuration:**

```yaml
# Sandbox
MIDTRANS_SERVER_KEY: SB-Mid-server-xxx
MIDTRANS_CLIENT_KEY: SB-Mid-client-xxx
MIDTRANS_MERCHANT_ID: G123456789
MIDTRANS_IS_PRODUCTION: false

# Production
MIDTRANS_SERVER_KEY: Mid-server-xxx
MIDTRANS_CLIENT_KEY: Mid-client-xxx
MIDTRANS_IS_PRODUCTION: true
```

**Webhook URL:**

- Sandbox: `https://api-dev.sricare.id/api/v1/webhooks/midtrans`
- Production: `https://api.sricare.id/api/v1/webhooks/midtrans`

### 8.2 SMS Gateway - OTP

**Option 1: Twilio**

```yaml
TWILIO_ACCOUNT_SID: ACxxxxx
TWILIO_AUTH_TOKEN: xxxxx
TWILIO_PHONE_NUMBER: +15005550006
```

**Option 2: Local Provider (Recommended for Indonesia)**

- Wavecell
- Infobip
- Mainapi

```yaml
SMS_PROVIDER: wavecell
SMS_API_KEY: xxxxx
SMS_SENDER_ID: SRICARE
```

### 8.3 Push Notifications - Firebase Cloud Messaging

```yaml
FIREBASE_PROJECT_ID: sricare-app
FIREBASE_PRIVATE_KEY: "-----BEGIN PRIVATE KEY-----\n..."
FIREBASE_CLIENT_EMAIL: firebase-adminsdk-xxx@sricare-app.iam.gserviceaccount.com
```

**Notification Topics:**

- `/topics/all` - Broadcast
- `/topics/customers` - All customers
- `/topics/caregivers` - All caregivers

### 8.4 Maps - Google Maps / Mapbox

```yaml
# Google Maps (Android)
GOOGLE_MAPS_API_KEY: AIzaSyxxxxx

# Mapbox (Alternative)
MAPBOX_ACCESS_TOKEN: pk.eyJ1Ijoixxx
```

**Features Used:**

- Places Autocomplete
- Directions API
- Distance Matrix
- Static Maps

### 8.5 Cloud Storage - AWS S3 / DigitalOcean Spaces

```yaml
# AWS S3
AWS_ACCESS_KEY_ID: AKIAxxxxx
AWS_SECRET_ACCESS_KEY: xxxxx
AWS_BUCKET: sricare-uploads
AWS_REGION: ap-southeast-1

# Or DigitalOcean Spaces
DO_SPACES_KEY: xxxxx
DO_SPACES_SECRET: xxxxx
DO_SPACES_BUCKET: sricare-uploads
DO_SPACES_REGION: sgp1
DO_SPACES_ENDPOINT: https://sgp1.digitaloceanspaces.com
```

**Buckets/Folders:**

- `/profiles/` - User profile photos
- `/ktp/` - KTP documents (private)
- `/chat/` - Chat images
- `/bookings/` - Completion photos

---

## 9. Security Requirements

### 9.1 Authentication & Authorization

| Requirement         | Implementation             |
| ------------------- | -------------------------- |
| Token Type          | JWT (RS256)                |
| Access Token Expiry | 30 days                    |
| Refresh Token       | Yes, rotate on use         |
| Phone Verification  | OTP via SMS                |
| Session Management  | Single device only         |
| Role-based Access   | customer, caregiver, admin |

### 9.2 Data Protection

| Data Type     | Protection                              |
| ------------- | --------------------------------------- |
| Passwords     | Not applicable (OTP-based)              |
| Phone Numbers | Masked in logs                          |
| KTP Documents | Encrypted at rest, private bucket       |
| Payment Data  | Handled by Midtrans (PCI-DSS)           |
| Location Data | Stored temporarily, purged after 7 days |
| Chat Messages | Encrypted in transit (TLS)              |

### 9.3 API Security

| Measure          | Implementation                 |
| ---------------- | ------------------------------ |
| HTTPS            | TLS 1.3 required               |
| Rate Limiting    | 100 req/min per user           |
| Input Validation | Joi / class-validator          |
| SQL Injection    | Parameterized queries (Prisma) |
| XSS              | Sanitize user inputs           |
| CORS             | Whitelist origins              |

### 9.4 Document Verification

```yaml
# KTP Verification Flow
1. User uploads KTP photo
2. System validates file (size, type)
3. Store in private S3 bucket
4. Admin reviews manually
5. After verification, original file encrypted

# Future: OCR Integration
- Google Vision API
- AWS Textract
```

### 9.5 Audit Logging

```sql
CREATE TABLE audit_logs (
  id          UUID PRIMARY KEY,
  user_id     UUID,
  action      VARCHAR(50), -- 'LOGIN', 'BOOKING_CREATE', 'PAYMENT', etc.
  entity      VARCHAR(50), -- 'booking', 'user', 'payment'
  entity_id   UUID,
  ip_address  INET,
  user_agent  TEXT,
  payload     JSONB,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 10. Testing Requirements

### 10.1 Testing Strategy

| Test Type         | Coverage Target | Tools                         |
| ----------------- | --------------- | ----------------------------- |
| Unit Tests        | 70%             | Jest                          |
| Integration Tests | Critical paths  | Jest + Supertest              |
| E2E Tests         | Happy paths     | Detox (mobile), Cypress (web) |
| Performance Tests | Load testing    | k6, Artillery                 |
| Security Tests    | OWASP Top 10    | Manual + ZAP                  |

### 10.2 Critical Test Cases

#### Authentication

| ID     | Test Case                          | Expected Result              |
| ------ | ---------------------------------- | ---------------------------- |
| TC-A01 | Register with valid phone          | OTP sent, can login          |
| TC-A02 | Register with invalid phone format | Error message                |
| TC-A03 | Verify with wrong OTP 3x           | Account blocked 5 min        |
| TC-A04 | Login from new device              | Previous session invalidated |

#### Booking

| ID     | Test Case                              | Expected Result                   |
| ------ | -------------------------------------- | --------------------------------- |
| TC-B01 | Create booking with all fields         | Booking created, caregivers shown |
| TC-B02 | Create booking without required fields | Validation error                  |
| TC-B03 | Apply valid promo code                 | Discount applied                  |
| TC-B04 | Apply expired promo code               | Error, no discount                |
| TC-B05 | Cancel booking >24h before             | Full refund                       |
| TC-B06 | Cancel booking <12h before             | No refund                         |

#### Payment

| ID     | Test Case                | Expected Result                      |
| ------ | ------------------------ | ------------------------------------ |
| TC-P01 | Pay with GoPay (success) | Payment confirmed, booking confirmed |
| TC-P02 | Pay with GoPay (failed)  | Payment failed, booking pending      |
| TC-P03 | Payment timeout          | Payment expired, booking cancelled   |
| TC-P04 | Double payment attempt   | Prevented, error message             |

#### Caregiver

| ID     | Test Case                         | Expected Result                      |
| ------ | --------------------------------- | ------------------------------------ |
| TC-C01 | Accept job within timeout         | Job assigned                         |
| TC-C02 | Accept job after timeout          | Error, job unavailable               |
| TC-C03 | Start service at correct location | Service started                      |
| TC-C04 | Start service at wrong location   | Error, must be within 500m           |
| TC-C05 | Complete service with notes       | Service completed, customer notified |

### 10.3 Performance Benchmarks

| Scenario                          | Metric            | Target  |
| --------------------------------- | ----------------- | ------- |
| Concurrent booking creation       | Response time P95 | < 2s    |
| Caregiver search (100 caregivers) | Response time P95 | < 1s    |
| Chat message delivery             | Delivery time     | < 500ms |
| Location update broadcast         | Latency           | < 200ms |

---

## 11. MVP Definition & Release Criteria

### 11.1 MVP Scope (v1.0)

#### Included in MVP

| Category      | Features                                                    |
| ------------- | ----------------------------------------------------------- |
| **Auth**      | Phone OTP registration/login                                |
| **Profile**   | Basic profile management                                    |
| **Services**  | 3 services: Hospital Companion, Dialysis Support, Home Care |
| **Booking**   | Create booking, select caregiver, cancel                    |
| **Payment**   | QRIS, GoPay, OVO (via Midtrans)                             |
| **Tracking**  | Basic location tracking                                     |
| **Chat**      | Text only                                                   |
| **Rating**    | Star rating + text                                          |
| **Caregiver** | Registration, verification, accept/complete jobs            |
| **Admin**     | Basic dashboard, verification, booking management           |

#### Excluded from MVP (v1.1+)

| Feature                   | Planned Version |
| ------------------------- | --------------- |
| Medical Escort service    | v1.1            |
| Medical Transport service | v1.1            |
| Monthly packages          | v1.1            |
| Voice messages in chat    | v1.2            |
| In-app calling            | v1.2            |
| Customer subscription     | v1.2            |
| Caregiver subscription    | v1.2            |
| Advanced analytics        | v1.2            |
| BPJS integration          | v2.0            |

### 11.2 Release Criteria

| Category           | Criteria                          |
| ------------------ | --------------------------------- |
| **Functionality**  | All P0 features working           |
| **Quality**        | Zero critical bugs, <5 major bugs |
| **Performance**    | Meets all performance benchmarks  |
| **Security**       | Pass security checklist           |
| **Testing**        | All critical test cases pass      |
| **Documentation**  | API docs, user guide ready        |
| **Infrastructure** | Production environment ready      |
| **Legal**          | Privacy policy, ToS published     |

### 11.3 MVP Launch Checklist

```markdown
## Pre-Launch Checklist

### Technical

- [ ] All P0 features implemented
- [ ] All critical bugs fixed
- [ ] Performance benchmarks met
- [ ] Security audit passed
- [ ] Production environment deployed
- [ ] SSL certificates installed
- [ ] Database backups configured
- [ ] Monitoring & alerting setup
- [ ] Error tracking (Sentry) setup
- [ ] Analytics (Mixpanel/Amplitude) setup

### Business

- [ ] 50+ caregivers onboarded
- [ ] 3+ hospital partnerships confirmed
- [ ] Payment gateway production access
- [ ] Customer support process ready
- [ ] Dispute resolution process ready

### Legal & Compliance

- [ ] Privacy Policy published
- [ ] Terms of Service published
- [ ] Caregiver agreement template
- [ ] Data processing agreement

### Marketing

- [ ] App store listings ready
- [ ] Social media accounts setup
- [ ] Landing page live
- [ ] Press release prepared
- [ ] Launch promo codes created

### Operations

- [ ] Admin team trained
- [ ] Customer support scripts ready
- [ ] Escalation procedures documented
- [ ] Incident response plan ready
```

---

## 12. Success Metrics

### 12.1 Key Performance Indicators (KPIs)

#### User Metrics

| Metric                  | MVP Target (M3) | M6 Target | M12 Target |
| ----------------------- | --------------- | --------- | ---------- |
| Total Customers         | 100             | 750       | 2,500      |
| Total Caregivers        | 50              | 150       | 300        |
| Monthly Active Users    | 50              | 400       | 1,500      |
| Customer Retention (M1) | 30%             | 40%       | 50%        |

#### Transaction Metrics

| Metric                  | MVP Target (M3) | M6 Target | M12 Target |
| ----------------------- | --------------- | --------- | ---------- |
| Monthly Transactions    | 30              | 300       | 700        |
| Average Order Value     | Rp 200K         | Rp 225K   | Rp 250K    |
| Monthly GMV             | Rp 6M           | Rp 67.5M  | Rp 175M    |
| Booking Completion Rate | 80%             | 85%       | 90%        |

#### Quality Metrics

| Metric                       | Target |
| ---------------------------- | ------ |
| Average Rating               | ≥ 4.5  |
| Customer Satisfaction (CSAT) | ≥ 80%  |
| Net Promoter Score (NPS)     | ≥ 30   |
| Customer Complaint Rate      | < 5%   |

#### Operational Metrics

| Metric                    | Target        |
| ------------------------- | ------------- |
| Caregiver Acceptance Rate | ≥ 70%         |
| Average Response Time     | < 5 minutes   |
| Service Start Accuracy    | ≥ 95% on time |
| App Crash Rate            | < 1%          |
| API Uptime                | ≥ 99.5%       |

### 12.2 Tracking Implementation

```javascript
// Mixpanel / Amplitude Events

// User Events
"user_registered";
"user_profile_completed";
"user_logged_in";

// Booking Events
"service_viewed";
"booking_started";
"caregiver_selected";
"payment_initiated";
"payment_completed";
"booking_confirmed";
"booking_cancelled";
"booking_completed";

// Engagement Events
"chat_message_sent";
"rating_submitted";
"promo_code_applied";

// Caregiver Events
"caregiver_registered";
"caregiver_verified";
"job_received";
"job_accepted";
"job_rejected";
"service_started";
"service_completed";
"payout_requested";
```

---

## 13. Risks & Mitigations

### 13.1 Technical Risks

| Risk                             | Probability | Impact   | Mitigation                                                  |
| -------------------------------- | ----------- | -------- | ----------------------------------------------------------- |
| Payment integration issues       | Medium      | High     | Use well-documented Midtrans, sandbox testing               |
| Real-time tracking battery drain | Medium      | Medium   | Optimize location updates, use significant location changes |
| App store rejection              | Low         | High     | Follow guidelines strictly, prepare appeal                  |
| Scalability bottleneck           | Low         | Medium   | Use auto-scaling, load testing before launch                |
| Data breach                      | Low         | Critical | Security audit, encryption, access controls                 |

### 13.2 Business Risks

| Risk                    | Probability | Impact | Mitigation                                                 |
| ----------------------- | ----------- | ------ | ---------------------------------------------------------- |
| Low caregiver supply    | High        | High   | Aggressive recruitment, sign-up bonus, referral program    |
| Low customer adoption   | Medium      | High   | Marketing campaign, promo discounts, hospital partnerships |
| Competitor entry        | Medium      | Medium | Build local moat, quality focus, customer loyalty          |
| Regulatory changes      | Low         | Medium | Legal counsel, stay compliant                              |
| Fraud (fake caregivers) | Medium      | High   | Strict verification, background checks                     |

### 13.3 Mitigation Actions

**Low Caregiver Supply:**

1. Partner with nursing schools for internship
2. Offer Rp 100K sign-up bonus after 5 jobs
3. Implement "refer a caregiver" (Rp 75K bonus)
4. Competitive 85% commission rate
5. Fast payout (daily option)

**Low Customer Adoption:**

1. 50% off first booking promo
2. Referral bonus (Rp 50K each)
3. Hospital partnership for patient referrals
4. Community events, health bazaars
5. Local influencer partnerships

**Fraud Prevention:**

1. KTP + selfie verification
2. Manual admin review
3. Customer rating system
4. Low-rating caregiver flagging
5. Customer complaint investigation

---

## Appendix

### A. Glossary

| Term      | Definition                          |
| --------- | ----------------------------------- |
| Caregiver | Non-medical companion/care provider |
| HD        | Hemodialysis (cuci darah)           |
| GMV       | Gross Merchandise Value             |
| OTP       | One-Time Password                   |
| JWT       | JSON Web Token                      |
| FCM       | Firebase Cloud Messaging            |
| VA        | Virtual Account                     |

### B. Related Documents

- [BUSINESS_ANALYSIS.md](./BUSINESS_ANALYSIS.md) - Market research, SWOT
- [TECH_STACK.md](./TECH_STACK.md) - Technology architecture
- [UI_MOCKUPS.md](./UI_MOCKUPS.md) - UI/UX design
- [PRICING_MODEL.md](./PRICING_MODEL.md) - Pricing strategy
- [COMPETITOR_ANALYSIS.md](./COMPETITOR_ANALYSIS.md) - Competitive landscape

### C. Revision History

| Version | Date         | Author       | Changes     |
| ------- | ------------ | ------------ | ----------- |
| 1.0     | January 2026 | SURIOTA Team | Initial PRD |

---

_Document Version: 1.0_
_Last Updated: January 2026_
_Status: Ready for Development_
