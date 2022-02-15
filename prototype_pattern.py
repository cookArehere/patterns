import copy
from abc import ABC, abstractmethod


class ControllerInterface(ABC):

    @abstractmethod
    def clone(self):
        pass


class Button():
    i = "button i"

    def __init__(self, name, clik):
        self.name = name
        self.clik = clik


class ControllerDeepCopy(ControllerInterface):

    def __init__(self, name: str, hardwaer: list, range: int, button: Button):
        self.name = name
        self.hardwaer = hardwaer
        self.range = range
        self.button = button
        self.set_name_button()
        self.name_button = button.name
        self.button_i = button.i

    def set_name_button(self):
        print("changed name button")
        self.button.name = f"Button {self.name}"

    def clone(self):
        return copy.deepcopy(self)


class ControllerShallowCopy(ControllerInterface):

    def __init__(self, name: str, hardwaer: list, range: int, button: Button):
        self.name = name
        self.hardwaer = hardwaer
        self.range = range
        self.button = button
        self.set_name_button()
        self.name_button = button.name
        self.button_i = button.i

    def set_name_button(self):
        print("changed name button")
        self.button.name = f"Button {self.name}"

    def clone(self):
        return copy.copy(self)


def chek_clon_metod():
    tumbler_button = Button(name="tumblet buttom", clik="clik")

    a = ControllerShallowCopy("A-Controller", ["corpys", "button"], 2, tumbler_button)

    b = a.clone()
    b.button_i = "i B controller"
    b.name = "B-Controller"
    b.set_name_button()
    b.hardwaer.append("newnewnew")
    b.range = 100000

    c = ControllerDeepCopy("C-Controller", [1, 2], 5, tumbler_button)
    c.name = "new Name"

    d = c.clone()
    d.name = "D-Controller"
    d.set_name_button()
    d.hardwaer.append("newnewnew")
    d.range = 100000

    # проверяю изменения в аргументе hardwaer: работает. При copy.copy изменяет аргумент в двух классах
    # при copy.deepcopy только в одном
    print(a.hardwaer, b.hardwaer)
    print(c.hardwaer, d.hardwaer)

    # проверяю изменения в аргументе range: не работает. При copy.copy должно изменить аргумент в двух классах
    print(a.range, b.range)
    print(c.range, d.range)

    # проверяю изменения в классе Button
    # аргумен name класса Controller меняется так же как и аргумент range (пример выше)
    # хотя при разных методах копирования должно наблюдатся разное поведение
    # функциия set_name_button не меняет имя кнопки класса Button
    # аргумент i класса Button при создании копии меняется только в скопированом классе
    l = [a, b, c, d]
    for i in l:
        print(
            f"Button Name: {i.name_button},\n Parameter i: {i.button_i},\n Controller Name: {i.name},\n Memory ID: {i}")


if __name__ == '__main__':
    chek_clon_metod()
