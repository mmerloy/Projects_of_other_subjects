#14 вариант
#4 лаба

from Time_default import Time
from Cake import Cake
from Product import Product
from Pastry import Pastry


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
    # print(c.minute_plus())
    past1 = Pastry(3, 1230, "Вкусная еда", 12, 39, 16)
    print(past1)
    print(past1.minute_plus())



if __name__ == '__main__':
    main()