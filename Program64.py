
def Pattern(iRows,iCols):
    for i in range(1,iRows+1):
        ch1 = 65
        for j in range(1,iCols+1):
            if(i % 2 == 0):
                print((chr)(ch1 + 32),end = ' ')
            else:
                print((chr)(ch1),end = ' ')
            ch1 = ch1 + 1
        print()
            
        

def main():

    print("Enter the rows : ")
    iNo1 = int(input())

    print("Enter the rows : ")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)

if __name__ == "__main__":
    main()