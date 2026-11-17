---
title: Radar-Presence-Issues
aliases: [ghost detection, false positives, false triggers, presence drops when sitting still, mmwave tuning, radar triggers with nobody there, zones not working, LD2410B tuning, LD2412 tuning, LD2450 zones]
type: troubleshooting
audience: customer
applies_to: ["[[MSR-2]]", "[[MTR-1]]", "[[R-PRO-1]]"]
sources:
  - https://wiki.apolloautomation.com/products/general/setup/apollo-mmwave-dashboard-setup/
  - https://wiki.apolloautomation.com/products/general/setup/apollo-mmwave-dashboard/
  - https://wiki.apolloautomation.com/products/general/calibrating-and-updating/radar-tuning/zones-ha/
  - https://wiki.apolloautomation.com/products/msr2/setup/msr2-general-tips/
  - https://wiki.apolloautomation.com/products/mtr1/setup/general-tips/
  - https://wiki.apolloautomation.com/products/rpro1/setup/rpro1-general-tips/
  - https://wiki.apolloautomation.com/products/msr2/faq/
  - https://wiki.apolloautomation.com/products/rpro1/faq/
  - https://wiki.apolloautomation.com/products/general/faq/
  - https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/
  - https://wiki.apolloautomation.com/products/msr2/setup/msr2-tuning-dashboard/
  - https://wiki.apolloautomation.com/products/general/tutorials/minimize-mmwave-activity-spam/
review_status: draft
last_verified: 2026-11-17
---
# Radar-Presence-Issues

## Summary

Every room is different. A ceiling fan, a moving curtain or someone in the next room can make an mmWave radar trigger with nobody there, and someone sitting very still can be missed. Most of these problems are fixed by mounting the sensor in the right spot and then tuning it with the **Apollo mmWave Dashboard** in Home Assistant:

- **MSR-2** (LD2410B radar) and **R PRO-1 with the LD2412 add-on**: run **Calibrate with empty room**, then fine-tune individual gates if needed.
- **MTR-1** and **R PRO-1** (LD2450 radar): draw zones on the zone map, and draw **Ignore** zones over things that move but aren't people.

## Applies to

- [[MSR-2]] (LD2410B radar, single target, distance gates)
- [[MTR-1]] (LD2450 radar, up to three targets, X/Y zones)
- [[R-PRO-1]] (LD2450 radar, plus the optional LD2412 radar for still presence)

## Symptoms

- The sensor shows presence when nobody is in the room ("ghost" detections).
- It triggers when someone moves in the next room or behind a wall.
- Presence turns off while someone is sitting still, reading or sleeping.
- On the MTR-1 or R PRO-1, the zone map shows nobody, only one person, or a dot where nobody is.
- A zone stays on after everyone has left.
- The Home Assistant Activity log is flooded with radar entries.

## Quick checks

1. **Is the sensor mounted where it will stay?** Tuning and zones describe the room from the sensor's position. If you move or turn the sensor, calibrate again or redraw your zones. On an MTR-1, never judge detection while holding the sensor in your hand: the dots and zones won't match the room.
2. **Check the mounting height:**
   - MSR-2: 1.5-2 m (about 5-6.5 ft) off the ground on a wall. It can also go on the ceiling using the articulating stand.
   - R PRO-1: 1.5-2 m off the ground on a wall, or 2.6-3 m (8-10 ft) high on the ceiling with the ceiling mount kit.
   - MTR-1: pick the spot before drawing zones (see the placement tips in Fix, step 1).
3. **Know what the radar can see:**
   - MSR-2 (LD2410B): 120 degrees wide (60 degrees each side of center), about 6 m (19.7 ft) range, one target.
   - MTR-1 and R PRO-1 (LD2450): 120 degrees wide, about 6 m (19.7 ft), up to three people.
   - R PRO-1 LD2412 add-on: 150 degrees wide (75 degrees each side of center), about 9 m (29.5 ft), one target.
4. **Remember the radar sees through thin walls.** The LD2410B can reliably go through drywall and some other materials, such as thin wood and some couches. Movement in an adjacent room can cause false triggers until you tune it out.
5. **Make sure the sensor is online** under **Settings > Devices & services > ESPHome**. Tuning and calibration need the radar online.

## Fix

### 1. Place the sensor well (MTR-1 placement tips)

These tips come from Apollo's MTR-1 mounting guide.

- Aim the sensor away from large mirrors, glass shower doors, windows and tiled walls. Radar bounces off them, so a bathroom in particular can show a target where nobody is, or show one person twice.
- The radar sees nothing behind itself. Where you can, put a neighboring room behind the sensor rather than beside its view.
- MTR-1 in a corner: aimed along the corner's diagonal, the 120-degree view reaches about 15 degrees past each wall, so it can pick up someone a short way into the next room through a thin wall.

