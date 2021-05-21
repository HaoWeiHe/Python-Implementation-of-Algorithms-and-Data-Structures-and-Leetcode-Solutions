
class Solution(object):
    def longestIncreasingPath(self, matrix):
        
        m,n = len(matrix), len(matrix[0])
        mem =  [[0] * n for _ in range(m)]
    

        def dfs(x,y):
            if mem[x][y] != 0:
                return mem[x][y]
            
            
            for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    mem[x][y] = max(mem[x][y], dfs(nx,ny))
    
        
            return mem[x][y] + 1
        
        ans = 0 
        for i in range(m):
            for j in range(n): 
                ans = max(ans,dfs(i,j))
        print(mem)
        return ans
matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix))