from abc import ABC, abstractmethod
from random import randint


class BakerInterface(ABC):

    @abstractmethod
    def to_bake(self):
        pass

    @abstractmethod
    def product(self):
        pass


class BakeInterface(ABC):

    @abstractmethod
    def get_bake(self):
        pass


class Bread(BakeInterface):

    def __init__(self, name):
        self.name = name

    def get_bake(self):
        return f"I'm {self.name}"


class Bun(BakeInterface):

    def __init__(self, name, addition):
        self.name = name
        self.addition = addition

    def get_bake(self):
        return f"I'm {self.name} with {self.addition}"


class BreadBaker(BakerInterface):

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.purpose = "wheat bread"

    def to_bake(self):
        self.count += 1
        bread = Bread(self.purpose)
        return bread

    def product(self):
        if self.count > 1:
            return self.purpose + "s"
        return self.purpose


class BunBaker(BakerInterface):

    def __init__(self, name, addition):
        self.name = name
        self.addition = addition
        self.count = 0
        self.purpose = "bun"

    def to_bake(self):
        self.count += 1
        bun = Bun(self.purpose, self.addition)
        return bun

    def product(self):
        prod = self.purpose

        if self.count > 1:
            prod = self.purpose + "s"

        return f"{prod} with {self.addition}"


if __name__ == '__main__':

    CavinBreadBaker = BreadBaker(name="Cavin")
    AustinBunBaker = BunBaker(name="Austin", addition="cherry")

    random_int = randint(1, 10)
    i = 0

    stock = []

    while i < random_int:
        e = randint(1, 2)
        stock.append(CavinBreadBaker.to_bake())
        if e == 1:
            AustinBunBaker.to_bake()
        i += 1

    print(f"Hello I'm baker {CavinBreadBaker.name}. Today I baked {CavinBreadBaker.count} {CavinBreadBaker.product()}.")
    print(f"Hello I'm baker {AustinBunBaker.name}. Today I baked {AustinBunBaker.count} {AustinBunBaker.product()}.")
    print(stock)

    # checking memory address object
    for i in stock:
        print(id(i))
