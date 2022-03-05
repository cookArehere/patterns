
class GetInt:

    def get_inf(self):
        return 1234567890

class GetStr:

    def get_inf(self):
        return "1234567890"

class Adapter(GetStr):

    def __init__(self, get_int: GetInt):
        self.get_int = get_int

    def get_inf(self):
        return str(get_int.get_inf())

def work_with_str(object: GetStr):
    return "Result: " + object.get_inf()

if __name__ == '__main__':


    get_int = GetInt()
    get_str = GetStr()
    adapter = Adapter(get_int)

    try:
        work_with_str(get_int)
    except TypeError:
        print("Need use GetStr object")

    print(work_with_str(get_str))
    print(work_with_str(adapter))