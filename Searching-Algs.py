def choice():
    print("1.Linear Search")
    print("1.Binary Search")

    c = int(input("Enter your choice: "))

    if c == 1:
        linearsearch()

def linearsearch():
    pass

def binarysearch():
    pass

MyList = list(map(int,input("\nEnter the Numbers : ").strip().split()))

num = int(input("Enter the Number you want to Search: "))