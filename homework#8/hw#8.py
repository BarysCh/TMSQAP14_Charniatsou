class Instrument():
    shop_name = "Music"

    def __init__(self, name, material, age, price):
        self.name = name
        self.material = material
        self._age = age #protected
        self._price = price #protected

    def tune(self):
        print(f"The {self.name} needs to be tuned every day.")

    def sell(self, age, price, discount=None):
        if discount is not None:
            self.price = self.price - discount*self.price/100
        else:
            if self.age > 10:
                self.price /= 2
        return self.price

    @classmethod
    def print_shop_name(cls):
        print(f"The name of the shop is {cls.shop_name}") #метод класса

    @staticmethod
    def warranty():
        print("The warranty is valid for three years") #статический метод


class Guitar(Instrument):
    def __init__(self, name, material, age, price, number_of_strings):
        super().__init__(name, material, age, price)
        self.__number_of_strings = number_of_strings #private

    def tune(self):
        print(f"The {self.name} needs to be tuned once in two days.") #переопределение метода

    def sell(self, age, price, discount): #используется перегрузка метода
        if discount is not None:
            self.price = self.price - discount*self.price/100
        else:
            if self.age > 10:
                self.price /= 2
        return self.price

