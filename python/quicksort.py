def partition(arr, l, r):
    pivot = arr[r] # last element is taken as pivot element
    i = l-1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quicksort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quicksort(arr, l, pi-1)
        quicksort(arr, pi+1, r)


arr = list(map(int, input("Enter the list elements separated by space: ").split()))
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array:", arr)
"""
def partition(arr, l, r):
    pivot = arr[l]  # first element taken as pivot element
    i = l+1
    for j in range(l+1, r+1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i-1] = arr[i-1], arr[l]
    return i-1

def quicksort(arr, l, r):
    if l < r:
        pi = partition(arr, l, r)
        quicksort(arr, l, pi-1)
        quicksort(arr, pi+1, r)
    print(arr)

arr = [5,4,3,2,1]
n = len(arr)
print(arr)
quicksort(arr, 0, n-1)
print("Sorted array:", arr)

"""
