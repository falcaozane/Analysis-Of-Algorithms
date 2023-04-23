import numpy as np

profit, weight = [0], [0]
noOfItems = int(input('Enter number of items: '))
maxWeight = int(input('Enter capacity of container: '))

# taking input of profits and weights of items
for i in range(noOfItems):
    profit.append(int(input(f'Enter profit of item {i+1}: ')))
    weight.append(int(input(f'Enter weight of item {i+1}: ')))

# initializing the table with zeros
table = np.zeros((noOfItems + 1, maxWeight + 1))

# filling up the table using dynamic programming approach
for i in range(1, noOfItems + 1):
    for w in range(1, maxWeight + 1):
        if weight[i] <= w:
            table[i][w] = max(profit[i] + table[i-1][w-weight[i]], table[i-1][w])
        else:
            table[i][w] = table[i-1][w]

# printing the final table and the maximum profit obtained
print('\n', table)
print(f'\nMaximum Profit = {table[noOfItems][maxWeight]}')