def SquareMeter(iValue):
    Ans = 0.0929 * iValue

    return Ans

def main():
    print("Enter area in square fit : ")
    iNo = int(input())

    dRet = SquareMeter(iNo)
    print(dRet)

if __name__ == "__main__":
    main()