'''
Blink the two controllable LEDs.
'''
import time

import board
import digitalio


pico_led = digitalio.DigitalInOut(board.LED)
pico_led.switch_to_output()

lcb_led = digitalio.DigitalInOut(board.GP3)
lcb_led.switch_to_output()


i = 0
while True:
    if i == 0:
        pico_led.value = not pico_led.value
    else:
        lcb_led.value = not lcb_led.value

    i = 1 - i
    time.sleep(0.125)
