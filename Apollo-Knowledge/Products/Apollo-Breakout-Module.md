---
title: Apollo-Breakout-Module
aliases: ["Apollo Breakout Module", "Breakout Module"]
type: product
audience: customer
source: https://apolloautomation.com/products/apollo-breakout-module
status: available
status_checked: 2026-11-15
power_source: [host-board]
last_verified: 2026-11-15
---
# Apollo-Breakout-Module

## Description

The Apollo Breakout Module is an accessory for the [[ESK-1]] ESPHome Starter Kit that gives a build room to grow. It is not part of the official ESPHome Starter Kit family and is not an officially licensed ESPHome product. It breaks out the ESP32-C6's pins to standard connectors so you can plug in off-the-shelf sensors or wire your own parts. It attaches to the [[ESPHome-C6-Board]] with one of the kit's FPC ribbon cables, then you add your component in the ESPHome Device Builder with no code. It is open hardware, runs locally, and connects to Home Assistant when wanted.

## Features

- Shared I2C bus (SCL on GPIO0, SDA on GPIO1; turn on pullups) feeding five connectors: STEMMA QT / Qwiic (3.3V), STEMMA (5V, 4-pin), Grove, a Sensirion SEN6x port, and a 3.5mm jack for an optional SHT20 temperature and humidity probe
- 1-Wire port (data on GPIO6) for DS18B20 temperature probes
- 3-pin STEMMA general-purpose 5V port (GPIO6, 5V, GND); GPIO6 is shared with the 1-Wire port
- 2x6 GPIO header with power, UART (TX and RX), and spare GPIOs (including IO2, IO3, IO7 and IO14) for jumper wires
- Either 14-pin FPC port on the C6 board works (top or bottom)
- Powered from the ESP32-C6's controlled rail by default, which is off during sleep to save battery; solder jumper J5 switches it to always-on 3.3V
- Works with any ESPHome component; no cloud, account, or subscription
- Use cases: plug in STEMMA QT / Qwiic / Grove sensors, DS18B20 probes for fridges, freezers, and fish tanks, a SEN6x air quality sensor, custom buttons, relays or displays

## Specs

- Power input: From the ESPHome C6 Board's Accessory Power Rail. Each connector carries power at its labeled voltage (3.3V or 5V). The module's 3.3V pin runs on the ESP32-C6's controlled rail (3vCTRL) by default; solder jumper J5 (back, top right) switches it to always-on 3.3V
- I2C: SCL GPIO0, SDA GPIO1 (pullups on)
- 1-Wire: GPIO6
- Battery life: N/A — powered by the ESPHome C6 Board, no battery of its own
- Operating temperature: Unknown — escalate to support
- Waterproof: Unknown — escalate to support
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: Connected parts lose power by default while the ESP32-C6 sleeps, because the controlled rail turns off (unless J5 is changed to always-on). Exact sleep draw Unknown — escalate to support
- What battery works with it: N/A — powered by the ESPHome C6 Board, no battery of its own

## Components

- [[ESP32-C6]] - the microcontroller whose pins the module breaks out (it sits on the [[ESPHome-C6-Board]], not on this module)
- [[SEN65]] - can plug into the dedicated SEN6x port (the port is for Sensirion SEN6x sensors; SEN65 is a SEN6x series part)

## Options and add-ons

- Apollo-FPC-Ribbon-Cable (to connect to the C6 board)
- Optional probes: SHT20 temperature and humidity probe (3.5mm jack); DS18B20 temperature probe ([[DS18B20]], 1-Wire port)
- In the [[ESK-1]] store listing, the [[Short-Temperature-Probe]], [[Long-Temperature-Probe]], [[SEN65]] air quality module and Dupont cables are offered as add-ons that require this module

## What's in the box

- Apollo Breakout Module

## Common questions and answers

### How do I connect the Breakout Module to the ESPHome C6 Board?

Unplug the USB-C cable from the C6 board first. Lift the latch on either FPC connector on the C6 board, slide the ribbon cable in blue side up, and press the latch down. Connect the other end to the Breakout Module's FPC connector the same way. Plug the board back in, add the component for what you wired in ESPHome, then click Install and flash over the network or USB. Guide: https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/modules/apollo-breakout-module/

### Nothing I plug into the Breakout Module works. What should I check?

Check that your ESPHome configuration has the Accessory Power GPIO switch. If it is missing, add the Accessory Power Rail card. Without it, nothing plugged into the Breakout Module gets enough power to work. Also check the ribbon cable is seated blue side up on both ends.

### Why do my sensors lose power when the board goes to sleep?

By default the Breakout Module runs on the ESP32-C6's controlled 3.3V rail, which turns off while the board sleeps to save battery. If you need always-on 3.3V, use solder jumper J5 on the back (top right): cut the bridge between the centre pad and 3vCTRL, then solder a bridge from the centre pad to 3V. This means cutting a trace, so only do it if you need it.

### Which port should I use for a STEMMA QT or Qwiic sensor?

Use the 3.3V STEMMA QT port, not the 5V STEMMA port.

### Which pins does the Breakout Module use?

I2C uses SCL on GPIO0 and SDA on GPIO1 (turn on pullups). The 1-Wire port for DS18B20 probes uses GPIO6, which is shared with the 3-pin STEMMA port. The 2x6 header has UART TX and RX and spare GPIOs including IO2, IO3, IO7 and IO14.

### Is the Breakout Module an official ESPHome product?

No. It is an Apollo accessory that works with the [[ESK-1]] and the [[ESPHome-C6-Board]], but it is not part of the official ESPHome Starter Kit family and is not an officially licensed ESPHome product.
