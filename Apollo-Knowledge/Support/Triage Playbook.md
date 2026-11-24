---
type: triage-playbook
---
<!--
Triage playbook: the guidance Inventori's AI ticket triage follows. Copy this file into the
Knowledge-Vault repo at exactly Apollo-Knowledge/Support/Triage Playbook.md: the playbook is
pinned to that path, and a "type: triage-playbook" note anywhere else is ignored. It takes
effect on tickets triaged after the next hourly vault sync. Protect it: branch protection on
main and a CODEOWNERS entry for this path.

THIS REPO IS PUBLIC: no personal names, email addresses, costs, prices, refund thresholds, or
failure or replacement rates and other internal quality data.

Safe to edit: the text after "When:" (what the category means), the text after "Do:" (what
staff do next) and everything under "## Tags". Everything inside a section reaches the AI
prompt: HTML comments like this one are stripped and fenced code blocks are dropped, but any
other note you leave there is sent.

Keep exact: the "type: triage-playbook" line above, every "## <key>" heading (the keys are
fixed in Inventori) and the "When:" / "Do:" labels at the start of a line. Any line starting
with "#" ends a section; a heading that is not exactly "## <key>" or "## Tags" is ignored and
logged. A missing or blank When: or Do: falls back to Inventori's built-in text, and so does a
part past the overall 20,000-character cap. Each part is cut at 1,500 characters. The safety
rules, the answer format, the tag keys (mmwave, ld241x, ld2450) and the ticket card's
"Recommended action" stay in Inventori and cannot be changed here.
-->
# Triage Playbook

## uncategorized
When: none of the categories below fits, or the ticket is too unclear to place.
Do: Staff read the ticket and pick a category by hand.

## shipping
When: the order has not shipped, has not arrived, or the customer asks where it is ("why hasn't my order shipped", "I haven't received the order I placed on ...").
Do: Our code compares the days since the last carrier scan with the reship threshold, and recommends either reshipping and filing a carrier claim, or reassuring the customer with the order date, the hand-off date, the last scan and a date to get back in touch if nothing moves. Base the next step on the recommendation in the shipping line of <facts>; when there is no shipping line, it says no tracking snapshot, or the recommendation is LookupFailed or TrackingUnavailable, the next step is to check the order's tracking; when it is CheckCarrier, the next step is to check the carrier's tracking page before promising anything. Never work out day counts or dates yourself.

## damaged_missing_item
When: the parcel arrived, but an item is damaged, broken in transit or missing from the box.
Do: Ask for photos of the damaged item and its packaging, and confirm that everything else arrived and works. Then replace per item and file the claim, as for a lost parcel.

## zooz
When: a Zooz device (Apollo resells Zooz Z-Wave products) that is dead on arrival, will not include or adopt, or misbehaves.
Do: Apollo is a Zooz reseller. Send the customer to the Zooz support ticket page (https://www.support.getzooz.com/new/). If they already factory reset the device, skip troubleshooting and go straight to Zooz. When Zooz says the device is dead, the customer forwards Zooz's answer and we replace or return it.

## tech_networking
When: the device cannot get onto the network: it cannot join Wi-Fi, shows no setup hotspot or a blank setup page, or cannot be found after setup.
Do: Walk through setup: the setup hotspot (CAST devices: 192.168.4.1/setup), Bluetooth (Improv) through Home Assistant where the device supports it, and the wiki pages. Ask whether the router sees the device after the hotspot step. Then the full firmware reflash article and the ESP32 network troubleshooting article. Still failing: treat it as a hardware fault.

## tech_home_assistant
When: the device is on the network and added to Home Assistant, but its entities, readings or automations do not behave.
Do: Ask for logs and screenshots. A firmware reflash usually fixes it; if not, it often turns into a hardware fault.

## tech_hardware
When: a hardware fault: no response on power, an add-on module that does not report, or a device that stopped responding.
Do: Ask for Home Assistant logs and screenshots plus the ESPHome device page at the device's IP, then a firmware reflash. Work out whether the add-on module or the main board is at fault (swap modules between identical devices), then replace the add-on or the main board.

## product_inquiry
When: a question before or about buying: can a product do X, compatibility, when it is back in stock in a country.
Do: Answer from the product notes in the knowledge vault (what the product can do, compatibility, stock by country).

## reviewer_collab
When: a reviewer, influencer or creator asking for free product or a collaboration.
Do: Tag it in Freshdesk and assign it to the collaborations owner. Support does not reply.

## spam
When: unsolicited offers: services, SEO, paid reviews, manufacturing or marketing pitches, anything not from a customer or a real prospect.
Do: Mark the contact as spam and delete the ticket.

## carrier_notification
When: an automated DHL, UPS, USPS (or other carrier) shipping update email, not written by a person.
Do: Delete it; nobody replies.

## return_cancellation
When: a message is from "do_not_reply@inventori.io" and includes information about a customer applying for a return or order cancellation.
Do: Look at the included order number and note the reason for the request and, if shipped, the date of shipping.

## invoice_requests
When: a customer message arrives requesting an invoice for a purchase
Do: Ask the customer for the company and tax information that they require for the invoice

## shipsurance
When: a message is from "shopifyclaims@shipsurance.com" and is related to a filed insurance claim.
Do: Tag and sort these messages.

## Tags
Tags are separate from the category and can go with any category; use [] when none fits.
- mmwave: the ticket is about an mmWave radar presence sensor, or a product's radar presence readings.
- ld241x: the radar is a single-target LD2410B or LD2412.
- ld2450: the radar is the multi-target LD2450.
Add mmwave whenever you add ld241x or ld2450. Use the knowledge vault to tell which radar a product carries (a product can carry both).
mmWave flows (for next_step on tech tickets with these tags):
- ld241x: explain the detection gates, install the dashboard and run the auto calibration, reflash the firmware, and try a different power supply and cable with no strain on the device. Still failing: a module or main board fault.
- ld2450: explain target tracking and the Zone Mapper, point to the wiki, ask for logs and screenshots, and reflash the firmware. Still failing: a hardware fault.
