def Pattern(iRows,iCols):

    for i in range(iRows):
        for j in range(iCols):
            if(i == j)or(i > j):
                print("*","\t",end = '')
            else:
                print("#","\t",end = '')
        print()
def main():

    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of column : ")
    iNo2 = int(input())

    Pattern(iNo1 , iNo2)

if __name__ == "__main__":
    main()