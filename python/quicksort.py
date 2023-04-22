 def partition(arr, l, r):
    pivot = arr[r]
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
