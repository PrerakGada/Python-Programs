def choice(arr, x):
    print("1.Linear Search")
    print("2.Binary Search")

    c = int(input("Enter your choice: "))

    if c == 1:
        linearsearch(arr, x)
    elif c == 2:
        binarysearch(arr, x)
    else:
        print("Wrong Choice!")
        choice(arr, x)

def linearsearch(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            print("{0} is Found on {1} Location",format(x,i))

def binarysearch(arr, x):
    arr.sort()

    pass

MyList = list(map(int,input("\nEnter the Numbers : ").strip().split()))

num = int(input("Enter the Number you want to Search: "))

choice(MyList, num)