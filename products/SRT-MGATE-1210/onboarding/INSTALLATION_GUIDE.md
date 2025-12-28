# SRT-MGATE-1210 - Installation Guide

## Panduan Lengkap Instalasi Hardware

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# DAFTAR ISI

1. [Package Contents](#1-package-contents)
2. [Specifications](#2-specifications)
3. [Pre-Installation](#3-pre-installation)
4. [Physical Installation](#4-physical-installation)
5. [Electrical Connections](#5-electrical-connections)
6. [Initial Power-On](#6-initial-power-on)
7. [Post-Installation Checklist](#7-post-installation-checklist)

---

# 1. PACKAGE CONTENTS

## Standard Package

| Item | Qty | Check |
|------|:---:|:-----:|
| SRT-MGATE-1210 Gateway Unit | 1 | [ ] |
| WiFi Antenna (SMA) | 1 | [ ] |
| Quick Start Guide | 1 | [ ] |
| DIN Rail Mounting Clip | 1 | [ ] |
| Terminal Block Connectors | 4 | [ ] |

## PoE Version Additional

| Item | Qty | Check |
|------|:---:|:-----:|
| All Standard items above | - | [ ] |
| PoE Injector (optional purchase) | 0/1 | [ ] |

## Optional Accessories (Separate Purchase)

| Item | Part Number |
|------|-------------|
| Power Adapter 12V DC 1A | SRT-PWR-12V1A |
| Power Adapter 24V DC 1A | SRT-PWR-24V1A |
| DIN Rail 35mm (1 meter) | SRT-DIN-35 |
| RS-485 Cable 2-wire (10m) | SRT-CBL-485 |

---

# 2. SPECIFICATIONS

## Physical

| Specification | Value |
|---------------|-------|
| **Dimensions** | 110 x 90 x 58 mm |
| **Weight** | ~250g |
| **Mounting** | DIN Rail 35mm / Wall Mount |
| **Enclosure** | PLA+ Industrial Grade |
| **Color** | Gray |

## Environmental

| Specification | Value |
|---------------|-------|
| **Operating Temp** | -40°C to +75°C |
| **Storage Temp** | -40°C to +85°C |
| **Humidity** | 5% to 95% RH (non-condensing) |
| **IP Rating** | IP20 (indoor use) |

## Power

| Model | Input Voltage | Current | Notes |
|-------|---------------|---------|-------|
| **Standard** | 12-48V DC | <500mA @12V | Terminal block |
| **PoE** | 36-57V DC (PoE) | <300mA | IEEE 802.3af/at |
| **PoE** | 12-48V DC | <500mA | DC backup |

## Interfaces

| Interface | Specification |
|-----------|---------------|
| **RS-485 Port 1** | 2-wire, 9600-115200 baud, up to 32 devices |
| **RS-485 Port 2** | 2-wire, 9600-115200 baud, up to 32 devices |
| **Ethernet** | RJ45, 10/100 Mbps |
| **WiFi** | 2.4GHz 802.11 b/g/n |
| **Bluetooth** | BLE 5.0 |
| **Antenna** | SMA female |

---

# 3. PRE-INSTALLATION

## Site Requirements

| Requirement | Specification | Check |
|-------------|---------------|:-----:|
| **Power** | 12-48V DC source available | [ ] |
| **Network** | Ethernet OR WiFi coverage | [ ] |
| **Temperature** | -40°C to +75°C | [ ] |
| **Humidity** | Non-condensing environment | [ ] |
| **Mounting** | DIN rail or wall space | [ ] |
| **Clearance** | 50mm around unit for ventilation | [ ] |

## Tools Required

| Tool | Purpose |
|------|---------|
| Screwdriver (Phillips) | Terminal block |
| Wire stripper | RS-485 cable prep |
| Multimeter | Voltage verification |
| Smartphone | BLE configuration |
| SURIOTA Config App | Configuration |

## Pre-Installation Checklist

| Task | Status |
|------|:------:|
| Review site conditions | [ ] |
| Verify power source voltage | [ ] |
| Verify network availability | [ ] |
| Prepare RS-485 cables | [ ] |
| Download SURIOTA Config App | [ ] |
| Verify Modbus device addresses | [ ] |

---

# 4. PHYSICAL INSTALLATION

## 4.1 DIN Rail Mounting

### Step 1: Prepare DIN Rail

```
     ┌─────────────────────────────────────────┐
     │         35mm DIN Rail                   │
     │  ═══════════════════════════════════    │
     │                                         │
     │  Pastikan rail terpasang kuat dan rata  │
     └─────────────────────────────────────────┘
```

### Step 2: Attach Unit to Rail

1. Posisikan gateway dengan DIN clip menghadap rail
2. Kaitkan clip atas ke rail
3. Tekan bagian bawah hingga "klik"
4. Pastikan unit terpasang kokoh

```
     Posisi Benar:

     ┌────────────┐
     │  Gateway   │ ← Klik!
     │            │
     └────┬───────┘
          │
     ═════╧════════  DIN Rail
```

### Step 3: Attach Antenna

1. Pasang antenna WiFi ke connector SMA
2. Putar searah jarum jam hingga kencang
3. Posisikan antenna vertikal untuk sinyal optimal

```
          │
         ╱│╲  Antenna vertikal
        ╱ │ ╲
     ┌────┴────┐
     │ Gateway │
     └─────────┘
```

## 4.2 Wall Mounting (Alternative)

1. Gunakan bracket mounting (optional accessory)
2. Tandai 2 titik lubang di dinding
3. Bor dan pasang fisher
4. Pasang bracket dengan sekrup
5. Kaitkan gateway ke bracket

---

# 5. ELECTRICAL CONNECTIONS

## 5.1 Power Connection

### Terminal Block Pinout

```
     ┌─────────────────────────────┐
     │   POWER TERMINAL BLOCK      │
     ├─────────────────────────────┤
     │                             │
     │   V+  │  GND                │
     │   (+) │  (-)                │
     │   12-48V DC                 │
     │                             │
     └─────────────────────────────┘
```

### Wiring Diagram

```
     Power Supply                    Gateway
     ┌──────────┐                 ┌──────────┐
     │   +12V ──────────────────► │ V+ (+)   │
     │          │                 │          │
     │   GND  ──────────────────► │ GND (-)  │
     └──────────┘                 └──────────┘
```

### Voltage Selection Guide

| Power Source | Recommended | Notes |
|--------------|:-----------:|-------|
| 12V DC Adapter | ✅ | Most common |
| 24V DC Industrial | ✅ | Factory standard |
| 48V DC Telecom | ✅ | Maximum voltage |
| PoE Switch (PoE model) | ✅ | Simplest cabling |

## 5.2 RS-485 Connection

### Terminal Block Pinout

```
     ┌─────────────────────────────────────────┐
     │        RS-485 TERMINAL BLOCK            │
     ├─────────────────────────────────────────┤
     │                                         │
     │   PORT 1          │      PORT 2         │
     │   A(+)  B(-)      │      A(+)  B(-)     │
     │                                         │
     └─────────────────────────────────────────┘
```

### Wiring Diagram (Single Device)

```
     Modbus Device              Gateway Port 1
     ┌──────────┐              ┌──────────┐
     │   A (+) ────────────────► A (+)   │
     │          │              │          │
     │   B (-) ────────────────► B (-)   │
     └──────────┘              └──────────┘
```

### Wiring Diagram (Multiple Devices - Daisy Chain)

```
     Gateway          Device 1        Device 2        Device 3
     ┌─────┐         ┌─────┐         ┌─────┐         ┌─────┐
     │ A+──┼────────►│A+  A+├───────►│A+  A+├───────►│ A+  │
     │     │         │      │        │      │        │     │
     │ B-──┼────────►│B-  B-├───────►│B-  B-├───────►│ B-  │
     └─────┘         └─────┘         └─────┘         └─────┘
                       │                │              │
                     Addr: 1          Addr: 2        Addr: 3
```

### RS-485 Best Practices

| Rule | Description |
|------|-------------|
| **Cable Type** | Twisted pair, shielded (STP) recommended |
| **Max Length** | 1200m total bus length |
| **Max Devices** | 32 per port |
| **Termination** | 120Ω at bus ends (long cables) |
| **Shield** | Ground at one end only |

## 5.3 Ethernet Connection

### Cable Requirements

| Specification | Requirement |
|---------------|-------------|
| Cable Type | Cat5e or Cat6 |
| Connector | RJ45 |
| Max Length | 100m |

### Connection

```
     Gateway                    Switch/Router
     ┌─────────┐               ┌─────────────┐
     │   RJ45 ─────────────────│ Port X      │
     │         │               │             │
     └─────────┘               └─────────────┘
```

---

# 6. INITIAL POWER-ON

## 6.1 Power-On Sequence

1. Verify all connections secure
2. Apply power to gateway
3. Wait 10-15 seconds for boot
4. Observe LED indicators

## 6.2 LED Status Reference

### Normal Operation LEDs

| LED | Color | Status | Meaning |
|-----|-------|--------|---------|
| **PWR** | Green | Solid | Power OK |
| **STS** | Green | Blinking | System Running |
| **CFG** | Yellow | Solid | Config Mode |
| **CFG** | Off | - | Normal Mode |
| **WiFi** | Green | Solid | WiFi Connected |
| **WiFi** | Blinking | - | WiFi Connecting |
| **NET** | Green | Solid | Cloud Connected |
| **NET** | Blinking | - | Sending Data |
| **RS1 TX** | Green | Blinking | Port 1 Transmit |
| **RS1 RX** | Green | Blinking | Port 1 Receive |
| **RS2 TX** | Green | Blinking | Port 2 Transmit |
| **RS2 RX** | Green | Blinking | Port 2 Receive |

### LED Diagram

```
     ┌────────────────────────────────────────┐
     │                                        │
     │   ● PWR   ● STS   ● CFG               │
     │                                        │
     │   ● WiFi  ● NET                       │
     │                                        │
     │   ● RS1-TX  ● RS1-RX                  │
     │   ● RS2-TX  ● RS2-RX                  │
     │                                        │
     └────────────────────────────────────────┘
```

## 6.3 First-Time Configuration

After power-on:

1. Open SURIOTA Config App on smartphone
2. Enable Bluetooth
3. Tap "Scan for Devices"
4. Select "SRT-MGATE-XXXX"
5. Enter PIN: **123456** (default)
6. Configure WiFi, MQTT, Modbus
7. Save configuration
8. Gateway will restart

---

# 7. POST-INSTALLATION CHECKLIST

## Physical Installation

| Check | Status |
|-------|:------:|
| Unit securely mounted | [ ] |
| Antenna attached and vertical | [ ] |
| All cables properly connected | [ ] |
| Adequate ventilation around unit | [ ] |
| No condensation risk | [ ] |

## Electrical

| Check | Status |
|-------|:------:|
| Power voltage verified (12-48V DC) | [ ] |
| Power polarity correct (+/-) | [ ] |
| RS-485 wiring correct (A/B) | [ ] |
| Ethernet cable connected (if used) | [ ] |

## LED Verification

| LED | Expected Status | Actual |
|-----|-----------------|:------:|
| PWR | Solid Green | [ ] |
| STS | Blinking Green | [ ] |
| WiFi | Solid/Blinking Green | [ ] |
| NET | Solid/Blinking Green | [ ] |

## Configuration

| Check | Status |
|-------|:------:|
| WiFi configured | [ ] |
| MQTT broker configured | [ ] |
| Modbus devices configured | [ ] |
| Data appearing in cloud | [ ] |

## Documentation

| Document | Provided |
|----------|:--------:|
| Installation location noted | [ ] |
| Serial number recorded | [ ] |
| Network credentials documented | [ ] |
| Customer trained on mobile app | [ ] |

---

# INSTALLATION SIGN-OFF

| Field | Value |
|-------|-------|
| **Installation Date** | _________________ |
| **Technician Name** | _________________ |
| **Customer Name** | _________________ |
| **Serial Number** | _________________ |
| **Firmware Version** | _________________ |
| **Notes** | _________________ |

---

**Signatures:**

| | |
|---|---|
| Technician | _________________ |
| Customer | _________________ |

---

_Document Version: 1.0_
_Last Updated: December 28, 2025_
