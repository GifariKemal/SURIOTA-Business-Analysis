# SURGE Platform - API Quick Start Guide

## Mulai Integrasi dalam 15 Menit

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# TL;DR - 5 Menit Quick Start

```bash
# 1. Login dan dapatkan token
curl -X POST https://api.suriota.com/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"you@company.com","password":"yourpass"}'

# 2. Query data terbaru
curl -X GET "https://api.suriota.com/v1/telemetry/latest?device_id=YOUR_DEVICE" \
  -H "Authorization: Bearer YOUR_TOKEN"

# Done!
```

---

# STEP-BY-STEP GUIDE

## Step 1: Dapatkan API Credentials

### Option A: Dari Dashboard

1. Login ke https://surge.suriota.com
2. Buka **Settings > API Access**
3. Klik **Generate API Key**
4. Copy API Key (hanya ditampilkan sekali!)

### Option B: Programmatic Login

```bash
curl -X POST https://api.suriota.com/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "password": "your_password"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "dGhpcyBpcyBhIHJlZnJlc2...",
  "expires_in": 3600,
  "token_type": "Bearer"
}
```

---

## Step 2: Test Connection

```bash
curl -X GET https://api.suriota.com/v1/health \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Expected Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "timestamp": "2025-12-28T08:30:00Z"
}
```

---

## Step 3: List Your Devices

```bash
curl -X GET https://api.suriota.com/v1/devices \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "devices": [
    {
      "id": "dev_abc123",
      "name": "Gateway IPAL Outlet 1",
      "type": "gateway",
      "status": "online",
      "last_seen": "2025-12-28T08:29:55Z"
    },
    {
      "id": "dev_xyz789",
      "name": "Gateway IPAL Outlet 2",
      "type": "gateway",
      "status": "online",
      "last_seen": "2025-12-28T08:29:50Z"
    }
  ],
  "total": 2
}
```

---

## Step 4: Get Latest Telemetry

```bash
curl -X GET "https://api.suriota.com/v1/telemetry/latest?device_id=dev_abc123" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "device_id": "dev_abc123",
  "timestamp": "2025-12-28T08:30:00Z",
  "data": {
    "ph": 7.2,
    "cod": 85.5,
    "tss": 32.1,
    "nh3": 4.5,
    "flow": 25.3
  }
}
```

---

## Step 5: Get Historical Data

```bash
curl -X GET "https://api.suriota.com/v1/telemetry/history?device_id=dev_abc123&start=2025-12-27&end=2025-12-28&interval=1h" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "device_id": "dev_abc123",
  "interval": "1h",
  "count": 24,
  "data": [
    {"timestamp": "2025-12-27T00:00:00Z", "ph": 7.1, "cod": 82, "tss": 30},
    {"timestamp": "2025-12-27T01:00:00Z", "ph": 7.2, "cod": 85, "tss": 32},
    {"timestamp": "2025-12-27T02:00:00Z", "ph": 7.0, "cod": 80, "tss": 28},
    ...
  ]
}
```

---

# API REFERENCE - QUICK CHEATSHEET

## Base URL

```
Production: https://api.suriota.com/v1
```

## Authentication

All requests require Bearer token:
```
Authorization: Bearer <access_token>
```

## Common Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login` | Get access token |
| POST | `/auth/refresh` | Refresh token |
| GET | `/health` | API health check |
| GET | `/devices` | List all devices |
| GET | `/devices/:id` | Get device detail |
| GET | `/telemetry/latest` | Latest readings |
| GET | `/telemetry/history` | Historical data |
| GET | `/alerts` | List alerts |
| GET | `/alerts/:id` | Get alert detail |
| POST | `/export` | Export data |

---

# CODE EXAMPLES

## Python

```python
import requests

# Configuration
BASE_URL = "https://api.suriota.com/v1"
EMAIL = "your@email.com"
PASSWORD = "your_password"

# Login
def get_token():
    response = requests.post(f"{BASE_URL}/auth/login", json={
        "email": EMAIL,
        "password": PASSWORD
    })
    return response.json()["access_token"]

# Get latest telemetry
def get_latest(device_id, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{BASE_URL}/telemetry/latest",
        params={"device_id": device_id},
        headers=headers
    )
    return response.json()

# Get historical data
def get_history(device_id, start, end, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"{BASE_URL}/telemetry/history",
        params={
            "device_id": device_id,
            "start": start,
            "end": end,
            "interval": "1h"
        },
        headers=headers
    )
    return response.json()

# Usage
token = get_token()
latest = get_latest("dev_abc123", token)
print(f"Current pH: {latest['data']['ph']}")

history = get_history("dev_abc123", "2025-12-01", "2025-12-28", token)
print(f"Data points: {len(history['data'])}")
```

---

## JavaScript / Node.js

