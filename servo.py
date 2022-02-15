from gpiozero import Servo
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory
#comment out factory and take it out the servo to see it work worse.
factory = PiGPIOFactory()
#pin_factory=factory

servo = Servo(12, pin_factory=factory)

print("Start in the middle")
servo.mid()
sleep(5)
servo.min()
sleep(5)
print("Go to Max")
servo.max()
sleep(5)
print("And back to middle")
servo.mid()
sleep(5)
servo.value = None;