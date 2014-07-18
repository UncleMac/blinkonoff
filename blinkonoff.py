import RPi.GPIO as GPIO 
import time


def Blink():
    for i in range(0,20):
        GPIO.output(7, True)
        time.sleep(.1)
        GPIO.output(7, False)
        time.sleep(.1)
    print "blink"
    GPIO.cleanup()

def On():
    GPIO.output(7, True)
    print "on"
    GPIO.cleanup()
def Off():
    GPIO.output(7, False)
    print "off"
    GPIO.cleanup()

while True:

    GPIO.setwarnings(False)    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)


    choice = raw_input("blink, on or off: ")
    
    if choice == "blink":
        Blink()
    if choice == "on":
        On()
    if choice == "off":
        Off()
    if choice == "quit":
        break

print "exiting"
Off()



        
