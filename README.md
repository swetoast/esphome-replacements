# ESPHome replacements

Smart home devices are sold to you but controlled by someone else. They need a vendor account, talk to servers you don't control, report on how you use them, and die the day the company loses interest, gets bought or shuts the servers down.

This project takes that cloud junk and puts ESPHome on it. The device stays on your network, answers only to your Home Assistant, and keeps working whether the company behind it exists or not.

You bought it. You should own it.

## How

Every device here is handled the same way.

**Nothing leaves your network.** No cloud, no account, no telemetry. Pull the internet cable and the device doesn't notice.

**It still does its job.** A clock keeps time, a smoke alarm still screams. Safety functions stay on the device's own hardware. The new firmware adds reporting, it doesn't take over.

**Home Assistant does the thinking.** The firmware reads sensors, drives outputs and reports state. Schedules, logic and anything you might change later live in Home Assistant, so you never have to reflash to tweak behaviour.

**You can always go back.** Every guide starts with a full backup of the stock firmware and ends with how to restore it.

**No guessing.** Every step is written out. If someone has to guess, the guide isn't done.

**No pretending.** Configs are validated, testable logic is tested, and every device README says plainly what has and hasn't been confirmed on real hardware.

## Finding the next one

Look for devices with a chip ESPHome can run on, or a module that can be swapped for one that can. Check what's inside before buying a batch, since the same product can ship with different insides.

Mains-powered devices are the simplest. Battery devices are harder, because they only wake the radio briefly to report.

## Don't brick it, don't burn it

- Back up the whole flash before writing anything. It's your only way back.
- Never publish a backup. It holds your network credentials and the device's keys.
- Unplug mains devices and pull the batteries before opening or wiring anything.
- Check the voltage and pinout before connecting anything. Devices with the same name don't always have the same insides.
- New firmware voids the warranty and can void certifications. Test the device after flashing, and keep testing it the way its manual says.

Each device README lists the tools it needs.

## Adding a device

One folder per device, named after brand and model. It needs:

- a README covering hardware, backup, flashing, entities, troubleshooting and restore
- the ESPHome config
- an example secrets file with placeholder values, if the config uses secrets

Add board photos when the device has to be opened, tests when the config has its own logic, and any printed or built parts. Then run `reuse lint`.
