# Простой Генератор паролей
# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

# Составляющие проекта:

#- Целые числа (тип int);
#- Переменные;
#- Ввод / вывод данных (функции input() и print());
#- Условный оператор (if/elif/else);
#- Цикл for;
# Написание пользовательских функций;
#- Работа с модулем random для генерации случайных чисел.

import random

# буквы, цифры и символы
low = list('abcdefghijklmnopqrstuvwxyz')
up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
nums = list('0123456789')
symbs = list('!#$%&*+-=?@^_')
bad = list('il1Lo0O')

all_chars = []

# спрашивает число с проверкой
def ask_number(text, min_n, max_n):
    while True:
        x = input(text)
        if x.isdigit():
            x = int(x)
            if min_n <= x <= max_n:
                return x
        print(f'Введи число от {min_n} до {max_n}!')

# спрашивает y/n
def ask_yesno(text):
    while True:
        ans = input(text + ' (y/n): ').lower()
        if ans == 'y':
            return True
        elif ans == 'n':
            return False
        else:
            print('Только "y" или "n"!')

# делаем пароли
def make_passwords(length, how_many):
    for _ in range(how_many):
        random.shuffle(all_chars)
        p = random.sample(all_chars, length)
        print(''.join(p))

# тут начинаем
print('Привет! Я сгенерирую тебе пароли :)')

n = ask_number('Сколько паролей нужно (1–50)? ', 1, 50)
l = ask_number('Длина каждого пароля (6–100)? ', 6, 100)

if ask_yesno('Добавить цифры?'):
    all_chars += nums
if ask_yesno('Добавить заглавные буквы?'):
    all_chars += up
if ask_yesno('Добавить маленькие буквы?'):
    all_chars += low
if ask_yesno('Добавить символы (!#$%&*+-=?@^_)?'):
    all_chars += symbs
if ask_yesno('Убрать непонятные символы (il1Lo0O)?'):
    all_chars = [c for c in all_chars if c not in bad]

if not all_chars:
    print('Ты ничего не выбрал! Пароль нельзя сделать :(')
else:
    print('\nВот твои пароли:\n')
    make_passwords(l, n)