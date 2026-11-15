---
source: https://apolloautomation.com/products/msr-2
type: product
---
Description: The MSR-2 is an mmWave multisensor for Home Assistant and an updated version of the MSR-1. It builds on the MSR-1 with a smaller form factor and an additional back expansion slot for new accessories, such as a rear-facing female USB port for clean installations. It combines mmWave presence detection with light/UV sensing, an RGB LED and a piezo buzzer, with an optional CO2 sensor.

Features:
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

Specs:
Battery life: Not stated on site
Operating temperature: Not stated on site
Waterproof: Not stated on site
Power consumption awake: Not stated on site
Power consumption sleeping: Not stated on site
What battery works with it: Not stated on site

Sensor Specs:
[[LD2410B]] - mmWave radar for presence and still-presence detection (1 target)
[[LTR390]] - LUX and UV light sensor
[[ESP32-C3]] - microcontroller (ESP32-C3-Mini); provides Wi-Fi and Bluetooth tracking
[[SCD40]] - optional CO2 sensor (With CO2 variant)

Options and add-ons: Variants: Base, With CO2. Add-ons: articulating stand; mount (90-degree mount, outlet mount only, outlet mount with US plug); back female USB-C port; USB-C charger (USA plug) and/or cable; GPIO header (header only or with Dupont cables).

What's in the box: Assembled sensor with case; Apollo sticker

Common questions and answers:
- Powered on but nothing happening: Reflash from website
- USB becoming detected and not detected: Put in boot mode to flash
