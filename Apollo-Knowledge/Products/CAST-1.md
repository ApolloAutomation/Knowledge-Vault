---
title: CAST-1
aliases: [CAST 1, CAST1, CAST-1 Audio Casting Device]
type: product
audience: customer
source: https://apolloautomation.com/products/cast-1-audio-casting-device
status: preorder
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-15
---
# CAST-1

## Description

The Apollo CAST-1 makes non-smart speakers smart. It plugs into powered speakers, amplifiers and AV receivers with a 3.5mm cable and connects them to ESPHome and Music Assistant via Sendspin. You can stream music, announcements and alarms to existing speakers and sync playback across several CAST-1 units or other Sendspin speakers. It connects over Wi-Fi or with the optional Ethernet HAT.

## Features

- Runs open source ESPHome firmware; supports Sendspin and the ESPHome media player
- 3.5mm analog stereo line out via a TI PCM5122 DAC
- Onboard RGB LED
- Acts as a Bluetooth proxy
- Solder pads for 5 V, GND and IO1 to connect an addressable RGB LED strip or external sensors
- Discovered automatically in Music Assistant and Home Assistant
- Fully local, no cloud required
- Use cases: vintage hi-fi revival, budget whole-home audio, Home Assistant announcements, garage/workshop/patio audio, reactive lighting

## Specs

- Connectivity: 2.4 GHz Wi-Fi; Ethernet with the optional W5500 Ethernet HAT (data only, no PoE)
- Audio output: 3.5mm analog stereo line out
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: Unknown — escalate to support
- Waterproof: Unknown — escalate to support
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: N/A — USB-C powered, no sleep mode
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[ESP32-S3]] — microcontroller; 2.4 GHz Wi-Fi and BLE, Bluetooth proxy
- [[PCM5122]] — Texas Instruments 32-bit stereo DAC for the analog audio output
- W5500 — Ethernet chip on the optional Ethernet HAT

## Options and add-ons

- USB-C cable
- USB-C charger
- 3.5mm audio/aux cable
- Ethernet cable
- W5500 Ethernet HAT (data only, no PoE)
- Related: [[CAST-PRO-1]] adds audio in, optical out and built-in Ethernet.

## What's in the box

- CAST-1 Audio Casting device with case

## Common questions and answers

### Will the CAST-1 make my old speakers or stereo smart?

Yes. The CAST-1 connects to powered speakers, amplifiers and AV receivers with a 3.5mm cable and adds them to ESPHome and Music Assistant via Sendspin, so you can stream music, announcements and alarms to them.

### Can I sync music across several rooms with CAST-1?

Yes. Playback can be synced across several CAST-1 units, [[CAST-PRO-1]] units, or other Sendspin speakers through Music Assistant.

### Does the CAST-1 have Ethernet or PoE?

Not built in. The CAST-1 uses 2.4 GHz Wi-Fi, and you can add wired Ethernet with the optional W5500 Ethernet HAT. The HAT is data only and does not supply PoE, so the CAST-1 still needs USB-C power. If you want built-in Ethernet, see the [[CAST-PRO-1]].

### Does the CAST-1 need the cloud?

No. It runs ESPHome firmware and works fully locally, and it is discovered automatically in Home Assistant and Music Assistant.

### What is the difference between CAST-1 and CAST PRO-1?

The [[CAST-PRO-1]] adds a 3.5mm Line In jack for sources like record players, an optical output, and built-in Ethernet. The CAST-1 has a 3.5mm analog line out only, with Ethernet available through the optional HAT.

### Can I connect an LED strip or sensors to the CAST-1?

Yes. The board has solder pads for 5 V, GND and IO1 that you can use to connect an addressable RGB LED strip or external sensors.

### Does the CAST-1 have optical or digital audio output?

No. The CAST-1 outputs 3.5mm analog stereo through a TI [[PCM5122]] DAC. Optical output is available on the [[CAST-PRO-1]].
