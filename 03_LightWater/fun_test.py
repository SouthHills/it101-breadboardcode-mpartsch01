# Due to using special pins, the higher abstracted GPIOZero library cannot be used.
# The RPi.GPIO library can be used instead.
import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():    
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)   # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led

def loop():
    while True:
        for pin in ledPins[::-1]:       # make led(on) move from right to left
            GPIO.output(pin, GPIO.HIGH)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        for pin in ledPins:     # make led(on) move from left to right
            GPIO.output(pin, GPIO.HIGH)  
            time.sleep(0.1)
            GPIO.output(pin, GPIO.LOW)
        
is_flashing = False #bool

def looop(): #trying to make lights flash for fun?
    global LED, is_flashing
    while True:
        if is_flashing:  #flash the lights after going through?
            for pin in ledPins:
                ledPins  # turn on led
                print ("led turned on >>>") # print information on terminal
                time.sleep(2)
                LED.off()
                print ("led turned off <<<")
                time.sleep(2)


def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()

