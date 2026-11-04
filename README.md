# ESPHome replacements

Replacement firmware for off-the-shelf smart home devices. Each device here runs ESPHome instead of its stock firmware and talks only to Home Assistant on the local network. No cloud account, no outside connections.

Every device has its own folder with everything needed to go from a stock unit to a working ESPHome device: hardware notes, backup and flashing steps, the ESPHome config and the Home Assistant side.

## Devices

| Device | What it is | Chip | First flash | State |
|---|---|---|---|---|
| [Deltaco SH-WS03](Deltaco%20SH-WS03/) | Wi-Fi smoke alarm, battery powered | Tuya TYWE3S (ESP8266) | Serial adapter, soldering required | Config validated and protocol tests passing; not yet flashed on a device |
| [Walltrix Emil](Walltrix%20Emil/) | Wall clock with a 36-LED ring | ESP8266EX, 4 MB | Micro-USB, no opening needed | Five ready-made clock examples |

## Before you start

These points apply to every device. Each device README has the specific steps.

1. **Back up the stock firmware first.** Read the whole flash before writing anything. Without a backup there is no way back.
2. **Keep backups private.** A stock firmware dump contains your Wi-Fi password and the device's own keys. Never upload one, here or anywhere else. `.gitignore` already blocks `*.bin`.
3. **Disconnect power.** Unplug mains devices and remove batteries before opening or wiring them. Only connect what the device README tells you to.
4. **Use 3.3 V.** ESP8266 and ESP32 modules are not 5 V tolerant. Set the serial adapter to 3.3 V and never connect its 5 V pin.
5. **Check the pinout with a multimeter** before soldering. Modules with the same name sometimes ship with a different internal layout.

### Tools

| Tool | Used for |
|---|---|
| USB to serial adapter, 3.3 V (CP2102, CH340) | First flash on devices without USB |
| Soldering iron, thin wire | Devices without a header |
| Multimeter | Checking pinouts and supply voltages |
| Python 3 | `pip install --upgrade esptool esphome pyserial` |

The device READMEs use esptool 5 command names (`read-flash`, `write-flash`, `erase-flash`).

### Secrets

Each device folder includes a `secrets.example.yaml`. Copy it to `secrets.yaml` next to the config and fill it in. `secrets.yaml` is ignored by git and never committed.

Generate an API encryption key with:

```bash
python3 -c "import secrets,base64;print(base64.b64encode(secrets.token_bytes(32)).decode())"
```

## Repository layout

```
.
├── README.md
├── LICENSE                     GPL-3.0 (configs, scripts, tests)
├── LICENSES/                   Full texts of every license used
├── REUSE.toml                  Which license applies to which file
├── Deltaco SH-WS03/
│   ├── README.md               Hardware, pinout, backup, flashing, entities
│   ├── deltaco-sh-ws03.yaml
│   ├── secrets.example.yaml
│   ├── tuya_sniff.py
│   ├── sh-ws03-wiring.png
│   └── tests/
└── Walltrix Emil/
    ├── README.md
    ├── docs/
    ├── examples/
    └── tests/
```

## Adding a device

Create a folder named after the brand and model, and include:

| Item | Required | Contents |
|---|---|---|
| `README.md` | Yes | What the device is, the hardware (chip, module, pinout), backup steps, flashing steps, Home Assistant entities, troubleshooting, restore steps |
| ESPHome config | Yes | One `.yaml` per variant, or an `examples/` folder for several |
| `secrets.example.yaml` | Yes | Placeholder values only |
| Photos or wiring images | When opening is needed | Board photos with the connection points marked |
| `tests/` | When the config has logic | Anything that can be checked without the device |
| `hardware/` | For printed or built parts | Source files (`.scad`, `.step`, `.f3d`) and printable files (`.stl`, `.3mf`) |

Then add a row to the device table above, and run `reuse lint` (see Licensing).

## Safety

Some of these devices have a safety function, for example a smoke alarm. Where that is the case, only the Wi-Fi part is replaced and the safety function keeps running on the device's own hardware. Test the device after flashing and after reassembly, and keep testing it as its manual says.

Replacing the firmware voids the warranty and may void certifications. These projects add local control and notifications. They are not a replacement for a certified alarm or safety system.

Everything here is provided without warranty; see the license texts.

## Licensing

The repository uses one license per kind of content. [REUSE](https://reuse.software/) metadata in `REUSE.toml` records which license applies to which file, and the full texts are in `LICENSES/`.

| Content | License | Why |
|---|---|---|
| ESPHome configs, Home Assistant packages, scripts, tests | [GPL-3.0-or-later](LICENSES/GPL-3.0-or-later.txt) | The firmware built from these configs contains the ESPHome C++ runtime, which is GPLv3. The configs follow the same terms, so improvements to them stay open. |
| Documentation and images | [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt) | Made for text and pictures. Guides can be copied and translated with credit, and changed versions stay under the same terms. |
| Hardware designs (cases, mounts, PCBs) | CERN-OHL-S-2.0 | Made for physical designs. Modified designs that are distributed or sold must share their sources. The license text is added to `LICENSES/` with the first hardware file. |

In short: use, change and share anything here, including commercially. Keep the credit, and when you share a changed version, share it under the same license.

ESPHome itself is licensed under MIT (Python) and GPLv3 (C++ runtime). Device names and trademarks belong to their owners.

To check the licensing after adding files:

```bash
pip install reuse
reuse lint
```

Copyright 2026 swetoast.
