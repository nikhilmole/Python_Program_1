def Pattern(Rows,Cols):

    for i in range(1,Rows+1):
        for j in range(1,Cols+1):
            print(j,end = ' ')
        print()

def main():
    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number ofd columns : ")
    iNo2 = int(input())

    Pattern(iNo1,iNo2)

if __name__ == "__main__":
    main()