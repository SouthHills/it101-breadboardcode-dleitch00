from gpiozero import RGBLED
import time
from pathlib import Path
import subprocess

# active_high must be true because it is a common anode RGBLed
LED = RGBLED(red=17, green=18, blue=27, active_high=True)
path = Path('/sys/class/thermal/thermal_zone0/temp')


def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)

def loop():
    
    
    while True:
        contents = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp']).decode()
        print(contents)
        temp = int(contents)/1000
        print(temp)
        if temp <= 15:
            set_color(0, 0, 1)
            print("All blue")
        elif temp >= 80:
            set_color(1, 0, 0)
            print("All red")
        else:
            set_color(temp / 80, 0, 15 / temp)
        time.sleep(1)
        
def destroy():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()