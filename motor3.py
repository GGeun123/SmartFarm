import time
import RPi.GPIO as GPIO

print("AkibaTV Servo Motor Test")

# White : Pin 12 : 18(PWM)
# RED   : Pin 2  : 5v
# Black : Pin 14 : GND
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

phz = GPIO.PWM(18, 50) # 18Pin, 50hz
phz.start(1)

# 루프가 3번을 반복하면서 모터를 돌리게끔 설정
for i in range(0, 3):
    print("10");
    phz.ChangeDutyCycle(10)
    time.sleep(2)

    print("20.5");
    phz.ChangeDutyCycle(20.5)
    time.sleep(2)

    print("5");
    phz.ChangeDutyCycle(5)
    time.sleep(2)

    print("30");
    phz.ChangeDutyCycle(30)
    time.sleep(2)

    print("7.5");
    phz.ChangeDutyCycle(7.5)
    time.sleep(2)

print("AkibaTV Servo Motor End")
GPIO.cleanup()