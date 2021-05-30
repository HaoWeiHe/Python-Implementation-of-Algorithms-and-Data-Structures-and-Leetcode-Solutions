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
