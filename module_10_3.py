import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Создание объекта Lock

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Блокировка потока при пополнении
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                # Если баланс достигает 500 и замок заблокирован, разблокируем
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            time.sleep(0.001)  # Имитация времени выполнения

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                with self.lock:  # Блокировка потока при снятии
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокируем поток, если недостаточно средств
            time.sleep(0.001)  # Имитация времени выполнения

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
