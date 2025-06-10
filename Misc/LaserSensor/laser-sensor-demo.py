import RPi.GPIO as GPIO
import time

receiverPin: int = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    
    # Setup reciever
    GPIO.setup(receiverPin, GPIO.IN)
    print (f'using pin {receiverPin}')

def loop():
    while True:
        inputs = []
        counter = 3
        while counter > 0:
            counter -= 1
            inputs.append(True if GPIO.input(receiverPin) == 0 else False)
        
        inputs.sort()
        print(inputs[1])
        time.sleep(0.5)

def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

