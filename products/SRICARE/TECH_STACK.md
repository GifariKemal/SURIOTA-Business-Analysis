# SRICARE - Technology Stack & Architecture

## Arsitektur Teknologi | Technical Architecture

> Version 1.0 | January 2026

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Mobile Application](#2-mobile-application)
3. [Backend Services](#3-backend-services)
4. [Database Design](#4-database-design)
5. [Real-time Features](#5-real-time-features)
6. [Payment Integration](#6-payment-integration)
7. [Maps & Location](#7-maps--location)
8. [Infrastructure](#8-infrastructure)
9. [Security](#9-security)
10. [Development Roadmap](#10-development-roadmap)

---

## 1. Architecture Overview

### 1.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           SRICARE PLATFORM                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐             │
│   │   User App   │    │ Caregiver    │    │   Admin      │             │
│   │   (Flutter)  │    │    App       │    │  Dashboard   │             │
│   │              │    │  (Flutter)   │    │  (Next.js)   │             │
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘             │
│          │                   │                   │                      │
│          └───────────────────┼───────────────────┘                      │
│                              │                                          │
│                              ▼                                          │
│                    ┌──────────────────┐                                 │
│                    │   API Gateway    │                                 │
│                    │   (Kong/Nginx)   │                                 │
│                    └────────┬─────────┘                                 │
│                             │                                           │
│          ┌──────────────────┼──────────────────┐                       │
│          ▼                  ▼                  ▼                        │
│   ┌────────────┐    ┌────────────┐    ┌────────────┐                   │
│   │   Auth     │    │  Booking   │    │  Payment   │                   │
│   │  Service   │    │  Service   │    │  Service   │                   │
│   │ (NestJS)   │    │  (NestJS)  │    │  (NestJS)  │                   │
│   └─────┬──────┘    └─────┬──────┘    └─────┬──────┘                   │
│         │                 │                 │                           │
│         └─────────────────┼─────────────────┘                          │
│                           │                                             │
│                           ▼                                             │
│                    ┌────────────────┐                                   │
│                    │   PostgreSQL   │                                   │
│                    │   + PostGIS    │                                   │
│                    └────────────────┘                                   │
│                                                                         │
│          ┌─────────────────────────────────────┐                       │
│          │         Supporting Services         │                       │
│          ├─────────────────────────────────────┤                       │
│          │  Redis │ Socket.IO │ Firebase FCM   │                       │
│          └─────────────────────────────────────┘                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Technology Stack Summary

| Layer                 | Technology           | Justification                                    |
| --------------------- | -------------------- | ------------------------------------------------ |
| **Mobile App**        | Flutter              | Cross-platform, single codebase, rich UI         |
| **Backend**           | NestJS (Node.js)     | TypeScript, modular, scalable, SURIOTA expertise |
| **Database**          | PostgreSQL + PostGIS | Relational + geospatial queries                  |
| **Cache**             | Redis                | Session management, real-time data               |
| **Real-time**         | Socket.IO            | Live tracking, chat, notifications               |
| **Maps**              | Google Maps / Mapbox | GPS, routing, ETA calculation                    |
| **Payment**           | Midtrans / Xendit    | QRIS, e-wallet, VA support                       |
| **Push Notification** | Firebase FCM         | Cross-platform push                              |
| **Cloud**             | Google Cloud / AWS   | Scalable infrastructure                          |

---

## 2. Mobile Application

### 2.1 Framework Choice: Flutter

**Why Flutter?**

| Criteria          | Flutter        | React Native | Native |
| ----------------- | -------------- | ------------ | ------ |
| Single Codebase   | Yes            | Yes          | No     |
| Performance       | Near-native    | Good         | Best   |
| GPS/Location      | Excellent      | Good         | Best   |
| Maps Integration  | Excellent      | Good         | Best   |
| Development Speed | Fast           | Fast         | Slow   |
| UI Consistency    | Perfect        | Good         | Varies |
| SURIOTA Expertise | Learning curve | Good         | Varies |

**Decision:** Flutter - best balance of cross-platform efficiency and performance for GPS-heavy apps.

### 2.2 App Architecture (Flutter)

```
lib/
├── main.dart
├── app/
│   ├── app.dart
│   ├── routes.dart
│   └── theme.dart
│
├── core/
│   ├── constants/
│   ├── errors/
│   ├── network/
│   │   ├── api_client.dart
│   │   └── api_endpoints.dart
│   └── utils/
│
├── features/
│   ├── auth/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── booking/
│   │   ├── data/
│   │   │   ├── models/
│   │   │   ├── repositories/
│   │   │   └── datasources/
│   │   ├── domain/
│   │   │   ├── entities/
│   │   │   ├── repositories/
│   │   │   └── usecases/
│   │   └── presentation/
│   │       ├── screens/
│   │       ├── widgets/
│   │       └── bloc/
│   │
│   ├── tracking/
│   ├── payment/
│   ├── chat/
│   └── profile/
│
└── shared/
    ├── widgets/
    └── services/
        ├── location_service.dart
        ├── socket_service.dart
        └── notification_service.dart
```

### 2.3 Key Flutter Packages

| Package                       | Purpose              | Version |
| ----------------------------- | -------------------- | ------- |
| `flutter_bloc`                | State management     | ^8.x    |
| `dio`                         | HTTP client          | ^5.x    |
| `geolocator`                  | GPS location         | ^11.x   |
| `google_maps_flutter`         | Maps integration     | ^2.x    |
| `socket_io_client`            | Real-time connection | ^2.x    |
| `firebase_messaging`          | Push notifications   | ^14.x   |
| `flutter_local_notifications` | Local notifications  | ^16.x   |
| `image_picker`                | Profile photos       | ^1.x    |
| `shared_preferences`          | Local storage        | ^2.x    |
| `intl`                        | Localization (ID/EN) | ^0.18.x |

### 2.4 Two Apps Strategy

| App                 | Target User        | Key Features                            |
| ------------------- | ------------------ | --------------------------------------- |
| **SRICARE User**    | Customers/Patients | Book caregiver, track, pay, rate        |
| **SRICARE Partner** | Caregivers         | Accept jobs, navigate, report, earnings |

**Shared Codebase:** 70% (core, network, utils)
**Separate:** UI screens, business logic specific to role

---

## 3. Backend Services

### 3.1 Framework Choice: NestJS

**Why NestJS?**

| Criteria                | NestJS         | Express | Fastify |
| ----------------------- | -------------- | ------- | ------- |
| TypeScript Native       | Yes            | Manual  | Manual  |
| Structure/Organization  | Excellent      | Minimal | Minimal |
| Dependency Injection    | Built-in       | Manual  | Manual  |
| WebSocket Support       | Built-in       | Manual  | Manual  |
| Documentation (Swagger) | Built-in       | Manual  | Manual  |
| SURIOTA Experience      | SURGE Platform | -       | -       |

**Decision:** NestJS - consistent with SURGE Platform, maintainable, scalable.

### 3.2 Service Architecture (Modular Monolith)

```
src/
├── main.ts
├── app.module.ts
│
├── modules/
│   ├── auth/
│   │   ├── auth.module.ts
│   │   ├── auth.controller.ts
│   │   ├── auth.service.ts
│   │   ├── strategies/
│   │   │   ├── jwt.strategy.ts
│   │   │   └── local.strategy.ts
│   │   └── dto/
│   │
│   ├── users/
│   │   ├── users.module.ts
│   │   ├── users.controller.ts
│   │   ├── users.service.ts
│   │   └── entities/
│   │       └── user.entity.ts
│   │
│   ├── caregivers/
│   │   ├── caregivers.module.ts
│   │   ├── caregivers.controller.ts
│   │   ├── caregivers.service.ts
│   │   └── entities/
│   │
│   ├── bookings/
│   │   ├── bookings.module.ts
│   │   ├── bookings.controller.ts
│   │   ├── bookings.service.ts
│   │   ├── matching.service.ts   # GPS matching algorithm
│   │   └── entities/
│   │
│   ├── payments/
│   │   ├── payments.module.ts
│   │   ├── payments.controller.ts
│   │   ├── payments.service.ts
│   │   └── gateways/
│   │       ├── midtrans.gateway.ts
│   │       └── xendit.gateway.ts
│   │
│   ├── tracking/
│   │   ├── tracking.module.ts
│   │   ├── tracking.gateway.ts    # WebSocket
│   │   └── tracking.service.ts
│   │
│   ├── chat/
│   │   ├── chat.module.ts
│   │   ├── chat.gateway.ts        # WebSocket
│   │   └── chat.service.ts
│   │
│   └── notifications/
│       ├── notifications.module.ts
│       ├── notifications.service.ts
│       └── fcm.service.ts
│
├── common/
│   ├── decorators/
│   ├── filters/
│   ├── guards/
│   ├── interceptors/
│   └── pipes/
│
└── config/
    ├── database.config.ts
    ├── redis.config.ts
    └── app.config.ts
```

### 3.3 API Design (REST + WebSocket)

**REST Endpoints (Core)**

| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| POST   | `/auth/register`         | User/Caregiver registration    |
| POST   | `/auth/login`            | Login with phone OTP           |
| POST   | `/auth/verify-otp`       | Verify OTP code                |
| GET    | `/users/me`              | Get current user profile       |
| PUT    | `/users/me`              | Update profile                 |
| GET    | `/caregivers`            | List caregivers (with filters) |
| GET    | `/caregivers/:id`        | Get caregiver detail           |
| GET    | `/caregivers/nearby`     | Find nearby caregivers (GPS)   |
| POST   | `/bookings`              | Create new booking             |
| GET    | `/bookings`              | List user bookings             |
| GET    | `/bookings/:id`          | Get booking detail             |
| PUT    | `/bookings/:id/accept`   | Caregiver accepts booking      |
| PUT    | `/bookings/:id/complete` | Complete booking               |
| POST   | `/payments`              | Create payment                 |
| POST   | `/payments/webhook`      | Payment gateway callback       |
| POST   | `/ratings`               | Submit rating/review           |

**WebSocket Events**

| Event                | Direction          | Description                  |
| -------------------- | ------------------ | ---------------------------- |
| `location:update`    | Caregiver → Server | Caregiver location update    |
| `location:broadcast` | Server → User      | Broadcast caregiver location |
| `booking:new`        | Server → Caregiver | New booking notification     |
| `booking:accepted`   | Server → User      | Booking accepted             |
| `booking:status`     | Server → Both      | Status change notification   |
| `chat:message`       | Both               | Chat messages                |
| `chat:typing`        | Both               | Typing indicator             |

---

## 4. Database Design

### 4.1 Database Choice: PostgreSQL + PostGIS

**Why PostgreSQL + PostGIS?**

| Feature                | Benefit                                     |
| ---------------------- | ------------------------------------------- |
| **PostGIS Extension**  | Geospatial queries (find nearest caregiver) |
| **JSONB**              | Flexible metadata storage                   |
| **Full-text Search**   | Search caregivers by skills                 |
| **Reliability**        | ACID compliant, battle-tested               |
| **SURIOTA Experience** | Already used in SURGE Platform              |

### 4.2 Entity Relationship Diagram

```
┌─────────────────┐       ┌─────────────────┐
│     users       │       │   caregivers    │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ phone           │       │ user_id (FK)    │──┐
│ name            │       │ skills          │  │
│ email           │       │ rating          │  │
│ role            │       │ total_jobs      │  │
│ avatar_url      │       │ is_verified     │  │
│ created_at      │       │ documents       │  │
│ updated_at      │       │ location (POINT)│  │
└────────┬────────┘       │ is_online       │  │
         │                │ created_at      │  │
         │                └─────────────────┘  │
         │                                     │
         │                                     │
         ▼                                     │
┌─────────────────┐                           │
│    bookings     │                           │
├─────────────────┤                           │
│ id (PK)         │                           │
│ user_id (FK)    │◄──────────────────────────┘
│ caregiver_id(FK)│
│ service_type    │
│ status          │
│ pickup_location │
│ destination     │
│ scheduled_at    │
│ started_at      │
│ completed_at    │
│ total_price     │
│ notes           │
│ created_at      │
└────────┬────────┘
         │
         │
         ▼
┌─────────────────┐       ┌─────────────────┐
│    payments     │       │    ratings      │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ booking_id (FK) │       │ booking_id (FK) │
│ amount          │       │ user_id (FK)    │
│ method          │       │ caregiver_id(FK)│
│ status          │       │ score (1-5)     │
│ gateway_ref     │       │ comment         │
│ paid_at         │       │ created_at      │
│ created_at      │       └─────────────────┘
└─────────────────┘
```

### 4.3 Key Tables Schema

```sql
-- Enable PostGIS
CREATE EXTENSION IF NOT EXISTS postgis;

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone VARCHAR(15) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    role VARCHAR(20) NOT NULL DEFAULT 'user', -- 'user', 'caregiver', 'admin'
    avatar_url TEXT,
    fcm_token TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Caregivers table
CREATE TABLE caregivers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    skills TEXT[], -- ['elderly_care', 'dialysis', 'hospital']
    rating DECIMAL(2,1) DEFAULT 0,
    total_jobs INTEGER DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    documents JSONB, -- {ktp: url, sertifikat: url}
    location GEOGRAPHY(POINT, 4326), -- PostGIS point
    is_online BOOLEAN DEFAULT FALSE,
    hourly_rate INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create spatial index for location queries
CREATE INDEX idx_caregivers_location ON caregivers USING GIST(location);

-- Bookings table
CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    caregiver_id UUID REFERENCES caregivers(id),
    service_type VARCHAR(50) NOT NULL, -- 'hospital_companion', 'dialysis', 'medical_escort', 'home_care'
    status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'accepted', 'ongoing', 'completed', 'cancelled'
    pickup_location GEOGRAPHY(POINT, 4326),
    pickup_address TEXT,
    destination GEOGRAPHY(POINT, 4326),
    destination_address TEXT,
    scheduled_at TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    duration_hours INTEGER,
    total_price INTEGER,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Payments table
CREATE TABLE payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id),
    amount INTEGER NOT NULL,
    method VARCHAR(30), -- 'qris', 'gopay', 'ovo', 'dana', 'va_bca', 'va_mandiri'
    status VARCHAR(20) DEFAULT 'pending', -- 'pending', 'paid', 'failed', 'refunded'
    gateway VARCHAR(20), -- 'midtrans', 'xendit'
    gateway_ref VARCHAR(100),
    paid_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Ratings table
CREATE TABLE ratings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    booking_id UUID REFERENCES bookings(id) UNIQUE,
    user_id UUID REFERENCES users(id),
    caregiver_id UUID REFERENCES caregivers(id),
    score INTEGER CHECK (score >= 1 AND score <= 5),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 4.4 Geospatial Query Example (Find Nearest Caregiver)

```sql
-- Find 10 nearest online caregivers within 10km
SELECT
    c.id,
    u.name,
    c.rating,
    c.hourly_rate,
    ST_Distance(
        c.location::geography,
        ST_SetSRID(ST_MakePoint($1, $2), 4326)::geography
    ) AS distance_meters
FROM caregivers c
JOIN users u ON c.user_id = u.id
WHERE
    c.is_online = true
    AND c.is_verified = true
    AND $3 = ANY(c.skills) -- e.g., 'dialysis'
    AND ST_DWithin(
        c.location::geography,
        ST_SetSRID(ST_MakePoint($1, $2), 4326)::geography,
        10000 -- 10km radius
    )
ORDER BY distance_meters ASC
LIMIT 10;

-- Parameters: $1 = longitude, $2 = latitude, $3 = skill required
```

---

## 5. Real-time Features

### 5.1 Socket.IO Implementation

**Server-side (NestJS Gateway)**

```typescript
// tracking.gateway.ts
@WebSocketGateway({
  cors: { origin: '*' },
  namespace: '/tracking'
})
export class TrackingGateway implements OnGatewayConnection, OnGatewayDisconnect {

  @WebSocketServer()
  server: Server;

  // Caregiver updates their location
  @SubscribeMessage('location:update')
visardasync handleLocationUpdate(
    @ConnectedSocket() client: Socket,
    @MessageBody() data: { lat: number; lng: number; bookingId?: string }
  ) {
    // Save to Redis for quick access
    await this.redis.set(`caregiver:${client.data.userId}:location`, JSON.stringify(data));

    // If on active booking, broadcast to user
    if (data.bookingId) {
      this.server.to(`booking:${data.bookingId}`).emit('location:broadcast', {
        caregiverId: client.data.userId,
        lat: data.lat,
        lng: data.lng,
        timestamp: new Date()
      });
    }
  }

  // User joins booking room to receive updates
  @SubscribeMessage('booking:join')
  handleJoinBooking(
    @ConnectedSocket() client: Socket,
    @MessageBody() data: { bookingId: string }
  ) {
    client.join(`booking:${data.bookingId}`);
    return { status: 'joined', room: `booking:${data.bookingId}` };
  }
}
```

**Client-side (Flutter)**

```dart
// socket_service.dart
class SocketService {
  late IO.Socket socket;

  void connect(String token) {
    socket = IO.io('https://api.sricare.id/tracking', <String, dynamic>{
      'transports': ['websocket'],
      'autoConnect': true,
      'auth': {'token': token}
    });

    socket.onConnect((_) => print('Connected to tracking'));

    socket.on('location:broadcast', (data) {
      // Update caregiver marker on map
      _locationController.add(LocationUpdate.fromJson(data));
    });
  }

  void updateLocation(double lat, double lng, String? bookingId) {
    socket.emit('location:update', {
      'lat': lat,
      'lng': lng,
      'bookingId': bookingId
    });
  }

  void joinBookingRoom(String bookingId) {
    socket.emit('booking:join', {'bookingId': bookingId});
  }
}
```

### 5.2 Location Tracking Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Caregiver   │     │    Server    │     │     User     │
│     App      │     │  (Socket.IO) │     │     App      │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       │ location:update    │                    │
       │ (every 5-10 sec)   │                    │
       │───────────────────►│                    │
       │                    │                    │
       │                    │ Save to Redis      │
       │                    │────────────────────│
       │                    │                    │
       │                    │ location:broadcast │
       │                    │───────────────────►│
       │                    │                    │
       │                    │                    │ Update map
       │                    │                    │ marker
       │                    │                    │
```

---

## 6. Payment Integration

### 6.1 Payment Gateway Options

| Gateway      | Pros                               | Cons                   | Recommendation |
| ------------ | ---------------------------------- | ---------------------- | -------------- |
| **Midtrans** | Gojek ecosystem, mature, QRIS      | Slightly higher fees   | Primary        |
| **Xendit**   | Fast payout, good API              | Less brand recognition | Secondary      |
| **DOKU**     | Local player, government contracts | Older tech             | Alternative    |

**Recommendation:** Start with **Midtrans** (primary), add Xendit later for redundancy.

### 6.2 Supported Payment Methods

| Method              | Provider               | Fee            | Implementation |
| ------------------- | ---------------------- | -------------- | -------------- |
| **QRIS**            | All banks/e-wallets    | 0.7%           | Midtrans       |
| **GoPay**           | Gojek                  | 2%             | Midtrans       |
| **OVO**             | Grab                   | 2%             | Midtrans       |
| **DANA**            | Dana Indonesia         | 1.5%           | Midtrans       |
| **ShopeePay**       | Shopee                 | 2%             | Midtrans       |
| **Virtual Account** | BCA, Mandiri, BNI, BRI | Rp 4,000-5,000 | Midtrans       |

### 6.3 Payment Flow

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│   User   │     │ SRICARE  │     │ Midtrans │     │  Bank/   │
│   App    │     │  Server  │     │   API    │     │ E-Wallet │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │
     │ 1. Book & Pay  │                │                │
     │───────────────►│                │                │
     │                │                │                │
     │                │ 2. Create      │                │
     │                │    Transaction │                │
     │                │───────────────►│                │
     │                │                │                │
     │                │ 3. Payment URL │                │
     │                │◄───────────────│                │
     │                │                │                │
     │ 4. Redirect to │                │                │
     │    Payment     │                │                │
     │◄───────────────│                │                │
     │                │                │                │
     │ 5. Pay via     │                │                │
     │    QR/E-wallet │                │                │
     │────────────────────────────────────────────────►│
     │                │                │                │
     │                │                │ 6. Webhook     │
     │                │                │    Callback    │
     │                │◄───────────────│                │
     │                │                │                │
     │ 7. Payment     │                │                │
     │    Confirmed   │                │                │
     │◄───────────────│                │                │
     │                │                │                │
```

### 6.4 Midtrans Integration (NestJS)

```typescript
// payments.service.ts
import Midtrans from "midtrans-client";

@Injectable()
export class PaymentsService {
  private snap: Midtrans.Snap;

  constructor() {
    this.snap = new Midtrans.Snap({
      isProduction: process.env.NODE_ENV === "production",
      serverKey: process.env.MIDTRANS_SERVER_KEY,
      clientKey: process.env.MIDTRANS_CLIENT_KEY,
    });
  }

  async createTransaction(booking: Booking, user: User) {
    const orderId = `SRICARE-${booking.id}-${Date.now()}`;

    const parameter = {
      transaction_details: {
        order_id: orderId,
        gross_amount: booking.totalPrice,
      },
      customer_details: {
        first_name: user.name,
        phone: user.phone,
      },
      item_details: [
        {
          id: booking.serviceType,
          price: booking.totalPrice,
          quantity: 1,
          name: `${booking.serviceType} - ${booking.durationHours} jam`,
        },
      ],
      enabled_payments: [
        "gopay",
        "shopeepay",
        "dana",
        "ovo",
        "qris",
        "bca_va",
        "bni_va",
      ],
    };

    const transaction = await this.snap.createTransaction(parameter);

    // Save payment record
    await this.paymentsRepository.save({
      bookingId: booking.id,
      amount: booking.totalPrice,
      status: "pending",
      gateway: "midtrans",
      gatewayRef: orderId,
    });

    return {
      token: transaction.token,
      redirectUrl: transaction.redirect_url,
    };
  }

  async handleWebhook(notification: MidtransNotification) {
    const payment = await this.paymentsRepository.findByGatewayRef(
      notification.order_id,
    );

    if (
      notification.transaction_status === "settlement" ||
      notification.transaction_status === "capture"
    ) {
      payment.status = "paid";
      payment.paidAt = new Date();
      payment.method = notification.payment_type;

      // Update booking status
      await this.bookingsService.updateStatus(payment.bookingId, "confirmed");

      // Notify caregiver
      await this.notificationsService.notifyCaregiver(
        payment.bookingId,
        "new_booking",
      );
    }

    await this.paymentsRepository.save(payment);
  }
}
```

---

## 7. Maps & Location

### 7.1 Map Provider Options

| Provider        | Pros                       | Cons            | Pricing               |
| --------------- | -------------------------- | --------------- | --------------------- |
| **Google Maps** | Best coverage, familiar    | Costly at scale | $2-7/1000 requests    |
| **Mapbox**      | Customizable, good pricing | Less local data | $0.50-5/1000 requests |
| **HERE Maps**   | Good routing, offline      | Less popular    | Enterprise pricing    |

**Recommendation:** Start with **Google Maps** (best coverage Indonesia), migrate to Mapbox if cost becomes issue.

### 7.2 Key Map Features

| Feature                    | Implementation                    |
| -------------------------- | --------------------------------- |
| **Show Nearby Caregivers** | Markers on map with PostGIS query |
| **Real-time Tracking**     | Socket.IO + marker updates        |
| **Route Display**          | Directions API polyline           |
| **ETA Calculation**        | Distance Matrix API               |
| **Geocoding**              | Address to coordinates            |
| **Reverse Geocoding**      | Coordinates to address            |

### 7.3 Flutter Maps Implementation

```dart
// booking_map_screen.dart
class BookingMapScreen extends StatefulWidget {
  final Booking booking;

  @override
  _BookingMapScreenState createState() => _BookingMapScreenState();
}

class _BookingMapScreenState extends State<BookingMapScreen> {
  late GoogleMapController _mapController;
  final Set<Marker> _markers = {};
  final Set<Polyline> _polylines = {};
  StreamSubscription? _locationSubscription;

  @override
  void initState() {
    super.initState();
    _initializeMap();
    _subscribeToLocationUpdates();
  }

  void _subscribeToLocationUpdates() {
    _locationSubscription = socketService.locationStream.listen((update) {
      setState(() {
        _markers.removeWhere((m) => m.markerId.value == 'caregiver');
        _markers.add(Marker(
          markerId: MarkerId('caregiver'),
          position: LatLng(update.lat, update.lng),
          icon: BitmapDescriptor.defaultMarkerWithHue(BitmapDescriptor.hueGreen),
          infoWindow: InfoWindow(title: 'Caregiver sedang menuju'),
        ));
      });

      // Update ETA
      _calculateETA(LatLng(update.lat, update.lng));
    });
  }

  Future<void> _calculateETA(LatLng caregiverPos) async {
    final destination = LatLng(
      widget.booking.pickupLat,
      widget.booking.pickupLng
    );

    final eta = await mapsService.getETA(caregiverPos, destination);
    setState(() => _estimatedArrival = eta);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          GoogleMap(
            initialCameraPosition: CameraPosition(
              target: LatLng(widget.booking.pickupLat, widget.booking.pickupLng),
              zoom: 15,
            ),
            markers: _markers,
            polylines: _polylines,
            onMapCreated: (controller) => _mapController = controller,
          ),
          Positioned(
            bottom: 20,
            left: 20,
            right: 20,
            child: BookingStatusCard(
              booking: widget.booking,
              eta: _estimatedArrival,
            ),
          ),
        ],
      ),
    );
  }
}
```

---

## 8. Infrastructure

### 8.1 Cloud Architecture (Google Cloud)

```
┌──────────────────────────────────────────────────────────────┐
│                    Google Cloud Platform                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────────┐    ┌─────────────────┐                │
│   │  Cloud Load     │    │   Cloud CDN     │                │
│   │   Balancer      │    │  (Static assets)│                │
│   └────────┬────────┘    └─────────────────┘                │
│            │                                                 │
│            ▼                                                 │
│   ┌─────────────────────────────────────────┐               │
│   │        Cloud Run (Auto-scaling)         │               │
│   │  ┌──────────┐  ┌──────────┐            │               │
│   │  │ API      │  │ Socket   │            │               │
│   │  │ Service  │  │ Service  │            │               │
│   │  └──────────┘  └──────────┘            │               │
│   └─────────────────────────────────────────┘               │
│                          │                                   │
│            ┌─────────────┼─────────────┐                    │
│            ▼             ▼             ▼                    │
│   ┌──────────────┐ ┌──────────┐ ┌──────────────┐           │
│   │  Cloud SQL   │ │  Redis   │ │ Cloud        │           │
│   │ (PostgreSQL) │ │ (Memorystore)│ Storage     │           │
│   │  + PostGIS   │ │          │ │ (Images)     │           │
│   └──────────────┘ └──────────┘ └──────────────┘           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 8.2 Cost Estimation (Monthly)

| Service             | Specification                     | Est. Cost (USD)    |
| ------------------- | --------------------------------- | ------------------ |
| Cloud Run           | 2 instances, 1vCPU, 2GB           | $50-100            |
| Cloud SQL           | PostgreSQL, 2vCPU, 8GB, 100GB SSD | $80-120            |
| Redis (Memorystore) | 1GB                               | $30-50             |
| Cloud Storage       | 50GB + bandwidth                  | $10-20             |
| Cloud CDN           | Bandwidth                         | $10-20             |
| Firebase (FCM)      | Push notifications                | Free tier          |
| **Total**           |                                   | **$180-310/month** |

### 8.3 Scaling Strategy

| Phase          | Users         | Infrastructure                          |
| -------------- | ------------- | --------------------------------------- |
| **MVP**        | <1,000        | Single Cloud Run instance, basic SQL    |
| **Growth**     | 1,000-10,000  | 2-4 Cloud Run instances, upgraded SQL   |
| **Scale**      | 10,000-50,000 | Auto-scaling, read replicas, CDN        |
| **Enterprise** | 50,000+       | Kubernetes, microservices, multi-region |

---

## 9. Security

### 9.1 Security Measures

| Layer              | Security Measure                     |
| ------------------ | ------------------------------------ |
| **Transport**      | HTTPS/TLS 1.3 everywhere             |
| **Authentication** | JWT + Phone OTP verification         |
| **Authorization**  | Role-based access control (RBAC)     |
| **Data at Rest**   | PostgreSQL encryption, Cloud KMS     |
| **API Security**   | Rate limiting, input validation      |
| **Payment**        | PCI-DSS compliant gateway (Midtrans) |
| **Personal Data**  | GDPR/UU PDP compliance               |

### 9.2 Data Privacy (UU PDP Compliance)

| Requirement         | Implementation                   |
| ------------------- | -------------------------------- |
| Consent             | Explicit consent at registration |
| Data Minimization   | Only collect necessary data      |
| Right to Access     | User can export their data       |
| Right to Delete     | Account deletion with data purge |
| Data Protection     | Encryption, access controls      |
| Breach Notification | Monitoring + alerting system     |

### 9.3 Caregiver Verification

| Step | Verification                       |
| ---- | ---------------------------------- |
| 1    | Phone OTP verification             |
| 2    | KTP photo upload + OCR validation  |
| 3    | Selfie with KTP (liveness check)   |
| 4    | Certificate upload (if applicable) |
| 5    | Background check (manual review)   |
| 6    | Training completion                |

---

## 10. Development Roadmap

### 10.1 MVP (Month 1-4)

| Week  | Backend                        | Mobile                         | Priority |
| ----- | ------------------------------ | ------------------------------ | -------- |
| 1-2   | Project setup, Auth module     | Flutter setup, Auth screens    | P0       |
| 3-4   | Users, Caregivers CRUD         | Profile screens, List views    | P0       |
| 5-6   | Bookings module, GPS matching  | Booking flow, Maps integration | P0       |
| 7-8   | Payments (Midtrans)            | Payment screens, Checkout      | P0       |
| 9-10  | Real-time tracking (Socket.IO) | Live tracking UI               | P1       |
| 11-12 | Ratings, Notifications         | Rating UI, Push notifications  | P1       |
| 13-14 | Testing, Bug fixes             | UI polish, Testing             | P0       |
| 15-16 | Beta deployment                | Beta release                   | P0       |

### 10.2 Post-MVP Features

| Feature               | Priority | Timeline  |
| --------------------- | -------- | --------- |
| In-app Chat           | P1       | Month 5   |
| Subscription packages | P2       | Month 6   |
| Caregiver analytics   | P2       | Month 6   |
| Admin dashboard       | P1       | Month 5-6 |
| Doctor visit service  | P3       | Month 7+  |
| Multi-language        | P3       | Month 8+  |

### 10.3 Team Requirements

| Role                     | Count | Responsibility                        |
| ------------------------ | ----- | ------------------------------------- |
| **Full-stack Developer** | 2     | Backend (NestJS) + Frontend (Flutter) |
| **Mobile Developer**     | 1     | Flutter specialist                    |
| **UI/UX Designer**       | 1     | App design, user research             |
| **QA Engineer**          | 1     | Testing, quality assurance            |
| **DevOps**               | 0.5   | Infrastructure, CI/CD                 |
| **Product Manager**      | 1     | Product direction, prioritization     |

**Total: 5-6 people** for MVP development

---

## Appendix

### A. Technology Comparison Summary

| Aspect    | SRICARE Choice       | Alternative     | Rationale              |
| --------- | -------------------- | --------------- | ---------------------- |
| Mobile    | Flutter              | React Native    | Performance + GPS      |
| Backend   | NestJS               | Express/Fastify | Structure + TypeScript |
| Database  | PostgreSQL + PostGIS | MongoDB         | Geospatial + Relations |
| Real-time | Socket.IO            | Firebase RTDB   | Control + Features     |
| Maps      | Google Maps          | Mapbox          | Coverage Indonesia     |
| Payment   | Midtrans             | Xendit          | Ecosystem + Features   |
| Cloud     | Google Cloud         | AWS             | Pricing + Integration  |

### B. Reference Links

- [Flutter Documentation](https://docs.flutter.dev)
- [NestJS Documentation](https://docs.nestjs.com)
- [PostGIS Documentation](https://postgis.net/documentation)
- [Midtrans API Docs](https://docs.midtrans.com)
- [Google Maps Flutter](https://pub.dev/packages/google_maps_flutter)
- [Socket.IO](https://socket.io/docs/v4)
- [Gojek Tech Stack](https://gojek.github.io)

---

_Document Version: 1.0_
_Last Updated: January 2026_
_Author: SURIOTA Team_
