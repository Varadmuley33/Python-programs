def main ():
    size = 0
    Value = 0 

    print("Enter the number of variables : ")
    size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(size):
        Value = int(input())
        Data.append(Value)

    sum = 0 

    for i in range(size):
        sum = sum + Data[i]

    print("Summation of Data is : ",sum)

if __name__ == "__main__":
    main()