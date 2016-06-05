import RPi.GPIO as GPIO
import time

def blink1():
        #GPIO.output(pin,GPIO.HIGH)
        #GPIO.output(21,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
       
        return
                    
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(35, GPIO.OUT)

for i in range(0,10):
       blink1()        
GPIO.cleanup() 
