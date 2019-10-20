import RPi.GPIO as gpio
import time
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

oneval=0
secondval=0
distance=0
difference=0

r_fpwm=32
l_fpwm=38
r_rpwm=36
l_rpwm=40

r_fen=31
r_ren=33
l_fen=35
l_ren=37

servo1=11
servo2=13

trig=16
echo=18

gpio.setup(r_fen,gpio.OUT)
gpio.setup(r_ren,gpio.OUT)
gpio.setup(l_fen,gpio.OUT)
gpio.setup(l_ren,gpio.OUT)

gpio.setup(r_fpwm,gpio.OUT)     # right motor fpwm
gpio.setup(l_fpwm,gpio.OUT)     # left motor fpwm
gpio.setup(r_rpwm,gpio.OUT)     # right motor rpwm
gpio.setup(l_rpwm,gpio.OUT)     # left motor rpwm

gpio.setup(servo1,gpio.OUT)     # input for servo1
gpio.setup(servo2,gpio.OUT)     # input for servo2

gpio.setup(echo,gpio.IN)        # echo pin used to receive ultrasound
gpio.setup(trig,gpio.OUT)       # trigger pin responsible for ultrasound

gpio.output(r_fen,gpio.HIGH)
gpio.output(r_ren,gpio.HIGH)
gpio.output(r_fen,gpio.HIGH)
gpio.output(r_fen,gpio.HIGH)

def forward():
    gpio.output(r_fpwm,gpio.HIGH)
    gpio.output(l_fpwm,gpio.HIGH)
    gpio.output(r_rpwm,gpio.LOW)
    gpio.output(l_rpwm,gpio.LOW)
def backward():
    gpio.output(r_fpwm,gpio.LOW)
    gpio.output(l_fpwm,gpio.LOW)
    gpio.output(r_rpwm,gpio.HIGH)
    gpio.output(l_rpwm,gpio.HIGH)
def right():
    gpio.output(r_fpwm,gpio.LOW)
    gpio.output(l_fpwm,gpio.HIGH)
    gpio.output(r_rpwm,gpio.HIGH)
    gpio.output(l_rpwm,gpio.LOW)
def left():
    gpio.output(r_fpwm,gpio.HIGH)
    gpio.output(l_fpwm,gpio.LOW)
    gpio.output(r_rpwm,gpio.LOW)
    gpio.output(l_rpwm,gpio.HIGH)
def stop():
    gpio.output(r_fpwm,gpio.LOW)
    gpio.output(l_fpwm,gpio.LOW)
    gpio.output(r_rpwm,gpio.LOW)
    gpio.output(l_rpwm,gpio.LOW)
def arm():
    pwm1=gpio.PWM(servo1,50)
    pwm1.start(2.5)
    pwm2=gpio.PWM(servo2,50)
    pwm2.start(2.5)
    pwm1.ChangeDutyCycle(7.5)
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(1)
    pwm1.ChangeDutyCycle(2.5)
    pwm2.ChangeDutyCycle(2.5)
    time.sleep(1)
print("intializing the program")
while(1):
    gpio.output(trig,gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(trig,gpio.LOW)
    while(gpio.input(echo)==0):
        oneval=time.time()
    while(gpio.input(echo)==1):
        secondval=time.time()
    difference=secondval-oneval
    distance=difference*17150
    if (distance<10) :
        stop()
        print('garbage detected !!!')
        time.sleep(2)
        forward()
        time.sleep(0.5)
        arm()
    else:
        forward()
gpio.cleanup()
