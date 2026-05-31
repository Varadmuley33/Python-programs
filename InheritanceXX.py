class Parent:
    def __init__(self):
        print("Inside Parent constructor")

    def fun(self):
        print("Inside Fun method of parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child constructor")

    def fun(self):
        super().fun()
        print("Inside fun Method of child")


cobj = Child()

cobj.fun()



