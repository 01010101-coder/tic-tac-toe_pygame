import pygame

class Square:
    def __init__(self, x, y, cx, cy):
        self.x = x
        self.y = y
        self.coordinates = [cx, cy]
        self.height = 100
        self.width = 100
        self.color = (0, 0, 0)

        self.isCursorOn = [False, False]
        self.condition = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.height, self.width), 1)
        if self.condition == 1:
            pygame.draw.circle(screen, (0, 255, 0), (self.x + round(self.width/2), self.y + round(self.height/2)), 30, 1)
        if self.condition == 2:
            pygame.draw.line(screen, (0, 0, 255), [self.x+20, self.y+20],
                             [self.x+self.width-20, self.y+self.height-20], 1)

            pygame.draw.line(screen, (0, 0, 255), [self.x + self.width - 20, self.y + 20],
                             [self.x + 20, self.y + self.height - 20], 1)

    def checkCursor(self, cursor):
        self.isCursorOn = [False, False]
        if cursor[0] < self.x + self.width and cursor[0] > self.x:
            self.isCursorOn[0] = True
        if cursor[1] < self.y + self.height and cursor[1] > self.y:
            self.isCursorOn[1] = True
        if self.isCursorOn[0] and self.isCursorOn[1]:
            self.color = (255, 0, 0)
        else:
            self.color = (0, 0, 0)

    def changeCondition(self, player_turn):
        if self.isCursorOn[0] and self.isCursorOn[1]:
            if player_turn == 1:
                self.condition = 1
            elif player_turn == 2:
                self.condition = 2


def checkVictory(squares, player_turn):
    for square in squares:
        pass
