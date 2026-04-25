'''
    Basic graph class 
        directed --> direct edges 
        Unweighted --> unweighted edges
'''

class Graph:
    def __init__(self):
        self.adjList = {} #dictionary

    def addVertex(self, vertex):#adding node to graph
        if vertex not in self.adjList:
            self.adjList[vertex] = []
        
    def addEdges(self, u, v): # u --> v.
        self.addVertex(u)
        self.addVertex(v)

        self.adjList[u].append(v) #
    
    def disp(self):
        for vertex in self.adjList:
            print(f'{vertex} --> {self.adjList[vertex]}')

if __name__ == '__main__':
    graph = Graph()
    graph.addEdges('A', 'B')
    graph.addEdges('A', 'C')
    graph.addEdges('B', 'D')

    graph.disp()

    
