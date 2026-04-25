'''
Union-Find Algorithm for Cycle Detection (Strategy: Disjoint Set):
    Union by Size
'''

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        print(f'Init: {size}')
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False #cycle detected --> 
        
        if self.size[rootX] > self.size[rootY]:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        else:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        
        return True

def hasCycle(num, edges):
    unFind = UnionFind(num) 
    
    for u, v in edges:
        if not unFind.union(u, v): #false --> union not possible
            return True
    return False 


if __name__ == '__main__':
    edges = [(0,1), (0,2), (1,2), (1,3)]
    print(f'Has Cycle: {hasCycle(4, edges)}')
        

        