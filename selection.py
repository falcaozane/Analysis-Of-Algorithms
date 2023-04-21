def swap(i, j, A):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
# selection sort algorithm    
def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if A[j] < A[index]:
                index = j
        swap(i, index, A)
    print("Sorted List: ", A)

A = list(map(int, input("Enter the list elements separated by space: ").split()))

selection_sort(A)

