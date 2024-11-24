def add_everything_up(a, b):
    try:
        # Пытаемся сложить два числа
        return a + b
    except TypeError:
        try:
            # Пытаемся соединить две строки
            return str(a) + str(b)
        except Exception as e:
            # Обрабатываем любые другие исключения
            return str(e)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))          # Вывод: 130.456
