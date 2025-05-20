# СОЗДАНИЕ ИГРЫ ТЕТРИС НА PYGAME

import pygame
import random

# нужно инициализировать Pygame с помощью функции init()
pygame.init()

# Затем мы создаём группу переменных-констант, отвечающую за основной геймплей
# Переменные-константы объявляются только с помощью заглавных букв
# Параметры экрана и сетки
WIDTH, HEIGHT = 300, 600
ROWS, COLS = 20, 10
BLOCK_SIZE = WIDTH // COLS
FPS = 60

# На следующем шаге мы создаем цвета для фигур, заднего фона игры и шрифта с помощью RGB палитры,
# где у каждого конкретного оттенка есть свой номер от 0 до 255. (0,0,0)-черный, (255,255,255)- белый

# Цвета
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BORDER_COLOR = (50, 50, 50)

COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0),    # Z
]

# Затем нам нужно записать все возможные формы фигур. Проще всего это сделать с помощью двумерных списков (матриц)
# Фигуры
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[1, 1], [1, 1]],        # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
]
# Окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тетрис")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont("arial", 24)

# Поле
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# Музыка
# pygame.mixer.music.load("tetris_theme.mp3")
# pygame.mixer.music.play(-1)

# Теперь пора создать первый класс в нашей игре. Он будет использоваться для представления фигур в игре: 
# будет хранить в себе форму фигуры, её положение (по координатам x, y), 
# случайным образом выбирать # цвет для новой фигуры, вращать картинку фигуры, а также её матрицу
# Класс фигуры
class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if not self.is_valid():
            self.x -= dx
            self.y -= dy
            return False
        return True

    def is_valid(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    nx, ny = self.x + j, self.y + i
                    if nx < 0 or nx >= COLS or ny >= ROWS:
                        return False
                    if ny >= 0 and grid[ny][nx]:
                        return False
        return True

    def lock(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    ny = self.y + i
                    nx = self.x + j
                    if 0 <= ny < ROWS and 0 <= nx < COLS:
                        grid[ny][nx] = self.color

def clear_lines():
    global grid
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    lines_cleared = ROWS - len(new_grid)
    for _ in range(lines_cleared):
        new_grid.insert(0, [0 for _ in range(COLS)])
    grid = new_grid
    return lines_cleared

# Создание сетки
def draw_grid():
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            color = grid[y][x]
            if color:
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
            else:
                pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

# Проверка границ
def draw_piece(piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                x = (piece.x + j) * BLOCK_SIZE
                y = (piece.y + i) * BLOCK_SIZE
                pygame.draw.rect(screen, piece.color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, BORDER_COLOR, (x, y, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont("arial", size, True)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)

# Основной цикл
def main():
    running = True
    fall_time = 0
    fall_speed = 0.5
    current_piece = Piece()
    next_piece = Piece()
    score = 0

    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick(FPS)

        if fall_time / 1000 >= fall_speed:
            if not current_piece.move(0, 1):
                current_piece.lock()
                cleared = clear_lines()
                score += cleared * 100
                current_piece = next_piece
                next_piece = Piece()
                if not current_piece.is_valid():
                    draw_text("GAME OVER", 40, (255, 0, 0), WIDTH // 2, HEIGHT // 2)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    return

            fall_time = 0

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    current_piece.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    current_piece.move(0, 1)
                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not current_piece.is_valid():
                        for _ in range(3):
                            current_piece.rotate()  # возвращаем обратно

        draw_grid()
        draw_piece(current_piece)
        draw_text(f"Score: {score}", 24, WHITE, WIDTH // 2, 20)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()