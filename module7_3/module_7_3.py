import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  # Сохраняем названия файлов в кортеже

    def get_all_words(self):
        all_words = {}  # Создаем пустой словарь для хранения слов из файлов

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем содержимое файла и переводим в нижний регистр
                    content = file.read().lower()
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    # Разбиваем текст на слова
                    words = content.split()
                    all_words[file_name] = words  # Записываем в словарь
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word)  # Сохраняем позицию первого вхождения

        return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()  # Получаем все слова из файлов

        for file_name, words in all_words.items():
            results[file_name] = words.count(word)  # Считаем количество вхождений

        return results


# Пример использования класса
if __name__ == "__main__":
    finder = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')

    # Получаем все слова из файлов
    all_words = finder.get_all_words()
    print("Все слова из файлов:", all_words)

    # Находим слово
    word_to_find = 'my'
    found_positions = finder.find(word_to_find)
    print(f"Позиции слова '{word_to_find}':", found_positions)

    # Считаем количество вхождений слова
    word_to_count = 'my'
    count_results = finder.count(word_to_count)
    print(f"Количество вхождений слова '{word_to_count}':", count_results)
