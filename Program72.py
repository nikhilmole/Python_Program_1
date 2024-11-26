def Pattern(iRows,iCols):

    for i in range(iRows):
        for j in range(1,iCols+1):
            print((i+j),"\t",end = '')
        print()

def main():

    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of cols : ")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)

if __name__ == "__main__":
    main()