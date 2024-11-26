
def Factorial(iNum):
    i = 0

    for i in range(1,iNum//2):
        if((iNum % i) == 0):
            print(i)

def main():
    iNo = 0

    print("Enter the number : ")
    iNo = int(input())

    Factorial(iNo)

if __name__ == "__main__":
    main()