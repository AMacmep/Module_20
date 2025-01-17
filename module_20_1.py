import time
import random

time_sleep=3

def pi_approximation(n):
    time.sleep(time_sleep)  # Пауза перед расчетом.
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / n) * 4
    return print(f"Приблизительное значение π для n = {n}: {pi_approx}")


def main():
    n_values = [10**7, 10**7, 10**6, 10**6]


    start_time = time.time()

    for n in n_values:
        pi_approximation(n)


    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Общее время выполнения: {execution_time:.2f} секунд")


if __name__ == "__main__":
    main()