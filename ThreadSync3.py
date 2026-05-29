
import threading 

iCnt = 0
lobj = threading.Lock()

def Update():
    global iCnt 

    for _ in range(2000000):
        with lobj:                    # yacyamule kalta pvm la ki pudha critical section aahe lock cha lobj navach object banavlay
            iCnt += 1


if __name__ == "__main__":
    iCnt = 0

    t1 = threading.Thread(target=Update)
    t2 = threading.Thread(target=Update)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of iCnt is : ",iCnt)