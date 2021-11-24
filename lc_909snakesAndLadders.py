from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        [-1 4]
        [-1 3]
     [curr + 1, min(curr + 6, n2)]
                     i*           
        i,0          i,j   
        
        
         [
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [13,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [1,2,3,4,5,6]    
         ]
         #{2:15, 14:35}
         
         lvl, counter = 0, 1
         for ele in (m-1,-1,-1):
            if lvl %2 == 0 -> 
            else: <- 
             for j in range(0, len(0))
         bfs, until reach m*n
         return steps
        """
        h = {}
        m,n = len(board), len(board[0])
        lvl, counter = 0 , 1
        for i in range(m-1,-1,-1):
            if lvl %2 == 0:
                for j in range(0,n):
                    
                    if board[i][j] != -1:
                        h[counter] = board[i][j]
                    counter += 1
            else:
                for j in range(n-1,-1,-1):
                    
                    if board[i][j] != -1:
                        h[counter] = board[i][j]
                    counter += 1
            lvl += 1
        q = deque([(1,0)])
        v = set()
        while q:
            top, steps = q.popleft()
            if top in v:
                continue
            if top > m*n  :
                continue
            if top == m*n:
                return steps

            for num in range(top + 1, min(top + 6, n*n)+1):
                if num in h:
                    num = h[num]
                q.append((num, steps + 1))
            v.add(top)
        return -1
board =[[1,1,-1],[1,1,1],[-1,1,1]]
print(Solution().snakesAndLadders(board))