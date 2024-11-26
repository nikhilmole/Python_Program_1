def DisplayDigits(iNum):
    Digit = 0

    while(iNum > 0):
        Digit = iNum % 10
        print(Digit)
        iNum = iNum // 10

def main():
    print("Enter the number ")
    iNo = int(input())

    DisplayDigits(iNo)

if __name__ == "__main__":
    main()