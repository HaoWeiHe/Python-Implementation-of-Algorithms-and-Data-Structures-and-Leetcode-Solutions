import collections
from heapq import heappop as pop, heappush as push	
class Solution(object):
	"""
	dist[v] = max(dist[u],cost[u,v])
	#notice dist[u] is the best Solution

	"""
	def minimumEffortPath(self, heights):
		m, n = len(heights), len(heights[0])
		q = [(0,0,0)]
		effort = collections.defaultdict(lambda: float('inf'))
		effort[(0,0)] = 0 
		seen = set((0,0))
		while q:
			val, x,y = pop(q)
			seen.add((x,y))
			for dx, dy in [[0,1],[0,-1],[-1,0],[1,0]]:
				nx, ny = dx + x, dy + y 
				if (nx,ny) in seen: 
					continue
				if not (0 <= nx < m and 0 <= ny < n):
					continue
				eff  = max(effort[(x,y)], abs(heights[x][y] - heights[nx][ny]))
				if effort[(nx,ny)] > eff:
					effort[(nx,ny)] = eff
					push(q,(effort[(nx,ny)] ,nx,ny))
			
				if x== m-1 and y == n-1: return effort[(m-1,n-1)]
		return effort[(m-1,n-1)]


	def minimumEffortPath2(self, heights):
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
heights = [[[1,2,3],[3,8,4],[5,3,5]], [[1,2,2],[3,8,2],[5,3,5]], [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]]
ans = [1,2,0]
for i,h in enumerate(heights):
	assert ans[i] == Solution().minimumEffortPath(h)