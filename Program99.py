def LastOcc(Arr, iLength, iNum):

    for i in range(iLength-1,0,-1):
        if(Arr[i] == iNum):

            return i + 1
        
    return -1

def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    print("Enter number to find Last oCcurance : ")
    iNo = int(input())

    iRet = LastOcc(P, iSize, iNo)

    if(iRet == -1):
        print("The number is not presnt")

    else:
        print("The last occurance is : ",iRet)

if __name__ == "__main__":
    main()