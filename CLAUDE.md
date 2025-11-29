# Claude AI Context - SRT-MGATE-1210 Business Analysis

## Project Overview

This repository contains business analysis documentation for the **SRT-MGATE-1210** Industrial IoT Gateway series by **PT Surya Inovasi Prioritas (SURIOTA)**.

## Product Information

### SRT-MGATE-1210 Standard Version
- **Price**: Rp 2,800,000 (~$175 USD)
- **COGS**: Rp 1,450,000 (Fully Loaded Cost)
- **Gross Margin**: 48%
- **Features**: Dual RS-485 with ESD protection, WiFi WPA3, BLE 5.0, Ethernet 10/100, RTC with battery backup, 9 LED indicators

### SRT-MGATE-1210-POE Version
- **Price**: Rp 3,500,000 (~$219 USD)
- **COGS**: Rp 1,650,000 (Fully Loaded Cost)
- **Gross Margin**: 53%
- **Additional Feature**: IEEE 802.3af/at PoE support (9W, 36-57V) with auto-switch

## Key Technical Specifications

- **MCU**: ESP32-S3-WROOM-1 (Dual-core 240MHz, 8MB PSRAM)
- **RS-485**: 2 ports with ESD protection (TVS diodes), up to 32 devices/port
- **WiFi**: 2.4GHz 802.11 b/g/n, WPA3-PSK with auto-failover
- **Bluetooth**: BLE 5.0 for mobile configuration
- **Ethernet**: W5500 10/100 Mbps with magnetic isolation
- **RTC**: DS3231 with CR1220 battery backup
- **LED Indicators**: 9 LEDs (Status, Config, WiFi, NET, RS485 TX/RX, Power)
- **Protocol Input**: Modbus RTU (RS-485), Modbus TCP (WiFi/Ethernet)
- **Protocol Output**: MQTT + JSON format
- **Cloud Support**: AWS, Datacake, Grafana, ThingsBoard, SURGE, etc.
- **Power**: 12-48V DC (Standard), + PoE 36-57V (PoE version)
- **Operating Temp**: -40C to +75C (Industrial Grade)
- **Dimensions**: 110 x 90 x 58 mm
- **Warranty**: 1.5 Year
- **Certifications**: RoHS & CE, FCC (planned)

## Unique Selling Propositions (USP)

1. **BLE Mobile Configuration** - Setup via smartphone in 5 minutes (EXCLUSIVE)
2. **WiFi Auto Failover** - Automatic switch Ethernet to WiFi (EXCLUSIVE)
3. **RTC with Battery Backup** - Accurate timestamps even after power loss
4. **9 LED Status Indicators** - Complete system monitoring
5. **ESD Protection** - Industrial grade RS-485 protection
6. **PoE + DC Redundant Power** - Auto-switch dual power (PoE version)
7. **Local Indonesia Support** - Technical support in Bahasa Indonesia

## Competitor Positioning (Modbus-to-MQTT Gateway)

SURIOTA targets the **mid-range market** with premium features:

| Competitor | Model | Price (Tokopedia) | vs SURIOTA |
|------------|-------|-------------------|------------|
| USR-IOT | N720-ETH | Rp 3,500,000 | SURIOTA 20% cheaper, +WiFi +BLE |
| USR-IOT | N540 H7-4 | Rp 1,820,000 | SURIOTA +WiFi +BLE +RTC +ESD |
| BLIIoT | BL100 | Rp 3,373,000 | SURIOTA 17% cheaper, +BLE +RTC |
| ICP DAS | tGW-725 | Rp 3,450,000 | SURIOTA 19% cheaper, +MQTT +WiFi +BLE |
| Moxa | AIG-101-T | Rp 8,956,000 | SURIOTA 69% cheaper, +WiFi +BLE |

**Key Insight**: SURIOTA is the ONLY Modbus-to-MQTT gateway in Indonesia with WiFi + BLE + RTC

## Financial Metrics

- **Exchange Rate**: 1 USD = Rp 16,648 (actual) / Rp 16,000 (rounded)
- **Break-even**: 134 units
- **Target Sales**: 200 units (2 years)

## File Structure

```
SRT-MGATE-1210-Business-Analysis/
├── README.md                              # Repository overview
├── CLAUDE.md                              # This context file
└── SRT-MGATE-1210_BUSINESS_ANALYSIS.md    # Full analysis document (v5.4)
```

## Main Document Contents (v5.4)

1. Executive Summary & Pricing Recommendation
2. Product Specifications (Updated with RTC, 9 LED, ESD)
3. COGS Analysis (Actual production data)
4. Competitor Analysis (5 Modbus-to-MQTT competitors)
5. Feature Comparison Matrix
6. Pricing Strategy & Volume Discounts
7. USP Breakdown
8. Sales & Marketing Guide (16 scenarios)
9. Objection Handling
10. Brand Awareness Strategy
11. Financial Projections
12. Technical Specifications Appendix

## Notes for AI Assistant

- **2kV Isolation claim REMOVED** - Schematic shows MAX485ESA+T (non-isolated)
- **ESD Protection ADDED** - TVS diodes (SMCJ60CA-M3/9AT) on RS-485
- **RTC ADDED** - DS3231SN# with CR1220 battery backup
- **9 LED Indicators ADDED** - Status, Config, WiFi, NET, RS485 TX/RX
- SD Card/MicroSD feature has been **deferred** (not included)
- Focus on Modbus-to-MQTT gateway competitors only
- All prices shown in both USD and IDR
- Target market: Indonesia industrial sector

## Related Repositories

- `GatewaySuriotaPOC` - Main firmware source code
- `GatewaySuriotaOTA` - OTA firmware releases

## Contact

PT Surya Inovasi Prioritas (SURIOTA)
- Email: sales@suriota.com
- Website: www.suriota.com
- Phone: +62 858-3567-2476
