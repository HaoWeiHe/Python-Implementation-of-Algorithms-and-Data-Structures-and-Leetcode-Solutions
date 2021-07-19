class Solution(object):
    def gameOfLife(self, board):
        """
         live: 
             <2 die
             ==2 or 3 live
             >3 dies, 
         die:
          ==3 live -> live
        """
        m,n = len(board), len(board[0])
        newb = [x[:] for x in board]
        
        for i in range(m):
            for j in range(n):
                die, live = 0,0
                for dx, dy in [[0,1],[0,-1], [1,0], [-1,0], [1,1], [1,-1],[-1,1],[-1,-1]]:
                    nx, ny = dx + i, dy + j 
                    if not (0 <= nx < m and 0 <= ny < n):
                        continue
                    if newb[nx][ny] == 0:
                        die +=1
                    else:
                        live +=1
                if newb[i][j] == 0 and live ==3:
                    board[i][j] = 1
                if newb[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 0
               
        return board 
        