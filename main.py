from ili934xnew import ILI9341, color565
from machine import Pin, ADC, SPI
import utime
import glcdfont
import tt14
from gfx import GFX
import urandom
from scope import Scope

BACKGROUND = color565(0, 0, 60)

led = Pin(25, Pin.OUT)
adc = ADC(28)

power = Pin(15, Pin.OUT)
power.value(0)

spi = SPI(
    0, 
    baudrate=40000000,
    polarity=0, 
    phase=0, 
    sck=Pin(18), 
    mosi=Pin(19),
    miso=Pin(16)
    )

tft = ILI9341(
    spi,
    cs=Pin(12),
    rst=Pin(13),
    dc=Pin(14),
    w=320,
    h=240,
    r=3
)

def fast_hline(x, y, width, color):
    tft.fill_rectangle(x, y, width, 1, color)

def fast_vline(x, y, height, color):
    tft.fill_rectangle(x, y, 1, height, color)

def draw_circle(xpos0, ypos0, rad, col=color565(255, 255, 255)):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        tft.pixel(xpos0 + x, ypos0 + y, col)
        tft.pixel(xpos0 + y, ypos0 + x, col)
        tft.pixel(xpos0 - y, ypos0 + x, col)
        tft.pixel(xpos0 - x, ypos0 + y, col)
        tft.pixel(xpos0 - x, ypos0 - y, col)
        tft.pixel(xpos0 - y, ypos0 - x, col)
        tft.pixel(xpos0 + y, ypos0 - x, col)
        tft.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)

gfx = GFX(240, 320, tft.pixel, hline=fast_hline, vline=fast_vline)


k = 3.3 / (65535)

power.value(1)
led.value(1)
tft.erase()
# y ticks


tft.fill_rectangle(0, 0, tft.width, tft.height, BACKGROUND)
v = 0
for i in range(7):
    v += 0.5
    tft.set_pos(0,198 - 32*i)
    tft.print(str(v))

tft.set_pos(0,0)
tft.set_font(tt14)
# tft.print('hola bola')
scope = Scope(tft, gfx)
# gfx.line(0, 0, 319, 239, color565(255, 0, 0))
# gfx.circle(60, 120, 50, color565(255, 255, 0))
# draw_circle(180, 120, 50, color565(0, 255, 0))
scope.draw_axis()
# for i in range(50):
#     gfx.line(
#         urandom.randint(0, 320),
#         urandom.randint(0, 240),
#         urandom.randint(0, 320),
#         urandom.randint(0, 240),
#         color565(255, 255, 0)
#     )

# utime.sleep(2)
# power.value(0)
led.value(0)

volt = adc.read_u16() * k
y = int(230 - volt / 3.3 * 230)    
last_y = y

# tft.scroll(30)
x = 32

while True:
    volt = adc.read_u16() * k
    y = int(230 - volt / 3.3 * 209)
    # print(y)
    # tft.pixel(x, y, color565(255,255, 0))
    gfx.line(x - 1, last_y, x, y, color565(255, 255, 0))
    x += 1
    last_y = y
    # fast_hline(0, y, 320, color565(255, 255, 0))
    # if y != last_y:
    #     tft.fill_rectangle(160, last_y, 50, 1, BACKGROUND)
    #     tft.fill_rectangle(160, y, 50, 1, color565(255, 255, 0))
    #     last_y = y
    if x >= 320:
        tft.fill_rectangle(31, 0, 289, 229, BACKGROUND)
        x = 32
    utime.sleep(0.05)
    led.toggle()