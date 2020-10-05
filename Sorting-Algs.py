# Choosing the Sorting Algorithm
def choice():
    print("Enter the sort you want to perform: ")
    print("1.Insertion Sort")
    print("2.Quick Sort")
    print("3.Selection Sort")
    print("4.Bubble Sort")
    print("5.Merge Sort")
    c = int(input("Enter your choice: "))


    if c == 1:
        return insertion_sort(MyList)
    elif c == 2:
        return quick_sort(MyList, 0, n-1)
    elif c == 3:
        return selection_sort(MyList)
    elif c == 4:
        return bubble_sort(MyList)
    elif c == 5:
        return merge_sort(MyList)
    else:
        print("Invalid Choice!!")

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

# Bubble Sort
def bubble_sort(arr): 

    for x in range(len(arr)): 
        for y in range(0, len(arr)-x-1): 
            if arr[y] > arr[y+1] : 
                arr[y], arr[y+1] = arr[y+1], arr[y]
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+= 1
            else: 
                arr[k] = right[j] 
                j+= 1
            k+= 1

        while i < len(left): 
            arr[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+= 1
            k+= 1

    return arr


# Inputing the List/Array
MyList = list(map(int,input("\nEnter the Numbers : ").strip().split()))

n = len(MyList)

SortedList = choice()

# Printing the Sorted List/Array
for x in SortedList:
    print(x,end=" ")
