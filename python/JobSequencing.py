def JS(A,t):
    n = len(A)
    # sort in descending order of profit
    A.sort(key=lambda x: x[2], reverse=True)
    res = [False] * t
    job = ['-1']*t
    total_profit = 0
    for i in range(n):
        for j in range(min(t-1,A[i][1]-1),-1,-1):
            if res[j] is False:
                res[j] = True
                job[j] = A[i][0]
                total_profit += A[i][2]
                break
    print("\nMax profit sequence: ")
    print(job)
    print("Total profit: ", total_profit)

array = [       
       ['j1', 2, 20],
       ['j2', 2, 15],
       ['j3', 1, 10],
       ['j4', 3, 5],
       ['j5', 3, 1]
       ]
JS(array, 3)
