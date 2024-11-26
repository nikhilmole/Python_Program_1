class Nnumbers:
    def __init__(self,iSize):
        self.iLength = iSize
        self.Arr = []
    
    def Accept(self):
        for i in range(self.iLength):
            iNo = int(input())
            self.Arr.append(iNo)
    
    def DifEvenOdd(self):
        OddCount = 0
        EvenCount = 0

        for i in range(self.iLength):
            if(self.Arr[i] % 2 == 0):
                EvenCount = EvenCount + 1
            
            else:
                OddCount = OddCount + 1

        return EvenCount - OddCount


def main():

    print("How many numbers you want to add : ")
    iSize = int(input())

    nobj = Nnumbers(iSize)

    nobj.Accept()
    iRet = nobj.DifEvenOdd()
    print(iRet)

if __name__ == "__main__":
    main()