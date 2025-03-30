import pygame
import random
from heapq import heappop, heappush

# Константы
CELL_SIZE = 40
WALL_COLOR = (200, 50, 50)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
EXIT_COLOR = (255, 255, 0)
VISITED_COLOR = (173, 216, 230)
PATH_FOUND_COLOR = (0, 0, 255)
GRID_COLOR = (0, 0, 0)

# Генерация лабиринта
def generate_maze(n, m):
    maze = [['+' for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if random.random() > 0.3:
                maze[i][j] = '.'

    # Начало ближе к центру
    start_x, start_y = n // 2, m // 2
    while maze[start_x][start_y] == '+':
        start_x, start_y = random.randint(n // 3, 2 * n // 3), random.randint(m // 3, 2 * m // 3)

    # Выход на границе
    exit_x, exit_y = random.choice([(0, random.randint(0, m - 1)), (n - 1, random.randint(0, m - 1)),
                                    (random.randint(0, n - 1), 0), (random.randint(0, n - 1), m - 1)])
    maze[exit_x][exit_y] = '.'

    return maze, (start_x, start_y), (exit_x, exit_y)


# Функция эвристики (Манхэттенское расстояние)
def heuristic(x, y, exit_x, exit_y):
    return abs(x - exit_x) + abs(y - exit_y)


# A*-поиск кратчайшего пути
def a_star_search(maze, start, exit_pos):
    n, m = len(maze), len(maze[0])
    exit_x, exit_y = exit_pos

    # Очередь с приоритетами (по f = g + h)
    heap = [(0 + heuristic(*start, exit_x, exit_y), 0, start[0], start[1], [])]  # (f, g, x, y, path)
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited_cells = []

    while heap:
        _, g, x, y, path = heappop(heap)
        visited_cells.append((x, y))

        if (x, y) == (exit_x, exit_y):
            return True, g, (x, y), path + [(x, y)], visited_cells

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.' and (nx, ny) not in visited:
                new_g = g + 1
                f = new_g + heuristic(nx, ny, exit_x, exit_y)
                heappush(heap, (f, new_g, nx, ny, path + [(x, y)]))

    return False, -1, (-1, -1), [], visited_cells


# Генерация лабиринта
N, M = 10, 10  # Размер лабиринта
maze, start_pos, exit_pos = generate_maze(N, M)
result, steps, exit_coordinates, path, visited_cells = a_star_search(maze, start_pos, exit_pos)

# Инициализация Pygame
pygame.init()
WIDTH, HEIGHT = M * CELL_SIZE, N * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабиринт с A*-поиском")


def draw_maze():
    for y in range(N):
        for x in range(M):
            color = WALL_COLOR if maze[y][x] == '+' else PATH_COLOR
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, GRID_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    pygame.draw.rect(screen, START_COLOR, (start_pos[1] * CELL_SIZE, start_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, EXIT_COLOR, (exit_coordinates[1] * CELL_SIZE, exit_coordinates[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def animate_search():
    for cell in visited_cells:
        if cell == start_pos or cell == exit_coordinates:
            continue
        pygame.draw.rect(screen, VISITED_COLOR, (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRID_COLOR, (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        pygame.display.update()
        pygame.time.delay(30)


def animate_path():
    for cell in path:
        if cell == start_pos or cell == exit_coordinates:
            continue
        pygame.draw.rect(screen, PATH_FOUND_COLOR, (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, GRID_COLOR, (cell[1] * CELL_SIZE, cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
        pygame.display.update()
        pygame.time.delay(70)


running = True
draw_maze()
pygame.display.update()
pygame.time.delay(500)
if result:
    animate_search()
    animate_path()
else:
    print("Выхода нет!")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
