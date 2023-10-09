import pygame
from classes import *

pygame.init()

screen = pygame.display.set_mode([500, 500])
fps = 30
clock = pygame.time.Clock()
time = 0

squares = []

x = 100
y = 100

for i in range(3):
    x = 100
    for j in range(3):
        squares.append(Square(x, y, i, j))
        x += 100
    y += 100

player_turn = 2

isGame = True
running = True
while running:
    cursor = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and isGame:
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

    if time%1800 == 0 and isGame:
        field = []
        # field = [[0], [1], [2],
        #          [3], [4], [5],
        #          [6], [7], [8]]
        for square in squares:
            field.append([square.coordinates, square.condition])
        for i in range(3):
            if field[i][1] == field[i+3][1] and field[i+3][1] == field[i+6][1] and field[i][1] != 0:
                isGame = False
                print("Player win!")
        for i in range(3):
            if field[3*i][1] == field[3*i+1][1] and field[3*i+1][1] == field[3*i+2][1] and field[3*i][1] != 0:
                isGame = False
                print("Player win!")
        if field[0][1] == field[4][1] and field[4][1] == field[8][1] and field[0][1] != 0:
            isGame = False
            print("Player win!")
        if field[2][1] == field[4][1] and field[4][1] == field[6][1] and field[2][1] != 0:
            isGame = False
            print("Player win!")


    pygame.display.flip()
    clock.tick(fps)

    if isGame:
        time += fps

pygame.quit()