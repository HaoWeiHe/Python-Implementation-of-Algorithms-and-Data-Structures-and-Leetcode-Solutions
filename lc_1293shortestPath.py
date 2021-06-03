from collections import deque
class Solution(object):
    def shortestPath(self, grid, k):
        """
        18
        bfs 
        (i,j, amount), amount <= k, else should be False
        
        """
        if not grid:
            return k == 0
        v = set((0,0,k))
        m,n = len(grid), len(grid[0])
        q = deque([(0,0, k,0)])
        if k > (len(grid)-1 + len(grid[0])-1):
            return len(grid)-1 + len(grid[0])-1        
        
        while q:
            
            i, j , remind, pace = q.popleft()
        
            # if k < 0:
            #     continue
            
            if i == m -1 and j == n -1:
                return pace
            
            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                nx, ny = i + dx, j + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue
   
                if grid[nx][ny] == 1 and remind > 0 and (nx,ny,remind -1) not in v:
                    v.add((nx, ny, remind -1))
                    q.append((nx,ny, remind - 1, pace + 1))
                if grid[nx][ny] == 0 and (nx,ny,remind) not in v:
                    v.add((nx,ny, remind))
                    q.append((nx,ny, remind, pace + 1))
        return -1
