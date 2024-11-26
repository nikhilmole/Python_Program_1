def Pattern(iRows, iCols):
    ch1 = '\0'
    ch2 = '\0'
    for i in range(iRows):
        ch1 = chr(ord('a') + i)
        for j in range(iCols):
            ch2 = chr(ord('a') + j)
            if(i % 2 == 0):
                print(j+1,"\t",end = ' ')
            else:
                print(ch2,"\t",end = ' ')
        print()
def main():
    print("Enter the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of rows : ")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)

if __name__ == "__main__":
    main()