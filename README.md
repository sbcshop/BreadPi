# BreadPi
Packages for BreadPi, a hardware designed by SB Components

Install breadpi package on your Raspberry Pi using

`pip3 install breadpi`

or

`python3 -m pip install breadpi`


import the module with 

`from breadpi import BreadPi`


Access PCF8591 or GPIOs directly

`bread_pi = BreadPi()`

`data = bread_pi.read_analog(register=1)  #  Read Data from AIN1`

`bread_pi.write_analog(register=1, value=100)  #  Covert Digital data to 
analog`

use led_on, led_off, buzzer_on, buzzer_off or take digital inputs from 
buttons using button function of BreadPi class.

You can pass string printed on BreadPi like, 'L1' or 'SW1' or customized pin
 number like 29, 31 directly to the functions. 