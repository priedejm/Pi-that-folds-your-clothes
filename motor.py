import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT) #right motor
gpio.setup(22, gpio.OUT) #right motor
gpio.setup(23, gpio.OUT) #left motor
gpio.setup(24, gpio.OUT) #left motor
gpio.setup(6, gpio.OUT) #middle motor
gpio.setup(13, gpio.OUT) #middle motor


# def forward(tf):
#     init()
#     gpio.output(17, True)
#     gpio.output(22, False)
#     gpio.output(23, True)
#     gpio.output(24, False)
#     time.sleep(tf)
 
#     gpio.cleanup()

# def reverse(tf):
#     init()
#     gpio.output(17,False)
#     gpio.output(22, True)
#     gpio.output(23, False)
#     gpio.output(24, True)
#     time.sleep(tf)
#     gpio.cleanup()

# for i in range(0,2):
#     print ("forward")
#     forward(2)
#     time.sleep(1)
#     print ("backward")
#     reverse(2)
#     time.sleep(1)
#     gpio.cleanup()
# GPIO.cleanup()

# def rightMotor():
#     #forward
#     gpio.output(17, True)
#     gpio.output(22, False)
#     time.sleep(.2)
#     #reverse
#     gpio.output(17,False)
#     gpio.output(22, True)
#     time.sleep(.2)
   


# def leftMotor():
#     #forward
#     gpio.output(23, True)
#     gpio.output(24, False)
#     time.sleep(.2)
#     #reverse
#     gpio.output(23,False)
#     gpio.output(24, True)
#     time.sleep(.2)
def middleMotor():
    #forward
    gpio.output(6, True)
    gpio.output(13, False)
    time.sleep(1)
    #reverse
    gpio.output(6,False)
    gpio.output(13, True)
    time.sleep(1)


    gpio.cleanup()