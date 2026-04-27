'''


'''
from functools import lru_cache

def travelingSP(map):
    size = len(map) #total number of nodes/cities

    @lru_cache
    def innerFun(mask, pos):
        #tracking cities visited
        if mask == (1 << size) -1:
            return map[pos][0]
        ans = float('inf')
        for city in range(size):
            if not (mask & (1 << city)):
                cost = map[pos][city] + innerFun(mask | (1<<city), city)
                ans = min(ans, cost)
    
        return ans 

    return innerFun(1, 0)

            



if __name__ == '__main__':
    map = [ [0, 10,15,20],
           [10, 0, 35, 25],
           [15,35, 0, 30],
           [10,25, 30, 0]]
    
    print(travelingSP(map))