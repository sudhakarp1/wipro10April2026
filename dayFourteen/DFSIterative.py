'''
    Using Iterative with stack operations (list as DS)
'''

def depthFirst(graph, start):    
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end = ' ')
            visited.add(node)

            stack.extend(reversed(graph[node]))
    print()
    
    
if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    depthFirst(graph, 'A')