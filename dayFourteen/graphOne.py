'''
    Basic graph class 
        Undirected --> undirect edges 
        Unweighted --> unweighted edges
            # A B C D
        matrix = [
            [0, 1, 1, 0],  # A
            [1, 0, 0, 1],  # B
            [1, 0, 0, 0],  # C
            [0, 1, 0, 0]   # D
        ]
'''

class Graph:
    def __init__(self):
        self.adjList = {} #dictionary

    def addVertex(self, vertex):#adding node to graph
        if vertex not in self.adjList:
            self.adjList[vertex] = []
        
    def addEdges(self, u, v): # u --> starting vertex and v -->end vertex
        self.addVertex(u)
        self.addVertex(v)

        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def disp(self):
        for vertex in self.adjList:
            print(f'{vertex} --> {self.adjList[vertex]}')

if __name__ == '__main__':
    graph = Graph()
    graph.addEdges('A', 'B')
    graph.addEdges('A', 'C')
    graph.addEdges('B', 'D')

    graph.disp()

    
