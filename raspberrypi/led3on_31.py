import RPi.GPIO as GPIO
import time

def blink1():
 
        GPIO.output(31,GPIO.HIGH)
        time.sleep(1)
        return
                    
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(31, GPIO.OUT)

for i in range(0,5):
       blink1()        
GPIO.cleanup() 
