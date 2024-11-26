class Nnumbers:
    def __init__(self,iSize):
        self.iLength = iSize
        self.Arr = []
        
    def Accept(self):
        print("Enter the numbers : ")
        for i in range(self.iLength):
            iNo = int(input())
            self.Arr.append(iNo)

    def EvenCount(self):
        iCnt = 0
        for i in range(self.iLength):
            if(self.Arr[i] % 2 == 0):
                iCnt = iCnt + 1
        return iCnt
def main():

    print("How many numbers you want to add : ")
    iSize = int(input())

    sobj = Nnumbers(iSize)

    sobj.Accept()
    iRet = sobj.EvenCount()
    print(f"Number of even count : {iRet}")
if __name__ == "__main__":
    main()