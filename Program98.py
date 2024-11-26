def FirstOcc(Arr, iLength, iNum):

    for i in range(iLength):
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

    print("Enter number you want get First occurunce")
    iNo = int(input())

    iRet = FirstOcc(P, iSize, iNo)

    if(iRet == -1):
        print("The number not present")
    else:
        print("The number First occurunce is : ",iRet)

if __name__ == "__main__":
    main()