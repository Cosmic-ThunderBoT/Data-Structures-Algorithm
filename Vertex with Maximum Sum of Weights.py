
#For Matrix
def maxSumVert(graph):
    max_sum = -1
    vertex = -1

    for i in range(len(graph)):
        res_sum = sum(graph[i])

        if res_sum > max_sum:
            max_sum = res_sum
            vertex = i

    return vertex, max_sum
#for list
def maxSumVerList(adjList):
    max_sum = -1
    max_vertex = -1

    for i in range(len(adjList)):
        weight_sum = 0

        for j in range(len(adjList[i])):
            weight_sum += adjList[i][j][1]

        if weight_sum > max_sum:
            max_sum = weight_sum
            max_vertex = i

    return max_vertex, max_sum