import pyodbc
import time
import RPi.GPIO as GPIO
pin=18
GPIO.setmode(GPIO.BCM) 
GPIO.setup(pin,GPIO.OUT)
p=GPIO.PWM(pin,50p.start(0)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
pwm = GPIO.PWM(24, 100) # pin 14 at 100 Hz
value = 0
pwm.start(value) # Start at 0
while 1:
sql = "SELECT * FROM status where id =팀 번호"
cursor.execute(sql)
rows = cursor.fetchone()
time.sleep(1)
if(rows[0] == 'open’):
p.ChangeDutyCycle(9.5) 
print ("180도")
time.sleep(0.5)
if(rows[0] == 'close'):
p.ChangeDutyCycle(2.5) 
print ("0도")
time.sleep(0.5)
light = rows[1]
value = int(light)
pwm.ChangeDutyCycle(value)