def Divi(Arr, iLength):

    print("The number divisible by 3 and 2 are : ")
    for i in range(iLength):
        if(Arr[i] % 5 == 0)and(Arr[i] % 3 == 0):
            print(Arr[i])

def main():

    P = []
    print("How many number you want to add : ")
    iSize = int(input())

    print("Enter the numbers : ")
    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    Divi(P,iSize)

if __name__ == "__main__":
    main()