### 2. Install the Apollo mmWave Dashboard

The Apollo mmWave Dashboard is the recommended way to tune any Apollo radar. It gives each radar its own tab in Home Assistant. It needs Home Assistant 2026.8.1 or newer, and the sensor must already be added through the ESPHome integration.

1. Install **Apollo mmWave Dashboard**:
   - Home Assistant 2026.11 or newer: go to **Settings > Marketplace**, search for **Apollo mmWave**, open **Apollo mmWave Dashboard**, click **Install**, then **Install** again in the dialog. If the Marketplace opens the setup dialog afterwards, skip to step 3; otherwise restart Home Assistant.
   - Home Assistant 2026.10 or earlier: open **HACS** (2.0.5 or newer), search for **Apollo mmWave**, open **Apollo mmWave Dashboard** and click **Download**, confirm with **Download** in the dialog, then restart Home Assistant.
2. Go to **Settings > Devices & services > Add integration**, search for **Apollo mmWave Dashboard** and select it.
3. Leave both boxes ticked, click **Submit**, then **Finish**.
4. Open **Apollo mmWave Dashboard** from the sidebar. With two or more radars, each has its own tab; with one radar, its cards fill the page. Each starts with a **Start here** card.
5. Look at the **Radar setup** card near the top of the tab. If it flags a setting, follow what it says; most problems have a button that fixes them.

Full setup guide with pictures: https://wiki.apolloautomation.com/products/general/setup/apollo-mmwave-dashboard-setup/

### 3. Stop false triggers: calibrate with an empty room (MSR-2, and R PRO-1 with LD2412)

Calibration listens to the empty room, notes the highest energy each gate picks up from the room itself (fans, curtains, plants), and sets each threshold a little above that. Your old thresholds are saved first, so you can undo it. Skip this on an MTR-1, or an R PRO-1 without the LD2412 add-on.

1. Clear the room of people, pets and robot vacuums. Leave fans, curtains and anything that normally moves as it usually is.
2. **R PRO-1 only:** press **Start Dynamic Background Correction** on the **LD2412 Controls** card and wait for **Background Correction Running** to turn off.
3. Press **Calibrate with empty room** on the **Auto-calibrate** card.
4. Leave during the 15-second countdown and close the door. Move away from the door and walls too: the radar can see through drywall and thin doors.
5. Come back after about a minute and a half, once the card shows **Thresholds updated**.
6. Do the walk test: walk around, then sit still for a minute or two. **Radar Target** (**LD2412 Presence** on an R PRO-1) should stay on the whole time, and turn off a few seconds after you leave.
7. If it now misses you or behaves worse, press **Undo (restore your previous values)**.

Run the calibration again whenever you move the sensor or rearrange the room.

### 4. Still triggers with nobody there

- Calibrate while whatever usually runs in the room is running, such as the fan on or the heating or air conditioning cycling.
- Update Apollo mmWave Dashboard to the latest version and calibrate again. Version 2.2.4 and later leave more headroom above the room's noise.
- If one spot still misbehaves, fine-tune that gate by hand:
  1. Press **Turn on Radar Engineering Mode** on the **Gate Energy** chart.
  2. Leave the room and watch the chart from your phone, out of the radar's view. A bar that is outlined while nobody is there is a gate causing false triggers.
  3. Press **Unlock** above the sliders, then raise that gate's threshold on **Move Thresholds** or **Still Thresholds** until its triangle sits a few points above the highest point the bar reaches.
  4. Turn off Radar Engineering Mode when you're done, using the button on the **Radar setup** card or the switch on the **Controls** card.
- Stop the radar looking too far, such as down a hallway past a doorway: on the **Detection Range** card, lower **Max Move Gate** and **Max Still Gate** (**Max Gate** on an R PRO-1). On an R PRO-1, raise **Min Gate** to ignore anything right next to the sensor.
- Gate distances:
  - MSR-2 (LD2410B): gates G0 to G8, each 0.75 m (about 2.5 ft) deep unless you changed **Gate Size**, out to about 6 m.
  - R PRO-1 LD2412: gates G0 to G13. Gate size is set by **Distance Resolution** (hidden until you enable its entity on the device page): 0.5 m gives finer tuning over a shorter range, 0.75 m reaches farther.
  - Each row on the threshold cards is named for how far out its gate reaches, so you don't need to work the distances out.
- A threshold of 100 means that gate never triggers, which turns it off.
- **MTR-1 and R PRO-1 zone map:** a dot that stays where nobody is, such as at a fan, a curtain or a plant, is a ghost target. Draw a zone over that spot and set its **Type** to **Ignore**.
- **MTR-1 next to another room:** draw your room zone about 30 cm (1 ft) inside any wall it shares with another room.

### 5. Presence turns off while someone sits still

