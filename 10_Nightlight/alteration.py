import time
from gpiozero import LEDBarGraph
from pathlib import Path
import sys
import math

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

LED_PINS : list[int] = [17, 18, 27, 22, 23, 24, 25, 12, 16, 15]
LEDS = LEDBarGraph(*LED_PINS, active_high=False)
ADC = ADCDevice()

def setup():
    global ADC, LEDS
    for led in LEDS:  # make led(on) move from left to right
        led.off()
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check+ the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
        
def loop():
    global ADC, LEDS
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0
        print (f'ADC Value: {value}')
        time.sleep(0.01)
        lights_on = math.floor(value/25.5) + 1
        print(f'how many lights: {lights_on}')
        for i in range(0, lights_on):
            LEDS[i].on()
        for i in range(lights_on, 9):
            LEDS[i].off()


            
def destroy():
    global ADC, LEDS
    ADC.close()
    for led in LEDS:  # make led(on) move from left to right
        led.close() 
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        
