class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 

    def add(self, *products):
        existing_products = set()

        # Считываем существующие продукты из файла
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    existing_products.add(line.split(',')[0].strip())
        except FileNotFoundError:
            pass  # Если файл не найден, просто продолжаем

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + 'n')
                existing_products.add(product.name)


# Пример работы программы
if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str

    s1.add(p1, p2, p3)

    print(s1.get_products())