from ili934xnew import color565


WHITE = color565(255, 255, 255)
RED = color565(255, 0, 0)
GREEN = color565(0, 255, 0)
BLUE = color565(0, 0, 255)
YELLOW = color565(255, 255, 0)
CYAN = color565(0, 255, 255)
MAGENTA = color565(255, 0, 255)
GRAY = color565(90, 90, 90)

class Scope():
    def __init__(self, tft, gfx):
        self.tft = tft
        self.gfx = gfx

    def draw_axis(self):
        # x axis
        # self.gfx.line(0, 230, 320, 230, color565(255, 255, 255))
        self.tft.fill_rectangle(0, 230, 320, 2, GRAY)
        # y axis
        # self.gfx.line(10, 5, 10, 240, color565(255, 255, 255))
        self.tft.fill_rectangle(30, 0, 2, 230, GRAY)
        # x ticks
        for i in range(9):
            # self.gfx.line(10 + 31*i, 0, 10 + 31*i, 235, color565(255, 255, 255))  
            self.tft.fill_rectangle(30 + 37*i, 230, 2, 5, GRAY)

        # y ticks
        v = 0.0
        for i in range(8):
            # self.gfx.line(10 + 31*i, 0, 10 + 31*i, 235, color565(255, 255, 255))  
            self.tft.fill_rectangle(25, 230 - 32*i, 5, 2, GRAY)
            v += 0.5
            # self.tft.set_pos(0,230 - 37*i)
            # self.tft.print(str(v))



    def draw_level(self, h):
        pass
