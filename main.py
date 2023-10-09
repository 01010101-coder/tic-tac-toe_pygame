import pygame
from classes import *

pygame.init()

screen = pygame.display.set_mode([500, 500])

squares = []

x = 100
y = 100

for i in range(3):
    x = 100
    for j in range(3):
        squares.append(Square(x, y))
        x += 100
    y += 100

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    cursor = pygame.mouse.get_pos()

    pygame.draw.rect(screen, (0, 0, 0))

    for square in squares:
        square.draw(screen)
        square.checkCursor(cursor)

    pygame.display.flip()

pygame.quit()