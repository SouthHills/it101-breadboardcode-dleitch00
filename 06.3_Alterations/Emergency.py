
from gpiozero import TonalBuzzer, Button, PWMLED
import time
from signal import pause

BUZZER = TonalBuzzer(17)
BUTTON = Button(18)
HIGH_TONE = 600 # The max is 880 but that hurts my ears
LOW_TONE = 220
LED = PWMLED(23)
    
def setup():
    # Setup events for when the button is pressed and released
    BUTTON.when_pressed = alertor
    BUTTON.when_released = stop_alertor

def alertor():
    print ('alertor turned on >>> ')
    led_diff = HIGH_TONE - LOW_TONE
    global LED
    while True:  
        # Linear
        for x in range(LOW_TONE, HIGH_TONE):
            BUZZER.play(x)
            LED.value = (x - LOW_TONE) / led_diff
            time.sleep(0.002)
            
            if not BUTTON.is_pressed:
                return  
            
        for x in range(HIGH_TONE, LOW_TONE, -1):
            BUZZER.play(x)
            LED.value = (x - LOW_TONE) / led_diff
            time.sleep(0.002)
            
            if not BUTTON.is_pressed:
                return 
        
def stop_alertor():
    global LED
    LED.off()
    BUZZER.stop()
    print ('alertor turned off <<<')

def destroy():
    BUZZER.close()
    BUTTON.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
