class Demo:
    No = 10      #class variable

    def __init__(self,A,B):    #It is written to create an instance
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside Instance method fun",self.Value1,self.Value2)

    @classmethod     #Decorator
    def sun(cls):
        print("Inside Class method sun",cls.No)

    @staticmethod
    def gun():
        print("Inside Static method gun",Demo.No)

Demo.sun()
print("Class Variable No : ",Demo.No)

obj = Demo(11,21)

obj.fun()
print("Instance Variable : ",obj.Value1,obj.Value2)

obj.gun()

