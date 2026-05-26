# Filter Map

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)

    FData = list(filter(CheckEven, Data))

    MData = list(map(Increment,FData))

    print("Data after filter is : ",FData)

    print("Data after filter is : ",MData)


if __name__ == "__main__":
    main()