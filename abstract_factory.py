from abc import ABC, abstractmethod

class AbstractFactory(ABC):

    @abstractmethod
    def made_shirt(self, size, material):
        pass

    @abstractmethod
    def made_pants(self, size, material):
        pass

    @abstractmethod
    def made_jacket(self, size, material):
        pass

class Product(ABC):

    @abstractmethod
    def specification(self):
        pass

class Shirt(Product):

    def __init__(self,name , label, size, material):
        self.name = name
        self.label = label
        self.size = size
        self.material = material

    def specification(self):
        return f"{self.name}: {self.label}, {self.size}, {self.material}."


class Pants(Product):

    def __init__(self,name , label, size, material):
        self.name = name
        self.label = label
        self.size = size
        self.material = material

    def specification(self):
        return f"{self.name}: {self.label}, {self.size}, {self.material}."


class Jacket(Product):

    def __init__(self,name , label, size, material):
        self.name =name
        self.label = label
        self.size = size
        self.material = material

    def specification(self):
        return f"{self.name}: {self.label}, {self.size}, {self.material}."

class GucciFactory(AbstractFactory):

    def __init__(self):
        self.name = "Gucci"

    def made_shirt(self, size, material):
        shirt = Shirt(name="Shirt", label=self.name, size=size, material=material)
        return shirt

    def made_pants(self, size, material):
        pants = Pants(name="Shirt", label=self.name, size=size, material=material)
        return pants

    def made_jacket(self, size, material):
        jacket = Jacket(name="Shirt", label=self.name, size=size, material=material)
        return jacket

class PradaFactory(AbstractFactory):

    def __init__(self):
        self.name = "Prada"

    def made_shirt(self, size, material):
        shirt = Shirt(name="Shirt", label=self.name, size=size, material=material)
        return shirt

    def made_pants(self, size, material):
        pants = Pants(name="Shirt", label=self.name, size=size, material=material)
        return pants

    def made_jacket(self, size, material):
        jacket = Jacket(name="Shirt", label=self.name, size=size, material=material)
        return jacket

class Shop():

    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def buy_shirt(self, size, material):
        return self.factory.made_shirt(size, material)

    def buy_pants(self, size, material):
        return self.factory.made_pants(size, material)

    def buy_jacket(self, size, material):
        return self.factory.made_jacket(size, material)

if __name__ == '__main__':

    label = "Gucci"
    factory: AbstractFactory = None

    if label == "Gucci":
        factory = GucciFactory()
    elif label == "Prada":
        factory = PradaFactory()

    shop = Shop(factory)

    print(shop.buy_shirt(size="S", material="cotton"), shop.buy_pants(size="S", material="cotton"))

