'''
    Basic graph class 
        Undirected --> undirect edges 
        Weighted --> Weighted edges
        enumerate(['A','B','C', 'D'])
        matrix = [
            [0, 10, 5, 0],
            [10, 0, 0, 3],
            [5, 0, 0, 0],
            [0, 3, 0, 0]
        ]
'''

class Graph:
    def __init__(self):
        self.adjList = {} #dictionary

    def addVertex(self, vertex):#adding node to graph
        if vertex not in self.adjList:
            self.adjList[vertex] = []
        
    def addEdges(self, u, v, weight): # u --> starting vertex and v -->end vertex
        self.addVertex(u)
        self.addVertex(v)

        self.adjList[u].append((v,weight))
        self.adjList[v].append((u,weight))
    
    def disp(self):
        for vertex in self.adjList:
            print(f'{vertex} --> {self.adjList[vertex]}')

if __name__ == '__main__':
    graph = Graph()
    graph.addEdges('A', 'B', 10)
    graph.addEdges('A', 'C', 5)
    graph.addEdges('B', 'D', 3)

    graph.disp()

    
