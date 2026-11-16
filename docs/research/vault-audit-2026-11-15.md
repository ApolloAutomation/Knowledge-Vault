AUDIT OF /Users/justinapollo/Code/ApolloAutomation/Knowledge-Vault/.claude/worktrees/freshdesk-ai-support-plan-102673/Apollo-Knowledge (no files edited)

Scope: 41 notes, 965 lines in total. Products/ has 20, Accessories/ has 5 and Components-Sensors/ has 16. .obsidian/app.json is empty ({}). The vault has no README, index/MOC, company or policy notes. Git history is two commits ("Add Apollo product, accessory and component knowledge notes", "Clean Up").

=== 1. TEMPLATE / SCHEMA PER TYPE ===
None of the notes use markdown headings (#/##). Sections are plain "Label:" lines, and specs are "Key: value" lines in the body, not frontmatter. No note puts its own product name in the body as a title; the name is only in the filename.

PRODUCT (20 files)
- Frontmatter: source (store URL), type: product.
- Sections, in order: Description:, Features: (bullets), Specs: (key: value), Sensor Specs: ([[component]] - role), Options and add-ons:, What's in the box:, Common questions and answers:
- Six fixed spec keys: Battery life, Operating temperature, Waterproof, Power consumption awake, Power consumption sleeping, What battery works with it.
- All 20 notes have all 7 sections in the same order, so the structure is fully consistent. Deviations:
  - Extra spec keys:
    - AIR-1: Temperature offset
    - CAST-PRO-1: Ethernet
    - M-1: Dimensions, Power input, Pixel count, LED pitch, Max panels chained
    - PUMP-1: Flow rate, Pump height, Pump length
  - "Sensor Specs" sometimes lists non-component items or placeholder lines:
    - CAST-1: W5500 (no note)
    - LED-1: ESP32-PICO and "Digital microphone" (no notes)
    - ESK-1: "Casita module" and "Button module"
    - NFC-1: "RGB LED and buzzer"
    - PLT-1: "Capacitive soil moisture sensor" and "Microcontroller: Not stated on site"
    - R-PRO-1: "Microcontroller: Not stated on site"
    - TEMP-1: "NTC probe" and "Microcontroller: ESP32-based"
    - PUMP-1: a parenthetical note
    - Apollo-Voice-Speaker-Add-on: "No chips or modules named"
    - PA-1: "No component is named"
  - "Options and add-ons" format varies. BTN-1 and M-1 use nested bullets; the other 18 use prose. M-1 also folds in 6+ kit SKUs and separate store pages.
  - "What's in the box" is inconsistent:
    - M-1 has a second line, "Kit pages list: ...".
    - PA-1 says "Not stated on site".
    - LED-1 says "(wording unclear on site)".
  - Stock status sits only in Description prose, not in frontmatter:
    - Sold out: Apollo-Voice-Speaker-Add-on, LED-1, NFC-1, PA-1
    - Preorder: CAST-1, CAST-PRO-1
    - Intermittent stock: AIR-1 (gas variant)

ACCESSORY (5 files)
- Frontmatter: source, type: accessory.
- Sections: Description:, Features:, type-specific spec lines, Compatible with:, Included/variants:
- Deviations:
  - HUB75-Matrix-Panel puts its spec lines (Pixel count, LED pitch) before Features.
  - PUMP-1-Tubing uses Inner/Outer diameter and says nothing about what's in the box.
  - The three probes use Probe type / Probe length / Max temperature and "What's in the box: not stated on site".
  - Accessories are not linked back from their parents:
    - TEMP-1 lists "short probe; long probe; food probe; multi-probe splitter" with no [[links]].
    - PLT-1 and ESK-1 mention the probes without links.
    - ESK-1 mentions "Breakout Module" without a link, although Apollo-Breakout-Module.md exists.

COMPONENT (16 files)
- Frontmatter: type: component only, with no source. LD2412.md is the exception: it has `source:` (listed after `type`), because it is also a store product.
- Sections: Description:, Used in: ([[links]]), then class-specific fields:
  - Radar (LD2410B, LD2412, ld2450), 8 keys: Number of occupants, Distance, Max distance, Max targets, Number of zones, Field of view, Max square footage of coverage given height off ground, Mounting orientation.
  - MCU (ESP32-C3, -C6, -S3), 3 keys: Operating range, Wifi capability, Can be bluetooth proxy.
  - LTR390: Operating temp, Lux value, UV value.
  - AHT20: Max/min temp reading, Max/min humidity reading, Accuracy.
  - MH-SR602: only 1 field (Detection range).
- 7 notes add a datasheet "Source:" block: DS18B20, MiCS-4514, PN7160, SCD40, SEN55, SEN65, PCM5122. The other 9 are site-only.
- PCM5122 has no blank line between "Used in" and its fields, and repeats the sample rate twice (page vs datasheet).
- Datasheet citations to verify:
  - PN7160 cites "Rev. 4.2, 22 July 2026".
  - SEN65 cites "SEN6x datasheet D1 Version 1.0, Oct 2026".
  - SEN55 cites a "SparkFun-hosted copy".
- "Used in" lists include plain-text names with no notes: M-1-Controller (ESP32-S3), MiCS-4514-Cable, SCD40-Breakout-Board, SEN55-SCD40-Breakout-Board.

=== 2. "NOT STATED ON SITE" PLACEHOLDERS (142 total) ===
Per file:
- 7: R-PRO-1, LED-1
- 6: PUMP-1, PA-1, NFC-1, MTR-1, MSR-2, M-1, ESK-1, DEV-2, DEV-1, CAST-PRO-1, CAST-1, Apollo-Voice-Speaker-Add-on, Apollo-Breakout-Module, AIR-1, LD2410B
- 5: ESPHome-C6-Board, LD2412
- 4: TEMP-1, PLT-1, BTN-1
- 3: ld2450
- 2: PCM5122, ESP32-C3, AHT20
- 1: LTR390, ESP32-S3, ESP32-C6, TEMP-1-Food-Probe, Short-Temperature-Probe, Long-Temperature-Probe, HUB75-Matrix-Panel
- 0: SEN65, SEN55, SCD40, PN7160, MiCS-4514, MH-SR602, DS18B20, PUMP-1-Tubing

Most-missing fields:
- Power consumption sleeping: 20
- Power consumption awake: 20
- Operating temperature: 19
- Waterproof: 18
- What battery works with it: 17
- Battery life: 16
- Operating range: 3
- Mounting orientation: 3
- Microcontroller: 3
- Max sq ft coverage: 3
- Included/variants (what's in the box): 3
- Number of zones: 2
- Field of view: 2
- Single occurrences: Distance, Max distance, Max targets, Number of occupants, ADC, Pixel count, Can be bluetooth proxy, AHT20 min/max ranges, LED-1 mic part number

Key point: about 110 of the 142 placeholders come from the six fixed battery/power/waterproof keys. For mains or USB-only devices (DEV-1, DEV-2, CAST-1, CAST-PRO-1, LED-1, M-1, NFC-1, MTR-1, MSR-2, R-PRO-1, Breakout Module, Voice Speaker), "Battery life" and "What battery works with it" are really not applicable, not missing. An LLM may answer "we don't know whether it takes a battery" instead of "it doesn't use a battery".

Real high-value gaps:
- Radar field of view and coverage for LD2410B (6 placeholders, only 1 field known), ld2450 FOV and mounting, and LD2412 mounting.
- Operating temperature for every product. ESPHome-C6-Board is the only product with one.
- The MCU is unknown for PLT-1, R-PRO-1 and TEMP-1 ("ESP32-based").
- Power draw everywhere. This matters for PoE budgets and USB power supplies.

=== 3. COMMON QUESTIONS AND ANSWERS ===
- 19 of 20 product notes have an empty "Common questions and answers:" section. Accessories and components have no Q&A section at all.
- Only Products/MSR-2.md has content: 2 Q&As, both non-actionable.
  - "Powered on but nothing happening: Reflash from website". No URL (Apollo flasher page or ESPHome web installer), no browser requirement (Chrome/Edge Web Serial), no steps, no firmware name, and no check of LED behaviour or power supply first.
  - "USB becoming detected and not detected: Put in boot mode to flash". The question wording is garbled. It doesn't say which button to hold, when to release it, that a data-capable USB-C cable is needed, or anything about USB drivers or ports.
- Q&A-worthy facts already sit in Features/Description prose and could be turned into Q&As:
  - AIR-1: 2-6 °C temperature offset from ESP32-C3 heat, lower in sleep.
  - MiCS-4514: methane spikes, so treat it as present/absent, not ppm.
  - MTR-1: smart-charging wall plugs may not work with the back USB-C adapter.
  - BTN-1: about 10 s wake on battery; buzzer, LED and multi-button presses only work while awake; Zigbee/Thread not ready yet.
  - R-PRO-1: ships with Wi-Fi firmware and switches to PoE in the device dashboard; heat offsets; CO2 skewed when recessed.
  - M-1: the mic works only on the Rev 6 board; third-party HUB75 panels may have compatibility issues; 4+ panels need power injection.
  - PLT-1 / TEMP-1: battery and charger not included; supported battery types.
  - TEMP-1-Food-Probe: not dishwasher safe and not splitter compatible.
  - CO2 and gas sensors are not safety-rated (NBIC/NFPA/IFC).
  - Apollo-Breakout-Module: the controlled rail is off during sleep; solder jumper J5 makes it always-on.

=== 4. WIKILINKS ===
- 35 distinct targets are linked. All resolve to existing files, so nothing is truly dangling.
- Case / naming inconsistency: the file is Components-Sensors/ld2450.md (lowercase) and is linked as [[ld2450]] from MTR-1, R-PRO-1 and LD2412. The sibling files are uppercase (LD2410B.md, LD2412.md), and prose says "LD2450"/"HLK-LD2450". Obsidian matches case-insensitively, but a case-sensitive retriever, script or Linux filesystem would not, and filename search for "LD2450" may miss it.
- Unlinked references with no note:
  - M-1 parts: M-1-Controller, M-1-Data-Cable, M-1-Power-Module, M-1-Digital-Microphone
  - PUMP-1 parts: PUMP-1-Fluid-Sensor, PUMP-1-Bottle, PUMP-1-Full-Accessory-Kit
  - Probes and cables: TEMP-1-Multi-Probe-Splitter, Apollo-FPC-Ribbon-Cable, MiCS-4514-Cable
  - Breakout boards: SCD40-Breakout-Board, SEN55-SCD40-Breakout-Board
  - Chips and modules: W5500 Ethernet HAT, ESP32-PICO (LED-1 MCU), SHT20 probe, Casita module
  - Other products: MSR-1 (predecessor of MSR-2), Home Assistant Voice PE, TEMP-1 16340 battery, magnet mount, the mounts/stands, and the R-PRO-1 gang box and ceiling kits
- Missing backlinks:
  - TEMP-1 and PLT-1 never link [[Long-Temperature-Probe]], [[Short-Temperature-Probe]] or [[TEMP-1-Food-Probe]].
  - ESK-1 never links [[Apollo-Breakout-Module]].
  - LED-1 has no component links at all.
  - PA-1 has no links at all.

=== 5. SUPPORT KNOWLEDGE MISSING FROM THE VAULT ===
None of the following is covered in any note:
- Company and policies: contact channels and support hours, escalation path, warranty terms and length, returns/RMA, refunds, shipping carriers/times/regions, international shipping and customs, order changes/cancellation, preorder and backorder policy, sold-out restock and notify-me behaviour, discounts, wholesale/B2B.
- Onboarding: first power-on, Improv Wi-Fi over BLE/USB (mentioned only as a feature on NFC-1, CAST-PRO-1 and R-PRO-1), the fallback hotspot (name, password, IP), adoption in the Home Assistant ESPHome integration and ESPHome Device Builder, the API encryption key, and HA discovery.
- Firmware: the web flasher URL, boot/download mode button procedure per device, OTA updates (stable vs beta channels are mentioned only on NFC-1), where the YAML/GitHub repos live, how to "take control" or adopt and customise YAML, and the WLED update flow for LED-1 and M-1.
- Troubleshooting: no trees for won't connect to Wi-Fi (2.4 GHz only, mesh/band steering), device offline/unavailable, inaccurate temperature (offsets), radar false positives/ghosts and tuning, still presence not detected, CO2 calibration (ASC/FRC), BLE proxy problems, battery drain, sleep-mode confusion, USB not detected, or PoE not powering.
- Known issues and errata per hardware revision. Only the M-1 Rev 6 is mentioned, and there are no revision identifiers otherwise.
- Docs links: only PUMP-1 links the wiki (wiki.apolloautomation.com). Discord is mentioned without a URL (MSR-2, MTR-1, Voice Speaker). There are no GitHub, YAML or CAD links even though the "open source/CAD" claim is repeated.
- Integration guides: Homey, Hubitat and HomeSeer are claimed on AIR-1 with no instructions. Blueprints, Music Assistant/Sendspin setup, and Zigbee/Thread status are missing.
- Physical: dimensions (only M-1 has them), weights, mounting instructions, recommended mounting height for radar, and power supply requirements (amps/W) except M-1's 5V 3A.
- Legacy and discontinued products: MSR-1 and any older SKUs customers will still own.
- Real ticket history: no Q&A pairs drawn from tickets, and no macros or canned replies.

=== 6. THINGS THAT WOULD CONFUSE AN LLM RETRIEVER ===
- Name variants for the same entity:
  - R-PRO-1 / "R PRO-1"; CAST-PRO-1 / "CAST PRO-1"
  - ESK-1 / "Official ESPHome Starter Kit" / "ESPHome Starter Kit"; ESPHome-C6-Board / "Official ESPHome C6 Board"
  - AHT20 / AHT20-F / AHT20F
  - SCD40 / SCD-40
  - LTR390 / LTR-390UV
  - LD2410B / HLK-LD2410B; ld2450 / LD2450 / HLK-LD2450
  - ESP32-C3 / ESP32-C3-Mini / ESP32-C3-MINI-1; ESP32-C6 / ESP32-C6-MINI / ESP32-C6-MINI-1
  - TEMP-1-Food-Probe (URL /food-probe); long and short probes also called "Dallas long/short probe"
  - Battery versions of PLT-1 and TEMP-1 are referenced as "(B)" with no SKU.
  - No note has an `aliases:` frontmatter key.
- Near-duplicate notes whose chunks look the same:
  - DEV-1 vs DEV-2: almost identical text except the chip.
  - CAST-1 vs CAST-PRO-1.
  - SEN55 vs SEN65: identical accuracy and PM figures.
  - Short vs Long-Temperature-Probe.
  - MSR-2 vs MTR-1: same LTR390/SCD40/buzzer/BT tracker language.
  - The Specs block (six "Not stated on site" lines) is word-for-word identical in about 12 product notes. Because notes have no in-body title, a chunk like "Battery life: Not stated on site..." cannot be traced to its product.
- Conflicting or contextual facts:
  - ESP32-C6 "Operating range -40 to +85 C" is borrowed from the C6 Board but sits on a note shared by 7 products.
  - The AHT20 accuracy figure comes from the ESK-1 page but applies to PLT-1 and TEMP-1 too.
  - ESP32-S3 is listed for M-1, while LED-1 (same WLED family) uses ESP32-PICO.
  - Breakout Module says it "is not part of the official ESPHome Starter Kit family", yet ESK-1 sells it as an add-on.
  - The R-PRO-1 Description calls the LD2450 the "base", and it is the only radar on MTR-1. That is fine, but "Number of zones: 3" on ld2450 is unsourced.
- Datasheet-derived numbers are mixed into site-claimed numbers. Only some notes separate them with "Source:", which risks the AI quoting datasheet maxima as Apollo guarantees. Examples: DS18B20 range -55 to 125 °C vs the probe's 85 °C max; SCD40 range 400-2000 ppm.
- Time-sensitive data (stock status, preorder, price-increase notes) is mixed into Description prose with no date or `status:` field, so it will go stale silently.
- The LD2412 component note doubles as a store product (it has `source:`), with type: component.
- Hedge phrases like "per the site", "Site note:", "wording unclear on site", "(as high as tested)" and "reported in customer reviews, not in the product text" leak into customer-facing answers if the AI quotes them verbatim.
- MSR-2's Q&A text is in a non-question form ("USB becoming detected and not detected"), so it will match poorly against real customer phrasing.