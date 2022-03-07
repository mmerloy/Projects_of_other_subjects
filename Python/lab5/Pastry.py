from Product import Product


class Pastry(Product):
    def __init__(self, expiration_date,quantity, company,hour , minute, second):
        super().__init__(company,hour , minute, second)
        self.__expiration_date = expiration_date
        self.__quantity=quantity

    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    @property
    def quantity(self):
        return self.__quantity


    @quantity.setter
    def quantity(self, quantity):
        if quantity > 1000:
            self.__quantity = quantity
        else:
            print("Количество продукции должно быть больше")


    def minute_plus(self):
        minute_1 = (((self.hour * 60) + self.minute) - 100) % 60
        hour_1 = (((self.hour * 60) + self.minute) - 100) // 60
        print("Время уменьшенное на 100 минут: {}:{}:{}".format(hour_1, minute_1, self.second))



    def __str__(self):
        return "Количество продукции: {} \t Срок годности продукции (в днях) {} \n{}".format(self.__quantity, self.__expiration_date,Product.__str__(self))
