import time
import random
import threading

# Продолжительность паузы перед началом расчета
time_sleep = 3

# Функция для вычисления приближенного значения π
def pi_approximation(n, results, index):
    time.sleep(time_sleep)  # Пауза перед расчетом
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / n) * 4
    print(f"Приблизительное значение π для n = {n}: {pi_approx}")  # Вывод на печать результатов

def main():
    n_values = [10**7, 10**7, 10**6, 10**6]
    results = [0] * len(n_values)  # Список для результатов
    threads = []  # Список для хранения потоков

    start_time = time.time()

    # Создание и запуск потоков
    for i, n in enumerate(n_values):
        thread = threading.Thread(target=pi_approximation, args=(n, results, i))
        thread.start()
        threads.append(thread)

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    # Вывод результатов
    for n, pi_value in zip(n_values, results):
        pi_value

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.2f} секунд")

if __name__ == "__main__":
    main()