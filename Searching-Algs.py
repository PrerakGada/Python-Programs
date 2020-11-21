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

t = ""
y = t.reverse()

def linearsearch(arr, x):
    o = 0
    for i in range(len(arr)):
        if arr[i] == x:
            print("{0} is Found on {1} Location".format(x, i))
            o += 1
    if o == 0:
        print("{0} is not Found in the List!".format(x))


def binarysearch(arr, x):
    arr.sort()
    min = 0
    max = len(arr) - 1
    mid = (min + max) // 2

    while arr[mid] != x:
        if x == arr[mid]:
            break
        elif x > arr[mid]:
            min = mid
            mid = (min + max) // 2
        elif x < arr[mid]:
            max = mid
            mid = (min + max) // 2
    print("{0} is Found at {1} Location".format(x, arr[mid]))


MyList = list(map(int, input("\nEnter the Numbers : ").strip().split()))

num = int(input("Enter the Number you want to Search: "))

choice(MyList, num)
