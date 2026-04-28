

def isSafe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def knightTour(rCnt, cCnt, moveCnt, board):
    if moveCnt == N * N:
        return True
    
    for dx, dy in moves:
        nextX, nextY = rCnt + dx, cCnt + dy #(2,1)

        if isSafe(nextX, nextY, board):
            board[nextX][nextY] = moveCnt #doing 
            if knightTour(nextX, nextY, moveCnt + 1, board):
                return True
            
            board[nextX][nextY] = -1 # undoing
    
    return False 

if __name__ == '__main__':
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    N = 5
    board = [[-1] * N  for _ in range(N)]
    board[0][0] = 0

    knightTour(0,0, 1, board)
    
    for row in board:
        print(*row)
    

