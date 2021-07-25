class Solution(object):
    def updateBoard(self, board, c):
        """
         board = [["E","E","E","E","E"],
                 ["m","E","M","E","E"],
                 ["E","E","E","E","E"],
                 ["B","E","E","E","E"]]
        """
        if board[c[0]][c[1]] == "M":
            board[c[0]][c[1]] = "X"
            return board
        m,n = len(board), len(board[0])
        def dfs(x,y):
            
            counter = 0
            nei = []
            for dx, dy in [[0,1],[0,-1], [1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] == "M" :
                        counter += 1
                    else:
                        if board[nx][ny] == "E":
                            nei.append((nx,ny))
                        
            if counter == 0:
                board[x][y] = "B"
                for a, b in nei:
                    dfs(a, b)
            else:
                board[x][y] = str(counter)
        dfs(c[0], c[1])
        return board