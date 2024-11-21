import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем содержимое файла и обрабатываем его
                    content = file.read().lower()
                    # Убираем пунктуацию
                    content = content.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    # Разбиваем на слова
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)  # Находим позицию первого вхождения
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            count = words.count(word)  # Считаем количество вхождений
            if count > 0:
                result[name] = count
        return result

# Пример использования:
# finder = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')
# print(finder.get_all_words())
# print(finder.find('word1'))
# print(finder.count('word1'))
