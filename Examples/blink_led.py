#!/usr/bin/python3

from breadpi import BreadPi
from random import randint
from time import sleep

led = BreadPi()


def blink_leds():
    pins = ['L1', 'L2', 'L3', 'L4']
    random_pin = pins[randint(0, 3)]
    print('LED pin: ', random_pin)
    led.led_on(random_pin)
    sleep(.5)
    led.led_off(random_pin)
    sleep(.5)


try:
    while True:
        blink_leds()
except KeyboardInterrupt:
    pass
