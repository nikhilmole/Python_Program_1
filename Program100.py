def Range(Arr, iLength, iStart, iEnd):

    for i in range(iLength):
        if(Arr[i] > iStart)and(Arr[i] < iEnd):
            print(Arr[i],end = '\t')


def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    print("Enter starting range")
    iNo1 = int(input())

    print("Enter ending range")
    iNo2 = int(input())

    Range(P, iSize, iNo1, iNo2)

if __name__ == "__main__":
    main()