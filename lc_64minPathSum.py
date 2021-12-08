class Solution(object):
    def minPathSum(self, grid):
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
        