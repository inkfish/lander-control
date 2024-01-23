'''
Read the battery voltages off the analog pins.
'''

import analogio
import board
import digitalio


pin_24v = analogio.AnalogIn(board.A1)
pin_48v = analogio.AnalogIn(board.A2)
pin_vsys = analogio.AnalogIn(board.A3)

# Resistor values below are from the voltage divider circuits in the schematic
adc_to_volts = lambda value, r1, r2: 3.3 * value * (r1 + r2) / (r2 * 65535)
batt_24v = adc_to_volts(pin_24v.value, 49_900, 4990)
batt_48v = adc_to_volts(pin_48v.value, 100_000, 4990)
vsys = adc_to_volts(pin_vsys.value, 200_000, 100_000)

print('24V battery voltage:', batt_24v, 'V')
print('48V battery voltage:', batt_48v, 'V')
print('VSYS voltage:', vsys, 'V')


# Check if USB is connected
pin_vbus = digitalio.DigitalInOut(board.VBUS_SENSE)
pin_vbus.switch_to_input(pull=digitalio.Pull.UP)
print('USB is connected:', pin_vbus.value)
