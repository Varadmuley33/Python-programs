import gc

class Demo:
    No1 = 10     #class variable   class chya aat mahnun class variable
    No2 = 11     #class variable

    def __init__(self):

        #Instance Variable
        self.A = 101
        self.B = 201
        print("Inside Constructor")


    def __del__(self):
        print("Inside Descructor")


print(Demo.No1)     #class variable
print(Demo.No2)     #class variable

obj = Demo()

print(obj.A)
print(obj.B)