```javascript
const axios = require('axios');

const BASE_URL = 'https://api.suriota.com/v1';

class SurgeAPI {
  constructor(email, password) {
    this.email = email;
    this.password = password;
    this.token = null;
  }

  async login() {
    const response = await axios.post(`${BASE_URL}/auth/login`, {
      email: this.email,
      password: this.password
    });
    this.token = response.data.access_token;
    return this.token;
  }

  async getLatest(deviceId) {
    const response = await axios.get(`${BASE_URL}/telemetry/latest`, {
      params: { device_id: deviceId },
      headers: { Authorization: `Bearer ${this.token}` }
    });
    return response.data;
  }

  async getHistory(deviceId, start, end, interval = '1h') {
    const response = await axios.get(`${BASE_URL}/telemetry/history`, {
      params: { device_id: deviceId, start, end, interval },
      headers: { Authorization: `Bearer ${this.token}` }
    });
    return response.data;
  }
}

// Usage
async function main() {
  const api = new SurgeAPI('your@email.com', 'password');
  await api.login();

  const latest = await api.getLatest('dev_abc123');
  console.log('Current pH:', latest.data.ph);

  const history = await api.getHistory('dev_abc123', '2025-12-01', '2025-12-28');
  console.log('Data points:', history.data.length);
}

main();
```

---

## cURL One-Liners

### Login
```bash
curl -X POST https://api.suriota.com/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"you@company.com","password":"pass"}'
```

### Get Devices
```bash
curl https://api.suriota.com/v1/devices \
  -H "Authorization: Bearer TOKEN"
```

### Get Latest Data
```bash
curl "https://api.suriota.com/v1/telemetry/latest?device_id=dev_abc123" \
  -H "Authorization: Bearer TOKEN"
```

### Get History (Last 7 Days)
```bash
curl "https://api.suriota.com/v1/telemetry/history?device_id=dev_abc123&start=2025-12-21&end=2025-12-28&interval=1h" \
  -H "Authorization: Bearer TOKEN"
```

### Export to CSV
```bash
curl -X POST https://api.suriota.com/v1/export \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "device_id": "dev_abc123",
    "parameters": ["ph", "cod", "tss"],
    "start": "2025-12-01",
    "end": "2025-12-28",
    "format": "csv"
  }' \
  -o export.csv
```

---

# ERROR HANDLING

## HTTP Status Codes

| Code | Meaning | Action |
|:----:|---------|--------|
| 200 | Success | Process response |
| 201 | Created | Resource created |
| 400 | Bad Request | Check request parameters |
| 401 | Unauthorized | Token expired, re-login |
| 403 | Forbidden | No permission |
| 404 | Not Found | Check resource ID |
| 429 | Rate Limited | Wait and retry |
| 500 | Server Error | Contact support |

## Error Response Format

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "Parameter 'device_id' is required",
    "details": {
      "parameter": "device_id",
      "expected": "string"
    }
  }
}
```

## Handling Token Expiry

```python
import requests

class SurgeAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None
        self.refresh_token = None

    def login(self):
        response = requests.post(f"{BASE_URL}/auth/login", json={
            "email": self.email,
            "password": self.password
        })
        data = response.json()
        self.token = data["access_token"]
        self.refresh_token = data["refresh_token"]

    def refresh(self):
        response = requests.post(f"{BASE_URL}/auth/refresh", json={
            "refresh_token": self.refresh_token
        })
        self.token = response.json()["access_token"]

    def request(self, method, endpoint, **kwargs):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.request(method, f"{BASE_URL}{endpoint}",
                                    headers=headers, **kwargs)

        if response.status_code == 401:
            # Token expired, try refresh
            self.refresh()
            headers = {"Authorization": f"Bearer {self.token}"}
            response = requests.request(method, f"{BASE_URL}{endpoint}",
                                        headers=headers, **kwargs)

        return response
```

---

# RATE LIMITS

| Tier | Requests/Minute | Requests/Day |
|------|:---------------:|:------------:|
| Trial | 10 | 100 |
| Starter | 30 | 1,000 |
| Business | 100 | 10,000 |
| Professional | 500 | Unlimited |

## Rate Limit Headers

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1703750400
```

## Handling Rate Limits

```python
import time

def api_request_with_retry(url, headers, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            # Rate limited
            reset_time = int(response.headers.get('X-RateLimit-Reset', 60))
            wait_time = reset_time - time.time() + 1
            print(f"Rate limited. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
            continue

        return response

    raise Exception("Max retries exceeded")
```

---

# PAGINATION

## Request

```bash
curl "https://api.suriota.com/v1/telemetry/history?device_id=dev_abc123&start=2025-12-01&end=2025-12-28&limit=100&offset=0" \
  -H "Authorization: Bearer TOKEN"
```

## Response

```json
{
  "data": [...],
  "pagination": {
    "total": 672,
    "limit": 100,
    "offset": 0,
    "has_more": true
  }
}
```

## Fetching All Pages

```python
def fetch_all_data(device_id, start, end, token):
    all_data = []
    offset = 0
    limit = 100

    while True:
        response = requests.get(
            f"{BASE_URL}/telemetry/history",
            params={
                "device_id": device_id,
                "start": start,
                "end": end,
                "limit": limit,
                "offset": offset
            },
            headers={"Authorization": f"Bearer {token}"}
        )

        data = response.json()
        all_data.extend(data["data"])

        if not data["pagination"]["has_more"]:
            break

        offset += limit

    return all_data
```

---

# SUPPORT

| Resource | Link/Contact |
|----------|--------------|
| Full API Docs | https://docs.suriota.com/api |
| API Status | https://status.suriota.com |
| Email Support | api@suriota.com |
| WhatsApp | +62 858-3567-2476 |

---

_Document Version: 1.0_
_For Developers_
_Last Updated: December 28, 2025_
