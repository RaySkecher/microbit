import serial
import keyboard
import time

# Change this to your micro:bit's port!
ser = serial.Serial("COM5", baudrate=115200)

print("Press arrow keys (Esc to quit)...")

try:
    while True:
        if keyboard.is_pressed("esc"):
            print("Exiting...")
            break

        if keyboard.is_pressed("up"):
            ser.write(b"UP\n")
            print("Sent UP")
            time.sleep(0.2)  # debounce

        if keyboard.is_pressed("down"):
            ser.write(b"DOWN\n")
            print("Sent DOWN")
            time.sleep(0.2)

        if keyboard.is_pressed("left"):
            ser.write(b"LEFT\n")
            print("Sent LEFT")
            time.sleep(0.2)

        if keyboard.is_pressed("right"):
            ser.write(b"RIGHT\n")
            print("Sent RIGHT")
            time.sleep(0.2)

except KeyboardInterrupt:
    pass
finally:
    ser.close()