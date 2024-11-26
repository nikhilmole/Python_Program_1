
def Number(iNum):
    if(iNum < 0):
        iNum = -iNum
        
    if(iNum == 0):
        print("Zero")

    elif(iNum == 1):
        print("One")
    
    elif(iNum == 2):
        print("Two")

    elif(iNum == 3):
        print("Three")
    
    elif(iNum == 4):
        print("Four")

    elif(iNum == 5):
        print("Five")

    elif(iNum == 6):
        print("Six")

    elif(iNum == 7):
        print("Seven")

    elif(iNum == 8):
        print("Eight")

    elif(iNum == 9):
        print("Nine")
    
    else:
        print("Invalid option")

def main():
    print("Enter the number : ")
    iNo = int(input())

    Number(iNo)

if __name__ == "__main__":
    main()