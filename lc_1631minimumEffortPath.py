
class Solution(object):
	def minimumEffortPath(self, heights):

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