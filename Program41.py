def EvenAdd(iNum1,iNum2):
    Ans = 0
    if(iNum1 > iNum2):
        print("Invalid Option")
    for i in range(iNum1, iNum2 + 1):
        if(i % 2 == 0):
            Ans = Ans + i

    return Ans

def main():

    print("Enter the first number : ")
    iNo1 = int(input())

    print("Enter the first number : ")
    iNo2 = int(input())

    iRet = EvenAdd(iNo1, iNo2)

    if(iNo1 <= iNo2):
        print(iRet)

if __name__ == "__main__":
    main()