class Time:
    def __init__(self, hour="Не задано", minute="Не задано", second="Не задано"):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        try:
            int(minute)
        except ValueError:
            print("Минуты должны быть числом")
        else:
            if int(minute) >= 0 and int(minute) <= 60:
                self.__minute = minute
            else:
                print("Ошибка, количество минут не может быть отрицательное")



    def minute_plus(self):
        minute = (((self.__hour * 60) + self.__minute) + 100) % 60
        hour = (((self.__hour * 60) + self.__minute) + 100) // 60
        print("Время увеличенное на 100 минут: {}:{}:{}".format(hour, minute, self.__second))


    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        try:
            int(hour)
        except ValueError:
            print("количество часов должно быть числом")
        else:
            if int(hour) > 0 and int(hour) < 25:
                self.__hour= hour
            else:
                print("Ошибка, количество часов не может быть отрицательное")

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, second):
        try:
            int(second)
        except ValueError:
            print("Секунды должны быть числом")
        else:
            if int(second) >= 0 and int(second) <= 60:
                self.__second = second
            else:
                print("Ошибка, количество секунд не может быть отрицательное")


    def minutes_to_midnight(self):
        if self.__minute==0:
            print((24- self.__hour) * 60)
        else:
            print((60-self.__minute)+(23-self.__hour)*60)

    def __str__(self):
        return "Часы: {} \t Минуты: {} \t Секунды: {}".format(self.__hour, self.__minute, self.__second)

    def __del__(self):
        print(self.__hour, self.__minute, self.__second, "удалено из памяти")
