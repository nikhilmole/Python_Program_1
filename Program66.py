class Display:
    def __init__(self,iRo, iCo):
        self.iRows = iRo
        self.iCols = iCo

    def Pattern(self):

        i = self.iRows
        j = self.iCols

        for i in range(self.iRows,0,-1):
            for j in range(self.iCols,0,-1):
                print(i,"   ",end='')

            print()

def main():

    print("Entee the number of rows : ")
    iNo1 = int(input())

    print("Enter the number of cols : ")
    iNo2 = int(input())

    dobj = Display(iNo1,iNo2)
    dobj.Pattern()

if __name__ == "__main__":
    main()