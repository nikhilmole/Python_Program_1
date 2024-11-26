class NonFacto:
    def __init__(self,iNum):
        self.Value = iNum
    
    def NonFactoSum(self):
        iSum = 0
        for i in range(1,self.Value):
            if(self.Value % i != 0):
                iSum = iSum + i
        return iSum

def main():
    print("Enter the number : ")
    iNo = int(input())

    dll = NonFacto(iNo)

    iRet = dll.NonFactoSum()
    print("The summation of non factos are : ",iRet)
    
if __name__ == "__main__":
    main()