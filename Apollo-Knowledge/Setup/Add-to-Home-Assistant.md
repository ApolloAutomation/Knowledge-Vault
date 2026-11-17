---
title: Add-to-Home-Assistant
aliases: [add to home assistant, adopt device, esphome integration, device not discovered, take control, esphome device builder, encryption key]
type: guide
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]", "[[AIR-1]]", "[[TEMP-1]]", "[[PLT-1]]", "[[PUMP-1]]", "[[BTN-1]]", "[[CAST-1]]", "[[CAST-PRO-1]]", "[[ESK-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/setup/getting-started/
  - https://wiki.apolloautomation.com/products/btn1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/cast1/setup/getting-started/
  - https://wiki.apolloautomation.com/products/cast1/additional-info/esphome-device-builder/
  - https://wiki.apolloautomation.com/products/castpro1/additional-info/esphome-device-builder/
  - https://wiki.apolloautomation.com/products/ESPHome-Starter-Kit/tutorials/connect-to-home-assistant/
  - https://wiki.apolloautomation.com/products/air1/faq/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/ubiquiti-unifi-mdns-auto-discover-issue/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/opnsense-mdns-auto-discover-issue/
  - https://wiki.apolloautomation.com/products/general/troubleshooting/removing-device-from-home-assistant/
  - https://www.home-assistant.io/integrations/esphome/
review_status: draft
last_verified: 2026-11-17
---
# Add-to-Home-Assistant

## Summary

Once your Apollo device is on your Wi-Fi, Home Assistant finds it automatically and you add it through the ESPHome integration. That's all most people need. Taking control of the device in the ESPHome Device Builder is optional and only needed if you want to rename the device or edit its YAML.

## Applies to

Apollo devices that run ESPHome firmware: [[MSR-2]], [[MTR-1]], [[R-PRO-1]], [[AIR-1]], [[TEMP-1]], [[PLT-1]], [[PUMP-1]], [[BTN-1]], [[CAST-1]], [[CAST-PRO-1]] and the [[ESK-1]] starter kit (which has its own steps below).

The [[M-1]] and [[LED-1]] run WLED, not ESPHome, so these steps don't apply to them.

## Before you start

- Your device must already be connected to your Wi-Fi (see [[Wi-Fi-Setup]]). The [[CAST-PRO-1]], and the [[CAST-1]] with its Ethernet HAT, can use an Ethernet cable instead.
  - [[R-PRO-1]]: it ships with Wi-Fi firmware. Add it on Wi-Fi first; switching to Ethernet (PoE) firmware is done afterwards from its device page (see [[PoE-Setup]]).
- Home Assistant and your Apollo device should be on the same network. If they are on different networks or VLANs, your router needs mDNS forwarding and firewall rules that allow traffic between them.
- If you set up Wi-Fi with Improv over Bluetooth, Home Assistant offers to add the device to the ESPHome integration right after. Click **Submit**, choose an **Area** and click **FINISH** (steps 4 and 5 below).
  - [[CAST-1]]: Improv adds it to Home Assistant as part of setup, so you can skip these steps.

## Steps

### Add the device with the ESPHome integration

1. In Home Assistant, click the **Notifications** bell in the bottom-left of the sidebar.
2. Click **Check it out** to open Integrations and find your new Apollo device. You can also open the ESPHome integration page directly from **Settings → Devices & services → ESPHome**.
3. Click **ADD** on the discovered device card.
4. Click **SUBMIT**.
5. Assign an **Area** and click **FINISH**. On the [[BTN-1]] you can also choose **Skip and Finish**.
6. To find the device later, go to **Settings → Devices & services → ESPHome** and click its name.

If the device was not discovered, you can add it by hand: go to **Settings → Devices & services**, select **Add Integration**, choose **ESPHome**, and enter the device's IP address or hostname. The port is 6053 (the default).

### Encryption key

- [[AIR-1]]: firmware 26.7.23.1 and later encrypts the connection to Home Assistant automatically. There is nothing to set up, and existing owners don't need to change anything.
- [[ESK-1]]: when Home Assistant asks for the encryption key, enter the `api_encryption_key` value from `secrets.yaml` in the ESPHome Device Builder. If both run on the same machine, it may already be filled in.

### ESK-1 starter kit

1. Make sure Home Assistant is on the same network as the kit, and that the kit's page opens in your browser at `esphome-starter-kit.local`.
2. In Home Assistant, go to **Settings → Devices & services**. Under **Discovered**, look for the ESPHome card for `esphome-starter-kit`. If it isn't there, click **Add Integration**, choose **ESPHome**, and enter the hostname `esphome-starter-kit.local` or the kit's IP address.
3. Click **Configure** on the card.
4. Enter the encryption key when asked (see above).
5. Optionally choose an Area, then click **Submit**.
6. Open **Settings → Devices & services → ESPHome** and select the kit. Its entities should show with a green online status, and toggling the **Onboard RGB LED** light should make the LED respond.

### Optional: take control in the ESPHome Device Builder

Skip this unless you want to rename the device or edit its YAML. Your device already works in Home Assistant without it.

1. Install the ESPHome Device Builder app if you don't have it yet, then open it.
2. Click **SECRETS** at the top right. Add your Wi-Fi details as `wifi_ssid` and `wifi_password`, keeping the values inside quotes.
   - [[CAST-1]] and [[CAST-PRO-1]]: their guides skip this step.
3. Click **Show** next to **Discovered** at the top to see your discovered devices.
4. Click **TAKE CONTROL** on your Apollo device.
5. Optionally change the name (this only changes its name in the dashboard), then click **TAKE CONTROL** again.
6. Click **INSTALL** (don't click skip). Compiling and installing takes a few minutes.
   - [[CAST-1]] and [[CAST-PRO-1]]: click **Install** (the up arrow icon), then **On the network**. This takes 5 to 10 minutes depending on how fast your device is.
7. When the log shows `INFO OTA successful`, click **STOP**.
   - [[CAST-1]]: when the install completes, click **Stop**, then press the **Reset** button on the device.
   - [[CAST-PRO-1]]: when the install completes, click **Stop**, then press the **reset** button on the left side of the device. It reboots and is ready to use.

If you build the [[AIR-1]] YAML yourself, firmware 26.7.23.1 and later needs ESPHome 2026.7.2 or newer. If validation fails on a version error, update the ESPHome Device Builder and validate again. Devices that update through the Firmware Update entity aren't affected (see [[Firmware-Updates]]).

## If it doesn't work

- **Device isn't discovered:** make sure mDNS is turned on in your router.
  - UniFi: in your UniFi controller go to **Network → Settings → Networks → Default Network** and check **Multicast DNS**. In the UniFi mobile app it's **Settings → Networks → Default Network → Multicast DNS**.
  - OPNsense: install the `os-mdns-repeater` plugin under **System → Firmware → Plugins**, then go to **Services → mDNS Repeater**, enable it, select the interfaces that hold Home Assistant and your Apollo devices, and click **Save**. If Home Assistant and your devices are on different networks, your firewall rules must also allow traffic between them.
  - You can also add the device by IP address, as described in the Steps.
- **"Failed to import device" in the ESPHome Device Builder:** check that Home Assistant has enough free storage, and delete old backups if needed. If storage isn't the problem, reboot or reinstall the ESPHome Device Builder app.
- **Encryption key rejected on the [[ESK-1]]:** copy the `api_encryption_key` from `secrets.yaml` again and paste it in. If the key changed since you last flashed the kit, reflash it so it has the new key.
- **Start over:** remove the device, then add it again.
  1. Only if you took control: open the ESPHome Device Builder, click the three dots on the device, select **Delete**, and confirm with **Delete**.
  2. Go to **Settings → Devices & services → ESPHome**, click the three dots next to the device, and select **Delete**.
  3. Add it again using the Steps above.
- **Other platforms:** OpenHAB works through the OpenHAB-ESPHome binding. Install it, restart OpenHAB, and your Apollo devices will show up to configure.
- If Home Assistant asks for an encryption key for any other Apollo device, or nothing above helps, contact Apollo support with your device model and a screenshot of the message.

## Customer phrasings

- "My sensor is on Wi-Fi but Home Assistant isn't finding it."
- "How do I add my MSR-2 to Home Assistant?"
- "Home Assistant is asking me for an encryption key."
- "Do I need to adopt the device in ESPHome?"
- "I get 'Failed to import device' when I click Take Control."
- "Nothing shows up under Discovered on my UniFi network."
