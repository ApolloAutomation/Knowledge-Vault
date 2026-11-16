---
title: PUMP-1
aliases: ["PUMP 1", "PUMP-1 Fluid Pump", "Apollo PUMP-1"]
type: product
audience: customer
source: https://apolloautomation.com/products/pump-1-fluid-pump
status: available
status_checked: 2026-11-15
power_source: [usb-c]
last_verified: 2026-11-16
---
# PUMP-1

## Description

The Apollo PUMP-1 is a compact, food-safe fluid pump built to work with the [[PLT-1]] plant sensor to automate watering. It has two ports for fluid sensors that detect water presence, so the pump stops when watering is done or the bottle runs empty. The PUMP-1 officially works with ESPHome and Home Assistant. Besides plants it suits filling fish tanks, robot vacuum mop tanks, pet bowls, coffee pots and more.

## Features

- Food-safe materials for liquids
- Mini DC fluid pump, powered over USB-C
- Two capacitive fluid level sensor ports (PUMP-1-Fluid-Sensor); the pump stops automatically when the bottle runs empty
- Pairs with the [[PLT-1]] for automated plant watering
- Officially works with ESPHome and Home Assistant
- Includes two 24 in pieces of silicone tubing
- Use cases: automated plant watering, fish tank filling and maintenance, robot vacuum mop tank refills, pet water bowl refills, coffee maker water supply, drain pump function
- Wiki: https://wiki.apolloautomation.com/products/pump1/introduction/
- The fluid sensor cable can be extended with cables sold by Apollo

## Specs

- Flow rate: Up to 900 ml/min
- Pump height: Tested to 14 ft+ tall
- Pump length: Tested to 33 ft (not a horizontal-run rating)
- Battery life: N/A — USB-C powered, no battery
- Operating temperature: -40 to 85 °C (rating of the ESP32-C6-MINI-1 module)
- Waterproof: No. The pump moves liquid through its tubing, but the PUMP-1 unit itself is not waterproof
- Power consumption awake: Unknown — escalate to support
- Power consumption sleeping: N/A — no sleep mode
- What battery works with it: N/A — USB-C powered, no battery

## Components

- [[ESP32-C6]] - ESP32-C6-MINI microcontroller module, gives the PUMP-1 Wi-Fi connectivity
- PUMP-1-Fluid-Sensor - optional capacitive fluid level sensors (add-on, two ports)

## Options and add-ons

PUMP-1 only, or with add-ons: USB-C Cable, PUMP-1-Fluid-Sensor, [[PUMP-1-Tubing]], PUMP-1-Bottle (bottle and stand), Front Facing USB-C Charger, or the PUMP-1-Full-Accessory-Kit.

## What's in the box

PUMP-1; two 24 in pieces of silicone tubing; Apollo sticker.

## Common questions and answers

### How does the PUMP-1 know when to stop pumping?

The PUMP-1 has two ports for capacitive fluid sensors (PUMP-1-Fluid-Sensor, sold as an add-on) that detect water presence. The pump stops when watering is done or when the bottle runs empty.

### Does the PUMP-1 come with tubing or fluid sensors?

Tubing is included: the box contains the PUMP-1, two 24 in pieces of silicone tubing and an Apollo sticker. Fluid sensors, a bottle and stand, a USB-C cable and a charger are add-ons, or you can get the PUMP-1-Full-Accessory-Kit. Extra tubing is available as [[PUMP-1-Tubing]].

### How high and how far can the PUMP-1 pump water?

It has been tested pumping 14 ft+ tall and to 33 ft of length (not a horizontal-run rating), with a flow rate of up to 900 ml/min.

### How is the PUMP-1 powered?

Over USB-C. It has no battery.

### Is the PUMP-1 waterproof?

No. The PUMP-1 moves liquid through its tubing, but the unit itself is not waterproof, so keep it out of water.

### Does the PUMP-1 work with ESPHome and Home Assistant?

Yes. The PUMP-1 officially works with ESPHome and Home Assistant.

### Can I use the PUMP-1 to refill a pet bowl or coffee maker?

Yes. The PUMP-1 is built from food-safe materials for liquids, and pet water bowl refills and coffee maker water supply are listed use cases.

### Can I extend the fluid sensor cable?

Yes. The fluid sensor cable can be extended with cables sold by Apollo.

### Does the PUMP-1 work with the PLT-1?

Yes. The PUMP-1 is built to work with the [[PLT-1]] plant sensor to automate plant watering.

### What tubing size does the PUMP-1 use?

The [[PUMP-1-Tubing]] is flexible silicone tubing with a 6 mm inner diameter and a 10 mm outer diameter.
