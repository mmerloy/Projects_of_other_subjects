import os
from multiprocessing import Process
from time import time


def func(file):
    word = "Key"
    if (file.endswith(".txt")) and (word in file):
        return 1


def multiprocessing1():
    path = os.path.dirname(__file__)
    for address, dirs, files in os.walk(path):
        for file in files:
            num = Process(target=func, args=(file,))
            if num.start() == 1:
                print(address + "/" + file)
                num.join()


def func1(file):
    if file.endswith(".txt"):
        return 1


def func2(file, word):
    if word in file:
        return 1


def multiprocessing2():
    path = os.path.dirname(__file__)
    for address, dirs, files in os.walk(path):
        for file in files:
            num1 = Process(target=func1, args=(file,))
            num2 = Process(target=func2, args=(file, 'Key'))
            if (num1.start() == 1) and (num2.start() == 1):
                print(address + "/" + file)
                num1.join()
                num2.join()


if __name__ == '__main__':
    start1 = time()
    multiprocessing1()
    print("Один поток: ", time() - start1)
    start2 = time()
    multiprocessing2()
    print("Два потока: ", time() - start2)
