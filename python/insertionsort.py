def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j=i-1
        while (j>=0 and A[j]>key):
            A[j+1] = A[j]
            j=j-1
        A[j+1] = key
    print("Sorted List: ", A)

A = list(map(int, input("Enter the list elements separated by space: ").split()))
insertion_sort(A)
