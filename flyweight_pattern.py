from random import choice as ch

class TreeType:

    def __init__(self, name, color, texture):
        self.__name = name
        self.__color = color
        self.__texture = texture

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def texture(self):
        return self.__texture


class Tree:

    def __init__(self, x, y, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        return f"Draw Tree {self.tree_type.name}, {self.tree_type.color}, {self.tree_type.texture}, in place {self.x}, {self.y}"


class TreeFactory:

    def __init__(self, ):
        self.__flyweight_tree_type = {}

    def get_tree(self, name, color, texture, x, y):
        key = "_".join(sorted([name, color, texture]))
        if key in self.__flyweight_tree_type:
            return Tree(x, y, self.__flyweight_tree_type[key]).draw()
        else:
            self.__flyweight_tree_type[key] = TreeType(name, color, texture)
            return Tree(x, y, self.__flyweight_tree_type[key]).draw()

    def get_catlog_flyweight(self):
        return self.__flyweight_tree_type



if __name__ == '__main__':

    forest = []
    tree_factory = TreeFactory()

    name = ["oak", 'pine', 'birch']
    color = ["green", "lite green", "dark green"]
    texture = ["texture1", "texture2", "texture3"]

    element = 0

    while element < 100:
        forest.append(tree_factory.get_tree(ch(name), ch(color), ch(texture), 1, 1))
        element += 1

    print(tree_factory.get_catlog_flyweight())
    print(forest)

    flag = "not same TreeType"
    l = []

    for i in tree_factory.get_catlog_flyweight():
        if i in l:
            flag = "have same key"
        else:
            l.append(i)

    print(flag)




