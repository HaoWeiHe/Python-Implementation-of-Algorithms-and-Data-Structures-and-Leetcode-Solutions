import collections
class unifind():
	def __init__(self, lst):
		self.parent = [i for i in range(len(lst))]
		C = collections.Counter(lst)
		self.rank = [C[ele] for ele in range(len(lst))]

	def find(self,x):
		if x!= self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self,x,y):

		px, py  = self.find(x), self.find(y)
		if px == py:
			return True
		if self.rank[px] < self.rank[py]:
			self.rank[py] += 1
			self.parent[px] = py
		elif self.rank[px] > self.rank[py]:
			self.rank[px] += 1
			self.parent[py] = px
		else:
			#px <- py
			self.rank[px] += 1
			self.parent[py] = px
		return False

tests = [[1,0], [0,0,2], [0,0,0],[3,0,0,3]]
class sol():
	def validTree(self, lst):
		uniF = unifind(lst)
		for idx, val in enumerate(lst):
			if idx == val:
				continue
			if uniF.union(val, idx):
				return False
		return len(set(uniF.parent)) == 1


for lst in tests:
	print(sol().validTree(lst))
