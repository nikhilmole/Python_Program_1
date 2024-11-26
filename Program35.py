def KMToMeter(meter, Kilometer):
    Ans = meter * Kilometer

    return Ans

def main():
    meter = 1000
    iNo = 0

    print("Enter meter : ")
    iNo = int(input())

    iRet = KMToMeter(meter,iNo)
    print(iRet)

if __name__ == "__main__":
    main()