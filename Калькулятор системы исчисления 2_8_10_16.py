# "Калькулятор систем счисления"

#- переводит число из любой системы счисления (2/8/10/16)
#- в любую другую систему счисления (2/8/10/16)
#- поддерживает как буквы A–F в 16-ричной, так и проверку ошибок
#- работает через консоль, просто и понятно

def to_decimal(number_str, base_from):
    try:
        return int(number_str, base_from)
    except ValueError:
        print("Ошибка: введено недопустимое число для этой системы счисления.")
        return None

def from_decimal(number_dec, base_to):
    if base_to == 2:
        return bin(number_dec)[2:]
    elif base_to == 8:
        return oct(number_dec)[2:]
    elif base_to == 10:
        return str(number_dec)
    elif base_to == 16:
        return hex(number_dec)[2:].upper()
    else:
        return None

def ask_base(message):
    while True:
        base = input(message)
        if base in ['2', '8', '10', '16']:
            return int(base)
        print("Допустимые значения: 2, 8, 10, 16.")

def main():
    print("🧮 Переводчик систем счисления (2 / 8 / 10 / 16)")

    base_from = ask_base("Из какой системы счисления переводим? (2/8/10/16): ")
    number = input(f"Введите число в системе счисления {base_from}: ").strip()

    base_to = ask_base("В какую систему счисления переводим? (2/8/10/16): ")

    decimal_value = to_decimal(number, base_from)
    if decimal_value is None:
        return  # завершение, если ошибка

    result = from_decimal(decimal_value, base_to)
    print(f"\nРезультат: {result} (в системе счисления {base_to})")

if __name__ == "__main__":
    main()