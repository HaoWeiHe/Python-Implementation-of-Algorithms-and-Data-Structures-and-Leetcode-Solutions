class Solution(object):
	def closedIsland(self, grid):

		m,n = len(grid), len(grid[0])
		res = 0
		self.flag = 1
		def dfs(x,y):

			if x == 0  or x == m-1 or y ==0 or y == n-1: 
				print(x,y, "happen here")
				self.flag = 0
			
			grid[x][y] ="#"
			for dx, dy in [(0,1),(0,-1), (-1,0), (1,0)]:
				newx, newy = x + dx, y +dy 
				if 0 <= newx < m and 0 <= newy <n:
					if grid[newx][newy]==0 : 
						dfs(newx,newy)

		for i in range(m):
			for j in range(n):
				if grid[i][j]==0:
					# print("ew")
					dfs(i,j)
					print(grid, bool(self.flag),(i,j))
					if self.flag:
					    res +=1
					self.flag = 1
		return res

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(Solution().closedIsland(grid))



