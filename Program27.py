
class Facto:
    def __init__(self,iValue):
        self.iNum = iValue

    def Factorial(self):
        iFacto = 1

        for i in range(1,self.iNum+1):
            iFacto = iFacto * i
        
        return iFacto

def main():
    print("Enter the number : ")
    iNo = int(input())

    fobj = Facto(iNo)

    iRet = fobj.Factorial()

    print("Factorial is : ",iRet)

if __name__ == "__main__":
    main()