#for matrix
def maxOutDegVerMatrix(graph):
    max_deg = -1
    vertex = -1

    for i in range(len(graph)):
        deg = 0
        for j in range(len(graph[i])):
            if graph[i][j] != 0:
                deg += 1

        if deg > max_deg:
            max_deg = deg
            vertex = i

    return vertex, max_deg
#for list
def maxOutDegVerList(adjList):
    max_deg = -1
    vertex = -1

    for i in range(len(adjList)):
        deg = 0
        for j in range(len(adjList[i])):
            if adjList[i][j][0] != 0 or adjList[i][j][1] != 0:
                deg += 1

        if deg > max_deg:
            max_deg = deg
            vertex = i

    return vertex, max_deg