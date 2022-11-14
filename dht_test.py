import spidev, time
import RPi.GPIO as GPIO


spi=spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=50000
h,t = dht.read_retry(dht.DHT11,4)
