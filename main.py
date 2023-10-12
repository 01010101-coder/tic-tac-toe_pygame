from classes import *

pygame.init()
pygame.display.set_caption('Крестики и нолики')

font = pygame.font.SysFont('timesnewromano', 24)

but_reset = font.render('Reset', True, (0, 0, 255))
firstPlayer_win = font.render('First player wins!', True, (0, 0, 0))
secondPlayer_win = font.render('Second player wins!', True, (0, 0, 0))
draw_win = font.render('Draw', True, (0, 0, 0))

screen = pygame.display.set_mode([500, 600])
fps = 60
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

player_turn = 1
player_win = 0

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
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1
        if event.type == pygame.MOUSEBUTTONUP:
            if cursor[0] < 300 and cursor[0] > 150 and cursor[1] < 550 and cursor[1] > 500:
                for square in squares:
                    square.condition = 0
                isGame = True
                player_win = 0
                player_turn = 1

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(100, 100, 301, 301), 1)
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), [100 + (i+1) * 100, 100], [100 + (i+1) * 100, 400], 1)
    for i in range(2):
        pygame.draw.line(screen, (0, 0, 0), [100, 100 + (i+1) * 100], [400, 100 + (i+1) * 100], 1)

    y = 100
    for i in range(3):
        x = 100
        for j in range(3):
            x += 100
        y += 100

    for square in squares:
        square.draw(screen)
        square.checkCursor(cursor)

    screen.blit(but_reset, (200, 515))
    pygame.draw.rect(screen, (81, 94, 184), pygame.Rect(150, 500, 150, 50), 1)

    if player_win == 1:
        screen.blit(firstPlayer_win, (170, 50))
    elif player_win == 2:
        screen.blit(secondPlayer_win, (170, 50))
    elif player_win == 3:
        screen.blit(draw_win, (215, 50))

    if time % 300 == 0 and isGame:
        field = []
        for square in squares:
            field.append([square.coordinates, square.condition])
        for i in range(3):
            if field[i][1] == field[i+3][1] and field[i+3][1] == field[i+6][1] and field[i][1] != 0:
                isGame = False
                if field[i][1] == 1:
                    player_win = 1
                elif field[i][1] == 2:
                    player_win = 2
        for i in range(3):
            if field[3*i][1] == field[3*i+1][1] and field[3*i+1][1] == field[3*i+2][1] and field[3*i][1] != 0:
                isGame = False
                if field[3*i][1] == 1:
                    player_win = 1
                elif field[3*i][1] == 2:
                    player_win = 2
        if field[0][1] == field[4][1] and field[4][1] == field[8][1] and field[0][1] != 0:
            isGame = False
            if field[0][1] == 1:
                player_win = 1
            elif field[0][1] == 2:
                player_win = 2
        if field[2][1] == field[4][1] and field[4][1] == field[6][1] and field[2][1] != 0:
            isGame = False
            if field[2][1] == 1:
                player_win = 1
            elif field[2][1] == 2:
                player_win = 2
        if player_win == 0:
            i = 0
            for square in field:
                if square[1] == 0:
                    break
                if i == 8:
                    isGame = False
                    player_win = 3
                i += 1

    pygame.display.flip()

    clock.tick(fps)
    if isGame:
        time += fps

pygame.quit()
