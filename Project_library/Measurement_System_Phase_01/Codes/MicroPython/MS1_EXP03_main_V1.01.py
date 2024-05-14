""" Micro Python Script for Raspberry Pi PicoW
    
    ### Program Tasks:
    
    1) To read the analog signal from adc capable pin
    2) To print the value of analog signal from adc pin every 1-5 seconds
    3) At ADC pin 26 an LDR input is connected with its other leg connected to 5.1K Ohm resistor
    4) MCU prints the Raw adc value as well as brightness percentage
    5) If brightness percent is less than a threshold it blinks an external LED

"""

# Libraries and modules

import machine
from machine import Pin
import time

# System variables and pin assignment

Polling_frequency = 1   
GPIO_ADC0 = 26                                # Pin 26 is ADC
ADC16_PC = 0.001525902                        # 100/65335
Brightness_percent = 0                        # Brightness level
LED_onboard = machine.Pin("LED", Pin.OUT)     # Onboard LED 
LED_ext = machine.Pin(15, machine.Pin.OUT)    # External LED


# Setting up ADC on Pin 26 
adc_0 = machine.ADC(machine.Pin(GPIO_ADC0))   # Pin 26

# Initial startup
time.sleep(5)

while True:
    
    ADC0_val = adc_0.read_u16()
    Brightness_percent = ADC0_val*ADC16_PC
    print(Brightness_percent, ADC0_val, sep = ',')
    
    if (Brightness_percent < 2.0):
        LED_ext.on()
    elif (Brightness_percent < 16.0):
        LED_onboard.on()
    else:
        LED_ext.off()
        LED_onboard.off()
        
    time.sleep(Polling_frequency)
