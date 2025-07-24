import pygame
import serial

WIDTH, HEIGHT = 128, 128
ser = serial.Serial("COM5", 115200)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ser.in_waiting:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            print("Received:", line)

            x, y, r, g, b = map(int, line.split(","))
            if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                screen.set_at((x, y), (r, g, b))
        except Exception as e:
            print("Parse error:", e)

    pygame.display.flip()

pygame.quit()