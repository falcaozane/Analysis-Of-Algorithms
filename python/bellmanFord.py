import numpy as np

adjacencyMatrix = []
noOfVertices = int(input('Enter number of vertices: '))
distList = [np.inf] * noOfVertices
sourceVertex = int(input('Enter source vertex: '))
distList[sourceVertex] = 0

for i in range(noOfVertices):
    tempList = []
    for j in range(noOfVertices):
        tempList.append(int(input(f'Enter edge weight ({i} -> {j}): ')))
    adjacencyMatrix.append(tempList)

adjacencyMatrix = np.array(adjacencyMatrix)
print('\nAdjacency Matrix:\n', adjacencyMatrix)

for i in range(noOfVertices - 1):
    for j in range(noOfVertices):
        for k in range(noOfVertices):
            if adjacencyMatrix[j][k] != 0:
                if distList[k] > distList[j] + adjacencyMatrix[j][k]:
                    distList[k] = distList[j] + adjacencyMatrix[j][k]

print('\nDistance from source:')
for i in range(noOfVertices):
    print(f'{i}: {distList[i]}')
