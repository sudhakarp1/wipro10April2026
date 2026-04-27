def floydWarshall(graph): #adjacency matrix
    size = len(graph)
    dist = [row[:] for row in graph]

    for k in range(size): # n ** 3
        for i in range(size):
            for j in range(size):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] 
    return dist 

if __name__ == '__main__':
    INF = float('inf')
    graph = [[0, 3, INF, 7],
             [INF, 0, 1, INF],
             [INF, INF, 0, 2],
             [INF,INF,INF, 0]] 
    
    res = floydWarshall(graph)
    for row in res:
        print(*row)
