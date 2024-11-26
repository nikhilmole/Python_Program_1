
def Pattern(iNum):
    i = 0
    ch = 'A'

    for i in range(iNum):
        print(ch)
        ch = chr(ord(ch) + 1)

def main():
    print("Enter the number : ")
    iNo = int(input())

    Pattern(iNo)

if __name__ == "__main__":
    main()