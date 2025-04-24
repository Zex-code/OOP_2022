import pygame
import math

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# Цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)
PINK = (255, 182, 193)
BLACK = (0, 0, 0)
BLUE = (100, 149, 237)


def draw_body(surface, x, y, scale):
    """Рисуем тело зайца"""
    pygame.draw.ellipse(surface, GRAY, (x - 60 * scale, y + 30 * scale, 120 * scale, 120 * scale))
    # Пушистая грудка
    pygame.draw.ellipse(surface, WHITE, (x - 50 * scale, y + 40 * scale, 100 * scale, 80 * scale))


def draw_head(surface, x, y, scale):
    """Рисуем голову зайца"""
    pygame.draw.ellipse(surface, GRAY, (x - 50 * scale, y - 50 * scale, 100 * scale, 80 * scale))
    # Щёчки
    pygame.draw.circle(surface, PINK, (int(x - 30 * scale), int(y + 10 * scale)), int(15 * scale))
    pygame.draw.circle(surface, PINK, (int(x + 30 * scale), int(y + 10 * scale)), int(15 * scale))


def draw_ears(surface, x, y, scale, angle):
    """Рисуем уши с анимацией"""
    # Левое ухо
    ear_x = x - 40 * scale + math.sin(angle) * 10 * scale
    pygame.draw.ellipse(surface, GRAY, (ear_x, y - 120 * scale, 35 * scale, 90 * scale))
    pygame.draw.ellipse(surface, PINK, (ear_x + 5 * scale, y - 110 * scale, 25 * scale, 70 * scale))

    # Правое ухо
    ear_x = x + 5 * scale - math.sin(angle) * 10 * scale
    pygame.draw.ellipse(surface, GRAY, (ear_x, y - 120 * scale, 35 * scale, 90 * scale))
    pygame.draw.ellipse(surface, PINK, (ear_x + 5 * scale, y - 110 * scale, 25 * scale, 70 * scale))


def draw_face(surface, x, y, scale, blink_progress):
    """Рисуем лицо с морганием"""
    # Глаза
    eye_radius = 12 * scale
    if blink_progress < 0.5:  # Открытые глаза
        # Левый глаз
        pygame.draw.circle(surface, WHITE, (int(x - 25 * scale), int(y - 10 * scale)), int(eye_radius))
        pygame.draw.circle(surface, BLUE, (int(x - 25 * scale), int(y - 10 * scale)), int(eye_radius / 2))
        # Правый глаз
        pygame.draw.circle(surface, WHITE, (int(x + 25 * scale), int(y - 10 * scale)), int(eye_radius))
        pygame.draw.circle(surface, BLUE, (int(x + 25 * scale), int(y - 10 * scale)), int(eye_radius / 2))
    else:  # Прикрытые глаза
        pygame.draw.line(surface, BLACK,
                         (x - 25 * scale - 10 * scale, y - 10 * scale),
                         (x - 25 * scale + 10 * scale, y - 10 * scale), 2)
        pygame.draw.line(surface, BLACK,
                         (x + 25 * scale - 10 * scale, y - 10 * scale),
                         (x + 25 * scale + 10 * scale, y - 10 * scale), 2)

    # Нос
    pygame.draw.polygon(surface, PINK, [
        (x, y + 5 * scale),
        (x - 10 * scale, y + 15 * scale),
        (x + 10 * scale, y + 15 * scale)
    ])

    # Усы (6 усов с каждой стороны)
    for i in range(3):
        # Левые усы
        whisker_length = 40 * scale
        angle = -0.3 + i * 0.3
        start_x = x - 8 * scale
        start_y = y + 12 * scale
        end_x = start_x - whisker_length * math.cos(angle)
        end_y = start_y + whisker_length * math.sin(angle)
        pygame.draw.line(surface, BLACK, (start_x, start_y), (end_x, end_y), 1)

        # Правые усы
        start_x = x + 8 * scale
        end_x = start_x + whisker_length * math.cos(angle)
        pygame.draw.line(surface, BLACK, (start_x, start_y), (end_x, end_y), 1)


def draw_feet(surface, x, y, scale):
    """Рисуем лапки с пальчиками"""
    # Задние лапы
    pygame.draw.ellipse(surface, GRAY, (x - 70 * scale, y + 120 * scale, 40 * scale, 30 * scale))
    pygame.draw.ellipse(surface, GRAY, (x + 30 * scale, y + 120 * scale, 40 * scale, 30 * scale))

    # Передние лапки
    pygame.draw.ellipse(surface, WHITE, (x - 50 * scale, y + 100 * scale, 30 * scale, 20 * scale))
    pygame.draw.ellipse(surface, WHITE, (x + 20 * scale, y + 100 * scale, 30 * scale, 20 * scale))

    # Пальчики
    for i in range(3):
        pygame.draw.circle(surface, PINK,
                           (int(x - 40 * scale + i * 15 * scale), int(y + 110 * scale)),
                           int(5 * scale))
        pygame.draw.circle(surface, PINK,(int(x + 30*scale + i*15*scale), int(y + 110*scale)),
                         int(5*scale))

def draw_rabbit(surface, x, y, scale, angle, blink_progress):
    """Рисуем всего зайца"""
    draw_body(surface, x, y, scale)
    draw_head(surface, x, y, scale)
    draw_ears(surface, x, y, scale, angle)
    draw_face(surface, x, y, scale, blink_progress)
    draw_feet(surface, x, y, scale)

# Основной цикл
clock = pygame.time.Clock()
angle = 0
blink_timer = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление анимации
    angle += 0.05
    blink_timer += 1
    blink_progress = (blink_timer % 120) / 120  # Моргаем каждые 2 секунды

    # Отрисовка
    screen.fill(WHITE)
    draw_rabbit(screen, width//2, height//2, 1, angle, blink_progress)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
