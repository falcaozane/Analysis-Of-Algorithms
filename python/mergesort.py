def merge(L, R, arr):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, arr)
    print(arr)
    

print("merge sort")
arr=[]
n=int(input("enter number of elements in array :"))
for i in range (0,n):
    ele=int(input())
    arr.append(ele)

print("list before sorting")
print(arr)
merge_sort(arr)
print("list after sorting")
print(arr)
