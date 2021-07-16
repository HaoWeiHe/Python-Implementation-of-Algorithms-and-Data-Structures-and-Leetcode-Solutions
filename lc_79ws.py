class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m,n = len(board), len(board[0])
        v = set()
        def dfs(x,y,idx):
            if idx == len(word)-1:
                return True if board[x][y] == word[idx] else False
            if board[x][y] != word[idx]:
                return False
            
            if (x,y) in v:
                return False
           
            ans = []
            tmp  =board[x][y]
            board[x][y] = "#"
            for dx, dy in [[0,1],[0,-1],[-1,0],[1,0]]:
                nx, ny = dx+x , dy + y 
                if 0 <= nx < m and 0 <= ny < n:
                    ans.append(dfs(nx,ny, idx + 1))
            board[x][y] = tmp
            return any(ans)
        tmp  = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    tmp.append((i,j))
        for x, y in tmp:
            if dfs(x,y,0):
                return True
        return False