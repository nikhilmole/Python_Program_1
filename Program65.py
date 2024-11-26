def Pattern(iRows, iCols):
    ch1 = '\0'
    ch2 = '\0'
    
    for i in range(iRows):
        ch1 = chr(ord('A') + i)
        for j in range(iCols):
            ch2 = chr(ord('A') + j)
            print(ch1, end="\t")
        print()

def main():
    iNo1 = int(input("Enter the number of rows: "))
    iNo2 = int(input("Enter the number of columns: "))

    Pattern(iNo1, iNo2)

if __name__ == "__main__":
    main()
