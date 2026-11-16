---
title: BTN-1
aliases: [BTN-1 Macro Deck, BTN1, BTN 1]
type: product
audience: customer
source: https://apolloautomation.com/products/btn-1-macro-deck
status: available
status_checked: 2026-11-15
power_source: [usb-c, battery]
last_verified: 2026-11-16
---
# BTN-1

## Description

The BTN-1 Macro Deck has four hot-swappable mechanical brown switches, white keycaps, and an LED in front of each button for status feedback. It runs on USB-C or an optional battery and connects over Wi-Fi to Home Assistant, Homey, or other smart home systems. Use it for macros, media controls, stream deck commands, smart home automations, or custom IoT projects. Zigbee firmware is in development but is not ready yet. The BTN-1 is Thread/Matter capable, but that needs firmware development before it can be used.

## Features

- Four hot-swappable switches, compatible with Cherry MX switches (no soldering to swap)
- LED in front of each button for visual feedback
- Each button has single, double, triple and hold functions, giving 16 different actions
- Home Assistant blueprint to set up each button's single, double, triple click and hold actions
- Powered via USB-C (wired) or battery (wireless)
- Onboard battery charges via the USB-C port
- Battery sleep behavior: takes around 10 seconds to wake up to record a single button press. Buzzer, LED commands and multi-button presses only work when the BTN-1 is awake
- Small footprint with a sturdy enclosure for desktop or mounted use
- Planned future updates (not available yet): extensive GPIO and expansion. Large modular attachments on top (high-contrast e-ink display, NFC tag reader and emitter). Smaller add-ons on the right side (additional buttons, rotary dials, OLED screens, LED matrices, a mezzanine board for sensors such as CO2 monitors)
- Use cases: streaming and broadcast control, Home Assistant scenes, smart lights, HVAC settings, machine controls, building automation

## Specs

- Battery life: Up to a year with about 4 presses a day in deep sleep mode, or about 38 hours in always-awake mode (battery variants)
- Operating temperature: -40 to 85 °C (rating of the ESP32-C6-MINI-1 module)
- Waterproof: No — the BTN-1 is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Unknown — escalate to support
- What battery works with it: 3.7V 2800 mAh battery with a PH 2.0 connector; size cannot exceed 80mm x 30mm x 8mm

## Components

- [[ESP32-C6]] - the ESP32-C6-MINI microcontroller that runs the BTN-1 and provides Wi-Fi

## Options and add-ons

- Power source variants:
  - USB-C (non-battery)
  - International battery-powered: no battery included; comes with the battery-style case and you source your own battery
  - USA battery-powered: battery included
- Add-ons: clear keycaps (4 pcs), smoke keycaps (4 pcs), icon keycap pack (16 common icons), angled stand with multiple screw holes and two magnets, USB-C cable (male to male, 1.5 m / 5 ft), flat 90-degree USB-C cable (male to male, 1 m / 3 ft), front facing USB-C plug (USA style)

## What's in the box

- BTN-1
- Brown switches x4
- White keycaps x4
- Rubber feet x4
- Apollo sticker

## Common questions and answers

### Why is my BTN-1 slow to respond on battery?

In deep sleep mode on battery, the BTN-1 takes around 10 seconds to wake up and record a single button press. An always-awake mode is also available, but battery life drops to about 38 hours. Buzzer and LED commands and multi-button presses only work while the BTN-1 is awake.

### Why don't the LEDs or buzzer respond when I send a command to my BTN-1?

If it is running on battery, the BTN-1 is probably asleep. Buzzer, LED commands and multi-button presses only work when it is awake.

### How long does the BTN-1 battery last?

On the battery-powered variants, up to a year with about 4 presses a day in deep sleep mode, or about 38 hours in always-awake mode.

### Is a battery included with the BTN-1?

Only with the USA battery-powered variant. The International battery-powered variant comes with the battery-style case but no battery, so you source your own. The USB-C variant has no battery.

### What battery can I use in the BTN-1?

A 3.7V 2800 mAh battery with a PH 2.0 connector, no larger than 80mm x 30mm x 8mm. The battery charges through the BTN-1's USB-C port.

### Does the BTN-1 work with Zigbee, Thread or Matter?

Not yet. It connects over Wi-Fi today. Zigbee firmware is in development but not ready, and Thread/Matter needs firmware development before it can be used.

### How many actions can the BTN-1 trigger?

16. Each of the four buttons supports single, double and triple press and hold. A Home Assistant blueprint is available to set up each button's actions.

### Can I swap the switches or keycaps on the BTN-1?

Yes. The switches are hot-swappable and compatible with Cherry MX switches, so no soldering is needed. Clear, smoke and icon keycap packs are available as add-ons.
