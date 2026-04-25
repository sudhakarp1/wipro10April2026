'''

'''
import heapq
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    priorityQueue =[(0,start)] #(distance, node)

    while priorityQueue:
        currDist, node = heapq.heappop(priorityQueue)

        if currDist > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            newDist = currDist + weight
            #relaxation
            if newDist < dist[neighbor]:
                dist[neighbor] = newDist
                heapq.heappush(priorityQueue, (newDist, neighbor))
    return dist

if __name__ == '__main__':
    graph = {
        'A': [('B',1), ('C',4), ('D',2)],
        'B': [('A',1), ('D',5)],
        'C': [('A',4), ('D',1)],
        'D': [('A',2), ('B',5), ('C',1)]
    }
    print(dijkstra(graph, 'A'))