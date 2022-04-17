class SingleTon(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__call__(*args, **kwargs)
            print(cls._instance)

        return cls._instance[cls]


class SingleTon2():

    _instance = {}

    def __new__(mcs, *args, **kwargs):
        if mcs not in mcs._instance:
            mcs._instance[mcs] = super().__new__(mcs)
        return mcs._instance


class Dog(metaclass=SingleTon):

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'Won! Won! My name is {self.name}!!')


class Cat(metaclass=SingleTon):

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'Miao! Miao! My name is {self.name}!!')


def main():
    a = Dog('Amy')
    b = Dog('Steve')
    c = Cat('Butter')
    a.bark()
    b.bark()
    c.bark()
    print(type(Dog))
    print(type(a))
    print(type(Cat))
    print(callable(a))


if __name__ == '__main__':
    main()
