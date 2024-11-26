def Frequency(Arr, iLength):
    iCnt = 0

    for i in range(iLength):
        if(Arr[i] == 11):
            iCnt = iCnt + 1

    return iCnt

def main():
    P = []

    print("How many numbers you want add : ")
    iSize = int(input())

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    iRet = Frequency(P, iSize)
    print("11 Frequency is : ",iRet)
    
if __name__ == "__main__":
    main()