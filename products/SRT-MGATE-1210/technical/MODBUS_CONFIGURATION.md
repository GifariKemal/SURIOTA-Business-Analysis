# SRT-MGATE-1210 - Modbus Configuration Guide

## Panduan Teknis Konfigurasi Modbus Devices

**Version**: 1.0 | **Last Updated**: December 28, 2025

---

# DAFTAR ISI

1. [Modbus Overview](#1-modbus-overview)
2. [RS-485 Wiring](#2-rs-485-wiring)
3. [Modbus RTU Configuration](#3-modbus-rtu-configuration)
4. [Common Device Configurations](#4-common-device-configurations)
5. [Advanced Settings](#5-advanced-settings)
6. [Testing & Verification](#6-testing--verification)

---

# 1. MODBUS OVERVIEW

## Protocol Support

| Protocol | Support | Notes |
|----------|:-------:|-------|
| Modbus RTU (RS-485) | ✅ | Primary protocol |
| Modbus TCP | ✅ | Via Ethernet/WiFi |
| Modbus ASCII | ❌ | Not supported |

## Function Codes Supported

| Code | Name | Description |
|:----:|------|-------------|
| 01 | Read Coils | Read discrete outputs |
| 02 | Read Discrete Inputs | Read discrete inputs |
| 03 | Read Holding Registers | Read analog outputs |
| 04 | Read Input Registers | Read analog inputs |
| 05 | Write Single Coil | Write single output |
| 06 | Write Single Register | Write single analog |
| 15 | Write Multiple Coils | Write multiple outputs |
| 16 | Write Multiple Registers | Write multiple analogs |

## Gateway Capacity

| Specification | Value |
|---------------|-------|
| RS-485 Ports | 2 |
| Devices per Port | Up to 32 |
| Total Devices | Up to 64 |
| Registers per Device | Up to 64 |
| Polling Interval | 1s - 60s configurable |

---

# 2. RS-485 WIRING

## Terminal Pinout

```
┌─────────────────────────────────────────────────────────┐
│                    RS-485 TERMINALS                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    PORT 1                         PORT 2                │
│   ┌─────┬─────┐                 ┌─────┬─────┐           │
│   │ A+  │ B-  │                 │ A+  │ B-  │           │
│   └─────┴─────┘                 └─────┴─────┘           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Signal Reference

| Pin | Signal | Description |
|-----|--------|-------------|
| A+ | Data+ | Non-inverting, positive |
| B- | Data- | Inverting, negative |

> **Note:** Some manufacturers label A as D+ and B as D-. Check device datasheet.

## Wiring Configurations

### Point-to-Point (1 Device)

```
Gateway                    Modbus Device
┌───────┐                 ┌───────┐
│  A+ ──────────────────── A+   │
│      │                 │      │
│  B- ──────────────────── B-   │
└───────┘                 └───────┘
```

### Daisy Chain (Multiple Devices)

```
Gateway     Device 1      Device 2      Device 3
┌───┐      ┌───┬───┐     ┌───┬───┐     ┌───┐
│A+─┼──────┤A+ │A+├──────┤A+ │A+├──────┤A+ │
│   │      │   │   │     │   │   │     │   │
│B-─┼──────┤B- │B-├──────┤B- │B-├──────┤B- │
└───┘      └───┴───┘     └───┴───┘     └───┘
           Addr:1        Addr:2        Addr:3
```

### Star Topology (NOT Recommended)

```
             ┌──── Device 1
Gateway ─────┼──── Device 2    ← AVOID THIS!
             └──── Device 3
```

> ⚠️ **Warning:** Star topology creates signal reflections. Always use daisy chain.

## Cable Specifications

| Specification | Recommended | Notes |
|---------------|-------------|-------|
| Cable Type | Twisted Pair | Shielded (STP) preferred |
| Wire Gauge | 22-24 AWG | |
| Max Length | 1200m (4000ft) | Total bus length |
| Impedance | 120Ω | |

## Termination

For cable runs > 50m, add 120Ω termination resistors at both ends:

```
Gateway (120Ω)                           Last Device (120Ω)
┌───────────┐                           ┌───────────┐
│  A+ ─┬────────────────────────────────┬─ A+      │
│     [R]                               [R]        │
│  B- ─┴────────────────────────────────┴─ B-      │
└───────────┘                           └───────────┘
     R = 120Ω                               R = 120Ω
```

---

# 3. MODBUS RTU CONFIGURATION

## Via SURIOTA Config App

### Step 1: Open Devices Menu

1. Connect to gateway via Bluetooth
2. Navigate to **Devices** → **RS485 Port 1** (or Port 2)

### Step 2: Serial Settings

| Parameter | Options | Default |
|-----------|---------|---------|
| **Baud Rate** | 9600, 19200, 38400, 57600, 115200 | 9600 |
| **Data Bits** | 7, 8 | 8 |
| **Parity** | None, Odd, Even | None |
| **Stop Bits** | 1, 2 | 1 |

> 💡 **Tip:** All devices on same port must use identical serial settings

### Step 3: Add Modbus Device

| Field | Description | Example |
|-------|-------------|---------|
| **Device Name** | Friendly name | "pH Sensor IPAL" |
| **Slave Address** | 1-247 | 1 |
| **Poll Interval** | Seconds | 10 |
| **Timeout** | Milliseconds | 1000 |

### Step 4: Add Registers

| Field | Description | Example |
|-------|-------------|---------|
| **Register Name** | Parameter name | "pH Value" |
| **Function Code** | 01-04 | 03 (Holding) |
| **Start Address** | 0x0000-0xFFFF | 0x0000 |
| **Data Type** | See below | Float32 |
| **Multiplier** | Scale factor | 0.01 |
| **Offset** | Zero offset | 0 |

## Data Types

| Type | Size | Range | Use Case |
|------|:----:|-------|----------|
| **Int16** | 16-bit | -32768 to 32767 | Integer values |
| **UInt16** | 16-bit | 0 to 65535 | Unsigned integers |
| **Int32** | 32-bit | ±2.1 billion | Large integers |
| **UInt32** | 32-bit | 0 to 4.2 billion | Large unsigned |
| **Float32** | 32-bit | ±3.4E38 | Decimal values |
| **Float64** | 64-bit | ±1.8E308 | High precision |

## Byte Order

| Setting | Description | Use When |
|---------|-------------|----------|
| **Big Endian (AB)** | High byte first | Most devices |
| **Little Endian (BA)** | Low byte first | Some PLCs |
| **Big Endian Swap (CDAB)** | High word first | Some sensors |
| **Little Endian Swap (DCBA)** | Low word first | Rare |

---

# 4. COMMON DEVICE CONFIGURATIONS

## pH Sensor (Generic 4-20mA with Modbus)

| Setting | Value |
|---------|-------|
| Slave Address | 1 |
| Baud Rate | 9600 |
| Parity | None |
| Function Code | 03 |
| Register | 0x0000 |
| Data Type | Float32 |

| Register | Address | Description |
|----------|---------|-------------|
| pH Value | 0x0000 | Current pH |
| Temperature | 0x0002 | Compensation temp |

## Flow Meter (Electromagnetic)

| Setting | Value |
|---------|-------|
| Slave Address | 2 |
| Baud Rate | 9600 |
| Function Code | 03/04 |

| Register | Address | Data Type | Unit |
|----------|---------|-----------|------|
| Flow Rate | 0x0000 | Float32 | m³/h |
| Totalizer | 0x0002 | UInt32 | m³ |
| Flow Velocity | 0x0004 | Float32 | m/s |

## Energy Meter (3-Phase)

| Setting | Value |
|---------|-------|
| Slave Address | 1 |
| Baud Rate | 9600 |
| Function Code | 03 |

| Register | Address | Data Type | Unit |
|----------|---------|-----------|------|
| Voltage L1 | 0x0000 | Float32 | V |
| Voltage L2 | 0x0002 | Float32 | V |
| Voltage L3 | 0x0004 | Float32 | V |
| Current L1 | 0x0006 | Float32 | A |
| Current L2 | 0x0008 | Float32 | A |
| Current L3 | 0x000A | Float32 | A |
| Total kWh | 0x000C | Float32 | kWh |
| Power Factor | 0x000E | Float32 | - |

## Level Sensor (Ultrasonic)

| Setting | Value |
|---------|-------|
| Slave Address | 3 |
| Baud Rate | 9600 |

| Register | Address | Data Type | Unit |
|----------|---------|-----------|------|
| Distance | 0x0001 | UInt16 | mm |
| Level | 0x0002 | UInt16 | mm |
| Temperature | 0x0003 | Int16 | °C x10 |

## Temperature Sensor (RTD/Thermocouple)

| Setting | Value |
|---------|-------|
| Slave Address | 4 |
| Baud Rate | 9600 |

| Register | Address | Data Type | Unit |
|----------|---------|-----------|------|
| Temperature | 0x0000 | Int16 | °C x10 |
| Status | 0x0001 | UInt16 | Bit flags |

---

# 5. ADVANCED SETTINGS

## Poll Groups

Group registers to reduce bus traffic:

| Group | Devices | Interval |
|-------|---------|----------|
| Fast (critical) | pH, Flow | 5s |
| Normal | Energy, Level | 30s |
| Slow | Temperature | 60s |

## Error Handling

| Setting | Options | Recommended |
|---------|---------|-------------|
| Retry Count | 0-5 | 2 |
| Retry Delay | 100-5000ms | 500ms |
| On Error | Last value / NaN / 0 | Last value |

## MQTT Topic Mapping

Data is published to MQTT with format:

```json
{
  "device": "pH Sensor IPAL",
  "timestamp": "2025-12-28T10:30:00Z",
  "data": {
    "ph_value": 7.25,
    "temperature": 28.5
  }
}
```

Topic: `surge/{org_id}/{location_id}/{gateway_id}/telemetry`

---

# 6. TESTING & VERIFICATION

## Using SURIOTA Config App

1. Navigate to **Devices** → Select device
2. Tap **"Read Now"**
3. Verify values match device display

## LED Indicators

| LED | Behavior | Meaning |
|-----|----------|---------|
| RS1-TX | Blinking | Gateway polling Port 1 |
| RS1-RX | Blinking | Device responding |
| RS1-TX only | Gateway polling, no response |
| Neither | Not configured or error |

## Common Test Scenarios

| Test | Expected Result |
|------|-----------------|
| Disconnect device | Timeout error in app |
| Wrong address | No response |
| Wrong baud | Garbage or timeout |
| Swap A/B wires | No response |

## Modbus Analyzer (Optional)

For advanced debugging, use USB-RS485 adapter with:
- Modbus Poll (Windows)
- QModMaster (Cross-platform)
- SURIOTA Modbus Test App (Android)

---

# TROUBLESHOOTING

| Problem | Possible Cause | Solution |
|---------|---------------|----------|
| No response | Wrong address | Check device DIP switches |
| No response | Wrong baud rate | Match to device setting |
| No response | A/B wiring swapped | Swap A and B wires |
| Wrong values | Wrong data type | Check Int16 vs Float32 |
| Wrong values | Wrong byte order | Try different endianness |
| Intermittent | Termination needed | Add 120Ω at bus ends |
| Intermittent | Cable too long | Check < 1200m total |
| Multiple errors | Address conflict | Ensure unique addresses |

---

# REFERENCE: COMMON BRANDS

## pH Sensors
- **Hach**: 9600 baud, Modbus RTU, Float32
- **Endress+Hauser**: Configurable
- **Yokogawa**: 9600/19200, Float32

## Flow Meters
- **Siemens MAG**: 9600, Float32
- **Endress+Hauser Promag**: 9600, Float32
- **ABB**: 9600, Int32/Float32

## Energy Meters
- **Schneider PM5xxx**: 9600, Float32
- **ABB**: 9600, Float32
- **Eastron SDM**: 9600, Float32

## PLC
- **Siemens S7**: Native Modbus TCP
- **Mitsubishi**: RS-485 option
- **Omron**: RS-485 option

---

_Technical Guide v1.0_
_Last Updated: December 28, 2025_
