from gpiozero import Servo
from time import sleep

servo = Servo(12)

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