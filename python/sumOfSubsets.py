w = [0]*10
n = s = count = 0
sol = [0]*10
tot_pl = 0

def promising(l, wsf, tpl):
    if wsf + w[l+1] <= s and wsf + tpl >= s:
        return 1
    return 0

def sum_of_subsets(l, wsf, tpl):
    global count
    if wsf == s:
        count += 1
        print("\n Solution Vector", count, ":", end="")
        print("[", end="")
        for i in range(1, n+1):
            print(sol[i], end="\t")
        print("]")
        print()
    elif promising(l, wsf, tpl):
        sol[l+1] = 1
        sum_of_subsets(l+1, wsf+w[l+1], tpl-w[l+1])
        sol[l+1] = 0
        sum_of_subsets(l+1, wsf, tpl-w[l+1])

n = int(input("\n Enter the number of distinct items : "))
for i in range(1, n+1):
    w[i] = int(input("\n Enter the weight of the Item Number {}: ".format(i)))
    tot_pl += w[i]

s = int(input("\n Enter the Maximum allowed weight : "))
sum_of_subsets(0, 0, tot_pl)
