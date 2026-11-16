---
source: https://apolloautomation.com/products/apollo-breakout-module
type: product
---
Description: The Apollo Breakout Module is an accessory for the ESPHome Starter Kit that gives a build room to grow. The site says it is not part of the official ESPHome Starter Kit family and is not an officially licensed ESPHome product. It breaks out the ESP32-C6's pins to standard connectors so you can plug in off-the-shelf sensors or wire your own parts. It attaches to the ESPHome C6 Board with one of the kit's FPC ribbon cables, then you add your component in the ESPHome Device Builder with no code. It is open hardware, runs locally, and connects to Home Assistant when wanted.

Features:
- Shared I2C bus (SCL on GPIO0, SDA on GPIO1; turn on pullups) feeding five connectors: STEMMA QT / Qwiic, STEMMA, Grove, a Sensirion SEN6x port, and a 3.5mm jack for an optional SHT20 temperature and humidity probe
- 1-Wire port (data on GPIO6) for DS18B20 temperature probes
- 3-pin STEMMA general-purpose port (GPIO6, 5V, GND)
- 2x6 GPIO header with power, UART (TX and RX), and spare GPIOs for jumper wires
- Either 14-pin FPC port on the C6 board works (top or bottom)
- Powered from the ESP32-C6's controlled rail by default, which is off during sleep to save battery; solder jumper J5 switches it to always-on 3.3V
- Works with any ESPHome component; no cloud, account, or subscription
- Use cases: plug in STEMMA QT / Qwiic / Grove sensors, DS18B20 probes for fridges, freezers, and fish tanks, a SEN6x air quality sensor, custom buttons, relays or displays

Specs:
Battery life: Not stated on site
Operating temperature: Not stated on site
Waterproof: Not stated on site
Power consumption awake: Not stated on site
Power consumption sleeping: Not stated on site
What battery works with it: Not stated on site

Sensor Specs:
[[ESP32-C6]] - the microcontroller whose pins the module breaks out (it sits on the ESPHome C6 Board, not on this module)
[[SEN65]] - can plug into the dedicated SEN6x port (the site says Sensirion SEN6x sensors; SEN65 is a SEN6x series part)

Options and add-ons: Apollo-FPC-Ribbon-Cable (to connect to the C6 board). Optional probes named on the site: SHT20 temperature and humidity probe (3.5mm jack), DS18B20 temperature probe (1-Wire port)

What's in the box: Apollo Breakout Module

Common questions and answers:
