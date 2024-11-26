def RevDisplay(Start , End):
    if(Start > End):
        print("Invalid Option")

    for i in range(End, Start-1, -1):
        print(i)

def main():
    print("Enter Starting point : ")
    iNo1 = int(input())

    print("Enter Ending point")
    iNo2 = int(input())

    RevDisplay(iNo1, iNo2)

if __name__ == "__main__":
    main()