import collections		
class Solution():
	def minimumEffortPath(self, heights):
		m, n = len(heights), len(heights[0])
		q = collections.deque([(0,0)])
		efforts =  {(0, 0): 0}
		while q:

			x,y = q.popleft()
			for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
				nx, ny = dx + x, dy + y 
				if not (0 <= nx < m and 0 <= ny < n):
					continue
				
				eff = max(efforts.get((x, y)), abs(heights[x][y] - heights[nx][ny]) )
				if (nx, ny) in efforts and efforts[(nx, ny)] <= eff:
					continue
				efforts[(nx,ny)] = eff
				q.append((nx,ny))	
		if (m - 1, n - 1) not in efforts:
			return -1
		
		return efforts[(m-1,n-1)]
	def minimumEffortPath2(self, heights):

			m,n = len(heights), len(heights[0])
			def bfs(cost):
				q = deque([(0,0)])
				
				seen = set()
				
				while q:
					x, y = q.popleft()
					# seen.add((x,y))
					if x == m-1 and y == n-1:
						return True
					for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
						nx, ny = dx + x, dy + y 
						if nx >= m or nx < 0 or ny >=n or ny < 0:
							continue
						if (nx,ny) in seen:
							continue
						if abs(heights[x][y] - heights[nx][ny]) > cost:
							continue
						seen.add((nx,ny))
						
						q.append((nx,ny))
				return False

			l,r = 0, 1000000
			while l < r:
				mid =l + (r-l)/2
				
				if bfs(mid):
					r = mid
				else:
					l = mid + 1
			return l
