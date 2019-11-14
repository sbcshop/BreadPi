from breadpi import BreadPi
from time import sleep

pcf = BreadPi()

Analog_Pin = 3

while True:
    analog_data = pcf.read_analog(register=Analog_Pin)
    print(analog_data)
    sleep(.1)
