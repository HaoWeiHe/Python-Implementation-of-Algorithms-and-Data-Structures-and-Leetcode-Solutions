class Solution(object):
    def numIslands(self, g):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0 
        m,n = len(g), len(g[0])
        
        def dfs(i,j):
            g[i][j] = 2
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx, ny = dx + i, dy + j
                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] =="1":
                    dfs(nx,ny)
                    
        
        if not g:
            return 0
        
        for i in range(len(g)):
            for j in range(len(g[0])):
                
                if g[i][j] == "1":
                    
                    res +=1
                    dfs(i,j)
        return res