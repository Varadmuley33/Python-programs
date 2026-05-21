def EmployeeInfo(Name = "Rahul", Age = 21, Salary = 1000, City = "Pune"):
    print("Name : " , Name)
    print("Age : ",Age)
    print("Salary : " , Salary)
    print("City : ",City)

def main():
    #Keyword 
    #EmployeeInfo(Age=26,Name="Rahul",City="Pune",Salary=2000.50)         # Correct
    EmployeeInfo()
   

if __name__ == "__main__":
    main()