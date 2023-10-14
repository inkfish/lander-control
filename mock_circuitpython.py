import os
import sys
import unittest.mock

import pyfakefs.fake_filesystem_unittest


# Mock out CircuitPython modules
modules = [
    'alarm',
    'analogio',
    'board',
    'busio',
    'digitalio',
    'microcontroller',
    'sdcardio',
    'storage',
    'supervisor',
    'watchdog',
    'wifi',
]

for m in modules:
    sys.modules[m] = unittest.mock.NonCallableMagicMock()


# Mock out the filesystem.
#
# Caveat: This does not mock out storage.VfsFat.open(), etc. which will not
# cause the desired effect on the filesystem.
patcher = pyfakefs.fake_filesystem_unittest.Patcher()
patcher.setUp()

def fake_storage_mount(filesystem, mount_path: str,
                       readonly: bool = False) -> None:
    os.mkdir(mount_path)

sys.modules['storage'].mount = fake_storage_mount



# Example of reading a value from a mocked analog GPIO pin
def main():
    import math
    import time

    import analogio
    import board


    class MockSinusoidAnalogIn(unittest.mock.MagicMock):
        def __init__(self, pin):
            super().__init__()
            self.pin = pin

        @property
        def value(self):
            if self.pin is board.A0:
                return int(math.sin(time.monotonic()) * 32767) + 32768
            elif self.pin is board.A1:
                return int(math.cos(time.monotonic()) * 32767) + 32768
            return 0

        # Make children as regular MagicMock instances
        def _get_child_mock(self, /, **kwargs):
            return unittest.mock.MagicMock(**kwargs)


    with unittest.mock.patch('analogio.AnalogIn', new=MockSinusoidAnalogIn):
        adc0 = analogio.AnalogIn(board.A0)
        adc1 = analogio.AnalogIn(board.A1)

        while True:
            print(f'ADC0: {adc0.value:5}  ADC1: {adc1.value:5}')
            time.sleep(1)


if __name__ == '__main__':
    main()
