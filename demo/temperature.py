'''
Read and interpret the RP2040 temperature according to the voltage reading
on ADC4. See CircuitPython's common_hal_mcu_processor_get_temperature().
'''

import time

import microcontroller


while True:
    print(f'Temperature is now {microcontroller.cpu.temperature}°C')
    time.sleep(1)
