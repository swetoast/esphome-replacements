# ESPHome replacements

Smart home devices are sold to you but controlled by someone else. They need a vendor account, talk to servers you don't control, report on how you use them, and die the day the company loses interest, gets bought or shuts the servers down.

This project takes back control of smart devices and puts ESPHome on them. The device stays on your network, answers only to your Home Assistant, and keeps working whether the company behind it exists or not.

You bought it. You should own it.

## How

Every device here is handled the same way.

**Nothing leaves your network.** No cloud, no account, no telemetry.

**It still does its job.** It keeps working on its own. Safety functions stay on the device's own hardware. The new firmware adds reporting, it doesn't take over.

**Home Assistant does the thinking.** The firmware reports state and does what it's told. Logic and anything you might change later live in Home Assistant, so you never have to reflash to tweak behaviour.

**You can always go back.** Every guide starts with a backup of the stock firmware and ends with how to restore it.

**No guessing.** Every step is written out. If someone has to guess, the guide isn't done.

**No pretending.** Configs are validated, testable logic is tested, and every device README says plainly what has and hasn't been confirmed on real hardware.

## Finding the next one

Pick devices that can run ESPHome or can be made to. Check what's inside before buying, since the same product can ship with different insides.

## Don't brick it, don't burn it

- Back up the stock firmware before writing anything. It's your only way back.
- Never publish a backup. It holds your credentials and the device's keys.
- Disconnect all power before opening or wiring anything.
- Check before you connect. Devices with the same name don't always have the same insides.
- New firmware voids the warranty and can void certifications. Test the device after flashing, and keep testing it the way its manual says.

Each device README lists what it needs.

## Adding a device

One folder per device, named after brand and model, with:

- a README covering hardware, backup, flashing, entities, troubleshooting and restore
- the ESPHome config
- example secrets with placeholder values, if the config uses secrets

Include anything else the device needs to be reproduced.

## Contributing

Pull requests are welcome. If you're not sure a device fits, open an issue first.

- Keep each pull request to one device or one change.
- Follow the layout in Adding a device.
- Say what you tested on real hardware and what you didn't.
- Never include backups, real credentials or keys.

Report bugs in issues. Say which device, what you expected and what happened.
