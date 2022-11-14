import spidev
import RPi_I2C_driver
import RPi.GPIO as GPIO
import time

led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1350000

def analog_read(channel):
    r = spi.xfer2([1, (8+channel) << 4,0])
    adc_out = ((r[1]&3)<<8)+r[2]
    return adc_out

mylcd = RPi_I2C_driver.lcd()

while True:
        reading = analog_read(1)
        voltage = reading * 3.3/1024
        print('reading={0:0.1f}  voltage={1:0.1f}'.format(reading, voltage))
        lcd.lcd_display_string("reading={0:0.1f}".format(reading), 1)
        lcd.lcd_display_string("voltage={0:0.1f}".format(voltage), 1)
        time.sleep(1)