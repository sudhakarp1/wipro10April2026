def bellmanFord(edges, V, source):
    dist = [float('inf')]  * V
    dist[source] = 0
    #relax edges V-1 times here 
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w 

    #checking for the negative cycle 
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print('Negative Cycle found')
            return -1
    return dist 

if __name__ == '__main__':
    edges = [(0,1,5), (1,2,1),(1,3,2), (3,4,-1), (4, 2,1)]
    res = bellmanFord(edges, 5, 0)
    print(res)