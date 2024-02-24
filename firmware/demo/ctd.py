'''
Read from a CTD device.
'''

import board
import busio


uart = busio.UART(
    tx=board.GP0,  # or None if unused
    rx=board.GP1,
    baudrate=9600,
    receiver_buffer_size=64,  # TODO: based on max length
)


while True:
    data = uart.read(32)
    print('Received data:', data)
    pass  # TODO: process the data
