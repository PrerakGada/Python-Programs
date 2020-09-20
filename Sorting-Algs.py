# Choosing the Sorting Algorithm
def choice(arr):
    print("Enter the sort you want to perform: ")
    print("1.Insertion Sort")
    print("2.Quick Sort")
    print("3.Selection Sort")
    c = int(input("Enter you choice: "))

    if c == 1:
        return insertion_sort(arr)
    if c == 2:
        return quick_sort(arr, 0, n-1)
    if c == 3:
        return selection_sort(arr)

# Insertion Sort
def insertion_sort(arr):
    for x in range(1, len(arr)):
        buffer = arr[x]
        j = x
        while buffer < arr[j - 1] and j > 0:
            arr[j] = arr[j - 1]
            arr[j - 1] = buffer
            j -= 1
    return arr

# Quick Sort
def quick_sort(arr,low,high):

    def partition(arr,low,high): 
        i = ( low-1 )         
        pivot = arr[high]     
    
        for j in range(low , high): 
    
            if   arr[j] < pivot: 
            
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
    
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 

    if low < high: 

        pi = partition(arr,low,high) 

        quick_sort(arr, low, pi-1) 
        quick_sort(arr, pi+1, high)

    return arr

# Selection Sort
def selection_sort(arr):
    
    for x in range(len(arr)):
        min = x
        for y in range(x+1, len(arr)):
            if arr[min] > arr[y]:
                min = y
        arr[x], arr[min] = arr[min], arr[x]
    return arr

# Inputing the List/Array
MyList = list(map(int,input("\nEnter the Numbers : ").strip().split()))

n = len(MyList)

SortedList = choice(MyList)

# Printing the Sorted List/Array
for x in SortedList:
    print(x,end=" ")
