'''
    Minimum Spanning Tree - Kruskal Algorithm
'''

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        print(f'Init: {size}')
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False #cycle detected --> 
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY 
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        
        return True


def kruskalAlgo(size, edges):
    edges.sort(key=lambda x:x[2]) # sort by weight
    uFind = UnionFind(size)
    mst, totalCost = [], 0

    for u, v, w in edges:
        if uFind.union(u, v):
            mst.append((u, v, w))
            totalCost += w
    return mst, totalCost


if __name__ == '__main__':
    listEdges =[(0,1,1), (0,3,3), (1,2,4), (1,3,4), (2,3, 5)]
    print(kruskalAlgo(4, listEdges))