"""
Practice metaclass

"""


class MyMeta(type):
    def __new__(mcls, name, base, attrs):
        name = 'Funky' + name
        _attrs = (('my_' + name, val) for name, val in attrs.items())
        _attrs = dict((name, val) for name, val in _attrs)
        return super().__new__(mcls, name, base, _attrs)


class MyClass(object, metaclass=MyMeta):
    def do_something(self):
        print('Do something!')


def main():
    base_object = MyClass()
    print(dir(MyClass))
    base_object.my_do_something()


if __name__ == '__main__':
    main()
