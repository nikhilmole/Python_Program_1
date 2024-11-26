def RangeAdd(iNum1, iNum2):
    Ans = 0
    if(iNum1 > iNum2):
        print("Invalid option beacuse 1 st number is greater than second ")
        return 0
    
    for i in range(iNum1, iNum2 + 1):
        Ans = Ans + i
    return Ans

def main():

    print("Enter first number : ")
    iNo1 = int(input())

    print("Enter Scond number : ")
    iNo2 = int(input())

    iRet = RangeAdd(iNo1, iNo2)

    if(iNo1 <= iNo2):
        print(iRet)

if __name__ == "__main__":
    main()