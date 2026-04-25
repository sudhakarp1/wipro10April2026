'''
Union-Find Algorithm for Cycle Detection (Strategy: Disjoint Set):
    Union by Rank
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

def hasCycle(num, edges):
    unFind = UnionFind(num) 
    
    for u, v in edges:
        if not unFind.union(u, v): #false --> union not possible
            return True
    return False 

if __name__ == '__main__':
    edges = [(0,1), (0,2), (2,3), (1,3)]
    print(f'Has Cycle: {hasCycle(4, edges)}')
