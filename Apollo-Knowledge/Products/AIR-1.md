---
source: https://apolloautomation.com/products/air-1
type: product
---
Description: The AIR-1 is described as a compact, feature-rich, affordable and expandable air sensor for Home Assistant. It uses Wi-Fi and ESPHome, is controlled locally with no subscription or cloud, and is powered via USB-C and a wall adapter. It also integrates with platforms like Homey, Hubitat and HomeSeer. Software and CAD drawings are offered to the community. Site note: the MiCS-4514 gas sensor is hard to source, so stock is intermittent and the full AIR-1 price increased.

Features:
- SEN55 particulate sensor: PM1, PM2.5, PM4, PM10, VOC, NOx, temperature, humidity
- Optional CO2 (SCD40), pre-calibrated; not meeting CO2 safety monitoring requirements per NBIC, NFPA or IFC
- Optional gas sensor (MiCS-4514 from DFRobot): CO, ethanol, H2, NO2, ammonia, methane; behaves more as exists/doesn't exist than an exact ppm readout; not meeting gas safety monitoring requirements per NBIC, NFPA or IFC
- Bluetooth tracker via ESP32-C3-Mini (YAML config required)
- RGB pixels for color-coded alerts
- Power and sensor expansion connector for future sensors and power methods
- Site note: a temperature offset is needed due to heat from the ESP32-C3; using the sleep function lowers the needed offset
- Open software and CAD files

Specs:
Temperature offset: Needed due to heat buildup from the ESP32-C3; between 2 and 6 °C, still being evaluated by Apollo; much lower when using the Sleep function
Battery life: Not stated on site
Operating temperature: Not stated on site
Waterproof: Not stated on site
Power consumption awake: Not stated on site
Power consumption sleeping: Not stated on site
What battery works with it: Not stated on site

Sensor Specs:
[[SEN55]] - particulate, VOC, NOx, temperature and humidity sensor
[[SCD40]] - optional CO2 sensor
[[MiCS-4514]] - optional multi-gas sensor
[[ESP32-C3]] - microcontroller (ESP32-C3-Mini); Wi-Fi and Bluetooth tracking

Options and add-ons: Variants: no CO2 / no gas; with CO2 / no gas; with CO2 / with gas. Add-ons: GPIO header; USB-C charger (USA plug) and/or cable.

What's in the box: Assembled sensor with case; Apollo sticker

Common questions and answers:
