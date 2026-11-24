---
title: MSR-2
aliases: ["MSR 2", "Apollo MSR-2", "MSR2"]
type: product
audience: customer
source: https://apolloautomation.com/products/msr-2
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-16
---
# MSR-2

## Description

The MSR-2 is an mmWave multisensor for Home Assistant and an updated version of the MSR-1. It builds on the MSR-1 with a smaller form factor and an additional back expansion slot for new accessories, such as a rear-facing female USB port for clean installations. It combines mmWave presence detection with light/UV sensing, an RGB LED and a piezo buzzer, with an optional CO2 sensor.

## Features

- mmWave radar presence sensing (HLK-LD2410B): 1 target tracking, very good still detection, very good tuning capability, ability to tune out false positives
- LUX and UV sensing (LTR-390UV)
- Optional CO2 sensor (SCD-40), true CO2 sensing
- Bluetooth tracker via the ESP32-C3-Mini (YAML config required): track Bluetooth devices in the house to see which is closest to the sensor; you need to know the MAC of the devices to track
- RGB pixel (RGB neopixel) for notifications
- Piezo buzzer for notifications
- Smaller (compact) form factor than the MSR-1
- Back expansion slot for new accessories (e.g. rear-facing female USB port)
- Open code and CAD files available; Discord community support
- Use cases: turn lights on when someone enters, keep lights on for still presence, bed occupancy under the bed, LED/buzzer notifications, UV/LUX light automations, CO2 alerts to open a window

## Specs

- Battery life: N/A — USB-C powered, no battery
- Operating temperature: -40 to 85 °C (rating of the ESP32-C3-MINI-1 module)
- Waterproof: No — the MSR-2 is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: N/A — no sleep mode
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[LD2410B]] - mmWave radar for presence and still-presence detection (1 target)
- [[LTR390]] - LUX and UV light sensor
- [[ESP32-C3]] - microcontroller (ESP32-C3-Mini); provides Wi-Fi and Bluetooth tracking
- [[SCD40]] - optional CO2 sensor (With CO2 variant)

## Options and add-ons

- Variants: Base, With CO2
- Add-ons: articulating stand; mount (90-degree mount, outlet mount only, outlet mount with US plug); back female USB-C port; USB-C charger (USA plug) and/or cable; GPIO header (header only or with Dupont cables)

## What's in the box

- Assembled sensor with case
- Apollo sticker

## Common questions and answers

### My MSR-2 is powered on but nothing is happening. What should I do?

Reflash the factory firmware. Use Chrome, Edge, another Chromium-based browser, or a recent version of Firefox. If the MSR-2 was ever added to Home Assistant, first remove it from the ESPHome integration and the ESPHome Device Builder. Then:

1. Put the MSR-2 into boot mode (see the next question).
2. Open the Apollo MSR-2 installer at https://install.apolloautomation.com/#/msr-2 and click Connect & Install.
3. Select the COM port that appears and click Connect.
4. Choose to install the ApolloAutomation.MSR-2_Factory firmware and confirm the install.
5. When it finishes, click Next and close the browser window.
6. Unplug the MSR-2 and plug it back in so it boots normally. It stays in boot mode until you do this.
7. Follow the MSR-2 getting started guide to set it up as a new device.

Full steps with pictures: https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/. If reflashing does not fix it, contact Apollo support.

### My computer keeps detecting and then losing the MSR-2 over USB. How do I put it in boot mode to flash it?

Put the MSR-2 into boot mode before flashing. The boot button is behind the right-hand of the two small slots; the reset button is behind the left-hand slot.

- Method 1 (boot button only): press and hold the boot button, plug the USB-C cable into the MSR-2 while still holding it, then release the button.
- Method 2 (boot and reset): unplug the MSR-2, then connect it to your computer. Press and hold the boot button, press and release the reset button, then release the boot button. Pressing reset on its own only restarts the MSR-2.

Then continue with the firmware upload steps. Full steps with pictures: https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-boot-mode/. If the device still connects and disconnects, contact Apollo support.

### Can the MSR-2 detect someone sitting still or sleeping?

Yes. The LD2410B mmWave radar has very good still detection, so it can keep lights on while someone is still, and it can be used for bed occupancy when placed under the bed. It tracks 1 target.

### How do I stop false detections on my MSR-2?

The LD2410B radar has very good tuning capability, and it can be tuned to remove false positives.

### How do I track Bluetooth devices with the MSR-2?

The MSR-2 can act as a Bluetooth tracker through its ESP32-C3-Mini to show which tracked device is closest to the sensor. This requires YAML configuration in ESPHome, and you need to know the MAC address of each device you want to track.

### What is the difference between the MSR-2 and the MSR-1?

The MSR-2 is the updated version of the MSR-1. It has a smaller form factor and an additional back expansion slot for new accessories, such as a rear-facing female USB port for clean installations.

### Which MSR-2 variants are there?

There are two: Base and With CO2. The With CO2 variant adds an SCD-40 for true CO2 sensing.

### Where can I get help or the source files for the MSR-2?

The code and CAD files are open, and community support is available on Discord.
