def Pattern(iRows, iCols):
    i = 0
    j = 0
    iCnt = 0

    for i in range(1,iRows+1):
        for j in range(1,iCols+1):
            iCnt =iCnt + 1
            print(iCnt,end=' ')
        print()


def main():
    print("enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of cols :")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)
if __name__ == "__main__":
    main()