from microbit import *

uart.init(baudrate=115200)

while True:
    if uart.any():
        data = uart.read()
        if data:
            uart.write(data) 