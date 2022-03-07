from time import time
from multiprocessing import Process, Queue


def func1(mas, n):
    for i in range(5000):
        mas[i] = mas[i]**2
        n.put(mas[i])


def func2(queue1, queue2, p2, q2):
    # заполняем нулями, чтобы потом по-нормальному заполнить
    r = [[i * 0.0] * 5000 for i in range(5000)]
    a = [queue1.get() * (i / i) for i in range(1, 5001)]
    b = [queue2.get() * (i / i) for i in range(1, 5001)]
    for i in range(1, 5000):
        for j in range(1, 5000):
            r[i][j] = 1 / (1 + (a[i] - 2 * p2[i] * q2[i] + b[i]))


def multiprocessing():
    p2 = [i for i in range(5000)]
    q2 = [i for i in range(5000)]
    queue1 = Queue()
    num1 = Process(target=func1, args=(p2, queue1,))
    queue2 = Queue()
    num2 = Process(target=func1, args=(q2, queue2,))
    num3 = Process(target=func2, args=(queue1, queue2, p2, q2))
    num1.start()
    num2.start()
    num3.start()
    num1.join()
    num2.join()
    num3.join()


def not_multiprocessing():
    r1 = []
    for p1 in range(1, 5001):
        a = []
        for q1 in range(1, 5001):
            a.append(1 / (1 + (q1 - p1) ** 2))
        r1.append(a)


if __name__ == '__main__':
    start1 = time()
    not_multiprocessing()
    print("Время без использования multiprocessing: ", time() - start1)
    start2 = time()
    multiprocessing()
    print("Время с использованием multiprocessing: ", time() - start2)
