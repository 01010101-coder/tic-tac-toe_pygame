import pygame

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 100
        self.width = 100
        self.color = (0, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.height, self.width), 1)

    def checkCursor(self, cursor):
        isCursorOn = [False, False]
        if cursor[0] < self.x + self.width and cursor[0] > self.x:
            isCursorOn[0] = True
        if cursor[1] < self.y + self.height and cursor[1] > self.y:
            isCursorOn[1] = True
        if isCursorOn[0] and isCursorOn[1]:
            self.color = (255, 0, 0)
        else:
            self.color = (0, 0, 0)
