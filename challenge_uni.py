import collections
class unifind():
	def __init__(self, lst):
		self.parent = [e for e in lst]
		C = collections.Counter(lst)
		self.rank = [C[ele] for ele in range(len(lst))]
	def find(self,x):
		if x!= self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	def union(self,x,y):
		px, py = self.find(x), self.find(y)
		if px == py:
			return 
		if self.rank[px] < self.rank[py]:
			self.rank[py] += 1
			self.parent[px] = py
		elif self.rank[px] > self.rank[py]:
			self.rank[px] += 1
			self.parent[py] = px
		else:
			self.rank[px] += 1
			self.rank[py] = px

lst = [0,0,2]
uniF = unifind(lst)
for idx, val in enumerate(lst):
	uniF.union(idx, val)


print(len(set(uniF.parent)) == 1)

