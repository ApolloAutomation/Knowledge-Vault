---
title: NFC-1
aliases: [NFC-1 NFC Reader Writer and Emulator, NFC1, NFC 1]
type: product
audience: customer
source: https://apolloautomation.com/products/nfc-1-nfc-reader-writer-and-emulator
status: sold-out
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-16
---
# NFC-1

## Description

The Apollo NFC-1 is an ESPHome-powered NFC reader and writer that connects to Home Assistant. Scanned tags show up as Home Assistant tag events that can run automations. It can also write URLs, text or new Home Assistant tags from the dashboard, clean and format tags, and emulate a tag so a phone can tap it to open a link or launch the Home Assistant app. It gives feedback with an RGB LED and buzzer.

## Features

- Tag modes: Read, Write, Clean, Format
- Writes URLs, text and Home Assistant tags, with automatic verify after each write
- Card Emulation: acts as a tag for phones to tap; optional Home Assistant app launch on Android
- Works with NTAG / MIFARE Ultralight and MIFARE Classic tags
- RGB LED and buzzer feedback with adjustable brightness and volume
- Home Assistant entities: last tag UID, type and content, tag present, NFC events
- Built-in Bluetooth proxy, can be switched on or off
- Setup with Improv over Bluetooth or USB serial, plus Wi-Fi fallback hotspot
- Over-the-air updates with stable and beta channels
- Open source ESPHome firmware
- Use cases: tap-to-run scenes, guest Wi-Fi and links, who's-home check-ins, tag programming station, Bluetooth coverage boost

## Specs

- Battery life: N/A — USB-C powered, no battery
- Operating temperature: -40 to 85 °C (rating of the ESP32-C6 module)
- Waterproof: No — the NFC-1 is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[PN7160]] - NXP NFC controller; reads, writes and emulates tags
- [[ESP32-C6]] - microcontroller (with 8MB flash); Wi-Fi and Bluetooth LE, Bluetooth proxy
- RGB LED and buzzer - user feedback

## Options and add-ons

None listed (single variant).

## What's in the box

- NFC-1

## Common questions and answers

### What NFC tags work with the NFC-1?

NTAG / MIFARE Ultralight and MIFARE Classic tags.

### How do I use an NFC tag to run a Home Assistant automation?

Scan the tag on the NFC-1. Scanned tags show up in Home Assistant as tag events, which can trigger automations. The NFC-1 also exposes the last tag UID, type and content, a tag-present entity and NFC events.

### Can the NFC-1 write tags?

Yes. It can write URLs, text or new Home Assistant tags from the Home Assistant dashboard, and it verifies each write automatically. It can also clean and format tags (Read, Write, Clean and Format modes).

### Can my phone tap the NFC-1 to open a link or the Home Assistant app?

Yes. In Card Emulation mode the NFC-1 acts as a tag that a phone can tap to open a link. Launching the Home Assistant app on tap is an optional feature on Android.

### How do I connect the NFC-1 to Wi-Fi?

Set it up with Improv over Bluetooth or USB serial. If it can't connect, it also offers a Wi-Fi fallback hotspot.

### Can I turn off the Bluetooth proxy on the NFC-1?

Yes. The built-in Bluetooth proxy can be switched on or off.

### How do I update the NFC-1 firmware?

It gets over-the-air updates, with a choice of stable and beta channels. The firmware is open source ESPHome.

### Can I change the LED brightness or buzzer volume?

Yes. The RGB LED brightness and buzzer volume are adjustable.
