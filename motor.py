import RPi.GPIO as GPIO
import time


#gpio.setmode(gpio.BCM)
#gpio.setup(17, gpio.OUT) #left motor
#gpio.setup(27, gpio.OUT) #left motor
#gpio.setup(23, gpio.OUT) #right motor
#gpio.setup(24, gpio.OUT) #right motor
#gpio.setup(6, gpio.OUT) #middle motor
#gpio.setup(5, gpio.OUT) #middle motor
#
#gpio.output(6, True)
#gpio.output(5, False)
#time.sleep(1)
#gpio.output(6,False)
#gpio.output(5, True)
#time.sleep(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT) #pwm
GPIO.setup(5, GPIO.OUT) #dir
GPIO.output(6, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
time.sleep(1)
GPIO.output(6, GPIO.LOW)
time.sleep(1)
GPIO.output(5, GPIO.LOW)
GPIO.cleanup()


#def moveAllMotors():
#    gpio.setmode(gpio.BCM)
#    gpio.setup(17, gpio.OUT) #left motor
#    gpio.setup(27, gpio.OUT) #left motor
#    gpio.setup(23, gpio.OUT) #right motor
#    gpio.setup(24, gpio.OUT) #right motor
#    gpio.setup(6, gpio.OUT) #middle motor
#    gpio.setup(13, gpio.OUT) #middle motor
#    #left motors:
#    gpio.output(17, True)
#    gpio.output(27, False)
#    time.sleep(.7)
#    gpio.output(17,False)
#    gpio.output(27, True)
#    time.sleep(.7)
#
#    #right motors:
#    gpio.output(23, True)
#    gpio.output(24, False)
#    time.sleep(.7)
#    gpio.output(23,False)
#    gpio.output(24, True)
#    time.sleep(.7)
#
#    #Middle motor:
#    gpio.output(6, True)
#    gpio.output(13, False)
#    time.sleep(.7)
#    gpio.output(6,False)
#    gpio.output(13, True)
#    time.sleep(.7)
#    gpio.cleanup()
#
#
#def forwardAll():
#    gpio.output(17, True)
#    gpio.output(27, False)
#    gpio.output(23, True)
#    gpio.output(24, False)
#    gpio.output(6, True)
#    gpio.output(13, False)
#    time.sleep(.7)
#    gpio.cleanup()
#
#def reverseAll():
#    gpio.output(17,False)
#    gpio.output(27, True)
#    gpio.output(23,False)
#    gpio.output(24, True)
#    gpio.output(6,False)
#    gpio.output(13, True)
#    time.sleep(.7)
#    gpio.cleanup()
#
## for i in range(0,2):
##     print ("forward")
##     forward(2)
##     time.sleep(1)
##     print ("backward")
##     reverse(2)
##     time.sleep(1)
##     gpio.cleanup()
## GPIO.cleanup()
#
#def rightMotor():
#    gpio.output(23, True)
#    gpio.output(24, False)
#    time.sleep(.7)
#    gpio.output(23,False)
#    gpio.output(24, True)
#    time.sleep(.7)
#    gpio.cleanup()
#   
#
#
#def leftMotor():
#    gpio.output(17, True)
#    gpio.output(27, False)
#    time.sleep(.7)
#    gpio.output(17,False)
#    gpio.output(27, True)
#    time.sleep(.7)
#    gpio.cleanup()
#
#def middleMotor():
#    gpio.output(6, True)
#    gpio.output(13, False)
#    time.sleep(.7)
#    gpio.output(6,False)
#    gpio.output(13, True)
#    time.sleep(.7)
#    gpio.cleanup()
#
#
##  gpio.cleanup()
