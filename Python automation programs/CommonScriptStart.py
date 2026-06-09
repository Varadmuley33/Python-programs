import sys
import os 
import time
import schedule


def fun(DirName):
    pass

def main():

    Border = "-"*50
    print(Border)
    print("-----------Marvellous Data Shield System----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to : ")
            print("1 : Takes Auto backup at given time ")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of an backup periodically")

            
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes foe periodic scheduling ")
            print("SourceDirectory : Name of Directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    #python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside Projects logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])
        
        #Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])

        print("Data Sheild System started successfully")
        print("Time Interval in minutes :",sys.argv[1])
        print("Press ctrl + c to stop the execution")

        #wait till abort

        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Inavlid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")




    print(Border)
    print("----------Thank you for using our Script ---------")
    print(Border)
    
    

if __name__ == "__main__":
    main()