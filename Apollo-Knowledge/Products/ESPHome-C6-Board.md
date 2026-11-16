---
title: ESPHome-C6-Board
aliases: ["Official ESPHome C6 Board", "ESPHome C6 Board", "C6 Board"]
type: product
audience: customer
source: https://apolloautomation.com/products/esphome-c6-board
status: available
status_checked: 2026-11-15
power_source: [usb-c, battery]
last_verified: 2026-11-16
---
# ESPHome-C6-Board

## Description

The Official ESPHome C6 Board is the compact ESP32-C6 board at the heart of the [[ESK-1]] ESPHome Starter Kit, sold on its own. It is built around the Espressif ESP32-C6-MINI-1 and brings Wi-Fi, Bluetooth LE and Thread on one chip (Zigbee is possible at chip level for advanced users, but is not part of the supported out-of-the-box experience). It is powered over USB-C or an optional rechargeable LiPo battery and is set up in the ESPHome Device Builder with no code required. Everything runs locally with no cloud, subscriptions or accounts.

## Features

- Connect up to two modules through its 14-pin FPC ports; two modules can run at once to make a multisensor
- Works with the Starter Kit modules: motion, temperature and humidity, button, and ESPHome Casita
- Works with the [[Apollo-Breakout-Module]] through either FPC port; with the Breakout Module you can add the [[Short-Temperature-Probe]] and [[Long-Temperature-Probe]]
- Onboard RGB status LED
- Wi-Fi, Bluetooth LE or Thread connection to Home Assistant
- Can be deployed cable-free on a rechargeable LiPo battery (battery not included)
- Open PCB-based design; most of the profit supports the Open Home Foundation
- Configured with ESPHome Device Builder (Mac, Windows, Linux) or the ESPHome Home Assistant app

## Specs

- Operating temperature: -40 to 85 °C (rating of the ESP32-C6-MINI-1 module)
- Power input: USB-C, or an optional rechargeable LiPo battery
- Battery connector: 2-pin JST-PH 2.0 battery port
- Battery charging: The battery charges over the same USB-C cable that powers the board, while the board keeps running; no separate charger is needed
- Accessory power: The onboard RGB LED and all connected modules are powered from the Accessory Power Rail, which must be present and switched on in the ESPHome configuration
- Battery life: Unknown — escalate to support
- Waterproof: No. The ESPHome C6 Board is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: Rechargeable 3.7V LiPo with a 2-pin JST-PH 2.0 connector (not included). Apollo does not sell or recommend a specific battery; the 3.7V 2800mAh LiPo used in Apollo's battery guide is one example that works.

## Components

- [[ESP32-C6]] - the microcontroller (Espressif ESP32-C6-MINI-1 module); Wi-Fi, Bluetooth LE and Thread, Zigbee possible at chip level

## Options and add-ons

No variants. Works with the modules in [[ESK-1]] and with the [[Apollo-Breakout-Module]].

## What's in the box

- ESPHome C6 Board

## Common questions and answers

### What battery can I use with the ESPHome C6 Board?

A rechargeable 3.7V LiPo battery with a 2-pin JST-PH 2.0 connector, plugged into the board's battery port. The battery is not included. Apollo does not sell or recommend a specific battery; the 3.7V 2800mAh LiPo used in Apollo's battery guide is one example that works. The connector only fits one way, but check the wire colours before pushing it in: the black (ground) wire goes on the side nearest the ESP32-C6 chip and the red wire on the side nearest the USB-C port. If the wires are reversed, stop and do not force it. To remove the battery, pull straight out by the connector body, not the wires. Guide: https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/battery/

### Do I need a separate charger for the battery?

No. The battery charges over the same USB-C cable that powers the board, and the board keeps running while it charges. Any USB-C power source works.

### Why does my board drop off Wi-Fi when running on battery?

Wi-Fi drains a battery quickly, so battery builds normally use deep sleep: the board wakes, reports its readings, then sleeps again. While it is asleep it drops off Wi-Fi, which is expected. Apollo's battery guide shows a Prevent Sleep switch you can use to keep it awake for updates.

### Why won't my LED, buzzer or module respond?

Check the Accessory Power Rail first. The onboard RGB LED and every module get their power from it. If the rail is missing from your ESPHome configuration, or its Accessory Power switch is off, these parts will not get enough power. Projects created from the kit board include the rail and turn it on at boot.

### Does the ESPHome C6 Board support Zigbee?

Wi-Fi, Bluetooth LE and Thread are officially supported. The ESP32-C6 chip has Zigbee at the hardware level, but Zigbee is not part of the supported out-of-the-box experience; it is for advanced users.

### Do I need Home Assistant to use the board?

No. Devices built with the board work standalone over Wi-Fi at their `.local` hostnames, and Home Assistant can be added later. Everything runs locally with no cloud, subscription or account.
