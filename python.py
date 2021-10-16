#RED=15
#YELLOW=16
#GREEN=18
import sys
import time
import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(15, GPIO.OUT) ## Setup GPIO Pin 15 to OUT
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 16 to OUT
GPIO.setup(18, GPIO.OUT) ## Setup GPIO Pin 18 to OUT
print(len(sys.argv))
def Red_led():
        print("Turning RED LED ON")
        GPIO.output(15,True)
        time.sleep(3)
        print("Turning RED LED OFF")
        GPIO.output(15,False)
        
def Yellow_led():
        print("Turning YELLOW LED ON")
        GPIO.output(16,True)
        time.sleep(3)
        print("Turning YELLOW LED OFF")
        GPIO.output(16,False)
def Green_led():
        print("Turning GREEN LED ON")
        GPIO.output(18,True)
        time.sleep(3)
        print("Turning GREEN LED OFF")
        GPIO.output(18,False)
        
def main():
    function=sys.argv[1]
    if(function=="Red_led"):
        Red_led()
    if(function=="Yellow_led"):
        Yellow_led()
    if(function=="Green_led"):
        Green_led()
        
if (__name__=="__main__"):
    main()

