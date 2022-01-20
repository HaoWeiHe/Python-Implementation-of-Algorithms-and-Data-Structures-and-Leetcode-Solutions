class Solution(object):
    def islandPerimeter(self, grid):
        """
        
       28 - 12
       block_num*4 -  2*(block_num-1) = 16
       1*4 - 2*(1-1) = 4
       16-8 = 8
        """
        m,n = len(grid), len(grid[0])
        self.w = 0 
        def dfs(i,j):
            ans = 1 
            grid[i][j] = "#"
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx, ny = dx + i,  dy + j 
                if not (0 <= nx < m and 0 <= ny < n ):#and grid[nx][ny]==1):
                    self.w += 1
                    continue
                if grid[nx][ny] == 0:
                    self.w += 1
                if grid[nx][ny] == 1:
                    # self.w += 1
                    dfs(nx,ny)
            return 
        flag = False
        block_num = 0 
        for i in range(m):
            if flag:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    
                    flag = True
                    break
        return self.w

grid = [[1,1],[1,1]]#[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(Solution().islandPerimeter(grid))