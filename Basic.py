class Basic:
    def __init__(self):
        self.x = 10

    def func(self):
        print("Basic Class")


class Base:
    def foo(self):
        print("This is Base")


class Child1(Basic):
    def func1(self):
        print("Child1 Class")


class Child2(Child1, Base):
    # def __init__(self):
    #     self.x = 20

    def func(self):
        print("Child2 Class: ", self.x, self.foo(), self.func1())


ch = Child2()
ch.func()
# print(Child2.__mro__)
