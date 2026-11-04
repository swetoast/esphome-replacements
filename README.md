# ESPHome replacements

Smart home devices are sold to you but controlled by someone else. They need a vendor account, talk to servers you don't control, report on how you use them, and die the day the company loses interest, gets bought or shuts the servers down.

This project takes that cloud junk and replaces its firmware with ESPHome. The device stays on your network, answers only to your Home Assistant, and keeps working whether the company behind it exists or not. Same hardware, no strings attached.

You bought it. You should own it.

## How

Every device here is handled the same way.

**Nothing leaves your network.** No cloud, no account, no telemetry. Pull the internet cable and the device doesn't notice.

**It still does its job.** A clock keeps time, a smoke alarm still screams. Safety functions stay on the device's own hardware. The new firmware adds reporting, it doesn't take over.

**Home Assistant does the thinking.** The firmware reads sensors, drives outputs and reports state. Schedules, logic and anything you might change later live in Home Assistant, so you never have to reflash to tweak behaviour.

**You can always go back.** Every guide starts with a full backup of the stock firmware and ends with how to restore it.

**No guessing.** Board photos, pinouts, exact commands, what every entity means and what to do when it goes wrong. If someone has to guess a step, the guide isn't done.

**No pretending.** Configs are validated, testable logic is tested, and every device README says plainly what has and hasn't been confirmed on real hardware.

## Finding the next one

The easy wins run on an ESP8266 or ESP32, often inside a Tuya module like the TYWE3S or TYWE2S. Newer Tuya modules often use BK7231 or RTL8710 chips instead, which ESPHome supports only partly or not at all. Check the FCC photos or open one up before buying a batch.

Mains-powered devices are the simplest. Battery devices are harder: a separate controller keeps the Wi-Fi module off and powers it only for a few seconds to report, so the firmware has to speak that controller's language fast.

## Don't brick it, don't burn it

- Back up the whole flash before writing anything. It's your only way back.
- Never publish a backup. It holds your Wi-Fi password and the device's keys. `.gitignore` blocks `*.bin` for that reason.
- Unplug mains devices and pull the batteries before opening or wiring anything.
- ESP chips run at 3.3 V. Set the serial adapter to 3.3 V and leave its 5 V pin alone.
- Check the pinout with a multimeter before soldering. Modules with the same name don't always have the same insides.
- New firmware voids the warranty and can void certifications. Test the device after flashing, and keep testing it the way its manual says.

Most devices need a 3.3 V USB serial adapter, a soldering iron, a multimeter and `pip install --upgrade esptool esphome pyserial`.

## Adding a device

One folder per device, named after brand and model. It needs:

- a README covering hardware, backup, flashing, entities, troubleshooting and restore
- the ESPHome config
- a `secrets.example.yaml` with placeholder values

Add board photos when the device has to be opened, a `tests/` folder when the config has its own logic, and a `hardware/` folder for printed or built parts. Then run `reuse lint`.
