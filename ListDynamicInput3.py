def Summation(Arr):
    sum = 0 

    for i in range(len(Arr)):
        sum = sum + Arr[i]
    
    return sum

def main ():
    size = 0
    Value = 0 
    Ret = 0

    print("Enter the number of elements : ")
    size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(size):
        Value = int(input())
        Data.append(Value)

    Ret = Summation(Data)

    print("Summation of Data is : ",Ret)

if __name__ == "__main__":
    main()