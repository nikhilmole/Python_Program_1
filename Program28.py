
def Table(iNum):
    for i in range(1,10+1):
        print(f"{iNum} * {i} = {iNum * i}")

def main():
    print("Enter the number : ")
    iNo = int(input())

    Table(iNo)

if __name__ == "__main__":
    main()