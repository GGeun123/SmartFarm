def read_spi_adc(adcChannel):
       adcValue=0
       buff =spi.xfer2([1,(8+adcChannel)<<4,0])
       adcValue = ((buff[1]&3)<<8)+buff[2]
       return adcValue

adcValue=read_spi_adc(0)
print(adcValue)