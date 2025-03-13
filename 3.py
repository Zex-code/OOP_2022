import math
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
scale = 0.45  # scale of window with the picture
screen = pygame.display.set_mode((int(2500 * scale), int(1666 * scale)))

yellow_sky_up = (254, 213, 162)
yellow_sky_middle = (254, 213, 148)
pink_sky = (254, 213, 196)
sun_color = (252, 238, 33)
orange = (252, 152, 49)
red = (172, 67, 52)
pink_ground = (179, 134, 148)
dark_ground = (48, 16, 38)
dark_birds = (66, 33, 11)


def background(scr, scl, color1, color2, color3, color4):
    rect(scr, color1, [0, 0, 2500 * scl, 349 * scl])
    rect(scr, color2, [0, 349 * scl, 2500 * scl, 492 * scl])
    rect(scr, color3, [0, 711 * scl, 2500 * scl, 354 * scl])
    rect(scr, color4, [0, 1065 * scl, 2500 * scl, 834 * scl])


def bird(scr, scl, height, width, x, y, size, color):

    d_y = height * size
    d_x = width * size
    r = 15 * size
    circle(scr, color, ((x - d_x) * scl, (y - d_y) * scl), (r * scl))
    polygon(scr, color,
            [[(x - d_x + r / 2 ** 0.5) * scl - 1, (y - d_y - r / 2 ** 0.5) * scl],
             [(x - d_x - r / 2 ** 0.5) * scl + 3, (y - d_y + r / 2 ** 0.5) * scl],
             [x * scl, y * scl],
             [(x + d_x) * scl, (y - d_y) * scl], [(x + d_x / 2) * scl, (y - d_y * 2 / 2) * scl],
             [x * scl, (y - d_y / 2) * scl]
             ])


def sun(scr, scl, color, x, y, size):

    circle(scr, color, (x * scl, y * scl), (size * scl))


def smart_polygon(scr, scl, color, points):

    new_points = []
    for pairs in points:
        new_points.append((pairs[0] * scl, pairs[1] * scl))
    polygon(scr, color, new_points)


def elliptic(scr, scl, color, rectangle, start_angle, stop_angle, size):

    for correct in range(-4, 4, 1):
        new_rectangle = []
        for num in rectangle:
            new_rectangle.append(num * scl + correct)
        arc(scr, color, new_rectangle, start_angle, stop_angle, int(size * scale))


mountains = [(0, 775), (30, 674), (514, 327), (611, 357), (644, 411),
             (653, 419), (958, 625), (1123, 603), (1212, 647), (1331, 531),
             (1450, 552), (1500, 500), (1770, 265), (1868, 309),
             (1980, 415), (2071, 390), (2339, 473), (2325, 471),
             (2500, 520)]
forest = [(0, 1125), (0, 830), (71, 858), (250, 825),
          (436, 1068), (546, 885), (723, 979),
          (807, 750), (1000, 800), (1200, 930),
          (1430, 876), (1750, 687), (2044, 845), (2153, 755),
          (2253, 820), (2300, 738), (2407, 743), (2500, 590),
          (2500, 1071)]
ground = [(0, 1666), (0, 857), (302, 937), (531, 1232),
          (813, 1580), (1171, 1637), (1579, 1408),
          (1689, 1463), (2089, 1400), (2500, 1000),
          (2500, 1666)]
birds = [(960, 600, 1), (1185, 621, 1), (1185, 709, 1.05), (991, 778, 1), (1944, 1335, 1.5), (1985, 1206, 0.6),
         (1700, 1252, 0.8), (1568, 1127, 1.0)]

background(screen, scale, yellow_sky_up, pink_sky, yellow_sky_middle, pink_ground)
sun(screen, scale, sun_color, 1192, 345, 144)
smart_polygon(screen, scale, orange, mountains)  # mountains
elliptic(screen, scale, orange, [1750, 245, 100, 200], 0, math.pi, 200)
smart_polygon(screen, scale, red, forest)  # red forest
elliptic(screen, scale, red, [1450, 687, 600, 550], math.pi / 2, math.pi * 0.9, 200)
elliptic(screen, scale, red, [60, 660, 400, 900], 0, math.pi * 5 / 6, 383)
smart_polygon(screen, scale, dark_ground, ground)
for i in birds:
    bird(screen, scale, 50, 65, i[0], i[1], i[2], dark_birds)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()