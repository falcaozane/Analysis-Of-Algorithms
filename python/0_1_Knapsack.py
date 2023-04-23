def knapsack(max_weight, weights, values, num_items):
    # initialize V matrix
    V = [[0 for x in range(max_weight+1)] for y in range(num_items+1)]
    
    # fill first row and column with 0
    for i in range(num_items+1):
        V[i][0] = 0
    for w in range(max_weight+1):
        V[0][w] = 0
    
    # fill the remaining V matrix
    for i in range(1, num_items+1):
        for w in range(1, max_weight+1):
            if weights[i-1] <= w:
                if values[i-1] + V[i-1][w-weights[i-1]] > V[i-1][w]:
                    V[i][w] = values[i-1] + V[i-1][w-weights[i-1]]
                else:
                    V[i][w] = V[i-1][w]
            else:
                V[i][w] = V[i-1][w]
    
    # find the solution set
    i = num_items
    k = max_weight
    solution_set = []
    while i > 0 and k > 0:
        if V[i][k] != V[i-1][k]:
            solution_set.append(i-1)
            k = k - weights[i-1]
        i = i - 1
    
    return (V[num_items][max_weight], solution_set)

W = 8
wt = [2,3,4,5]
val = [1,2,5,6]
n = len(wt)

max_value, solution_set = knapsack(W, wt, val, n)

print("Maximum profit:", max_value)
print("Solution set:", solution_set)
