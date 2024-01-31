'''

'''

import board
import busio
import digitalio

import adafruit_pcf8574


gpio_expander = adafruit_pcf8574.PCF8574(
    busio.I2C(
        board.GP21,  # SCL
        board.GP20   # SDA
    )
)


# Power switches attached to the GPIO expander
pin_camera_power = gpio_expander.get_pin(0)
pin_spare_24v_power = gpio_expander.get_pin(1)
pin_modem_power = gpio_expander.get_pin(2)
pin_light_power = gpio_expander.get_pin(3)
pin_spare_48v_power = gpio_expander.get_pin(4)
pin_burn_wire = gpio_expander.get_pin(6)

for pin in [ pin_camera_power, pin_spare_24v_power, pin_modem_power,
             pin_light_power, pin_spare_48v_power, pin_burn_wire ]:
    pin.switch_to_output()


# Enable pin for burn wire
pin_burn_enable = digitalio.DigitalInOut(board.GP2)
pin_burn_enable.switch_to_output()


# Menu
print('''
Enter command: [number] [on|off]
    (24V)  1: Camera   2: Burn wire   3: Spare
    (48V)  4: Modem    5: Lights      6: Spare
           7: Burn wire enable
''')

while True:
    choice, _, state = input('> ').partition(' ')

    if state.lower() not in ('on', 'off', '1', '0', 'hi', 'high', 'lo', 'low'):
        print(f'Unknown state {state}, try again.')
        continue

    state = state.lower() in ('on', '1', 'hi', 'high')

    try:
        {
            '1': pin_camera_power,
            '2': pin_burn_wire,
            '3': pin_spare_24v_power,
            '4': pin_modem_power,
            '5': pin_light_power,
            '6': pin_spare_48v_power,
            '7': pin_burn_enable
        }[choice].value = state
    except KeyError:
        print(f'Unknown pin {choice}, try again.')
        continue

    print('Switched pin', choice, 'to', 'on' if state else 'off')
