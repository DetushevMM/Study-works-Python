# Шифр Цезаря
# Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря. Она должна запрашивать у пользователя следующие данные:

# - направление: шифрование или дешифрование;
# - язык алфавита: русский или английский;
# - шаг сдвига (со сдвигом вправо).
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".

# Составляющие проекта:

#- Целые числа (тип int);
#- Модульная арифметика;
#- Переменные;
#- Ввод / вывод данных (функции input() и print());
#- Условный оператор (if/elif/else);
#- Цикл for/while;
#- Строковые методы.

def get_alphabet(language):
    if language == 'en':
        return ('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    else:  # 'ru'
        return ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.replace('ё', ''), 
                'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.replace('Ё', ''))

def caesar_cipher(text, shift, language, direction):
    result = ''
    shift = shift % 26 if language == 'en' else shift % 32
    if direction == 'decrypt':
        shift *= -1

    lower_alpha, upper_alpha = get_alphabet(language)

    for char in text:
        if char in lower_alpha:
            index = lower_alpha.index(char)
            new_index = (index + shift) % len(lower_alpha)
            result += lower_alpha[new_index]
        elif char in upper_alpha:
            index = upper_alpha.index(char)
            new_index = (index + shift) % len(upper_alpha)
            result += upper_alpha[new_index]
        else:
            result += char  # неалфавитные символы остаются без изменений
    return result

# Запрос данных у пользователя
print('Добро пожаловать в программу "Шифр Цезаря"!')

while True:
    direction = input('Выберите направление (encrypt - шифрование, decrypt - дешифрование): ').lower()
    if direction in ['encrypt', 'decrypt']:
        break
    print('Нужно ввести encrypt или decrypt.')

while True:
    language = input('Выберите язык (en - английский, ru - русский): ').lower()
    if language in ['en', 'ru']:
        break
    print('Введите en или ru.')

while True:
    try:
        shift = int(input('Введите шаг сдвига (целое число): '))
        break
    except ValueError:
        print('Нужно ввести ЦЕЛОЕ число!')

text = input('Введите текст для обработки: ')

# Шифрование / дешифрование
result = caesar_cipher(text, shift, language, direction)
print(f'Результат: {result}')