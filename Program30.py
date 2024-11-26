
def DollerToINR(iNum):
    Rs = 70
    Ans = Rs * iNum
    return Ans
def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = DollerToINR(iNo)
    print("Doller into indian rs is : ",iRet)

if __name__ == "__main__":
    main()