def Pattern(iNum):
    i = 0
    for i in range(1,iNum+1):
        print(i * 2)

def main():
    print("Enter the number : ")
    iNo = int(input())

    Pattern(iNo)

if __name__ == "__main__":
    main()