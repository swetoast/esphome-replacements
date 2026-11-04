import sys, types, importlib.util
def fr(cmd, data, ver=0):
    f = bytes([0x55, 0xAA, ver, cmd, len(data) >> 8, len(data) & 0xFF]) + bytes(data)
    return f + bytes([sum(f) & 0xFF])
stream = [b"\x00\xff\x55", fr(0x01, b'{"p":"abc","v":"1.0.0"}')[:10], fr(0x01, b'{"p":"abc","v":"1.0.0"}')[10:],
          fr(0x05, [1,4,0,1,0, 14,4,0,1,2]), fr(0x08, [1,0x1a,11,2,16,9,5, 15,2,0,4,0,0,0,100]),
          fr(0x07, [1,1,0,1,1], ver=3), b"\x55\xaa\x00\x05\x00\x01\x00\x99"]
class FakeSerial:
    def __init__(self, *a, **k): self.i = 0
    def read(self, n):
        if self.i >= len(stream): raise KeyboardInterrupt
        self.i += 1; return stream[self.i - 1]
sys.modules["serial"] = types.SimpleNamespace(Serial=FakeSerial)
spec = importlib.util.spec_from_file_location("s", sys.argv[1]); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
sys.argv = ["x", "/dev/null"]
try: m.main()
except KeyboardInterrupt: pass
