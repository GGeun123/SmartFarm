import spidev
import RPi_I2C_driver
import time

spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=50000

def analog_read(channel):
    r = spi.xfef2([1, (8 + channel)<<4,0])
    adc_value = ((r[1]&3)<<8) + r[2]
    return adc_value

mylcd = RPi_I2C_driver.lcd()

while True:
        reading = analog_read(0)
        print(now.strftime('%Y-%m-%d %H:%M:%S') + 'Reading=%d' % (reading))
        mylcd.lcd_display_string("Water={0:0.1f}%".format(humidity), 1)
        time.sleep(1)
       


    # if humidity is not None and temperature is not None:
    #     print('Water={1:0.1f}%'.format(temperature, humidity))
    #     mylcd.lcd_display_string("Water={0:0.1f}%".format(humidity), 1)
    # else:
    #     print('Failed to get reading. Try again!')
    # time.sleep(1);