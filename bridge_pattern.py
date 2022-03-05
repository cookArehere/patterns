from abc import ABC, abstractmethod
from random import randint, choice


class Game(ABC):

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def game(self):
        pass

    @abstractmethod
    def get_prize(self, point):
        pass


class Prize:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class GameWithInt(Game):

    def __init__(self, name):
        self.name = name
        self.__prize = []
        self.__tumbler = 10
        self.__limit = 100
        self.__a = 0
        self.__b = 0
        self.__separator = ""

    @property
    def tumbler(self):
        return self.__tumbler

    @tumbler.setter
    def tumbler(self, tumbler):
        self.__tumbler = tumbler

    @property
    def prize(self):
        return self.__prize

    @prize.setter
    def prize(self, new_prize: Prize):
        self.__prize.append(new_prize)

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    def play(self):
        result = self.game()
        print(f"Questioh: {self.__a} {self.__separator} {self.__b} = ?")
        i = input("Your result: ")
        if int(i) == result:
            return "Wining"
        else:
            return "Losing"

    def game(self):
        self.__a = randint(0, self.__tumbler)
        self.__b = randint(0, self.__tumbler)
        self.__separator = choice(["+", "-", "*"])
        if self.__separator == "+":
            return self.__a + self.__b
        elif self.__separator == "-":
            return self.__a - self.__b
        elif self.__separator == "*":
            return self.__a * self.__b

    def get_prize(self, point):
        quantity_prize = len(self.__prize) - 1
        prize_index = randint(0, quantity_prize)
        if point >= self.__limit:
            return self.__prize[prize_index]
        else:
            return f"You have {point} points.\nNeeds {self.__limit} point."


class User():

    def __init__(self, game: Game):
        self.game = game


class Player(User):

    def __init__(self, game, name):
        super(Player, self).__init__(game=game)
        self.name = name
        self.point = 0

    def play_game(self):
        if self.game.play() == "Wining":
            print("Wining")
            self.point += 10
        else:
            print("Losing")

    def get_prize(self):
        return self.game.get_prize(self.point)


class Admin(User):

    def __init__(self, game, name):
        super(Admin, self).__init__(game=game)
        self.name = name

    def get_tumbler(self):
        return game.tumbler

    def set_tumbler(self, tumbler):
        game.tumbler = tumbler

    def check_limit_points(self):
        return game.limit

    def set_limit_point(self, limit: int):
        game.limit = limit

    def check_prize(self):
        return game.prize

    def add_prize(self, prize: Prize):
        game.prize.append(prize)
        print(f"Prize {prize} added")

    def remove_prize(self, prize: Prize):
        game.prize.remove(prize)
        print(f"Prize {prize} removed")


if __name__ == '__main__':

    game = GameWithInt("game")
    player = Player(game, name="Alik")
    admin = Admin(game, name="admin")

    prize1 = Prize("hat")
    prize2 = Prize("boots")
    prize3 = Prize("cloak")

    prize_list = [prize1, prize2, prize3]

    for i in prize_list:
        admin.add_prize(i)

    admin.set_tumbler(11)
    admin.set_limit_point(20)
    print(admin.check_prize())

    while input("You want play?: ") == "y":
        player.play_game()
        print(player.point)

    print(player.get_prize())
