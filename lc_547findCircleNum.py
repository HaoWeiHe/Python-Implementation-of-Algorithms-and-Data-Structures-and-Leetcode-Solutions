class UnifindSet():
	def __init__(self,n):
		self.parent = [x for x in range(n)]
		self.rank = [0] * n
	
	def find(self,x):
		if x != self.parent[x]:
			self.parent[x]  = self.find(self.parent[x])
		return self.parent[x]

	def Union(self,x,y):
		px, py = self.find(x),self.find(y)
		if self.rank[px] > self.rank[py]:
			self.parent[py] = px
		elif self.rank[px] < self.rank[py]:
			self.parent[px] = py
		else:
			self.parent[py] = px
			self.rank[px]  += 1

class Solution(object):
	def findCircleNum(self, isConnected):
		"""
		:type isConnected: List[List[int]]
		:rtype: int
		"""
		n = len(isConnected)
		U = UnifindSet(n)
		ans = set()
		# [[1,1,0],[1,1,0],[0,0,1]]
		for idx, v in enumerate(isConnected):
				
			for i,e in enumerate(v):
				if e == 1 :
					U.Union(idx, i)
		
		for i in range(n):
			ans.add(U.find(i))
		
		return len(ans)
