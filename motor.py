import RPi.GPIO as GPIO #RPi.GPIO 라이브러리를 GPIO로 사용
import time  #time 라이브러리의 sleep함수 사용

servo_pin=18

GPIO.setmode(GPIO.BCM)          #gpio 모드 세팅
GPIO.setup(servo_pin,GPIO.OUT)
        #모터출력
pwm = GPIO.PWM(servo_pin, 50)              #펄스폭변조 세팅 핀,주파수
pwm.start(3.0)

time.sleep(2.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
GPIO.cleanup()