def Search(Arr, iLength, iNum):
    bFlag = False

    for i in range(iLength):
        if(Arr[i] == iNum):
            bFlag = True
            break

    return bFlag



def main():

    print("How many numbers you want to add in array : ");
    iSize = int(input())

    P = []

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    print("Enter number you want search is present or not")
    iNo = int(input())

    bRet = Search(P, iSize, iNo)
    
    if(bRet == True):
        print("True")
    
    else:
        print("False")

if __name__ == "__main__":
    main()