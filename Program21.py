
def Pattern(iNum):
    for i in range(1,iNum):
        print(i)
def main():
    print("Enter the number : ")
    iNo = int(input())

    Pattern(iNo)

if __name__ == "__main__":
    main()