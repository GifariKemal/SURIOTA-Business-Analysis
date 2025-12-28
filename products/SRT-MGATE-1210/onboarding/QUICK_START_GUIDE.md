# SRT-MGATE-1210 - Quick Start Guide

## Setup dalam 15 Menit

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# TL;DR - 5 Steps

```
1. Pasang power → LED PWR nyala hijau
2. Download SURIOTA Config App
3. Connect via Bluetooth (PIN: 123456)
4. Masukkan WiFi + MQTT + Modbus settings
5. Save → Data mengalir ke cloud!
```

---

# BEFORE YOU START

## Requirements

| Item | Check |
|------|:-----:|
| SRT-MGATE-1210 gateway | [ ] |
| Power adapter 12-48V DC | [ ] |
| RS-485 cable to Modbus device | [ ] |
| WiFi network credentials | [ ] |
| MQTT broker credentials | [ ] |
| Smartphone (Android/iOS) | [ ] |

## Download App

| Platform | Link |
|----------|------|
| **Android** | Play Store → "SURIOTA Config" |
| **iOS** | App Store → "SURIOTA Config" |

---

# STEP 1: POWER ON (2 menit)

## Connect Power

1. Hubungkan power adapter ke terminal V+ dan GND
2. Colok adapter ke listrik

```
Power Adapter          Gateway
    (+) ───────────► V+
    (-) ───────────► GND
```

## Verify LEDs

| LED | Status | Meaning |
|-----|--------|---------|
| **PWR** | 🟢 Solid | Power OK |
| **STS** | 🟢 Blinking | System Running |
| **CFG** | 🟡 Solid | Ready to Configure |

> **Tunggu 15 detik** sampai LED STS blinking

---

# STEP 2: CONNECT VIA BLUETOOTH (2 menit)

## On Your Phone

1. **Enable Bluetooth** di phone settings
2. **Open** SURIOTA Config App
3. Tap **"Scan"** button

## Find Your Gateway

Gateway akan muncul sebagai:
```
SRT-MGATE-XXXX
(XXXX = 4 digit serial number)
```

## Connect

1. Tap gateway name
2. Enter PIN: **123456**
3. Tap **Connect**

> ✅ Status: "Connected to SRT-MGATE-XXXX"

---

# STEP 3: CONFIGURE WIFI (3 menit)

## Navigate to WiFi Settings

1. Tap **"Network"** menu
2. Tap **"WiFi"** tab

## Enter Credentials

| Field | Value |
|-------|-------|
| **SSID** | [Your WiFi name] |
| **Password** | [Your WiFi password] |
| **Security** | WPA2-PSK (default) |

## Verify (Optional)

1. Tap **"Test Connection"**
2. Wait for result: "WiFi Connected"

> **Note:** Hanya support **2.4GHz** WiFi, bukan 5GHz

---

# STEP 4: CONFIGURE MQTT (3 menit)

## Navigate to MQTT Settings

1. Tap **"Cloud"** menu
2. Tap **"MQTT"** tab

## Enter Broker Details

### For SURGE Platform:

| Field | Value |
|-------|-------|
| **Broker** | mqtt.suriota.com |
| **Port** | 8883 |
| **TLS** | Enabled |
| **Username** | [From SURGE Dashboard] |
| **Password** | [From SURGE Dashboard] |

### For AWS IoT:

| Field | Value |
|-------|-------|
| **Broker** | [your-endpoint].iot.[region].amazonaws.com |
| **Port** | 8883 |
| **TLS** | Enabled |
| **Certificate** | [Upload via app] |

### For Other Platforms:

| Field | Value |
|-------|-------|
| **Broker** | [Your MQTT broker address] |
| **Port** | 1883 (no TLS) or 8883 (TLS) |
| **Username** | [If required] |
| **Password** | [If required] |

---

# STEP 5: CONFIGURE MODBUS (5 menit)

## Navigate to Modbus Settings

1. Tap **"Devices"** menu
2. Tap **"Add Device"**

## Enter Device Details

| Field | Example | Your Value |
|-------|---------|------------|
| **Name** | pH Sensor | _________ |
| **Port** | RS485-1 | _________ |
| **Slave Address** | 1 | _________ |
| **Baud Rate** | 9600 | _________ |
| **Data Bits** | 8 | _________ |
| **Parity** | None | _________ |
| **Stop Bits** | 1 | _________ |

## Add Registers

| Field | Example | Your Value |
|-------|---------|------------|
| **Register Name** | pH Value | _________ |
| **Address** | 0x0000 | _________ |
| **Function** | 03 (Read Holding) | _________ |
| **Data Type** | Float32 | _________ |

> 💡 **Tip:** Lihat datasheet sensor untuk address dan data type

## Save & Apply

1. Tap **"Save Device"**
2. Tap **"Apply All"**
3. Gateway akan restart (10 detik)

---

# VERIFY OPERATION

## Check LEDs

| LED | Expected Status |
|-----|-----------------|
| PWR | 🟢 Solid Green |
| STS | 🟢 Blinking Green |
| WiFi | 🟢 Solid Green |
| NET | 🟢 Blinking Green |
| RS1-TX | 🟢 Blinking (if polling) |
| RS1-RX | 🟢 Blinking (if data) |

## Check Cloud

1. Login ke SURGE / your cloud platform
2. Find your device
3. Verify data is coming through

---

# TROUBLESHOOTING QUICK FIX

| Problem | Solution |
|---------|----------|
| Gateway tidak terdeteksi BLE | Restart app, pastikan Bluetooth ON |
| WiFi tidak connect | Cek SSID/password, pastikan 2.4GHz |
| MQTT tidak connect | Cek credentials, port, TLS setting |
| No Modbus data | Cek wiring A/B, slave address, baud rate |
| LED CFG tetap kuning | Restart gateway (power cycle) |

---

# WHAT'S NEXT?

1. **Add more devices** - Repeat Step 5 untuk device lain
2. **Set up alerts** - Configure di cloud platform
3. **Create dashboards** - Visualisasi data
4. **Change default PIN** - Security best practice

---

# SUPPORT

| Channel | Contact |
|---------|---------|
| WhatsApp | +62 858-3567-2476 |
| Email | support@suriota.com |
| Website | www.suriota.com |

---

_Quick Start Guide v1.0_
_Last Updated: December 28, 2025_
