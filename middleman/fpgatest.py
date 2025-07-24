# fake_fpga.py
import serial
import time
import random

# Replace with your micro:bit's COM port
ser = serial.Serial("COM5", 115200)

width, height = 64, 64  # Simulate small cornell box render

try:
    while True:
        for y in range(height):
            for x in range(width):
                r = (x * 4) % 256
                g = (y * 4) % 256
                b = random.randint(0, 100)
                line = f"{x},{y},{r},{g},{b}\n"
                ser.write(line.encode('utf-8'))
                time.sleep(0.0005)  # Tune this to avoid overloading micro:bit
        print("Frame sent")
        time.sleep(1)  # simulate frame interval
except KeyboardInterrupt:
    ser.close()