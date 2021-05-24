class Solution(object):
    def getMaximumGold2(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(g), len(g[0])
        
        def dfs(x,y,acc):
           
            orignal = g[x][y]
            g[x][y] = 0 
            res = acc
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n and g[nx][ny]!=0:    
                    res = max(res, dfs(nx,ny, acc + g[nx][ny]))
            g[x][y] = orignal
                    
            return res
        ans = 0 
        for i in range(m):
            for j in range(n):
                if g[i][j]!=0:
                    ans = max(ans,dfs(i,j,g[i][j]))
        return ans
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        self.res = 0
        visited = set()
        def dfs(i,j,acc):
            self.res = max(acc,self.res)
            visited.add((i,j))
            tmp = grid[i][j]
            grid[i][j] = 0
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    dfs(nx,ny, acc + grid[nx][ny])
            
            grid[i][j] = tmp
        for x in range(m):
            for y in range(n):
                if grid[x][y]!=0 and (x,y) not in visited:
                    dfs(x,y,grid[x][y])
        return self.res