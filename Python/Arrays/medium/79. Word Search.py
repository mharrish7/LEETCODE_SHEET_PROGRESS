class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        path = set()
        
        def bfs(row, col, i):
            if i == len(word):
                return True
            if (row<0 or col <0 or row >= rows or col >= columns or word[i] != board[row][col] or (row, col) in path):
                return False
            path.add((row, col))
            
            res = ( 
                bfs(row+1, col, i +1) or
                bfs(row-1, col, i +1) or
                bfs(row, col+1, i +1) or
                bfs(row, col-1, i +1)                 
                  )
            
            path.remove((row, col))
            return res
            
                
                
            
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if bfs(i,j,0): return True
        return False