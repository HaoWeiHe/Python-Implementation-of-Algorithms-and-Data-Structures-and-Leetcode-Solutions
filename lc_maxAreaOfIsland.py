# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         seen = set()
#         def area(r, c):
#             if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
#                     and (r, c) not in seen and grid[r][c]):
#                 return 0
#             seen.add((r, c))
#             return (1 + area(r+1, c) + area(r-1, c) +
#                     area(r, c-1) + area(r, c+1))

#         return max(area(r, c)
#                    for r in range(len(grid))
#                    for c in range(len(grid[0])))

class Solution(object):
	def maxAreaOfIsland(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		m,n = len(grid), len(grid[0])
		res = 0

		def dfs(x,y):
			
			
			if not (0 <= x < m and 0 <= y < n and grid[x][y]>0): return 0

			grid[x][y] = -1
			return (dfs(x+1,y) + dfs(x,y+1) + dfs(x-1,y) +dfs(x,y-1) + 1)
			

		for i in range(m):
			for j in range(n):
				if grid[i][j]: res = max(res,dfs(i,h))
					
		return res

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,0,0,0,0,0], #3 1+1+1
 [0,1,0,0,1,1,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
