def PhToCs(temp):
    Celcius = (temp - 32) * (5/9)
    return Celcius

def main():
    print("Enter temprature : ")
    iNo = int(input())

    iRet = PhToCs(iNo)
    print(iRet)
if __name__ == "__main__":
    main()