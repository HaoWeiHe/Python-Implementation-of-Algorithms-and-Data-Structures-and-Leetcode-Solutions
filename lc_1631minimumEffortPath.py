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
			
				if x== m-1 and y == n-1: 
					return effort[(m-1,n-1)]
		return -1 

heights = [[[1,2,3],[3,8,4],[5,3,5]], [[1,2,2],[3,8,2],[5,3,5]], [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]]
ans = [1,2,0]
for i,h in enumerate(heights):
	print(ans[i],Solution().minimumEffortPath(h) )
	assert ans[i] == Solution().minimumEffortPath(h)