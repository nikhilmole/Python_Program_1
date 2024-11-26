
def Multiple(iNum):
    for i in range(1,5+1):
        print(iNum * i)
def main():
    iNo = 0

    print("Enter the number ; ");
    iNo = int(input())

    Multiple(iNo)

if __name__ == "__main__":
    main()