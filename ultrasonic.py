import RPi.GPIO as gpio
import time
trig=
echo=
oneval=0
secondval=0
differnce=0
distance=0
cota=0
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)
while(1):
    sleep(2)
    gpio.output(trig,gpio.HIGH)
    sleep(0.00001)
    gpio.output(trig,gpio.LOW)
    while(gpio.input(echo)==0)
        oneval=time.time()
    while(gpio.input(echo)==1)
        secondval=time.time()
    difference=secondval-firstval 
    distance=difference*17150
    print("distance ",distance)
gpio.cleanup()
