#!/usr/bin/env python3
"""Passive TuyaMCU UART sniffer.

Wire adapter GND to board GND and adapter RX to the TYWE3S RXD pin
(that line carries what the MCU sends). Do not connect adapter 3V3 or TX.
Leave the batteries in, run this, then press the test button.

Usage: python3 tuya_sniff.py /dev/ttyUSB0
"""
import sys
from datetime import datetime

import serial

CMDS = {
    0x00: "heartbeat",
    0x01: "product info",
    0x02: "network status",
    0x03: "reset wifi",
    0x04: "reset / pairing mode",
    0x05: "DP report",
    0x06: "local time",
    0x07: "DP report (standard protocol)",
    0x08: "DP record",
    0x0A: "update check",
    0x0B: "signal strength",
}
TYPES = {0: "raw", 1: "bool", 2: "value", 3: "string", 4: "enum", 5: "bitmap"}


def decode_dps(d: bytes) -> str:
    out, i = [], 0
    while i + 4 <= len(d):
        dp, t, ln = d[i], d[i + 1], (d[i + 2] << 8) | d[i + 3]
        v = d[i + 4:i + 4 + ln]
        if t in (1, 2, 4, 5):
            val = int.from_bytes(v, "big")
        elif t == 3:
            val = v.decode(errors="replace")
        else:
            val = v.hex()
        out.append(f"dp{dp}={val} ({TYPES.get(t, t)})")
        i += 4 + ln
    return ", ".join(out)


def main() -> None:
    port = sys.argv[1] if len(sys.argv) > 1 else "/dev/ttyUSB0"
    baud = int(sys.argv[2]) if len(sys.argv) > 2 else 9600
    ser = serial.Serial(port, baud, timeout=0.1)
    print(f"Listening on {port} at {baud} baud, Ctrl+C to stop", flush=True)
    buf = bytearray()
    while True:
        buf += ser.read(256)
        while True:
            start = buf.find(b"\x55\xaa")
            if start < 0:
                del buf[:-1]
                break
            del buf[:start]
            if len(buf) < 7:
                break
            ln = (buf[4] << 8) | buf[5]
            if ln > 255:
                del buf[:1]
                continue
            if len(buf) < 7 + ln:
                break
            frame = bytes(buf[:7 + ln])
            del buf[:7 + ln]
            ok = (sum(frame[:-1]) & 0xFF) == frame[-1]
            ver, cmd, data = frame[2], frame[3], frame[6:-1]
            if cmd in (0x05, 0x07):
                info = decode_dps(data)
            elif cmd == 0x08 and len(data) > 7:
                info = decode_dps(data[7:])
            elif cmd == 0x01 and data:
                info = data.decode(errors="replace")
            else:
                info = data.hex(" ")
            ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            flag = "" if ok else " BAD CHECKSUM"
            print(f"{ts} v{ver} 0x{cmd:02X} {CMDS.get(cmd, '?')}{flag}: {info}  | {frame.hex(' ')}", flush=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
