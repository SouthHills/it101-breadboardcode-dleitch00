
from gpiozero import RGBLED, Button
import time
import random

LED = RGBLED(red=17, green=18, blue=27, active_high=True)
BUTTON = Button(23)
pressed = True
colors = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
BLINK = 5
timer_pressed = 0
not_green = True

def set_color(r, g, b):
    """ Invert the colors due to using a common anode """
    LED.color = (1 - r, 1 - g, 1 - b)
    
def check_winner(pressed_color):
    global colors, BLINK
    if pressed_color == (colors[1]):
        for i in range(0, BLINK):
            set_color(0, 1, 0)
            time.sleep(.5)
            set_color(0, 0, 0)
            time.sleep(.5)
            
    else:
        for i in range(0, BLINK):
            set_color(1, 0, 0)
            time.sleep(.5)
            set_color(0, 0, 0)
            time.sleep(.5)
            
    destroy()
def loop():
    global BUTTON, pressed, not_green
    while True :
        if pressed:  # if button is pressed
            while not_green:
                rand_color = random.randint(1, 3)
                pressed_color = (1, 0, 0)
                match rand_color:
                    case 1:
                        set_color(colors[0][0], colors[0][1], colors[0][2])
                    case 2:
                        not_green = not not_green
                        pressed_color = (0, 1, 0)
                        set_color(colors[1][0], colors[1][1], colors[1][2])
                    case 3:
                        set_color(colors[2][0], colors[2][1], colors[2][2])  
            
                rand_sleep = random.randint(10, 100)
                time.sleep(rand_sleep / 100)
              
        else:  # if button is pressed again
            check_winner(pressed_color)
            return            
                   
def changeLedState():
    global pressed, not_green
    pressed = not pressed
    not_green = not not_green
    print ("button pressed >>>")
          
        
def destroy():
    LED.close()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting ... ')
    
    try:
        BUTTON.when_pressed = changeLedState
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
