import numpy as np

edgeInfo, shortestPathDict, pathHolder = {}, {}, {}
noOfVertices = int(input('Enter number of vertices: '))
asciiVertex = 65

for i in range(noOfVertices):
    pathHolder.update({chr(asciiVertex) : ''})
    edgeInfo.update({ chr(asciiVertex) : {} })
    shortestPathDict.update({chr(asciiVertex) : np.inf})
    asciiColVertex = 65
    for j in range(noOfVertices):
        edgeInfo[chr(asciiVertex)].update({ chr(asciiColVertex): int(input(f'Enter edge length of {chr(asciiVertex)} to {chr(asciiColVertex)}: '))})
        asciiColVertex += 1
    asciiVertex += 1

source = input('Enter source vertex: ')
pathHolder[source] = pathHolder[source].replace('', 'A')
visitedVertex = []
currentVertex, distanceFromSource = source, 0

for i in range(noOfVertices):
    checkList = list(edgeInfo[currentVertex].items())
    for x in checkList:
        if x[0] != currentVertex and x[1] != 0 and (distanceFromSource + x[1]) < shortestPathDict[x[0]]:
            shortestPathDict[x[0]] = distanceFromSource + x[1]
            pathHolder[x[0]] = pathHolder[currentVertex] + f'{x[0]}'
    temp = [x for x in list(shortestPathDict.items()) if x[0] not in visitedVertex]
    minList = sorted(temp, key=lambda x: x[1])
    if len(minList) > 0:
        currentVertex = minList[0][0]
        visitedVertex.append(currentVertex)
        distanceFromSource = shortestPathDict[currentVertex]

shortestPathDict.update({'A': '0'})
formattedPath = dict(map(lambda x: (x[0], '->'.join([z for z in x[1]])), pathHolder.items()))

print(f'Shortest distance: {shortestPathDict}')
print(f'Shortest path to each vertex from source: {formattedPath}')
