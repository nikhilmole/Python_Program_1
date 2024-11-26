def Pattern(iRows, iCols):
    
    for i in range(iRows):
        ch1 = 'A'
        for j in range(iCols):
            print(ch1, end=" ")
            ch1 = chr(ord(ch1) + 1) 
        print() 

def main():
    print("Enter the Rows: ")
    iNo1 = int(input())

    print("Enter the Cols: ")
    iNo2 = int(input())

    Pattern(iNo1, iNo2)


if __name__ == "__main__":
    main()
