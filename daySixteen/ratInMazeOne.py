def solveMaze(maz):
    size = len(maz)
    sol = [[0] * size for  _ in range(size)]

    def backTrack(x, y):
        if x == size - 1 and y == size - 1:
            sol[x][y] = 1
            return True
        
        if 0 <= x < size and 0 <= y < size and maz[x][y] == 1:
            sol[x][y] = 1

            if backTrack(x+1, y): return True #right (1, 0)
            if backTrack(x, y+1): return True # down (0, 1)
            if backTrack(x-1, y): return True #back (-1, 0)
            if backTrack(x, y-1): return True #up (0,-1)

            sol[x][y] = 0
        return False 
    backTrack(0,0)
    return sol

if __name__ == '__main__':
    maz = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    print(solveMaze(maz))