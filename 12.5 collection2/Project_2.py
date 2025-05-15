
from gpiozero import LED as LEDClass # Alias
from pathlib import Path
import sys
from gpiozero import PWMLED
import time

HERE = Path(__file__).parent.parent
sys.path.append(str(HERE / 'Common'))
from ADCDevice import * 

USING_GRAVITECH_ADC = False # Only modify this if you are using a Gravitech ADC

ADC = ADCDevice() # Define an ADCDevice class object

LED_GREEN = LEDClass(17)  # define led
LED_BLUE = LEDClass(27)
LED_YELLOW = LEDClass(22)
LED_RED = LEDClass(18)


def setup():
    global ADC
    if(ADC.detectI2C(0x48) and USING_GRAVITECH_ADC): 
        ADC = GravitechADC()
    elif(ADC.detectI2C(0x48)): # Detect the pcf8591.
        ADC = PCF8591()
    elif(ADC.detectI2C(0x4b)): # Detect the ads7830
        ADC = ADS7830()
    else:
        print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
        exit(-1)
    

def loop():
    global ADC, LED_BLUE, LED_GREEN, LED_RED, LED_YELLOW
    while True:
        value = ADC.analogRead(0)   # read the ADC value of channel 0      
        voltage = value / 255.0 * 3.3
        time.sleep(0.01)
        
        percentage = value / 255
        print (f'ADC Value: {value} \tVoltage: {voltage:.2f} \tPercentage: {percentage*100}%')
        
        if percentage >= .25:
            LED_BLUE.on()
            print('Blue on')
        else:
            LED_BLUE.off()
            print('Blue off')
        if percentage >= .50:
            LED_GREEN.on()  
        else:
            LED_GREEN.off()
        if percentage >= .75:
            LED_YELLOW.on()
        else:
            LED_YELLOW.off()  
        if percentage >= .95:
            LED_RED.on()
        else:
            LED_RED.off()
            
def destroy():
    global LED_GREEN, LED_BLUE, LED_RED, LED_YELLOW
    # Release resources
    LED_YELLOW.close()
    LED_RED.close()
    LED_BLUE.close()
    LED_GREEN.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
