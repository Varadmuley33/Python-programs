import gc

class Demo:
    No1 = 10     #class variable   class chya aat mahnun class variable
    No2 = 11     #class variable

    def __init__(self):
        print("Inside Constructor")


    def __del__(self):
        print("Inside Descructor")


print(Demo.No1)     #class variable
print(Demo.No2)     #class variable



