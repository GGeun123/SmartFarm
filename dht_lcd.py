import Adafruit_DHT
import RPi_I2C_driver
import time

sensor = Adafruit_DHT.DHT11

pin = 27

mylcd = RPi_I2C_driver.lcd()

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        mylcd.lcd_display_string("Temp={0:0.1f} C".format(temperature), 1)
        mylcd.lcd_display_string("Humidity={0:0.1f}%".format(humidity), 2)
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1);