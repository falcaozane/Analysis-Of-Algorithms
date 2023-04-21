import numpy as np

inf = 1000
adjacencyMatrix = []
noOfVertices = int(input('Enter number of vertices: '))

for i in range(noOfVertices):
    tempList = []
    for j in range(noOfVertices):
        tempVar = input(f'Enter edge value of vertex {i} from vertex {j}: ').lower().strip()
        if tempVar == 'inf':
            tempVar = inf
        tempList.append(int(tempVar))
    adjacencyMatrix.append(tempList)

adjacencyMatrix = np.array(adjacencyMatrix)

print('\nA0:')
print(adjacencyMatrix)

for k in range(noOfVertices):
    for i in range(noOfVertices):
        for j in range(noOfVertices):
            adjacencyMatrix[i][j] = min(adjacencyMatrix[i][j], adjacencyMatrix[i][k] + adjacencyMatrix[k][j])

    print(f'\nA{k+1}: ')
    print(adjacencyMatrix)
