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
