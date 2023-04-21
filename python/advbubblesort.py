def swap(i, j, A):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
# Bubble sort algorithm    
def bubble_sort(A):
    n = len(A)
    for pass_num in range(1, n):
        flag = 0  # flag denotes are there any swaps done in pass
        for i in range(0, n - pass_num):
            if A[i] > A[i + 1]:
                swap(i, i + 1, A)
                flag = 1  # After swap, set flag to 1
        if flag == 0:
            break  # No swaps indicates we can terminate loop

    print("Sorted List: ", A)

A = list(map(int, input("Enter the list elements separated by space: ").split()))

bubble_sort(A)

