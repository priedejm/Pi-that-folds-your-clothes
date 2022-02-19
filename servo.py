import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)
#pwm.ChangeDutyCycle(1) #full left
#pwm.ChangeDutyCycle(12) #full right
#pwm.ChangeDutyCycle(7.5) #middle

pwm.start(7.5)

for i in range(0,5):
    desiredPosition=input("where do you want the servo? 1-12")
    DC = int(desiredPosition)
    pwm.ChangeDutyCycle(DC)
    
pwm.stop() #stop the servo
GPIO.cleanup()