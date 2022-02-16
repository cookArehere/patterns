from base_data import order

class SingletonMeta():

    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
        return cls._instances


class BaseDate(SingletonMeta):

    def geet_some_info(self, id:str):
        return order[id]



if __name__ == '__main__':

    s1 = BaseDate()
    s2 = BaseDate()

    print(s1.geet_some_info("id_1"))
    print(s2.geet_some_info("id_2"))
    print(s1 == s2)