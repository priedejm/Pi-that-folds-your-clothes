import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)

def forward(tf):
    init()
    gpio.output(17, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(17, False)
    time.sleep(tf)
    gpio.cleanup()

print ("forward")
forward(4)
print ("backward")
reverse(2)

