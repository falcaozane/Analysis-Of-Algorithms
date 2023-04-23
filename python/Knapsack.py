def knapsack(n,w,p,capacity):
    sol = [0.0]*n
    tp = 0
    u = capacity
    
    for i in range(n):
        if w[i]>u:
            break
        else:
            sol[i] = 1.0
            tp = tp+p[i]
            u = u-w[i]
    if i<n:
        sol[i] = u/w[i]
    tp = tp + (sol[i]*p[i])
    print("Solution vector:")
    for i in range(n):
        print(sol[i],end="\t")
    print("\nMax profit: ",tp)



n = int(input("Enter no. of items: "))
w = [0.0]*n
p = [0.0]*n

print("\n enter profit and weight")
for i in range(n):
    p[i], w[i] = map(float,input().split())
capacity = float(input("\n Enter capacity of knapsack: "))
ratio = [0.0]*n
for i in range(n):
    ratio[i] = p[i]/w[i]

knapsack(n,w,p,capacity)

