def Divi(Arr, iLength):

    print("Number divisible 11 is : ")
    for i in range(iLength):
        if(Arr[i] % 11 == 0):
            print(Arr[i])


def main():

    P = []

    print("How many numbers you want to add : ")
    iSize = int(input())

    print("Enter the numbers : ")
    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    Divi(P, iSize)

if __name__ == "__main__":
    main()