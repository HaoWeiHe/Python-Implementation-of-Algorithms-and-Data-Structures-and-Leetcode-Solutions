class Solution(object):
	def minPathSum(self, grid):
		if not grid:
			return 0

		n = len(grid[0])
		m = len(grid)
		# print(grid)

		for i in range(1, n):
			grid[0][i] += grid[0][i-1]
		# print(grid)
		for i in range(1, m):
			grid[i][0] += grid[i-1][0]
		# print(grid)

		for i in range(1,m):
			for j in range(1,n):
			    # print(i,j)
				grid[i][j] = min(grid[i][j-1],grid[i-1][j])+ grid[i][j]        
			
		return grid[-1][-1]
    
    