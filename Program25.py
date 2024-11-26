def Number(iNum):
    if(iNum <= 50):
        print("Small")
    elif(iNum < 100) and (iNum > 50):
        print("medium")
    elif(iNum > 100):
       print("Greater")

def main():
    print("Enter the number : ")
    iNo = int(input())

    Number(iNo);
if __name__ == "__main__":
    main()