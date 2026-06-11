from machine import Pin, PWM
import time

trig = Pin(3,Pin.OUT)
echo = Pin(2, Pin.IN)

servo = PWM(Pin(15))
servo.freq(50)
 
Buzzer = Pin(16, Pin.OUT)

def set_servo_angle(angle):
    duty = int((angle / 180)* 6000 + 2000)
    servo.duty_u16(duty)

def get_distance():

    trig.low()
    time.sleep_us(2)

    trig.high()
    time.sleep_us(10)
    trig.low()

while echo.value() == 0:
    pluse_start = time.ticks_us()

while echo_value() == 1:
    pluse_end = time.ticks_us()

    pluse_time = pluse_end - pluse_start

    distance = (pluse_time * 0.0343) / 2
    return distance

while True:
    distance = get_distance()
    print("Distance ="round(distance,2),"cm")

if distance < 50:
    set_servo_angle (90)
    buzzer.value(1)
    time_sleep(0.2)
    buzzer.value(0)
    time_sleep(0.2)
    else:
        set_servo_angle(0)
        buzzer.value(0)
    
    time.sleep(1)
