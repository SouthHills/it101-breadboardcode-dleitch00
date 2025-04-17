from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define led
LED2 = LEDClass(12)

def loop():
    global LED
    while True:
        LED.on() 
        LED2.off()
        print ("led turned on >>>") # print information on terminal
        time.sleep(1)
        LED.off()
        LED2.on()
        print ("led turned off <<<")
        time.sleep(1)
        
def destroy():
    global LED
    # Release resources
    LED.close()

if __name__ == "__main__":    # Program start point
    print("Program is starting ... \n")
    print(f"Using pin {LED.pin}")
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
