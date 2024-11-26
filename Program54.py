def Pattern(iNum):
    i = 0

    for i in range(iNum,0,-1):
        print(i,"  #  ",end = ' ')

def main():
    print("Enter the number : ")
    iNo = int(input())

    Pattern(iNo)

if __name__ == "__main__":
    main()