'''
    N - Queens
'''
def SolveNQueens(N):
    board = [['.'] * N for _ in range(N)]

    def isSafe(row, col):
        #column wise
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        #left diagonal 
        i, j = row-1, col-1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i, j = i-1, j-1
        
        #right diagonal
        i, j = row - 1, col + 1
        while i>=0 and j < N:
            if board[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        
        return True
    
    def backTrack(row):
        if row == N:
            for r in board:
                print(' '.join(r))
            print()
            return
        
        for col in range(N):
            if isSafe(row, col):
                board[row][col] = 'Q'
                backTrack(row + 1)
                board[row][col] = '.' #back tracking/undoing
    
    backTrack(0)


if __name__ == '__main__':
    SolveNQueens(5)