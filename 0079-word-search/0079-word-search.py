class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(board)
        m = len(board[0])
        
        direc = [(1,0),(-1,0),(0,1),(0,-1)]
        vis = set()
        def corr(r,c,i):
            if i == len(word):
                return True
            for dr,dc in direc:
                row = r+dr
                col = c+dc
                if 0 <= row < n and 0 <= col < m and (row,col) not in vis and board[row][col] == word[i]:
                    vis.add((row,col))
                    if corr(row,col,i+1):
                        return True
                    vis.remove((row,col))
            return False
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    vis.add((i,j))
                    if corr(i,j,1):
                        return True
                    vis.remove((i,j))
        return False

