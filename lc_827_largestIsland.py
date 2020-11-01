import collections
class Solution(object):
	def largestIsland(self, grid):

		if not grid: return 0
		m,n = len(grid), len(grid[0])
		self.number_of_island = 0 
		island_number_and_its_area = collections.defaultdict(int)
		island_number_and_its_area[0] = 0
		
		def explore(x,y):
			grid[x][y] = (self.number_of_island,self.tmp_area)
			
			island_number_and_its_area[self.number_of_island] = self.tmp_area

			for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
				nx, ny = dx + x, dy + y
				if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
					self.tmp_area += 1 
					explore(nx,ny)  

	# mark and update on map
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					self.tmp_area = 1
					explore(i,j)
					self.number_of_island += 1
					
		#trace all the 0s and get the maxArea
		res = 0
		for i in range(m):
			for j in range(n):
				visited, tmp_area = set(), 1
				
				if grid[i][j] != 0: continue
				for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
					nx, ny = dx + i, dy + j
					if 0<=nx< m and 0<= ny <n and grid[nx][ny] != 0:
						number_of_island, _ = grid[nx][ny] 
						if number_of_island not in visited:
							tmp_area += island_number_and_its_area[number_of_island]
							visited.add(number_of_island)
							
				res = max(res, tmp_area)
		
		return max(res, max(island_number_and_its_area.values()))
