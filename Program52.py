def SumEvenOdd(iNum):
    iDigit = 0
    OddSum = 0
    EvenSum = 0
    
    if(iNum < 0):
        iNum = -iNum
    while(iNum > 0):
        iDigit = iNum % 10
        if(iDigit % 2 == 0):
            EvenSum = EvenSum + iDigit
        else:
            OddSum = OddSum + iDigit
        iNum = iNum // 10

    return EvenSum - OddSum

def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = SumEvenOdd(iNo)
    print(iRet)

if __name__ == "__main__":
    main()