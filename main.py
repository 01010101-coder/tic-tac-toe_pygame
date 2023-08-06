import pygame, sys
from pygame.locals import *

pygame.init() # initiate pygame

clock = pygame.time.Clock() # set up clock
pygame.display.set_caption('Pygame window') # name of the window

WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32) # initiate screen

image = pygame.image.load('images/ball.png') # load image

moving_right = False
moving_left = False

image_location = [50, 50]
image_y_impuls = 0

# рисуем вокруг изображения невидимый прямоугольник для колизии
image_rect = pygame.Rect(image_location[0], image_location[1], image.get_width(), image.get_height())
# тестовый прямоугольник
test_rec = pygame.Rect(100, 100, 100, 50)

while True: # main loop
    screen.fill((255, 255, 255)) # закрашиваем в один цвет

    screen.blit(image, image_location) # render image (image, (coordinates))

    # делаем подпрыгивания
    if image_location[1] > WINDOW_SIZE[1] - image.get_height():  # проверяем на границу
        image_y_impuls = -image_y_impuls # меняем направление полета
    else:
        image_y_impuls += 0.2 # ускоряем/замедляем
    image_location[1] += image_y_impuls # двигаем по вертикали

    if moving_right:
        image_location[0] += 5
    if moving_left:
        image_location[0] -= 5

    # обновляем позиции в image_rect, потому что само оно не обновляется
    image_rect.x = image_location[0]
    image_rect.y = image_location[1]

    # проверяем на соприкосновения изображения и тестового прямоугольника
    if image_rect.colliderect(test_rec):
        pygame.draw.rect(screen, (255, 0, 0), test_rec)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rec)
        
    for event in pygame.event.get():
        if event.type == QUIT: # if we want to close event
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update() # update screen
    clock.tick(60) # FPS
