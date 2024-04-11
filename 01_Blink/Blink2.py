from gpiozero import LED as LEDClass # Alias
import time

LED = LEDClass(17)  # define led
LED2 = LEDClass(22)

def loop():
    global LED
    while True:
        LED.on() 
        LED2.off()
        print ("blue led turned on, green led turned on >>>") # print information on terminal
        time.sleep(1)
        LED.off()
        LED2.on()
        print ("blue led turned off, green led turned on <<<")
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
        loop(LED2)
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
