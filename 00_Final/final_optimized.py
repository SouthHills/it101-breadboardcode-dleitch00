import RPi.GPIO as GPIO
from lcd_display import LCDDisplayWrapper as LCDDisplay
from time import sleep
from datetime import datetime
from gpiozero import LED as LEDClass # Alias

receiverPin_away: int = 21
receiverPin_home: int = 22
LED_HOME = LEDClass(19)
LED_AWAY = LEDClass(26)
lcd = LCDDisplay()


def setup():
    GPIO.setmode(GPIO.BCM)
    lcd.display_message(f'Home: 0  0 :Away', row=2)
    
    # Setup reciever
    GPIO.setup(receiverPin_away, GPIO.IN)
    print (f'using pin {receiverPin_away}')
    
    GPIO.setup(receiverPin_home, GPIO.IN)
    print (f'using pin {receiverPin_home}')
    # sleep(5)
    # todo set up loop
    
def goal():
    pass



def loop():
    global LED_HOME, LED_AWAY
    clock = 60
    home_score = 0
    away_score = 0
    while True:
        if clock == 0:
            lcd.clear()
            lcd.display_message('   Game Over!', row=1)
            lcd.display_message(f'Home: {home_score}  {away_score} :Away', row=2)
            break

        inputs_away = []
        counter = 3
        while counter > 0:
            counter -= 1
            inputs_away.append(True if GPIO.input(receiverPin_away) == 0 else False)
            
          
        inputs_away.sort()
        if inputs_away[1] == True:
            home_score += 1
            print(f'The home team scores! {home_score}')
            LED_HOME.on()
            sleep(1)
            LED_HOME.off()
            print('Play!')
            lcd.display_message(f'Home: {home_score}  {away_score} :Away', row=2)
        
        
        inputs_home = []
        counter = 3
        while counter > 0:
            counter -= 1
            inputs_home.append(True if GPIO.input(receiverPin_home) == 0 else False)
            # inputs_home.append(False)
           
        inputs_home.sort()
        print(inputs_home)
        if inputs_home[1] == True:
            away_score += 1
            print(f'The away team scores! {away_score}')
            LED_AWAY.on()
            sleep(1)
            LED_AWAY.off()
            print('Play!')
            lcd.display_message(f'Home: {home_score}  {away_score} :Away', row=2)
            
        clock -= .1
        clock = round(clock, 2)
        lcd.display_message(f'Time: {str(clock)}', row=1)
        
        sleep(.05)




def destroy():
    GPIO.cleanup()  

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()