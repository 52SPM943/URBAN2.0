import multiprocessing
import time
import threading
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список (без лишних пробелов)
    # Не возвращаем all_data, так как это не требуется по условию

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"{linear_duration} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multi_duration = time.time() - start_time
    print(f"{multi_duration} (многопроцессный)")