- **MSR-2 (and R PRO-1 with LD2412):**
  1. Raise **Radar Timeout** on the **Detection Range** card to 60 seconds or more. On an MSR-2 it is 5 seconds from the factory. Changing it restarts the radar, so do it while nobody is sitting in the room.
  2. If it started after a calibration, press **Undo** on the **Auto-calibrate** card, or lower the still threshold of the gate where the person sits by a few points.
  3. Use **Radar Target** (MSR-2) in your automations for the whole room, not the zone sensors.
- **R PRO-1 automations:** on firmware newer than 26.3.2.1, use **Combined Presence**, which is on while either radar sees someone. On earlier firmware, use **LD2412 Presence**.
- **MTR-1 and R PRO-1 zones:** the LD2450 can lose someone who sits very still. In the zone's editor in the **Zones** panel, pick a **Hold** time (15 s up to 30 min) so the zone stays on after the radar loses them. Draw the zone with at least half a meter (1.5 ft) of room around the seat. On an R PRO-1, the optional LD2412 radar is the one suited to still targets, such as someone in bed or on a couch.

### 6. Zone map problems (MTR-1 and R PRO-1)

- **No dot at all:** on the LD2450 **Radar setup** card, press **Set Zone Type to Disabled** (or **Use recommended settings**). With Zone Type on Detection and no built-in zones set, the radar reports nobody.
- **Only one dot with several people:** press **Turn on Multi Target Tracking**. On an R PRO-1 this setting is hidden at first: open the sensor's device page (**All settings for this device** on the **Start here** card), open the entities that aren't shown under **Configuration** and select **LD2450 Multi Target Tracking**, open its settings (cog), turn on **Enabled**, select **Update**, then reload the dashboard after a minute. The **Radar setup** card then offers **Turn on Multi Target Tracking** if it's off.
- **Map doesn't match the room:** open **Map settings** and drag **Cone rotation** until the view cone points the way the sensor faces. If the slider is gray, press **Locked** on the map first. If your dot moves the opposite way from you, tick **Flip the map left to right (display only)**.
- **A zone stays on after everyone left:** if its label ends in **(held)**, pick a shorter **Hold** or **Off**. If a dot is still inside it where nobody is, draw an **Ignore** zone over that spot.
- **Zone presence reads unavailable:** this is normal while the radar is offline and after a Home Assistant restart until the radar reconnects. If it stays unavailable, check the sensor's power and Wi-Fi, and that it shows as online under **Settings > Devices & services > ESPHome**.

Full tuning and zone guide: https://wiki.apolloautomation.com/products/general/setup/apollo-mmwave-dashboard/

### 7. MSR-2 triggers with nobody there, even after tuning

1. Restart the radar: press **Restart Radar** on the **LD2410 Controls** card, or **Restart device** on the **Device** card.
2. Reflash the factory firmware ([[Factory-Reflash]]): https://wiki.apolloautomation.com/products/msr2/troubleshooting/msr2-code/
   - Before reflashing, remove the MSR-2 from the ESPHome integration and the ESPHome Device Builder.
   - Use Chrome, Edge, another Chromium-based browser, or a recent Firefox.
   - After the install, unplug and replug the MSR-2, then set it up again as a new device.
3. Calibrate again with an empty room (step 3).

Don't press **Factory Reset Radar** unless Apollo support asks you to.

### 8. Too many radar entries in the Activity log

Radar sensors report often by design. To hide them from Activity, or to stop Home Assistant saving every LD2450 target position, follow: https://wiki.apolloautomation.com/products/general/tutorials/minimize-mmwave-activity-spam/

## When to escalate

Hand the ticket to a person at Apollo support when:

- An MSR-2 still triggers with nobody there after restarting, reflashing the factory firmware and calibrating with an empty room. Apollo support may walk the customer through reseating the LD2410B radar module.
- The radar never reports presence, or the zone map never shows a dot, after the Radar setup card reads **Radar settings look good** and the sensor is online.
- Calibration keeps failing with the same error, or the radar keeps going offline during calibration.
- The customer reports physical damage, or the device doesn't power on.
- The customer asks about a warranty claim, replacement or return. The MSR-2 and R PRO-1 have a one-year warranty.

When escalating a radar issue, ask the customer to attach a support file. A Home Assistant administrator goes to **Settings > Devices & services**, opens **Apollo mmWave Dashboard**, opens the three-dot menu and chooses **Download diagnostics**. The file includes zone names, which can show the layout of the home.

## Customer phrasings

- "My MSR-2 says someone is in the room but nobody is there."
- "The lights turn off while I'm sitting on the couch."
- "My sensor picks up people walking in the next room."
- "The MTR-1 zone map shows a person where my ceiling fan is."
- "My R PRO-1 only tracks one person even with three of us in the room."
- "How do I tune the gates on my radar?"
