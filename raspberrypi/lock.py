import RPi.GPIO as GPIO
import time

def blink1():
        #GPIO.output(pin,GPIO.HIGH)
        #GPIO.output(21,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
        GPIO.output(19,GPIO.LOW)
        GPIO.output(31,GPIO.LOW)
        #time.sleep(2)
        return
                    
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(37, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

for i in range(0,1):
       blink1()        
GPIO.cleanup() 
