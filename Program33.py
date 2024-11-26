

def DifOddEvenFacto(iNum):
    i = 0
    iOddFacto = 1
    iEvenFacto = 1

    if(iNum < 0):
        iNum = -iNum
    
    for i in range(1, iNum + 1):
        if(i % 2 == 0):
            iEvenFacto = iEvenFacto * i
        
        else:
            iOddFacto = iOddFacto * i
    
    return iEvenFacto - iOddFacto

def main():
    print("Enter the number : ")
    iNo = int(input())

    iRet = DifOddEvenFacto(iNo)
    print(iRet)

if __name__ == "__main__":
    main()