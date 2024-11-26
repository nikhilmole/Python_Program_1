def CountRange(iNum):
    iDigit = 0
    Freq = 0
    if(iNum < 0):
        iNum = -iNum
    while(iNum > 0):
        iDigit = iNum % 10
        if((iDigit > 3) and (iDigit < 7)):
            Freq = Freq + 1
        iNum = iNum // 10

    return Freq

def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = CountRange(iNo)
    print(iRet)

if __name__ == "__main__":
    main()