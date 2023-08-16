# """
# Эта программа создает 5 потоков и запускает функцию worker() в каждом из них.
# Функция worker() занимает 3 секунды на выполнение. Весь код работает многопоточно,
# то есть каждый поток работает независимо от других,
# и выполнение программы не блокируется на время выполнения функции.
# """
# import threading
# import time
#
#
# def worker(num):
#     print(f"Начало работы потока {num}")
#     time.sleep(3)
#     print(f"Конец работы потока {num}")
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(
#     i,))  # threading.Thread отвечает за работу с потоками, target=worker - цель worker, те функция которая будет работать в потоке
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
# print("Все потоки завершили работу")

"""
Эта программа создает 5 потоков и запускает функцию worker() в каждом из них. 
Функция worker() занимает 3 секунды на выполнение. 
Весь код работает многопоточно, но в отличие от предыдущего примера, 
потоки запускаются и завершаются последовательно, 
блокируя выполнение программы на время выполнения каждого потока.
"""

# import threading
# import time
#
#
# def worker(num):
#     print(f"Начало работы потока {num}")
#     time.sleep(3)
#     print(f"Конец работы потока {num}")
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,)) # создали 5 потоков, которые будут работать с функцией
#     threads.append(t)
#
# for t in threads:
#     t.start() # стартуем поток
#     t.join() # просим подождать пока поток завершится
# print("Все потоки завершили работу")

"""
Эта программа создает 5 потоков и запускает функцию increment() в каждом из них. 
Функция increment() увеличивает значение глобальной переменной counter на 1 миллион раз.
 Весь код работает многопоточно,но из-за того,что несколько потоков работают с одной переменной, 
 может возникнуть проблема гонки данных (race condition),
 когда результат выполнения программы может быть непредсказуемым.
"""

# import threading
#
# counter = 0
#
#
# def increment():
#     global counter
#     for _ in range(1_000_000):
#         counter += 1
#     print(f"Значение счетчика: {counter:_}")
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(f"Значение счетчика в финале: {counter:_}")
