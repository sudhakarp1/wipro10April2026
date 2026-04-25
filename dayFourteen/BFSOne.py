'''
    Focus on the algorithm
'''

from collections import deque

def breadthFirst(graph, start):
    visited = set() #keeps track of visited nodes no duplicates
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft() 
        print(node, end= ' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    breadthFirst(graph, 'A')



