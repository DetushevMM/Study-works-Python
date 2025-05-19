# Изучаем модуль turtle

# Задание: программы с использованием модуля turtle, которая выполняет требования:
# 1. Рисует силуэты многоэтажек.
# 2. Рисует окна.
# 3. Добавляет случайные звезды на небе.
# 4. Добавляет луну.
# 5. Рисует многоугольную звезду по щелчку мыши с разным числом сторон, цветами и размерами.

import turtle
import random
import math

# Настройка экрана
screen = turtle.Screen()
screen.bgcolor("midnight blue")
screen.title("Силуэты многоэтажек с луной и звездами")

# Глобальная черепаха
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
screen.setup(WIDTH, HEIGHT)

# --- Рисование здания ---
def draw_building(x, width, height):
    pen.penup()
    pen.goto(x, -HEIGHT // 2)
    pen.color("black")
    pen.begin_fill()
    pen.pendown()
    pen.setheading(0)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()

# --- Рисование окон ---
def draw_windows(x, width, height):
    cols = width // 30
    rows = height // 40
    for i in range(rows):
        for j in range(cols):
            win_x = x + 5 + j * 25
            win_y = -HEIGHT // 2 + 5 + i * 35
            if random.random() < 0.5:
                pen.penup()
                pen.goto(win_x, win_y)
                pen.color("yellow")
                pen.begin_fill()
                pen.pendown()
                for _ in range(4):
                    pen.forward(10)
                    pen.left(90)
                pen.end_fill()

# --- Рисование случайных звёзд (точек) ---
def draw_random_stars(count):
    for _ in range(count):
        x = random.randint(-WIDTH // 2, WIDTH // 2)
        y = random.randint(0, HEIGHT // 2)
        pen.penup()
        pen.goto(x, y)
        pen.dot(random.randint(2, 4), "white")

# --- Рисование луны ---
def draw_moon():
    moon = turtle.Turtle()
    moon.color("gray")
    moon.speed(1)
    moon.penup()
    moon.goto(WIDTH // 2 - 120, HEIGHT // 2 - 120)
    moon.begin_fill()
    moon.pendown()
    moon.circle(50)
    moon.end_fill()

# --- Рисование многоугольной звезды ---
def draw_star(x, y):
    sides = random.randint(5, 50)
    size = random.randint(10, 40)
    color = random.choice(["white", "yellow", "light blue", "light gray", "orange", "gold"])
    angle = 360 / sides

    star = turtle.Turtle()
    star.penup()
    star.goto(x, y)
    star.setheading(0)
    star.color(color)
    star.begin_fill()
    star.pendown()
    for _ in range(sides):
        star.forward(size)
        star.right(180 - angle)
    star.end_fill()
    star.hideturtle()

# --- Обработчик клика ---
def on_click(x, y):
    draw_star(x, y)

# --- Основной процесс ---
def main():
    # Здания
    for i in range(-WIDTH // 2, WIDTH // 2, random.randint(60, 120)):
        building_width = random.randint(50, 100)
        building_height = random.randint(150, 300)
        draw_building(i, building_width, building_height)
        draw_windows(i, building_width, building_height)

    # Небо — звезды
    draw_random_stars(100)

    # Луна
    draw_moon()

    # Клик мыши
    screen.onclick(on_click)

    screen.mainloop()

main()
