class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        grid = [[float('inf')] *len(grid[0])]  + grid
        for col in range(len(grid)):
            grid[col] = [float('inf')] + grid[col]
        m, n = len(grid),  len(grid[0])
       
        for i in range(1,m):
            for j in range(1,n):
                if i == 1 and j == 1:
                    continue
                grid[i][j] +=  min(grid[i-1][j], grid[i][j-1])
  
                
        
        return grid[-1][-1]
    def minPathSum2(self, grid):
        """
        f(i,j) = val + min(f(i-1,j), f(i+1,j))
        until i == 0 and j ==0 
        if i < 0 and j < 0 break
        :rtype: int
        """
        self.mem = {}
        def dfs(i,j):
            if (i,j) in self.mem:
                return self.mem[(i,j)]
            
            if i < 0 or j < 0:
                return float('inf')
            if i == 0 and j == 0:
                return grid[0][0]
            self.mem[(i,j)]  = grid[i][j] + min(dfs(i-1,j), dfs(i,j-1))
            return self.mem[(i,j)] 
            
        return dfs(len(grid)-1, len(grid[0])-1)
        