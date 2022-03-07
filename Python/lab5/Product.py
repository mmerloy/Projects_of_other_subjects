from Time_default import Time


class Product(Time):
    def __init__(self, company,hour , minute, second):
        super().__init__(hour , minute, second)
        self.__company = company


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company



    def __str__(self):
        return "Компания , производящая товар: {} \t Время производства товара {} \n".format(self.__company,  Time.__str__(self))
