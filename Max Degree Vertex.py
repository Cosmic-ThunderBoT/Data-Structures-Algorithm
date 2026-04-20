def maxDegVerMatrix(graph):
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