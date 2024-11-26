def Difference(Arr, iLength):
    
    SumEven = 0
    SumOdd = 0
    Ans = 0

    for i in range(iLength):
        if(Arr[i] % 2 == 0):
            SumEven = SumEven + Arr[i]
        else:
            SumOdd = SumOdd + Arr[i]
    
    Ans = SumEven - SumOdd
    return Ans



def main():

    Arr = [] 
    iRet = 0

    print("Enter the numbers : ")
    iSize = int(input())

    print("Enter the number of elements : ")
    for i in range(iSize):
        iNo = int(input())
        Arr.append(iNo)

    iRet = Difference(Arr, iSize)
    print(iRet)
if __name__ == "__main__":
    main()