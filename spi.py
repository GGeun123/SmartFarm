import spidev
import time


spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=50000

def analog_read(channel):
    r = spi.xfef2([1, (8 + channel)<<4,0])
    adc_value = ((r[1]&3)<<8) + r[2]
    return adc_value

try:
    while True:
        now = time
        reading = analog_read(0)
        print(now.strftime('%Y-%m-%d %H:%M:%S') + 'Reading=%d' % (reading))
        time.sleep(5)

except KeyboardInterrupt
        print('User stopped.')
finally:
    spi.close()