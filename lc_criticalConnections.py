import Collections.defaultdict


class Solution(object):
	def __init__(self):
		self.d = defaultdict(list)
		self.timer = 0
		self.visited = set()

	def criticalConnections(self, n, connections):

		d = self.d
		for a,b in connections:
			d[a].append(b)
			d[b].append(a)

		def dfs(cur, parent,t ):

			self.timer += 1
			
			for node in d[cur]:
				dfs(node, cur,self.timer )



		dfs(0)
	 # n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
	criticalConnections()

		