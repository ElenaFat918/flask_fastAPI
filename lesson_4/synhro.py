# """
# Эта программа выводит обратный отсчет от заданного числа до 1 с интервалом в 1 секунду.
# В данном случае это синхронный код, так как каждое выполнение цикла for блокирует выполнение
# программы на 1 секунду.
# """
# import time
#
#
# def count_down(n):
#     for i in range(n, 0, -1):
#         print(i)
#         time.sleep(1)
#
#
# count_down(5)
#
# """
# Эта программа вызывает функцию slow_function(), которая занимает 5 секунд на выполнение.
# Весь код работает синхронно, то есть выполнение программы блокируется на время выполнения функции.
# """
# import time
#
#
# def slow_function():
#     print("Начало функции")
#     time.sleep(5)
#     print("Конец функции")
#
#
# print("Начало программы")
# slow_function()
# print("Конец программы")

"""
Эта программа запускает длительную задачу long_running_task(), 
которая выполняется в течение случайного времени от 1 до 3 секунд. 
Весь код работает синхронно, поэтому выполнение программы блокируется 
на время выполнения задачи.
"""

import random
import time


def long_running_task():
    for i in range(5):
        print(f"Выполнение задачи {i}")
        time.sleep(random.randint(1, 3))


def main():
    print("Начало программы")


long_running_task()
print("Конец программы")
main()
