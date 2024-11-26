
def EvenFactorial(iNum):
    iFacto = 1
    if(iNum < 0):
        iNum = -iNum
    for i in range(1,iNum + 1):
        if(i % 2 == 0):
            iFacto = iFacto * i

    return iFacto
def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = EvenFactorial(iNo)
    print(iRet)

if __name__ == "__main__":
    main()