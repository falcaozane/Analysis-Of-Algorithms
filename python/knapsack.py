def knapsack(n, weight, profit, capacity):
    sol = [0.0] * n
    tp = 0
    u = capacity

    for i in range(n):
        if weight[i] > u:
            break
        else:
            sol[i] = 1.0
            tp += profit[i]
            u -= weight[i]

    if i < n:
        sol[i] = u / weight[i]

    tp += (sol[i] * profit[i])

    print("The solution vector is: ", end="")
    for i in range(n):
        print(sol[i], end="\t")

    print("\n\nThe maximum profit is:", tp)


num = int(input("Enter the no. of objects: "))
weight = [0.0] * num
profit = [0.0] * num

print("\nEnter the weight and profit of each object:")
print("Weight , Profit")
for i in range(num):
    weight[i], profit[i] = map(float, input().split())

capacity = float(input("\nEnter the capacity of the knapsack: "))
ratio = [0.0] * num
for i in range(num):
    ratio[i] = profit[i] / weight[i]

for i in range(num):
    for j in range(i+1, num):
        if ratio[i] < ratio[j]:
            ratio[i], ratio[j] = ratio[j], ratio[i]
            weight[i], weight[j] = weight[j], weight[i]
            profit[i], profit[j] = profit[j], profit[i]

knapsack(num, weight, profit, capacity)
