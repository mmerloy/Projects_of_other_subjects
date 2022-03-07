#14 вариант
#4 лаба
import unittest
from Time_default import Time
from Cake import Cake
from Product import Product
from Pastry import Pastry
from My_exception import My_exception

def main():
    time1 = Time(12, 10, 30)
    time2 = Time(16, 45, 13)
    time3 = Time(21, 59, 59)
    time1.hour = input("Введите количество часов : ")
    time1.minute = input("Введите количество минут : ")
    time1.second = input("Введите количество секунд  : ")
    print(time1, "\n", time2, "\n", time3)
    del time1, time2, time3

    prod1 = Product("Русский бисквит", 13, 21, 47)
    print(prod1)
    print(prod1.minute_plus())
    print( prod1.minutes_to_midnight())
    c = Cake("Торт Дружба", "Сметанный крем", "Бисквит", 6, 1099, "Мергер", 18, 11, 30)
    print(c)
    past1 = Pastry(3, 1230, "Вкусная еда", 12, 39, 16)
    print(past1)
    print(past1.minute_plus())




if __name__ == '__main__':
    main()

########

print("Введите часы, будет проверка на пользовательское исключение ")
a = input()
if not a.isnumeric():
    raise My_exception("Было введено не число")
else:
    a = int(a)
while True:
    try:
        b = int(input("Введите минуты: "))
        break
    except ValueError as e:
        print("Сведения об исключении", e)

while True:
    try:
        c = int(input("Введите секунды: "))
        break
    except ValueError as e:
        print("Сведения об исключении", e)


Mas = [a, b, c]

Fin = open("test.bin", "wb")
for item in Mas:
    s = str(item) + '\n'
    bt = s.encode() #конвертируем строку в последовательность байт
    Fin.write(bt)
Fin.close()

Mass = []
try:
    Fin = open('test.bin', 'rb')
    for ln in Fin:
        try:
            x = int(ln)
            Mass = Mass + [x]
        except ValueError as e:
            print("Сведения об исключении", e)
except FileNotFoundError:
    print("Невозможно открыть файл")

Fin.close()
time = Time()
# Берем из списка который у нас сохрнаился для проверки того, что действительно список сохранился
time.hour = Mass[0]
time.minute = Mass[1]
time.second = Mass[2]
print(time.minute_plus())

