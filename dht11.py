import Adafruit_DHT

sensor = Adafruit_DHT.DHT11

pin = 18

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)   # 센서 객체에서 센서 값(ㅇ노도, 습도) 읽기

      
if humidity is not None and temperature is not None:   #습도 및 온도 값이 모두 제대로 읽혔다면 
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))  # 온도, 습도 순으로 표시
else:                                                  # 에러가 생겼다면 
    print('Failed to get reading. Try again!')        #  에러 표시
