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

    def __init__(self, name: str, hardwaer: list, range: int):
        self.name = name
        self.hardwaer = hardwaer
        self.range = range
        self.button = Button(self.name, "clik")
        self.set_name_button()
        self.button_name = self.button.name
        self.button_i = self.button.i

    def set_name_button(self):
        print("changed name button")
        self.button.name = f"Button {self.name}"

    def clone(self):
        return copy.deepcopy(self)


class ControllerShallowCopy(ControllerInterface):

    def __init__(self, name: str, hardwaer: list, range: int):
        self.name = name
        self.hardwaer = hardwaer
        self.range = range
        self.button = Button(self.name, "clik")
        self.set_name_button()
        self.button_name = ""
        self.button_i = self.button.i

    def set_name_button(self):
        print("changed name button")
        self.button.name = f"Button {self.name}"
        self.button_name = self.button.name

    def clone(self):
        return copy.copy(self)


def chek_clon_metod():

    a = ControllerShallowCopy("A-Controller", ["corpys", "button"], 2)

    b = a.clone()
    b.button_i = "i B controller"
    b.name = "B-Controller"
    b.set_name_button()
    b.hardwaer.append("newnewnew")
    b.range = 100000

    c = ControllerDeepCopy("C-Controller", [1, 2], 5)

    d = c.clone()
    d.name = "D-Controller"
    d.set_name_button()
    d.hardwaer.append("newnewnew")
    d.range = 100000

    print(a.hardwaer, b.hardwaer)
    print(c.hardwaer, d.hardwaer)

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
            f"Controller Name: {i.name},\n Button Name: {i.button_name},\n Parameter i: {i.button_i},\n Memory ID: {i}")


if __name__ == '__main__':
    chek_clon_metod()
