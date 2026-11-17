# Setup and Troubleshooting notes — review checklist

Status: draft · 2026-11-17

There are 14 new notes, in `Apollo-Knowledge/Setup/` (8) and `Apollo-Knowledge/Troubleshooting/` (6). For each note:

- A writer drafted it from the official Apollo wiki.
- A separate checker fetched every source page and removed anything it couldn't confirm.
- A final pass fixed contradictions between notes and added cross-links.

Every note has `review_status: draft`. Change a note to `reviewed` once a person has checked it.

## Notes

| Setup | Troubleshooting |
|---|---|
| Wi-Fi-Setup | Wont-Connect-to-Wi-Fi |
| Add-to-Home-Assistant | Device-Unavailable |
| Factory-Reflash | USB-Not-Detected |
| Boot-Mode | Temperature-Reads-High |
| Firmware-Updates | Radar-Presence-Issues |
| WLED-Setup | CO2-Readings |
| PoE-Setup | |
| Battery-and-Sleep | |

## Questions for the team

### Official sources that conflict

1. **What does holding BOOT for 10 seconds do?** The per-device wiki reset pages say it only clears Wi-Fi. The wake-up-battery-sensor page says it is a full factory reset. The notes currently warn on the safe side.
2. **BTN-1 always-awake battery life:** the wiki FAQ says about 18 h; `Products/BTN-1.md` says about 38 h.
3. **PLT-1B battery life:** the product note says about 6 months at default settings. The wiki FAQ says about a year at the 12 h default.
4. **TEMP-1B battery life:** "up to 6 months" (store) vs "around 6+ months" (wiki).
5. **AIR-1 boot button:** the wiki text says the opening is on the left of the USB-C port, but calls it "the right button".
6. **Hidden Wi-Fi networks:** the Apollo wiki uses `fast_connect: true`. ESPHome's own docs recommend `hidden: true`. Which should we recommend?

### Not documented on the wiki

7. **R PRO-1 Wi-Fi reset and boot mode:** SW6 is on the board inside the case. Do customers really need to open it?
8. **Ethernet firmware on the R PRO-1:** should customers plug in the Ethernet cable after switching firmware? How does the device then get into Home Assistant?
9. **Hotspot passwords:** does any device's hotspot have a password? The notes assume it is open.
10. **2.4 GHz requirement:** is 2.4 GHz-only true for every device? The wiki states it only for the CAST range.
11. **USB drivers:** do any Apollo boards need CH34x or CP210x drivers, or are they all native USB?
12. **Prevent Sleep:** does a battery device need to be awake before Home Assistant can change it?
13. **Entity names:** do these exist on every device, or only some?
    - "Firmware Update" and "Firmware Channel"
    - the CO2 button "Calibrate SCD40 to 420 ppm"
    - MTR-1 temperature offset entities
14. **"Factory Reset Radar" button:** should customers be told to use it, or only when support asks?
15. **Missing guides:**
    - NFC-1, LED-1, DEV-1 and DEV-2 have no wiki pages for setup, boot mode or reflash. The notes leave these devices out.
    - Should the CAST PRO-1 product note mention its hotspot setup?

### Gaps in the vault

16. **Products the wiki covers that have no vault notes:** MSR-1, H-1, H-2 and H-3. TEMP-1B and PLT-1B are covered as variants of TEMP-1 and PLT-1. Should we add product notes for the others?
17. **Escalation wording:** the "When to escalate" sections and the support@apolloautomation.com contact line are support policy, not wiki content. Please approve or edit them.
