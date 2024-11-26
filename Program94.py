def Search(Arr, iLength):
    bFlag = False

    for i in range(iLength):
        if(Arr[i] == 11):
            bFlag = True
            break

    return bFlag


def main():

    print("How many numbers you want to add in array : ")
    iSize = int (input())

    Arr = []

    print('Enter the numbers : ')
    for i in range(iSize):
        iNo = int(input())
        Arr.append(iNo)


    bRet = Search(Arr, iSize)
    if(bRet == True):
        print("11 is present")
    
    else:
        print("11 is not present")

if __name__ == "__main__":
    main()