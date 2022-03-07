from Product import Product

#filling-начинка
#dough-тесто
class Cake(Product):
    def __init__(self, name="не задано", filling="не задано", dough="не задано", expiration_date="1",quantity="1", company="не задано",hour="1" , minute="1", second="1"):
        super().__init__(company, hour , minute, second)
        self.__name = name
        self.__filling= filling
        self.__dough = dough

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def filling(self):
        return self.__filling

    @filling.setter
    def filling(self, filling):
        self.__filling = filling

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    def __str__(self):
        return "Название десерта: {} \t Начинка {} \t Тесто : {} \n{}".format(self.__name, self.__filling, self.__dough, Product.__str__(self))
