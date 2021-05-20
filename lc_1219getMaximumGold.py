class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        self.res = 0
        def dfs(i,j,acc):
            self.res = max(acc,self.res)
            tmp = grid[i][j]
            grid[i][j] = 0
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    dfs(nx,ny, acc + grid[nx][ny])
            
            grid[i][j] = tmp
        for x in range(m):
            for y in range(n):
                if grid[x][y]!=0:
                    dfs(x,y,grid[x][y])
        return self.res