import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# GPIO Servo모터 제어

servo_pin = 18

GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50) # 50Hz( 서보모터 PWM 동작을 위한 주파수 )
servo.start(0) # 서보모터의 0도 위치( 0.6ms ) 이동: 값 3.0은 pwm 주기인 20ms 의 3% 를 의미

servo_min_duty = 3
servo_max_duty = 12

def set_servo_degree(degree):

    if degree > 180:
        degree = 180
    elif degree < 0:
        degree = 0

    duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180.0)
    servo.ChangeDutyCycle(duty)

### 이부분은 아두이노 코딩의 loop()에 해당합니다
try:                                    # 이 try 안의 구문을 먼저 수행하고
    while True:                         # 무한루프 시작: 아두이노의 loop()와 같음
        set_servo_degree(0)             # 서보모터의 각도를 0도로
        sleep(1)                        # 1초간 대기
        set_servo_degree(90)
        sleep(1)
        set_servo_degree(120)
        sleep(1)
        set_servo_degree(180)
        sleep(1)

### 이부분은 반드시 추가해주셔야 합니다.
finally:                                # try 구문이 종료되면
    GPIO.cleanup()                      # GPIO 핀들을 초기화