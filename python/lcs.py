import numpy as np

str1 = '0' + input('Enter string 1: ')
str2 = '0' + input('Enter string 2: ')

tableRow = len(str1)
tableCol = len(str2)
rowList = [[0] * (tableRow)] * tableCol
table = np.array(rowList)

for i in range(1, tableRow):
    for j in range(1, tableCol):
        if str1[j] == str2[i]:
            table[i][j] = table[i - 1][j - 1] + 1
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])

print(table)
print(f'\nLCS is {table[tableRow - 1][tableCol - 1]}')

LCS = []
i = tableRow - 1
j = tableCol - 1

while (i > 0 and j > 0):
    if (str1[j] == str2[i]):
        LCS.insert(0, str1[j])
        i -= 1
        j -= 1
    elif (table[i - 1][j] > table[i][j - 1]):
        i -= 1
    else:
        j -= 1

print(LCS)
