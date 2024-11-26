
def Pattern(iRows, iCols):

    for i in range(iRows):
        for j in range(iCols):
            if(i == j):
                print("$",end='\t')
            else:
                print("*",end='\t')
        print()

def main():
    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of rows : ")
    iNo2 = int(input())

    Pattern(iNo1 ,iNo2)
if __name__ == "__main__":
    main()