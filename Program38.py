def Display(iNum1, iNum2):
    for i in range(iNum1,iNum2 + 1):
        print(i)

def main():
    print("Enter the first number : ")
    iNo1 = int(input())

    print("Enter the first number : ")
    iNo2 = int(input())

    Display(iNo1,iNo2)

if __name__ == "__main__":
    main()