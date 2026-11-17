---
title: CAST-PRO-1
aliases: [CAST PRO-1, CAST PRO 1, CAST-PRO 1, CASTPRO-1, CAST PRO]
type: product
audience: customer
source: https://apolloautomation.com/products/cast-pro-1
status: preorder
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-16
---
# CAST-PRO-1

## Description

The Apollo CAST PRO-1 adds a 3.5mm Line In jack to the casting idea of [[CAST-1]], so a record player, CD player or TV becomes a source in Music Assistant. For output it connects to speakers, soundbars, amplifiers and AV receivers over analog and optical and joins Home Assistant and Music Assistant via Sendspin. It has built-in Ethernet with Wi-Fi as a backup.

## Features

- Audio in: 3.5mm Line In for line-level sources (some turntables may require a phono preamp)
- Audio out: 3.5mm dual analog and optical jack, selected in Home Assistant; analog uses a PCM5122 DAC
- Built-in 10/100 Ethernet (data only, no PoE) and 2.4 GHz Wi-Fi
- Open source ESPHome firmware with OTA updates; Sendspin support; syncs with other CAST PRO-1 and CAST-1 units
- Bluetooth proxy; Bluetooth LE also used for Improv Wi-Fi setup
- Onboard RGB LEDs (4) plus screw terminal (5V, GND, IO1) for addressable LED strips
- Works with WiZ WizMote remotes, every button configurable in Home Assistant
- Use cases: soundbar or AV receiver in whole-home audio, record player in every room, media cabinet over Ethernet, announcements, music-reactive lighting

## Specs

- Ethernet: Built-in 10/100 (data only, no PoE)
- Wi-Fi: 2.4 GHz
- Audio input: 3.5mm Line In (line level; some turntables may require a phono preamp)
- Audio output: 3.5mm dual analog and optical jack
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: -40 to 65 °C (rating of the ESP32-S3 module, most conservative ESP32-S3 range)
- Waterproof: No. The CAST PRO-1 is not waterproof; keep it indoors and dry
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: N/A — no sleep mode
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[ESP32-S3]] — processor; 2.4 GHz Wi-Fi and BLE, Bluetooth proxy
- [[PCM5122]] — DAC for the analog audio output

## Options and add-ons

- USB-C cable
- USB-C charger
- Ethernet cable
- 3.5mm audio/aux cable
- Optical to 3.5mm (Toslink to mini Toslink) cable for optical out
- Optional bundled [[CAST-1]]

## What's in the box

- CAST PRO-1 with case

## Common questions and answers

### Can I connect my record player, CD player or TV to the CAST PRO-1?

Yes. The CAST PRO-1 has a 3.5mm Line In jack for line-level sources, so a record player, CD player or TV becomes a source in Music Assistant that you can play in other rooms.

### Do I need a phono preamp to connect my turntable to the CAST PRO-1?

Some turntables may require a phono preamp to use the 3.5mm Line In, which is built for line-level sources.

### How do I switch the CAST PRO-1 between analog and optical output?

The 3.5mm output jack is a dual analog and optical jack. You choose which output is used in Home Assistant. For optical, use an optical to 3.5mm (Toslink to mini Toslink) cable.

### Does the CAST PRO-1 support PoE?

No. The built-in 10/100 Ethernet is data only, with no PoE, so the device still needs USB-C power. Wi-Fi (2.4 GHz) is available as a backup.

### How do I set up Wi-Fi on the CAST PRO-1?

Wi-Fi setup uses Improv Wi-Fi over Bluetooth LE. You can also connect it with an Ethernet cable.

### Can I use a remote with the CAST PRO-1?

Yes. It works with WiZ WizMote remotes, and every button can be configured in Home Assistant.

### Can the CAST PRO-1 play in sync with my CAST-1 units?

Yes. It syncs with other CAST PRO-1 and [[CAST-1]] units through Music Assistant and Sendspin.

### Can I add LED strips to the CAST PRO-1?

Yes. It has 4 onboard RGB LEDs plus a screw terminal (5V, GND, IO1) for addressable LED strips, which you can use for music-reactive lighting.

### What is the difference between CAST PRO-1 and CAST-1?

The CAST PRO-1 adds a 3.5mm Line In jack, an optical output and built-in Ethernet. The [[CAST-1]] has a 3.5mm analog line out only, with Ethernet available through an optional HAT.
