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
         self.button.name = f"Button {self.name}"

    def clone(self):
        return copy.deepcopy(self)


class ControllerShallowCopy(ControllerInterface):

    def __init__(self, name: str, hardwaer: list, range: int, button: Button):
        self.name = name
        self.hardwaer = hardwaer
        self.range = range
        self.name_button = button.name
        self.button = button
        self.set_name_button()
        self.name_button = button.name
        self.button_i = button.i

    def set_name_button(self):
         self.button.name = f"Button {self.name}"

    def clone(self):
        return copy.copy(self)


if __name__ == '__main__':
    tumbler_button = Button(name="tumblet buttom", clik="clik")

    name = "A-Controller"

    a = ControllerShallowCopy(name, ["corpys", "button"], 2, tumbler_button)
    b = a.clone()
    b.button_i = "i B controller"
    b.name = "B-Controller"
    b.set_name_button()

    c = ControllerDeepCopy(name, [1, 2], 5, tumbler_button)
    c.name = "C-Controller"
    d = c.clone()
    d.name = "D-Controller"

    l = [a, b, c, d]
    for i in l:
        print(f"Button Name: {i.name_button}, Parameter i: {i.button_i}, Controller Name: {i.name}, Memory ID: {id(i)}")