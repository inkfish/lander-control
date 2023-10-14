'''
Benchmark an SD card connected to the SPI bus.
'''

import time

import board
import busio
import sdcardio
import storage


# SD card reader over SPI bus
sd = sdcardio.SDCard(
    spi=busio.SPI(
        clock=board.GP14,
        MOSI=board.GP15,
        MISO=board.GP12,
    ),
    cs=board.GP13,
    baudrate=25_000_000
)

# Inspect the card size
print(f'Capacity is {sd.count() * 512 // (1024*1024)} MB')


# Mount the filesystem on the card.
#
# CircuitPython only supports FAT32, though it might be possible to build with
# support for LittleFS.
vfs = storage.VfsFat(sd)
storage.mount(vfs, '/sd')

# Benchmark read/write speeds with the filesystem
buffer = bytearray(512)
start = time.monotonic()
with open('/sd/example.txt', 'wb') as f:
    for _ in range(0, 1024*1024, len(buffer)):
        f.write(buffer)
stop = time.monotonic()
print(f'Wrote 1 MB (fs) at {1/(stop - start):.2f} MB/s')

start = time.monotonic()
with open('/sd/example.txt', 'rb') as f:
    for _ in range(0, 1024*1024, len(buffer)):
        f.readinto(buffer)
stop = time.monotonic()
print(f'Read 1 MB (fs) in {1/(stop - start):.2f} MB/s')
