
from multiprocessing import process
from gpiozero import Button
from time import sleep
from signal import pause
import subprocess

BUTTON1 = Button(18)  # define buttonPin
BUTTON2 = Button(23)  # define buttonPin
firefox_toggle = False
chrome_toggle = False
process1 = process
process2 = process


def toggle_firefox():
    global BUTTON1, firefox_toggle, process1
    
    firefox_toggle = not firefox_toggle
    if firefox_toggle:
        print('Opening firefox')
        process1 = subprocess.Popen(["firefox"])
    else:
        print('Closing firefox')
        process1.terminate()
        
   
def toggle_chrome():
    global BUTTON2, chrome_toggle, process2
    
    chrome_toggle = not chrome_toggle
    if chrome_toggle:
        print('Opening chrome')
        process2 = subprocess.Popen(["chromium"])
    else:
        print('Closing chrome')
        process2.terminate()


def destroy():
    global BUTTON
    # Release resources  
    BUTTON1.close()
    BUTTON2.close()

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        BUTTON1.when_pressed = toggle_firefox
        BUTTON2.when_pressed = toggle_chrome
        pause()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()