
def Pattern(iRows, iCols):
    if(iRows != iCols):
        iCols = iRows

    for i in range(1,iRows+1):
        for j in range(1,iRows+1):
            if(j <= iCols - i + 1):
                print("*\t",end='\t')
            else:
                print("#\t",end='\t')
        print()
def main():

    print("Enter the number of rows : ")
    iNo1 = int (input())

    print("Enter the number of rows : ")
    iNo2 = int (input())

    Pattern(iNo1 , iNo2)

if __name__ == "__main__":
    main()