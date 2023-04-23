def printLCS(i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 'c':
        printLCS(i - 1, j - 1)
        print(x[i - 1], end='')
    elif b[i][j] == 'u':
        printLCS(i - 1, j)
    else:
        printLCS(i, j - 1)

def lcs():
    m = len(x)
    n = len(y)
    for i in range(m + 1):
        c[i][0] = 0
    for i in range(n + 1):
        c[0][i] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'c'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 'u'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 'l'

    print("The Longest Common Subsequence is ", end='')
    printLCS(m, n)
    print("\n\nThe LCS Matrix is:")
    for i in range(m + 1):
        for j in range(n + 1):
            print(c[i][j], end=' ')
        print()

x = input("Enter 1st sequence:")
y = input("Enter 2nd sequence:")
m = len(x)
n = len(y)
c = [[0] * (n + 1) for _ in range(m + 1)]
b = [[''] * (n + 1) for _ in range(m + 1)]
lcs()
