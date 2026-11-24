---
title: ESK-1
aliases: ["Official ESPHome Starter Kit", "ESPHome Starter Kit", "ESK1"]
type: product
audience: customer
source: https://apolloautomation.com/products/esk-1-esphome-starter-kit
status: available
status_checked: 2026-11-15
power_source: [usb-c, battery]
last_verified: 2026-11-16
---
# ESK-1

## Description

The Official ESPHome Starter Kit is a way to build your own smart home devices with no soldering, breadboards or coding experience. You plug in a module, set it up in the visual ESPHome Device Builder, and use it standalone or with Home Assistant. Everything runs locally with no cloud, subscriptions or accounts. The majority of profit supports the Open Home Foundation, which maintains ESPHome and Home Assistant.

## Features

- Solder-free: modules snap off the panel and connect to the main board with a single FPC ribbon cable
- Any two modules can run at the same time to make a multisensor
- Example projects: PIR motion light, temperature and humidity automations, button-triggered Home Assistant automations, status colors and chimes from the Casita module
- Learning Wiki explains each step
- Modules: PIR motion, temperature and humidity, ESPHome Casita notification module (10 RGB LEDs and a piezo buzzer), button module
- Main board ([[ESPHome-C6-Board]]) has an onboard RGB LED, 2 x 14-pin FPC ports, USB-C power with optional LiPo battery support

## Specs

- Power input: USB-C, with support for an optional rechargeable LiPo battery
- Connectivity: Wi-Fi, Bluetooth LE and Thread (officially supported); Zigbee exists at chip level but is not supported out of the box
- Battery life: Unknown — escalate to support
- Operating temperature: -40 to 85 °C (rating of the ESP32-C6-MINI-1 module on the ESPHome C6 Board)
- Waterproof: No. The kit and its modules are not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: Optional rechargeable 3.7V LiPo with a 2-pin JST-PH 2.0 connector (not included). Apollo does not sell or recommend a specific battery; the 3.7V 2800mAh LiPo used in Apollo's battery guide is one example that works.

## Components

- [[ESPHome-C6-Board]] - the main board, with the [[ESP32-C6]] microcontroller (ESP32-C6-MINI-1); Wi-Fi, Bluetooth LE and Thread
- [[MH-SR602]] - PIR motion sensor module for presence/motion detection
- [[AHT20]] - temperature and humidity sensor module (also listed as AHT20F)
- Casita module - 10 RGB LEDs and a piezo buzzer for status colors, chimes and reminders (designed by Apollo)
- Button module - button to trigger Home Assistant automations (designed by Apollo)
- [[SEN65]] - optional air quality module add-on (requires the [[Apollo-Breakout-Module]])

## Options and add-ons

- USB-C cable (male to male)
- USB-C charger (USA style)
- Extra 3x FPC cables (spare 14-pin ribbon cables)
- Extra [[ESPHome-C6-Board]]
- [[Apollo-Breakout-Module]] (STEMMA QT, Qwiic, Grove, 1-Wire and a GPIO header)
- Dupont cables (require the Breakout Module)
- [[Short-Temperature-Probe]] and [[Long-Temperature-Probe]] (require the Breakout Module)
- [[SEN65]] air quality module (requires the Breakout Module)

## What's in the box

- ESPHome C6 Board
- ESPHome Starter Kit module board (holds the button, temperature and humidity, and ESPHome Casita modules)
- PIR sensor
- FPC ribbon cables (x3)
- ESPHome Casita stand

## Common questions and answers

### Do I need to know how to code to use the ESPHome Starter Kit?

No. Setup is visual in the ESPHome Device Builder (also available as the free ESPHome desktop app for Mac, Windows and Linux). Learning YAML is optional.

### Do I need to solder anything?

No. Modules snap off the panel and each one connects to the main board with a single FPC ribbon cable.

### Which way does the ribbon cable go in?

Blue side up. Lift the latch, slide the cable in until it seats, then press the latch down. Do not pull on the cable.

### Do I need Home Assistant to use the kit?

No. Devices work standalone over Wi-Fi at their `.local` hostnames. You can add Home Assistant later and it will find them on your network.

### Can I use more than one module at the same time?

Yes. Any two modules can run at the same time to make a multisensor, one on each 14-pin FPC port.

### Can the kit run on battery power?

Yes. The board supports an optional rechargeable 3.7V LiPo battery with a 2-pin JST-PH 2.0 connector, which charges over the same USB-C cable. The battery is not included, and Apollo does not sell or recommend a specific battery; the 3.7V 2800mAh LiPo used in Apollo's battery guide is one example that works. See the [[ESPHome-C6-Board]] note and https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/battery/ for wiring polarity.

### Does the kit support Zigbee?

The kit officially supports Wi-Fi, Bluetooth LE and Thread. The ESP32-C6 has Zigbee at the hardware level, but it is not part of the supported out-of-the-box experience.

### Why won't my LEDs light up, my buzzer play, or my module respond?

Check the Accessory Power Rail first. The onboard RGB LED and every module get their power from it. If the rail is missing from your configuration, or its Accessory Power switch is off, these parts will not get enough power. Projects created from the kit board include the rail and turn it on at boot.

### Can I add air quality or temperature probes to the kit?

Yes, with the [[Apollo-Breakout-Module]]. The [[Short-Temperature-Probe]] and [[Long-Temperature-Probe]] are compatible with the kit. The [[SEN65]] air quality module, both temperature probes, and Dupont cables all require the Breakout Module.

### Does the kit need a cloud account or subscription?

No. It runs fully locally, with no account, subscription or telemetry.
