#!/usr/bin/python3

from sys import exit, version_info
import RPi.GPIO as GPIO

try:
    from smbus import SMBus
except ImportError:
    if version_info[0] < 3:
        exit("This library requires python-smbus\nInstall with: sudo "
             "apt-get install python-smbus")
    elif version_info[0] == 3:
        exit("This library requires python3-smbus\nInstall with: sudo "
             "apt-get install python3-smbus")


class PCF8591:
    input_pin = {0: 0x40,
                 1: 0x41,
                 2: 0x42,
                 3: 0x43
                 }

    def __init__(self, i2c_address=0x48):
        """
        :param i2c_address: i2c address of pcf8591
        """
        self.bus = SMBus(self.bus_id())
        self.address = i2c_address

    def bus_id(self):
        """
        :return: Returns SMBUS id of Raspberry Pi
        """
        revision = [lines[12:-1] for lines in open('/proc/cpuinfo',
                                                   'r').readlines() if
                    "Revision" in lines[:8]]
        revision = (revision + ['0000'])[0]
        return 1 if int(revision, 16) >= 4 else 0

    def read_analog(self, register):
        """
        :param register: Register to read data from (0, 1, 2, 3)
        :return: Analog to digitally converted value(Integer)
        """
        self.bus.write_byte(self.address, self.input_pin[register])
        value = self.bus.read_byte(self.address)
        return value

    def write_analog(self, register, value):
        """
        :param register: Register to write data in
        :param value: Digital Value to write (varies from 0-256)
        :return: None
        """
        self.bus.write_byte_data(self.address, self.input_pin[register], value)


class BreadPi(PCF8591):
    led_pins = {
        'L1': 32,
        'L2': 36,
        'L3': 38,
        'L4': 40
    }
    button_pins = {
        'SW1': 29,
        'SW2': 31
    }

    def __init__(self):
        super(BreadPi, self).__init__(i2c_address=0x48)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.input_pins = []
        self.output_pins = []

    def setup(self, input_pin=None, output_pin=None):
        """
        Set Input and Output modes for pins
        :return: None
        """
        if output_pin:
            if output_pin not in self.output_pins:
                self.output_pins.append(output_pin)
                GPIO.setup(output_pin, GPIO.OUT)
            if output_pin in self.input_pins:
                self.input_pins.remove(output_pin)

        elif input_pin:
            if input_pin not in self.input_pins:
                self.input_pins.append(input_pin)
                GPIO.setup(input_pin, GPIO.IN)
            if input_pin in self.output_pins:
                self.output_pins.remove(input_pin)

    def led_on(self, led_pin='L1'):
        """
        Turn on Led/ Send high on given pin
        :param led_pin: Led Pin string('L1', 'L2', 'L3', or 'L4') or Board
        pins nnumbers(integer)
        :return: None
        """
        if not isinstance(led_pin, int):
            led_pin = self.led_pins[led_pin]
        self.setup(output_pin=led_pin)
        GPIO.output(led_pin, GPIO.HIGH)

    def led_off(self, led_pin='L1'):
        """
        Turn Off Led/ Send low on given pin
        :param led_pin: Led Pin string('L1', 'L2', 'L3', or 'L4') or Board
        pins nnumbers(integer)
        :return: None
        """
        if not isinstance(led_pin, int):
            led_pin = self.led_pins[led_pin]
        self.setup(output_pin=led_pin)
        GPIO.setup(led_pin, GPIO.OUT)
        GPIO.output(led_pin, GPIO.LOW)

    def buzzer_on(self):
        """
        Turn on Buzzer of Breadpi
        :return: None
        """
        buzzer_pin = 37
        self.setup(output_pin=buzzer_pin)
        GPIO.output(buzzer_pin, GPIO.HIGH)

    def buzzer_off(self):
        """
        Turn off Buzzer of Breadpi
        :return: None
        """
        buzzer_pin = 37
        GPIO.output(buzzer_pin, GPIO.LOW)

    def button(self, button_pin='SW1'):
        """
        Take Digital input from Button
        :param button_pin: String('SW1' or 'SW2') or Board Pin Number(integer)
        :return: Button Status as Boolean
        """
        if not isinstance(button_pin, int):
            button_pin = self.button_pins[button_pin]
        self.setup(input_pin=button_pin)
        return GPIO.input(button_pin)


try:
    pcf = PCF8591()
    pcf.read_analog(3)
except IOError:
    pass
