class Factorial:
    def __init__(self,iValue):
        self.iNum = iValue
    
    def OddFacto(self):
        i = 0
        iFacto = 1

        for i in range(1, self.iNum +1):
            if(i % 2 != 0):
                iFacto = iFacto * i

        return iFacto

def main():
    print("Enter the number : ")
    iNo = int(input())

    fobj = Factorial(iNo)

    iRet = fobj.OddFacto()
    print(iRet)
    
if __name__ == "__main__":
    main()