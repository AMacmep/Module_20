import time
import random
import multiprocessing

time_sleep =3


def pi_approximation(n):
    time.sleep(time_sleep)  # Пауза перед расчетом
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / n) * 4
    return pi_approx  # Возвращаем значение π


def main():
    n_values = [10 ** 7, 10 ** 7, 10 ** 6, 10 ** 6]

    # Создаем пул процессов
    with multiprocessing.Pool(4) as pool:
        results = pool.map(pi_approximation, n_values)

    # Вывод результатов
    for n, pi_value in zip(n_values, results):
        print(f"Приблизительное значение π для n = {n}: {pi_value}")


if __name__ == "__main__":
    start_time = time.time()

    main()  # Вызываем основную функцию

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Общее время выполнения: {execution_time:.2f} секунд")