from abc import ABC, abstractmethod


class ProductInterface(ABC):

    @abstractmethod
    def get_price(self):
        pass


class Product(ProductInterface):

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class CompoundProduct(ProductInterface):

    def __init__(self, name: str):
        self.name = name
        self.products = []
        self.price = 0

    def get_price(self):
        price = 0
        for i in self.products:
            price += i.get_price()
        self.price = price
        return self.price

    def add_product(self, product: ProductInterface):
        self.products.append(product)

    def remove_product(self, product: ProductInterface):
        self.products.remove(product)


if __name__ == '__main__':

    dough_ingredients = {"flour": 3.5, "edge": 1, "sugar": 2.1}
    dough = CompoundProduct("dough")

    for name, price in dough_ingredients.items():
        dough.add_product(Product(name, price))

    topping_ingredients = {"chicken": 10, "cheese": 5, "tomato": 2.5, "pineapple": 8.7}
    topping = CompoundProduct("topping")

    for name, price in topping_ingredients.items():
        topping.add_product(Product(name, price))

    pizza = CompoundProduct("pizza")
    pizza.add_product(dough)
    pizza.add_product(topping)

    print(dough.products)
    print(pizza.get_price())
