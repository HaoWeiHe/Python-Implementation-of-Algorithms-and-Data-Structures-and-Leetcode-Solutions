class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0 
        def dfs(i,j): 
            grid[i][j] = 2
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    dfs(nx, ny)
                    
  
                
        def bfs(x,y,v):
            q = deque([(x,y,0)])
           
            while q:
                (i,j, lev) = q.popleft()
                if (i,j) in v:
                    continue
                
                v.add((i,j))
                
                for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                    nx, ny = i + dx, j + dy 
                    
                    if 0 > nx or m <= nx or 0 > ny or n <= ny:
                        continue
                   
                    if grid[nx][ny] == 0:
                        q.append((nx,ny,lev +1 ))
                        
                    if grid[nx][ny] == 2:
                        return lev
          
         
            
            return float('inf')
        res = float('inf')
        flag = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 : 
                    if flag:
                        dfs(i,j)
                        flag = False
                    else:
                    
                        res = min(res, bfs(i,j,set()))
                        
                    
            
        return res