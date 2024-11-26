def Freq(Arr, iLength, iNum):

    iCnt = 0

    for i in range(iLength):
        if(Arr[i] == iNum):
            iCnt = iCnt + 1

    return iCnt

def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []
    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    print("Enter number that you want to get freq : ")
    iNo = int(input())

    iRet = Freq(P, iSize, iNo)

    print(f"Frequency of number {iNo} is : {iRet}")
if __name__ == "__main__":
    main()