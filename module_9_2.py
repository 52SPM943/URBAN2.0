
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Задача 1: Список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Задача 2: Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Задача 3: Словарь, где ключ - строка, значение - длина строки, только для четной длины
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
