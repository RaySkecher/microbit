from microbit import *

uart.init(baudrate=115200)

while True:
    if uart.any():
        try:
            msg = uart.read()
            if msg:
                msg = msg.decode('utf-8').strip()
                if msg == "UP":
                    display.show(Image.ARROW_N)
                elif msg == "DOWN":
                    display.show(Image.ARROW_S)
                elif msg == "LEFT":
                    display.show(Image.ARROW_W)
                elif msg == "RIGHT":
                    display.show(Image.ARROW_E)
        except:
            display.scroll("ERR")