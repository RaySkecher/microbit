# fake_fpga_cornell.py
import serial
import time

# Change to your micro:bit COM port
ser = serial.Serial("COM5", 115200)

WIDTH = 64
HEIGHT = 64

try:
    while True:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                # Simulate Cornell Box Walls
                if x < WIDTH // 3:
                    r, g, b = 255, 0, 0  # Left red wall
                elif x > 2 * WIDTH // 3:
                    r, g, b = 0, 255, 0  # Right green wall
                else:
                    # Middle zone — light gradient
                    r = g = b = min(255, int(255 * (1 - abs((y - HEIGHT//2) / (HEIGHT//2)))))
                
                # Send as CSV
                pixel = f"{x},{y},{r},{g},{b}\n"
                ser.write(pixel.encode('utf-8'))
                time.sleep(0.0005)  # small delay to avoid flooding
        print("Frame sent!")
        time.sleep(0.5)
except KeyboardInterrupt:
    ser.close()

