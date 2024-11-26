
def CircleArea(PI,Radius):
    Area = PI * Radius * Radius
    return Area
def main():
    PI = 3.14
    print("Enter the Radius : ")
    iNo = float(input())

    iRet = CircleArea(PI,iNo)
    print(iRet)
if __name__ == "__main__":
    main()