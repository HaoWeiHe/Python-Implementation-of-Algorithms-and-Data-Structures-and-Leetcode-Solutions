
# # [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
class Solution(object):
	def numDistinctIslands(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		m, n = len(grid), len(grid[0])
		presentation = []
		d = {"r":(0,1), "u":(1,0), "l":(-1,0), "d":(0,-1)}
		def dfs(x, y):
			hst = ""
			grid[x][y] = 2
			for way in ["r","u","l","d"]:
				nx, ny = x + d[way][0], y + d[way][1]
				if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
					hst += way + dfs(nx,ny)
			
			return hst
		
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					presentation.append(dfs(i,j))
		
		return len(set(presentation))
