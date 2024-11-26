def EvenDivisible(Arr, iLenght):
    print("The number are even and divisible by 5 are : ")
    for i in range(iLenght):
        if(Arr[i] % 5 == 0) and(Arr[i] % 2 == 0):
            print(Arr[i])

def main():

    P = []
    print("How many number you want to add in Array : ")
    iSize = int(input())

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    EvenDivisible(P,iSize)

if __name__ == "__main__":
    main()