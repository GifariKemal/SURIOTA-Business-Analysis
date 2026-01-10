# SRICARE - Product Features & User Experience

## Fitur Produk & Pengalaman Pengguna

> Version 1.0 | January 2026

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [User App Features](#2-user-app-features)
3. [Caregiver App Features](#3-caregiver-app-features)
4. [Admin Dashboard Features](#4-admin-dashboard-features)
5. [User Flows](#5-user-flows)
6. [UI/UX Guidelines](#6-uiux-guidelines)
7. [Feature Roadmap](#7-feature-roadmap)

---

## 1. Product Overview

### 1.1 Product Suite

| Product                 | Platform     | Target User                  |
| ----------------------- | ------------ | ---------------------------- |
| **SRICARE User App**    | iOS, Android | Patients, families, perantau |
| **SRICARE Partner App** | iOS, Android | Caregivers                   |
| **SRICARE Admin**       | Web          | Operations team              |

### 1.2 Core Value Proposition

```
┌─────────────────────────────────────────────────────────────┐
│                    SRICARE VALUE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   FOR USERS:                                                │
│   "Find trusted caregivers in minutes, not days"           │
│   • GPS-based instant matching                              │
│   • Verified & rated caregivers                             │
│   • Real-time tracking                                      │
│   • Secure payment                                          │
│                                                             │
│   FOR CAREGIVERS:                                           │
│   "Earn more with flexible work"                            │
│   • Steady job flow                                         │
│   • Fair 85% earnings                                       │
│   • Fast payouts                                            │
│   • Professional support                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. User App Features

### 2.1 MVP Features (Priority 0)

#### 2.1.1 Authentication

| Feature                | Description                      | Acceptance Criteria            |
| ---------------------- | -------------------------------- | ------------------------------ |
| **Phone Registration** | Register with phone number + OTP | OTP received within 30 seconds |
| **Phone Login**        | Login with phone + OTP           | Seamless re-login              |
| **Profile Setup**      | Name, photo, emergency contact   | Profile completion tracking    |
| **Session Management** | Auto-logout after 30 days        | Secure token handling          |

**Screen Flow:**

```
Welcome → Phone Input → OTP Verification → Profile Setup → Home
```

#### 2.1.2 Service Booking

| Feature                | Description                          | Acceptance Criteria            |
| ---------------------- | ------------------------------------ | ------------------------------ |
| **Service Selection**  | Choose from 4 service types          | Clear service descriptions     |
| **Date & Time Picker** | Select booking schedule              | Min 2 hours advance booking    |
| **Location Input**     | Pickup & destination (if applicable) | GPS auto-detect + manual input |
| **Patient Details**    | Input patient info (optional)        | Age, condition, special needs  |
| **Duration Selection** | Choose hours/shift/package           | Price updates dynamically      |
| **Price Estimation**   | Show total price breakdown           | Transparent pricing            |

**Booking Form Fields:**

| Service Type       | Required Fields                                |
| ------------------ | ---------------------------------------------- |
| Hospital Companion | Hospital name, room (optional), duration       |
| Dialysis Support   | Pickup address, dialysis clinic, package type  |
| Medical Escort     | Pickup address, clinic/hospital, service level |
| Home Care          | Address, duration, patient condition           |

#### 2.1.3 Caregiver Discovery

| Feature               | Description                             | Acceptance Criteria   |
| --------------------- | --------------------------------------- | --------------------- |
| **Nearby Caregivers** | Show caregivers on map                  | Within 10km radius    |
| **List View**         | Sortable list (distance, rating, price) | Filterable by skill   |
| **Caregiver Profile** | Photo, rating, reviews, experience      | Complete info visible |
| **Skills Filter**     | Filter by service expertise             | Multi-select filters  |

**Caregiver Card Display:**

```
┌──────────────────────────────────────┐
│ [Photo]  Siti Rahayu ★ 4.8 (127)    │
│          2.3 km away                 │
│          Hospital • Dialysis         │
│          Rp 50,000/jam               │
│                        [PILIH]       │
└──────────────────────────────────────┘
```

#### 2.1.4 Payment

| Feature             | Description             | Acceptance Criteria |
| ------------------- | ----------------------- | ------------------- |
| **Payment Methods** | QRIS, e-wallet, VA      | Min 5 options       |
| **Price Breakdown** | Service + fee breakdown | Transparent         |
| **Payment Status**  | Real-time status update | Webhook integration |
| **Receipt**         | Digital receipt         | PDF/shareable       |

#### 2.1.5 Real-time Tracking

| Feature            | Description                   | Acceptance Criteria        |
| ------------------ | ----------------------------- | -------------------------- |
| **Map Tracking**   | See caregiver location        | Updates every 5-10 seconds |
| **ETA Display**    | Estimated arrival time        | Updates dynamically        |
| **Status Updates** | "On the way", "Arrived", etc. | Push notifications         |

#### 2.1.6 Rating & Review

| Feature            | Description               | Acceptance Criteria          |
| ------------------ | ------------------------- | ---------------------------- |
| **Star Rating**    | 1-5 stars                 | Required after service       |
| **Written Review** | Text feedback             | Optional, 500 char max       |
| **Quick Tags**     | Pre-defined feedback tags | "Tepat waktu", "Ramah", etc. |

---

### 2.2 P1 Features (Post-MVP)

#### 2.2.1 In-App Chat

| Feature            | Description                   |
| ------------------ | ----------------------------- |
| **Text Messages**  | Real-time chat with caregiver |
| **Photo Sharing**  | Send/receive images           |
| **Voice Messages** | Audio messages                |
| **Auto-translate** | Translate messages (future)   |

#### 2.2.2 Booking History

| Feature                 | Description                  |
| ----------------------- | ---------------------------- |
| **Past Bookings**       | List of completed services   |
| **Rebook**              | Quick rebook same caregiver  |
| **Favorite Caregivers** | Save preferred caregivers    |
| **Booking Details**     | View past receipts & ratings |

#### 2.2.3 Notifications

| Feature                   | Description             |
| ------------------------- | ----------------------- |
| **Push Notifications**    | Booking updates, promos |
| **In-App Notifications**  | Activity feed           |
| **Notification Settings** | Customize preferences   |

---

### 2.3 P2 Features (Future)

| Feature                | Description                         |
| ---------------------- | ----------------------------------- |
| **Subscription Plans** | SRICARE Plus membership             |
| **Emergency SOS**      | Quick emergency contact             |
| **Family Account**     | Multiple patients under one account |
| **Care Report**        | Caregiver activity report           |
| **Health Integration** | Connect with health apps            |

---

## 3. Caregiver App Features

### 3.1 MVP Features (Priority 0)

#### 3.1.1 Registration & Verification

| Feature                 | Description                 | Acceptance Criteria       |
| ----------------------- | --------------------------- | ------------------------- |
| **Phone Registration**  | Register with phone + OTP   | Same as user app          |
| **Profile Setup**       | Name, photo, bio, skills    | Complete profile required |
| **Document Upload**     | KTP, certificates, photo    | Clear image capture       |
| **Verification Status** | Track verification progress | Real-time status          |

**Verification Flow:**

```
Register → Upload Documents → Admin Review → Training (optional) → Approved
```

**Document Requirements:**

- KTP (mandatory)
- Selfie with KTP (mandatory)
- Health certificate (recommended)
- Care training certificate (optional)
- Previous work references (optional)

#### 3.1.2 Job Management

| Feature               | Description                           | Acceptance Criteria |
| --------------------- | ------------------------------------- | ------------------- |
| **Job Notifications** | Receive new job alerts                | Push + sound        |
| **Job Details**       | View service details before accepting | Complete info       |
| **Accept/Decline**    | Respond to job requests               | 60 second timeout   |
| **Active Jobs**       | View current assignments              | Dashboard view      |
| **Job History**       | Past completed jobs                   | Searchable          |

**Job Notification Card:**

```
┌──────────────────────────────────────┐
│ 🔔 NEW JOB REQUEST                   │
│                                      │
│ Service: Dialysis Support            │
│ Location: 3.2 km away                │
│ Time: Today, 08:00 - 13:00           │
│ Earnings: Rp 255,000                 │
│                                      │
│    [DECLINE]         [ACCEPT]        │
│                                      │
│         ⏱️ 45 seconds remaining       │
└──────────────────────────────────────┘
```

#### 3.1.3 Navigation & Check-in

| Feature                | Description          | Acceptance Criteria              |
| ---------------------- | -------------------- | -------------------------------- |
| **Navigate to Pickup** | Maps integration     | Google/Waze integration          |
| **Check-in**           | GPS-verified arrival | Within 100m radius               |
| **Status Updates**     | Update job status    | "On the way", "Arrived", etc.    |
| **Check-out**          | Complete job         | GPS-verified + user confirmation |

#### 3.1.4 Earnings & Payout

| Feature                | Description             | Acceptance Criteria  |
| ---------------------- | ----------------------- | -------------------- |
| **Earnings Dashboard** | Today/week/month view   | Real-time balance    |
| **Payout Request**     | Request withdrawal      | Instant/daily/weekly |
| **Payout History**     | Track all payouts       | Searchable           |
| **Earnings Breakdown** | Per-job earnings detail | Transparent          |

**Earnings Dashboard:**

```
┌──────────────────────────────────────┐
│        SALDO TERSEDIA                │
│        Rp 1,275,000                  │
│        [TARIK DANA]                  │
├──────────────────────────────────────┤
│ Hari ini     Rp 510,000   (2 jobs)   │
│ Minggu ini   Rp 1,785,000 (7 jobs)   │
│ Bulan ini    Rp 5,015,000 (23 jobs)  │
└──────────────────────────────────────┘
```

#### 3.1.5 Online/Offline Toggle

| Feature          | Description          | Acceptance Criteria  |
| ---------------- | -------------------- | -------------------- |
| **Go Online**    | Start receiving jobs | GPS enabled required |
| **Go Offline**   | Stop receiving jobs  | One-tap toggle       |
| **Auto-offline** | After idle period    | Configurable         |

---

### 3.2 P1 Features (Post-MVP)

#### 3.2.1 In-App Chat

Same as user app - communicate with customers.

#### 3.2.2 Activity Report

| Feature              | Description                        |
| -------------------- | ---------------------------------- |
| **Job Report**       | Document activities during service |
| **Photo Log**        | Take photos (with consent)         |
| **Notes**            | Add notes for family               |
| **Condition Update** | Report patient condition           |

#### 3.2.3 Performance Stats

| Feature             | Description              |
| ------------------- | ------------------------ |
| **Rating Overview** | Average rating & trends  |
| **Completion Rate** | Job completion %         |
| **Response Time**   | Average response to jobs |
| **Reviews**         | Read customer feedback   |

---

### 3.3 P2 Features (Future)

| Feature                   | Description             |
| ------------------------- | ----------------------- |
| **Training Center**       | In-app learning modules |
| **Certification**         | Earn badges for skills  |
| **Partner+ Subscription** | Premium features        |
| **Shift Scheduling**      | Pre-set availability    |
| **Team Mode**             | Handle jobs as team     |

---

## 4. Admin Dashboard Features

### 4.1 Core Features

| Module                   | Features                                        |
| ------------------------ | ----------------------------------------------- |
| **User Management**      | View/edit users, suspend accounts               |
| **Caregiver Management** | Verify documents, approve/reject, manage status |
| **Booking Management**   | View all bookings, handle disputes              |
| **Payment Management**   | View transactions, process refunds              |
| **Analytics**            | Dashboard with key metrics                      |
| **Support**              | Handle customer inquiries                       |

### 4.2 Key Dashboards

**Main Dashboard Metrics:**

- Total users / caregivers
- Active bookings today
- GMV today / this month
- Average rating
- Open support tickets

**Caregiver Verification Queue:**

```
┌─────────────────────────────────────────────────────────────┐
│ VERIFIKASI CAREGIVER                        [Filter ▼]      │
├─────────────────────────────────────────────────────────────┤
│ 📋 Pending: 12 | ✅ Approved: 287 | ❌ Rejected: 23         │
├─────────────────────────────────────────────────────────────┤
│ Name          | Phone        | Submitted  | Status  | Action│
│ Ani Yuliani   | 0812xxxx     | 2 hours    | Pending | [View]│
│ Budi Santoso  | 0813xxxx     | 5 hours    | Pending | [View]│
│ Dewi Lestari  | 0857xxxx     | 1 day      | Pending | [View]│
└─────────────────────────────────────────────────────────────┘
```

---

## 5. User Flows

### 5.1 User: Book Dialysis Support

```
┌─────────────────────────────────────────────────────────────┐
│                    DIALYSIS BOOKING FLOW                    │
└─────────────────────────────────────────────────────────────┘

[1. HOME SCREEN]
    │
    └──► Tap "Cuci Darah"
           │
[2. SERVICE SETUP]
    │
    └──► Select package: "With Transport"
    └──► Enter pickup address (auto-detect GPS)
    └──► Enter dialysis clinic
    └──► Select date & time
    └──► Add patient notes (optional)
    └──► Tap "Cari Caregiver"
           │
[3. CAREGIVER SELECTION]
    │
    └──► View available caregivers (sorted by distance)
    └──► Tap caregiver to see profile
    └──► Tap "Pilih Caregiver Ini"
           │
[4. BOOKING CONFIRMATION]
    │
    └──► Review booking details
    └──► See price breakdown (Rp 300,000)
    └──► Tap "Lanjut ke Pembayaran"
           │
[5. PAYMENT]
    │
    └──► Select payment method (QRIS)
    └──► Scan QR code / Pay via e-wallet
    └──► Payment confirmed
           │
[6. WAITING FOR ACCEPTANCE]
    │
    └──► Caregiver receives notification
    └──► Caregiver accepts (within 60 sec)
    └──► User receives confirmation
           │
[7. SERVICE DAY]
    │
    └──► Caregiver goes online
    └──► User can track caregiver location
    └──► Caregiver arrives, checks in
    └──► Service begins (4-5 hours)
    └──► Caregiver checks out
           │
[8. COMPLETION]
    │
    └──► User receives completion notification
    └──► User rates caregiver (1-5 stars)
    └──► User writes review (optional)
    └──► Booking completed
```

### 5.2 Caregiver: Accept & Complete Job

```
┌─────────────────────────────────────────────────────────────┐
│                    CAREGIVER JOB FLOW                       │
└─────────────────────────────────────────────────────────────┘

[1. GO ONLINE]
    │
    └──► Open app, toggle "Go Online"
    └──► GPS location shared with platform
           │
[2. RECEIVE JOB REQUEST]
    │
    └──► Push notification: "Job baru!"
    └──► View job details
    └──► Tap "Accept" (within 60 sec)
           │
[3. NAVIGATE TO PICKUP]
    │
    └──► Tap "Navigate" → Opens Google Maps
    └──► Drive/ride to pickup location
    └──► Update status: "On the way"
           │
[4. ARRIVE & CHECK-IN]
    │
    └──► Arrive at pickup location
    └──► Tap "Check In" (GPS verified)
    └──► Meet patient/family
    └──► Update status: "Service started"
           │
[5. DURING SERVICE]
    │
    └──► Perform service (e.g., accompany to dialysis)
    └──► Log activities (optional)
    └──► Communicate via in-app chat if needed
           │
[6. COMPLETE SERVICE]
    │
    └──► Return patient home (if applicable)
    └──► Tap "Complete Job"
    └──► GPS verified at destination
           │
[7. EARNINGS]
    │
    └──► Earnings added to balance (Rp 255,000)
    └──► User rates caregiver
    └──► View rating/review
    └──► Request payout (optional)
```

### 5.3 User: Emergency Contact Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    EMERGENCY FLOW (Future)                  │
└─────────────────────────────────────────────────────────────┘

[ACTIVE BOOKING]
    │
    └──► User taps "SOS" button
           │
[SOS ACTIVATED]
    │
    └──► Notification to:
         • Emergency contact (SMS)
         • SRICARE support team
         • Caregiver (if during service)
    └──► GPS location shared
    └──► Support team calls user
```

---

## 6. UI/UX Guidelines

### 6.1 Design Principles

| Principle       | Description                                  |
| --------------- | -------------------------------------------- |
| **Simple**      | Minimal steps to complete tasks              |
| **Clear**       | No ambiguous text or icons                   |
| **Accessible**  | Large fonts, high contrast for elderly users |
| **Trustworthy** | Professional, calming design                 |
| **Local**       | Bahasa Indonesia first, culturally relevant  |

### 6.2 Color Palette

| Color             | Hex             | Usage                          |
| ----------------- | --------------- | ------------------------------ |
| **Primary**       | #4A90D9 (Blue)  | CTAs, headers, primary actions |
| **Secondary**     | #50C878 (Green) | Success, online status         |
| **Accent**        | #FF6B6B (Coral) | Alerts, notifications          |
| **Neutral Dark**  | #2D3436         | Text, icons                    |
| **Neutral Light** | #F5F6FA         | Backgrounds                    |
| **White**         | #FFFFFF         | Cards, content areas           |

### 6.3 Typography

| Type          | Font           | Size | Usage           |
| ------------- | -------------- | ---- | --------------- |
| **Heading 1** | Inter Bold     | 24sp | Screen titles   |
| **Heading 2** | Inter SemiBold | 20sp | Section headers |
| **Body**      | Inter Regular  | 16sp | Main content    |
| **Caption**   | Inter Regular  | 14sp | Secondary text  |
| **Button**    | Inter SemiBold | 16sp | Button labels   |

### 6.4 Key Screen Mockup Descriptions

**Home Screen:**

```
┌─────────────────────────────────────┐
│ 📍 Batam, Kepulauan Riau      [👤] │
├─────────────────────────────────────┤
│                                     │
│  Halo, Andi!                        │
│  Butuh bantuan apa hari ini?        │
│                                     │
│  ┌─────────┐  ┌─────────┐          │
│  │ 🏥      │  │ 💉      │          │
│  │ Jaga RS │  │ Cuci    │          │
│  │         │  │ Darah   │          │
│  └─────────┘  └─────────┘          │
│                                     │
│  ┌─────────┐  ┌─────────┐          │
│  │ 👨‍⚕️     │  │ 🏠      │          │
│  │ Antar   │  │ Home    │          │
│  │ Berobat │  │ Care    │          │
│  └─────────┘  └─────────┘          │
│                                     │
│  ─────────────────────────────      │
│  CAREGIVER TERDEKAT                 │
│  ┌─────────────────────────────┐   │
│  │ [Foto] Siti R. ★4.8  2.3km │   │
│  └─────────────────────────────┘   │
│                                     │
├─────────────────────────────────────┤
│  🏠      📋      💬      👤        │
│  Home   Booking  Chat   Profile    │
└─────────────────────────────────────┘
```

**Tracking Screen:**

```
┌─────────────────────────────────────┐
│ ← Booking #12345                    │
├─────────────────────────────────────┤
│                                     │
│         [MAP VIEW]                  │
│                                     │
│     🔵 Caregiver location           │
│     📍 Your location                │
│                                     │
│                                     │
├─────────────────────────────────────┤
│ ┌─────────────────────────────────┐ │
│ │ Siti Rahayu sedang menuju       │ │
│ │ Perkiraan tiba: 12 menit        │ │
│ │                                 │ │
│ │ [📞 Hubungi]    [💬 Chat]       │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

---

## 7. Feature Roadmap

### 7.1 MVP (Month 1-4)

| Feature               | User App | Caregiver App | Admin |
| --------------------- | :------: | :-----------: | :---: |
| Phone Auth + OTP      |    ✅    |      ✅       |   -   |
| Profile Setup         |    ✅    |      ✅       |   -   |
| Service Booking       |    ✅    |       -       |   -   |
| Caregiver Discovery   |    ✅    |       -       |   -   |
| Job Notifications     |    -     |      ✅       |   -   |
| Accept/Decline Jobs   |    -     |      ✅       |   -   |
| GPS Tracking          |    ✅    |      ✅       |   -   |
| Check-in/Check-out    |    -     |      ✅       |   -   |
| Payment (Midtrans)    |    ✅    |       -       |   -   |
| Earnings Dashboard    |    -     |      ✅       |   -   |
| Rating & Review       |    ✅    |      ✅       |   -   |
| Basic Admin Dashboard |    -     |       -       |  ✅   |

### 7.2 V1.1 (Month 5-6)

| Feature             | User App | Caregiver App | Admin |
| ------------------- | :------: | :-----------: | :---: |
| In-App Chat         |    ✅    |      ✅       |   -   |
| Booking History     |    ✅    |      ✅       |   -   |
| Favorite Caregivers |    ✅    |       -       |   -   |
| Activity Report     |    -     |      ✅       |   -   |
| Dispute Handling    |    -     |       -       |  ✅   |
| Analytics Dashboard |    -     |       -       |  ✅   |

### 7.3 V1.2 (Month 7-9)

| Feature            | User App | Caregiver App | Admin |
| ------------------ | :------: | :-----------: | :---: |
| Subscription Plans |    ✅    |      ✅       |  ✅   |
| Promo Codes        |    ✅    |       -       |  ✅   |
| Referral Program   |    ✅    |      ✅       |  ✅   |
| Performance Stats  |    -     |      ✅       |   -   |
| Reporting Tools    |    -     |       -       |  ✅   |

### 7.4 V2.0 (Month 10-12)

| Feature          | User App | Caregiver App | Admin |
| ---------------- | :------: | :-----------: | :---: |
| Family Account   |    ✅    |       -       |   -   |
| Emergency SOS    |    ✅    |       -       |  ✅   |
| Training Center  |    -     |      ✅       |  ✅   |
| Multi-language   |    ✅    |      ✅       |  ✅   |
| API for Partners |    -     |       -       |  ✅   |

---

## Appendix

### A. Glossary

| Term          | Definition                                        |
| ------------- | ------------------------------------------------- |
| **Booking**   | A service request from user to caregiver          |
| **Check-in**  | GPS-verified arrival at service location          |
| **Check-out** | GPS-verified completion of service                |
| **GMV**       | Gross Merchandise Value - total transaction value |
| **OTP**       | One-Time Password for authentication              |

### B. Accessibility Considerations

| Feature                 | Implementation                   |
| ----------------------- | -------------------------------- |
| **Large Touch Targets** | Min 48dp for buttons             |
| **High Contrast**       | 4.5:1 ratio for text             |
| **Screen Reader**       | Semantic labels for all elements |
| **Font Scaling**        | Support system font size         |
| **Color Blindness**     | Don't rely on color alone        |

### C. Localization

| Language         | Priority | Status |
| ---------------- | -------- | ------ |
| Bahasa Indonesia | P0       | MVP    |
| English          | P2       | V2.0   |
| Mandarin         | P3       | Future |

---

_Document Version: 1.0_
_Last Updated: January 2026_
_Author: SURIOTA Team_
