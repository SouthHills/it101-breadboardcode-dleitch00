import subprocess
from gpiozero import LED as LEDClass # Alias


LED = LEDClass(17)  # define led
LED2 = LEDClass(18)

def is_internet_connected():
    try:
    # Run the ping command with a timeout of 2 seconds and count 1 packet
        subprocess.check_output(['ping', '-c', '1', '-W', '2', 'www.google.com'])
        return True
    except subprocess.CalledProcessError:
        return False
    
def loop():
    global LED, LED2
    while True:
        if is_internet_connected():
            LED.on()
            LED2.off()
        else:
            LED2.on()
            LED.off()    
        
def destroy():
    global LED, LED2
    # Release resources
    LED.close()
    LED2.close()
    
if __name__ == '__main__':   # Program entrance
    print ('Program is starting... ')
    
    try:
        loop()
            
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
            