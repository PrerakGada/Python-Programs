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


MyList = list(map(int,input("\nEnter the List : ").strip().split()))
print(insertion_sort(MyList))
