def Pattern(Rows,Cols):
    i = 1
    j = 1
    for i in range(Rows,0,-1):
        for j in range(Cols,0,-1):
            print(j,"  ",end = ' ')
        print()

def main():
    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number ofd columns : ")
    iNo2 = int(input())

    Pattern(iNo1,iNo2)

if __name__ == "__main__":
    main()