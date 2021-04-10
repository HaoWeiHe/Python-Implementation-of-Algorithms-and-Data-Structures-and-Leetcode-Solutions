class Solution(object):
    def maxAreaOfIsland(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(g), len(g[0])
        self.c = 0 
        
        def dfs(i,j):
            
            g[i][j] = "#"
            for x,y in [[0,1],[1,0],[-1,0],[0,-1]]:
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == 1:
                    dfs(nx,ny) 
                    self.c +=1 
                    
            
            
        ans = 0        
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    self.c = 1
                    dfs(i,j)
                    ans  = max(ans,self.c)
        return ans