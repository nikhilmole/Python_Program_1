def DigiMulti(iNum):
    iDigit = 0
    Freq = 0
    iMulti = 1
    if(iNum < 0):
        iNum = -iNum
    while(iNum > 0):
        iDigit = iNum % 10
        iMulti = iMulti * iDigit;    
        iNum = iNum // 10

    return iMulti

def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = DigiMulti(iNo)
    print(iRet)

if __name__ == "__main__":
    main()