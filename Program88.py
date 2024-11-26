def Divisible(Arr,iLength):

    print("Divisible by 5 numbers is : ")
    for i in range(iLength):
        if(Arr[i] % 5 == 0):
            print(Arr[i])

def main():
    Arr = []
    print("How many you want to add in array : ")
    iSize = int(input())

    print("Enter the numbers : ")
    for i in range(iSize):
        iNo = int(input())
        Arr.append(iNo)

    Divisible(Arr, iSize)

if __name__ == "__main__":
    main()