def EvenDis(iNum1,iNum2):
    for i in range(iNum1,iNum2 + 1):
        if(i % 2 == 0):
            print(i)

def main():
    print("Enter first number : ")
    iNo1 = int(input())

    print("Enter first number : ")
    iNo2 = int(input())

    EvenDis(iNo1, iNo2)

if __name__  == "__main__":
    main()