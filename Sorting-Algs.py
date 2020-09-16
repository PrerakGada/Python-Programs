def insertion_sort(arr):
    for x in range(1, len(arr)):
        buffer = arr[x]
        j = x
        while buffer < arr[j - 1] and j > 0:
            arr[j] = arr[j - 1]
            arr[j - 1] = buffer
            j -= 1
    return arr


def quick_sort(arr):

    return arr

def choice(arr):
    print("Enter the sort you want to perform: ")
    print("1.Insertion Sort\n2.Quick Sort")
    c = int(input("Enter you choice: "))

    if c == 1:
        return insertion_sort(arr)
    if c == 2:
        quick_sort(arr)

MyList = list(map(int,input("\nEnter the Numbers : ").strip().split()))
print(choice(MyList))
