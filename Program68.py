
def Pattern(iRows, iCols):
    
    iCnt = 1

    for i in range(1,iRows+1):
        for j in range(1, iCols+1):
            print(iCnt,"\t",end=' ')
            iCnt = iCnt + 1

            if(iCnt == 10):
                iCnt = 1

        print()

def main():

    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of cols : ")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)

if __name__ == "__main__":
    main()