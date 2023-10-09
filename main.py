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

player_turn = 2

running = True
while running:
    cursor = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            for square in squares:
                square.checkCursor(cursor)
                square.changeCondition(player_turn)
            print(player_turn)
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1


    screen.fill((255, 255, 255))


    for square in squares:
        square.draw(screen)
        square.checkCursor(cursor)

    pygame.display.flip()

pygame.quit()