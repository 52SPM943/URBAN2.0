class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS] else None

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}" if self.__color else "Цвет: Неизвестный"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)

# Пример использования
if __name__ == "__main__":
    my_sedan = Sedan("Иван", "Toyota Camry", 150, "red")
    my_sedan.print_info()

    my_sedan.set_color("blue")  # Изменяем цвет на допустимый
    my_sedan.print_info()

    my_sedan.set_color("yellow")  # Пытаемся изменить цвет на недопустимый
