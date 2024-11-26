
def OddNumber(iNum):
    for i in range(1,iNum):
        if(i % 2 != 0):
            print(i,end=" ")
def main():

    print("Enter the number : ")
    iNo = int(input())

    OddNumber(iNo)

if __name__ == "__main__":
    main()