
class Solution(object):
	def numIslands(self, grid):
			FALG = "#"
			m,n = len(grid), len(grid[0])
			res = 0
			SEA_CODE = "0", Island_CODE = "1"
			def dfs(x,y):
				grid[x][y] = FALG
				for dx, dy in [(0,1),(0,-1), (-1,0), (1,0)]:
					newx, newy = x + dx, y +dy 
					if 0 <= newx < m and 0 <= newy <n:
						if grid[newx][newy]==Island_CODE: dfs(newx,newy)
					
			for i in range(m):
				for j in range(n):
					if grid[i][j]==Island_CODE:
						dfs(i,j)
						res +=1
			return res

