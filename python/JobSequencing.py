def printJobScheduling(arr, t):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][2] < arr[j+1][2]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    res = [False] * t
    job = ['-1'] * t
    for i in range(n):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            if res[j] is False:
                res[j] = True
                job[j] = arr[i][0]
                break
    print("Maximum profit sequence of jobs is- ")
    print(", ".join(job))

array = [
       ['j1', 2, 20],
       ['j2', 2, 15],
       ['j3', 1, 10],
       ['j4', 3, 5],
       ['j5', 3, 1]
       ]
printJobScheduling(array, 3)
