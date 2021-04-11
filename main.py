from machine import Pin, ADC
import utime

led = Pin(25, Pin.OUT)
adc = ADC(28)

k = 3.3 / (65535)

while True:
    volt = adc.read_u16() * k

    print(volt)
    led.toggle()
    utime.sleep(0.1)