import RPi.GPIO as GPIO #import RPi.GPIO module
import hal.hal_led as led
import hal.hal_input_switch as switch
import time
from time import sleep

def main():
    # Initialize LED HAL driver 
    led.init()

    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    start_time = time.time()
    end_time = start_time + 5
    #Set LED output level, 1 = ON, 0 = OFF
    while (1):
        if switch.read_slide_switch()==0:
            led.set_output(0, 1)
            sleep(0.1)
            led.set_output(0, 0)
            sleep(0.1)
        else:
            while time.time()<end_time:
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)    
            while switch.read_slide_switch()==1:
                start_time = time.time()
                end_time = start_time + 5


# Main entry point
if __name__ == "_main_":
    main()