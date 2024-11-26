def DisplayDigits(iNum):
    Digit = 0

    while(iNum > 0):
        Digit = 0
        Digit = iNum % 10
        iNum = iNum // 10
        if(Digit == 0):
            return True

def main():
    print("Enter the number ")
    iNo = int(input())

    iRet = DisplayDigits(iNo)

    if(iRet == True):
        print("Zero Available")
    else:
        print("No Zero")

if __name__ == "__main__":
    main()