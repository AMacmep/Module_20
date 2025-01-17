import asyncio
import random
import time

time_sleep = 3

async def pi_approximation(n):
    await asyncio.sleep(time_sleep)  # Асинхронная пауза перед расчетом
    inside_circle = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / n) * 4
    return pi_approx

async def main():
    n_values = [10 ** 7, 10 ** 7, 10 ** 6, 10 ** 6]
    results = []

    start_time = time.time()  # Начало отсчета времени

    # Запускаем все корутины с помощью gather
    tasks = [pi_approximation(n) for n in n_values]
    results = await asyncio.gather(*tasks)

    for n, pi_value in zip(n_values, results):
        print(f"Приблизительное значение π для n = {n}: {pi_value}")

    end_time = time.time()  # Конец отсчета времени
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.2f} секунд")

# Запуск основной функции
asyncio.run(main())