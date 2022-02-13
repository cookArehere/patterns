from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):

    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def water(self, t: int, ml: int):
        pass

    @abstractmethod
    def green_tee(self):
        pass

    @abstractmethod
    def black_tee(self):
        pass

    @abstractmethod
    def coffee(self, count: int):
        pass

    @abstractmethod
    def sugar(self, count: int):
        pass

class CoffeeBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def product(self):
        product = self._product
        self.reset()
        return product

    def water(self, t: int, ml:int):
        self._product.add(f"Watter {ml} ml {t} degrees")

    def green_tee(self):
        self._product.add("Green tee")

    def black_tee(self):
        self._product.add("Black tee")

    def coffee(self, count: int):
        self._product.add(f"Coffe {count} g.")

    def sugar(self, count: int):
        self._product.add(f"Sugar {count} parts")

class Product():

    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts: {', '.join(self.parts)}", end="")

class Director:

    def __init__(self):
        self.__builder = None

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder: Builder):
        self.__builder = builder

    def get_green_tee(self, suger:int):
        self.builder.water(t=90, ml=80)
        self.builder.green_tee()
        self.builder.sugar(suger)

    def get_coffee(self, suger: int):
        self.builder.water(t=95, ml=80)
        self.builder.coffee(count=12)
        self.builder.sugar(suger)

if __name__ == '__main__':
    director = Director()
    builder = CoffeeBuilder()
    director.builder = builder

    print("Your Green tee:")
    director.get_green_tee(suger=2)
    builder.product().list_parts()

    print("\n")

    print("Your coffee:")
    director.get_coffee(suger=0)
    builder.product().list_parts()