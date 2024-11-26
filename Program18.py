def NonFacto(iNum):
    if(iNum < 0):
        iNum = -iNum
    
    for i in range(1,iNum):
        if(iNum % i != 0):
            print("Non Factoroial number is : ",i)
        

def main():
    print("Enter the number : ")
    iNo = int(input())

    NonFacto(iNo)

if __name__ == "__main__":
    main()