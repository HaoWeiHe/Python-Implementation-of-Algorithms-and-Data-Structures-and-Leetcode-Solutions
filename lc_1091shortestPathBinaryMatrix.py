

class Solution(object):
	def shortestPathBinaryMatrix(self, grid):
	  	s = set()
		if not grid:
			return -1
		if grid[0][0]: 
			return -1
		q = collections.deque([(1,0,0)])
		m,n = len(grid), len(grid[0])
		while q:

			level, x, y = q.popleft()
			
			if (x,y) in s:
				continue
			s.add((x,y))
			if x == m - 1 and y == n - 1:
				return level
			
			for dx, dy in [(1,1),(-1,-1),(1,0),(0,1),(0,-1),(-1,0),(-1,1),(1,-1)]:
				nx, ny = x + dx, y + dy
				
				if 0 <= nx < m and 0 <= ny < n  and grid[nx][ny] == 0 :
					q.append((level+1, nx, ny))
			
			
		return -1
