import serial

# Adjust this based on your system — COM3 is just an example
ser = serial.Serial('COM3', 115200)

while True:
    key = input("Type a key to send to micro:bit: ")
    ser.write(key.encode())