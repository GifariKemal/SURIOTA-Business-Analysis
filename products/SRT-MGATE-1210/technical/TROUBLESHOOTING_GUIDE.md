# SRT-MGATE-1210 - Troubleshooting Guide

## Panduan Lengkap Pemecahan Masalah

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# QUICK DIAGNOSIS

## LED Status Quick Reference

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LED QUICK DIAGNOSIS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PWR OFF        → Check power source (12-48V DC)                           │
│  STS not blink  → System hang, power cycle needed                          │
│  CFG solid      → Still in config mode, save & restart                     │
│  WiFi OFF       → WiFi not configured or AP not found                      │
│  NET OFF        → MQTT not connected, check broker settings                │
│  RS1-TX only    → Modbus device not responding                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# DAFTAR ISI

1. [Power Issues](#1-power-issues)
2. [Bluetooth/BLE Issues](#2-bluetoothble-issues)
3. [WiFi Issues](#3-wifi-issues)
4. [Ethernet Issues](#4-ethernet-issues)
5. [MQTT/Cloud Issues](#5-mqttcloud-issues)
6. [Modbus/RS-485 Issues](#6-modbusrs-485-issues)
7. [System Issues](#7-system-issues)
8. [LED Indicator Reference](#8-led-indicator-reference)
9. [Factory Reset](#9-factory-reset)
10. [Support Contact](#10-support-contact)

---

# 1. POWER ISSUES

## 1.1 Gateway Tidak Menyala (PWR LED OFF)

| Check | Action |
|-------|--------|
| Power source | Verify 12-48V DC available |
| Polarity | Check V+ to positive, GND to negative |
| Voltage | Measure with multimeter (should be 12-48V) |
| Connections | Tighten terminal block screws |
| Adapter | Try different power adapter |

### Troubleshooting Steps

```
Step 1: Measure voltage at terminal block
        Expected: 12-48V DC

Step 2: Check polarity
        V+ = Positive (+)
        GND = Negative (-)

Step 3: If PoE version, check PoE switch/injector
        - PoE LED on switch should be ON
        - Try different PoE port

Step 4: Try backup DC power (PoE version has dual input)
```

## 1.2 Intermittent Power (Gateway Reboots Randomly)

| Cause | Solution |
|-------|----------|
| Voltage fluctuation | Add capacitor or use regulated supply |
| Loose connection | Tighten all terminal screws |
| Power supply weak | Use higher current adapter (≥1A) |
| PoE overload | Check total PoE load on switch |

### Power Requirements

| Model | Input | Current | Notes |
|-------|-------|---------|-------|
| Standard | 12-48V DC | <500mA @12V | |
| PoE | 36-57V PoE | <300mA @48V | IEEE 802.3af/at |
| PoE | 12-48V DC | <500mA @12V | Backup input |

---

# 2. BLUETOOTH/BLE ISSUES

## 2.1 Gateway Tidak Terdeteksi di App

| Check | Action |
|-------|--------|
| Phone Bluetooth | Ensure Bluetooth is ON |
| Location permission | Grant location access to app |
| Distance | Stay within 10 meters |
| CFG LED | Should be solid yellow when in config mode |
| App version | Update to latest SURIOTA Config App |

### Troubleshooting Steps

```
Step 1: Restart app
        - Force close app
        - Reopen and tap "Scan"

Step 2: Toggle phone Bluetooth
        - Turn OFF, wait 5 seconds
        - Turn ON, scan again

Step 3: Check permissions
        Android: Settings → Apps → SURIOTA → Permissions
        iOS: Settings → SURIOTA → Bluetooth & Location

Step 4: Power cycle gateway
        - Disconnect power
        - Wait 10 seconds
        - Reconnect power
        - Wait for CFG LED
```

## 2.2 Connection Drops During Configuration

| Cause | Solution |
|-------|----------|
| Distance too far | Move closer to gateway |
| Interference | Move away from other BLE devices |
| Phone issue | Restart phone Bluetooth |
| Multiple phones | Disconnect other phones first |

## 2.3 Wrong PIN Error

| Issue | Solution |
|-------|----------|
| Default PIN rejected | Factory default is **123456** |
| PIN changed | Contact admin for current PIN |
| PIN forgotten | Factory reset required (see Section 9) |

---

# 3. WIFI ISSUES

## 3.1 WiFi Tidak Connect (WiFi LED OFF)

| Check | Action |
|-------|--------|
| SSID spelling | Verify exact name (case-sensitive) |
| Password | Re-enter password carefully |
| 2.4GHz | Must be 2.4GHz, not 5GHz |
| WiFi coverage | Check signal strength at location |
| AP capacity | Router may have device limit |

### Troubleshooting Steps

```
Step 1: Verify WiFi settings via BLE
        - Connect with SURIOTA Config App
        - Navigate to Network → WiFi
        - Confirm SSID and password

Step 2: Check WiFi frequency
        - SRT-MGATE-1210 ONLY supports 2.4GHz
        - 5GHz networks will NOT appear
        - Many routers broadcast both - select 2.4GHz SSID

Step 3: Test WiFi with phone
        - Stand at gateway location
        - Connect phone to same WiFi
        - If phone can't connect, WiFi issue

Step 4: Reboot router/AP
        - Sometimes AP needs restart
        - Wait 2 minutes after router reboot
```

## 3.2 WiFi Intermittent Disconnect

| Cause | Solution |
|-------|----------|
| Weak signal | Move gateway closer to AP or add AP |
| Interference | Change WiFi channel (1, 6, or 11) |
| Router overload | Reduce devices or upgrade router |
| IP conflict | Set static IP or check DHCP |
| Power save | Disable WiFi power save on router |

### Signal Strength Guide

| RSSI | Signal | Reliability |
|:----:|--------|-------------|
| > -50 dBm | Excellent | Best |
| -50 to -60 dBm | Good | Recommended |
| -60 to -70 dBm | Fair | May have issues |
| < -70 dBm | Poor | Move gateway/AP |

## 3.3 Connected to WiFi but No Internet

| Check | Action |
|-------|--------|
| DNS | Try 8.8.8.8 or 1.1.1.1 |
| Gateway IP | Verify router gateway address |
| Firewall | Check if router blocks MQTT ports |
| Proxy | Gateway doesn't support proxy |

---

# 4. ETHERNET ISSUES

## 4.1 Ethernet Tidak Connect (ETH LED OFF)

| Check | Action |
|-------|--------|
| Cable | Try different Ethernet cable |
| Port | Try different switch port |
| Link LED | Check switch port LED |
| Cable length | Max 100 meters |
| Cable type | Cat5e or Cat6 recommended |

### Troubleshooting Steps

```
Step 1: Check physical connection
        - Cable fully inserted at both ends
        - Audible "click" when inserted

Step 2: Check switch port
        - Switch port LED should blink
        - Try different port

Step 3: Test cable
        - Use cable tester or try different cable
        - Check for bent pins in RJ45

Step 4: Check IP settings
        - DHCP: Router should assign IP
        - Static: Verify IP, subnet, gateway correct
```

## 4.2 Ethernet Connected but No MQTT

| Cause | Solution |
|-------|----------|
| VLAN | Check VLAN settings on switch |
| Firewall | Open port 8883 (or 1883) |
| DNS | Verify DNS server can resolve broker |
| Proxy | Gateway doesn't support HTTP proxy |

---

# 5. MQTT/CLOUD ISSUES

## 5.1 MQTT Tidak Connect (NET LED OFF)

| Check | Action |
|-------|--------|
| Broker address | Verify hostname/IP correct |
| Port | 1883 (no TLS) or 8883 (TLS) |
| Username/Password | Re-enter credentials |
| TLS setting | Match broker TLS requirement |
| Network | Ensure internet access available |

### Troubleshooting Steps

```
Step 1: Verify broker settings via app
        - Broker: mqtt.example.com or IP address
        - Port: 8883 (TLS) or 1883 (no TLS)
        - Username/Password: from your platform

Step 2: Check TLS requirement
        - SURGE: Port 8883, TLS enabled
        - AWS IoT: Port 8883, TLS + certificate
        - Mosquitto: Usually port 1883, no TLS (local)

Step 3: Test broker reachability
        - From same network, try:
          ping mqtt.example.com
          telnet mqtt.example.com 8883

Step 4: Check firewall
        - Outbound port 8883 or 1883 must be open
        - Some corporate networks block these
```

## 5.2 MQTT Connect but Data Tidak Muncul di Cloud

| Cause | Solution |
|-------|----------|
| Topic mismatch | Verify publish topic matches subscription |
| Permission | Check user has publish rights |
| QoS | Try QoS 1 instead of QoS 0 |
| Payload format | Verify JSON format correct |

### Check Data Flow

```
Gateway → MQTT Broker → Cloud Platform

1. Gateway sending? (RS-TX/RX blinking, NET blinking)
2. Broker receiving? (Check broker logs)
3. Platform subscribed? (Check topic subscription)
```

## 5.3 Data Delay / Not Real-time

| Cause | Solution |
|-------|----------|
| Poll interval | Reduce poll interval (min 1 second) |
| Network latency | Check internet connection |
| QoS 2 | Use QoS 1 for faster delivery |
| Broker overload | Contact cloud provider |

---

# 6. MODBUS/RS-485 ISSUES

## 6.1 No Response from Modbus Device

| Check | Action |
|-------|--------|
| Wiring | A+ to A+, B- to B- |
| Slave address | Verify device address setting |
| Baud rate | Match device baud rate |
| Parity | Match device parity setting |
| Termination | Add 120Ω for long cables |

### Troubleshooting Steps

```
Step 1: Verify wiring
        Gateway A+ → Device A+ (or D+)
        Gateway B- → Device B- (or D-)

        ⚠️ Some manufacturers swap A/B labels!
        If not working, try swapping A and B

Step 2: Check device settings
        - Slave address (1-247)
        - Baud rate (usually 9600)
        - Parity (usually None)
        - Stop bits (usually 1)

Step 3: LED diagnosis
        RS-TX blinking = Gateway sending
        RS-RX NOT blinking = Device not responding

Step 4: Test with known-good device
        - If available, test with another Modbus device
        - Confirms gateway port is working
```

## 6.2 RS-TX Blinking but RS-RX Not Blinking

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     PROBLEM: TX ONLY, NO RX                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Gateway is SENDING but NOT RECEIVING responses                            │
│                                                                             │
│  Possible Causes:                                                           │
│  ─────────────────                                                          │
│  1. Wrong slave address configured                                          │
│  2. Wrong baud rate / parity / stop bits                                   │
│  3. A/B wires swapped                                                       │
│  4. Device powered off                                                      │
│  5. Device in wrong mode                                                    │
│  6. Cable too long without termination                                      │
│  7. Multiple devices with same address (conflict)                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 6.3 Wrong Data Values

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Garbage values | Wrong data type | Check Int16/Float32/etc |
| Reversed bytes | Wrong endianness | Try different byte order |
| Values x10 or /10 | Scale factor | Adjust multiplier |
| Always zero | Wrong register address | Check device datasheet |
| Negative values | Signed vs unsigned | Check data type |

### Data Type Reference

| Type | Size | Use When |
|------|------|----------|
| Int16 | 16-bit | Integer with negatives |
| UInt16 | 16-bit | Integer, always positive |
| Float32 | 32-bit | Decimal values |
| Int32/UInt32 | 32-bit | Large integers |

### Byte Order (Endianness)

| Setting | Description | Try When |
|---------|-------------|----------|
| Big Endian (AB) | Most common | First attempt |
| Little Endian (BA) | Some PLCs | If values wrong |
| Big Swap (CDAB) | Some sensors | 32-bit values wrong |
| Little Swap (DCBA) | Rare | Last resort |

## 6.4 Intermittent Communication

| Cause | Solution |
|-------|----------|
| Loose connection | Check and tighten terminals |
| No termination | Add 120Ω at both ends |
| Cable too long | Max 1200m for RS-485 |
| Electrical noise | Use shielded cable, ground shield |
| Baud rate too high | Try lower baud rate |

### RS-485 Cable Guidelines

| Cable Length | Termination | Shielding |
|--------------|:-----------:|:---------:|
| < 50m | Optional | Optional |
| 50-200m | Recommended | Recommended |
| > 200m | Required | Required |

---

# 7. SYSTEM ISSUES

## 7.1 Gateway Hang (STS LED Not Blinking)

| Action | Steps |
|--------|-------|
| Power cycle | Disconnect power, wait 10s, reconnect |
| Check power | Verify stable 12-48V DC |
| Check temperature | Ensure < 75°C |
| Factory reset | If persists (see Section 9) |

## 7.2 Configuration Not Saved

| Cause | Solution |
|-------|----------|
| Not applied | Tap "Apply All" after changes |
| BLE disconnected | Stay connected during save |
| App crashed | Restart app and reconfigure |

## 7.3 Firmware Update Failed

| Action | Steps |
|--------|-------|
| Retry | Wait 5 minutes, try again |
| Check connection | Ensure stable WiFi/Ethernet |
| Check battery | Phone battery > 20% |
| Check version | May already be latest |
| Contact support | If still fails |

## 7.4 RTC Time Wrong

| Cause | Solution |
|-------|----------|
| Battery depleted | Replace CR1220 battery |
| Never synced | Connect to cloud (auto-sync via NTP) |
| Timezone wrong | Set timezone in config |

---

# 8. LED INDICATOR REFERENCE

## Complete LED Table

| LED | Color | Status | Meaning |
|-----|-------|--------|---------|
| **PWR** | Green | Solid | Power OK |
| **PWR** | Off | - | No power |
| **STS** | Green | Blinking | System running normally |
| **STS** | Green | Solid | Booting |
| **STS** | Off | - | System hang |
| **CFG** | Yellow | Solid | Configuration mode active |
| **CFG** | Off | - | Normal operation |
| **WiFi** | Green | Solid | WiFi connected |
| **WiFi** | Green | Blinking | WiFi connecting |
| **WiFi** | Off | - | WiFi disabled or failed |
| **ETH** | Green | Solid | Ethernet link up |
| **ETH** | Green | Blinking | Ethernet activity |
| **ETH** | Off | - | No Ethernet link |
| **NET** | Green | Solid | Cloud/MQTT connected |
| **NET** | Green | Blinking | Sending data |
| **NET** | Off | - | Cloud disconnected |
| **RS1-TX** | Green | Blinking | Port 1 transmitting |
| **RS1-RX** | Green | Blinking | Port 1 receiving |
| **RS2-TX** | Green | Blinking | Port 2 transmitting |
| **RS2-RX** | Green | Blinking | Port 2 receiving |

## Quick Status Patterns

| Pattern | Status |
|---------|--------|
| PWR + STS blinking | System OK, check network |
| PWR + STS + WiFi | Connected to WiFi |
| PWR + STS + WiFi + NET | Fully operational |
| PWR + STS + RS-TX only | Modbus issue |
| PWR only | System not booting |

---

# 9. FACTORY RESET

## When to Factory Reset

- Forgotten BLE PIN
- Cannot connect via BLE
- Configuration corrupted
- Before transferring to new user

## Factory Reset Procedure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FACTORY RESET PROCEDURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Method 1: Via SURIOTA Config App                                           │
│  ─────────────────────────────────────                                      │
│  1. Connect via Bluetooth                                                   │
│  2. Navigate to System → Factory Reset                                      │
│  3. Confirm reset                                                           │
│  4. Gateway will restart                                                    │
│                                                                             │
│  Method 2: Hardware Button (If BLE not accessible)                          │
│  ─────────────────────────────────────────────────────                      │
│  1. Locate RESET button (small hole on enclosure)                          │
│  2. Power on gateway                                                        │
│  3. Press and hold RESET button for 10 seconds                             │
│  4. All LEDs will blink 3 times                                            │
│  5. Release button                                                          │
│  6. Gateway resets to factory defaults                                      │
│                                                                             │
│  ⚠️ WARNING: This erases ALL settings!                                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Factory Defaults

| Setting | Default Value |
|---------|---------------|
| BLE PIN | 123456 |
| WiFi | Not configured |
| Ethernet | DHCP enabled |
| MQTT | Not configured |
| RS-485 Port 1 | 9600, 8N1 |
| RS-485 Port 2 | 9600, 8N1 |
| Modbus devices | None |

---

# 10. SUPPORT CONTACT

## Before Contacting Support

Prepare this information:

| Information | Your Value |
|-------------|------------|
| Serial Number | ______________ |
| Firmware Version | ______________ |
| Problem Description | ______________ |
| LED Status | ______________ |
| Steps Already Tried | ______________ |

## Support Channels

| Channel | Contact | Response |
|---------|---------|----------|
| **WhatsApp** | +62 858-3567-2476 | < 1 jam (jam kerja) |
| **Email** | support@suriota.com | < 24 jam |
| **Phone** | +62 858-3567-2476 | Langsung |
| **Website** | www.suriota.com | Self-service |

## Support Hours

| Day | Hours (WIB) |
|-----|-------------|
| Senin - Jumat | 08:00 - 17:00 |
| Sabtu | 09:00 - 12:00 |
| Minggu / Libur | Email only |

## Warranty

| Condition | Coverage |
|-----------|----------|
| Standard warranty | 1 tahun |
| Extended warranty | Available |
| DOA (Dead on Arrival) | Replacement |
| User damage | Not covered |

---

# DIAGNOSTIC FLOWCHART

## General Troubleshooting Flow

```
                         START
                           │
                           ▼
                    ┌─────────────┐
                    │ PWR LED ON? │
                    └─────────────┘
                      │         │
                     YES        NO
                      │         │
                      ▼         ▼
              ┌───────────┐   Check power
              │ STS LED   │   connections
              │ blinking? │
              └───────────┘
                │       │
               YES      NO
                │       │
                ▼       ▼
         ┌──────────┐  Power cycle
         │WiFi/ETH  │  gateway
         │ LED ON?  │
         └──────────┘
           │      │
          YES     NO
           │      │
           ▼      ▼
    ┌──────────┐  Check WiFi/
    │ NET LED  │  Ethernet
    │   ON?    │  settings
    └──────────┘
      │      │
     YES     NO
      │      │
      ▼      ▼
   Check    Check MQTT
   Modbus   settings
   config
```

---

_Document Version: 1.0_
_Last Updated: December 28, 2025_
