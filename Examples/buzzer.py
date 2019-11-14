from breadpi import BreadPi
from time import sleep

Buzzer = BreadPi()


def buzz(delay=1):
    Buzzer.buzzer_on()
    sleep(delay)
    Buzzer.buzzer_off()
    sleep(delay)


while True:
    buzz(delay=1)
