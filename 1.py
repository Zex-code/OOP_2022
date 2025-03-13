import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((220, 220, 220))

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 101,2)

circle(screen, (255, 0, 0), (150, 175), 20)
circle(screen, (0, 0, 0), (150, 175), 21, 2)

circle(screen, (255, 0, 0), (250, 175), 20)
circle(screen, (0, 0, 0), (250, 175), 21, 2)

circle(screen, (0, 0, 0), (150, 175), 5)
circle(screen, (0, 0, 0), (250, 175), 5)

polygon(screen, (0, 0, 0), [(70, 50), (85, 35), (185, 135), (170, 150)])
polygon(screen, (0, 0, 0), [(210, 135), (225, 150), (365, 75), (350, 60)])

rect(screen, (0, 0, 0), (125, 220, 150, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()