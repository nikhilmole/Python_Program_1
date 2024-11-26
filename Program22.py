
def Pattern(iNum):
    for i in range (-iNum,iNum+1):
        print(i,end=" ")

def main():
    print("Enter the number : ")
    iNo = int(input())

    Pattern(iNo)

if __name__ == "__main__":
    main()