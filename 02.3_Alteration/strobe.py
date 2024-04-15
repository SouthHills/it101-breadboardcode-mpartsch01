from gpiozero import LED as LEDClass, Button
from signal import pause
import time

LED = LEDClass(17)  # define ledPin
BUTTON = Button(18)  # define buttonPin
is_flashing = False #bool

def changeLedState():
    global is_flashing
    is_flashing = not is_flashing
    if is_flashing:
        print ("led strobing >>>")
    else:
        print ("led not strobing <<<")
    

def destroy():
    global LED, BUTTON
    # Release resources
    LED.close()
    BUTTON.close()

            
def loop():
    global LED, is_flashing
    while True:
        if is_flashing:  # if button is pressed
            LED.on()  # turn on led
            print ("led turned on >>>") # print information on terminal
            time.sleep(0.1)
            LED.off()
            print ("led turned off <<<")
            time.sleep(0.1)

if __name__ == "__main__":     # Program entrance
    print ("Program is starting...")
    try:
        # If the button gets pressed, call the function
        # This is an event
        BUTTON.when_pressed = changeLedState
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

