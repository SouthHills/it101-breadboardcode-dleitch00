
from gpiozero import LED
from time import sleep

LED_red = LED(17)
LED_green = LED(22)
LED_yellow = LED(18)

def loop():
    global LED
    while True:
        LED_red.on()
        sleep(5)
        LED_red.off()
        LED_green.on()
        sleep(7)
        LED_green.off()
        LED_yellow.on()
        sleep(2)
        LED_yellow.off()

def destroy():
    global LED
    # Release resources
    LED_red.close()
    LED_green.close()
    LED_yellow.close()

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
