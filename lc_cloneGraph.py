# """
# # Definition for a Node.
# class Node(object):
# 	def __init__(self, val = 0, neighbors = None):
# 		self.val = val
# 		self.neighbors = neighbors if neighbors is not None else []
# """

# class Solution(object):
# 	def cloneGraph(self, node):
# 		"""
# 		:type node: Node
# 		:rtype: Node
# 		"""
# 		if not node: return node

# 		visted =dict()
# 		def dfs(node,visted):
# 			if not node: return node
# 			if node in visted: return visted[node]

# 			cur = Node(node.val, [])
# 			visted[node]= cur
# 			for e in node.neighbors:
# 				cur.neighbors.append(dfs(e,visted))
# 			return cur
# 		return dfs(node, visted)

"""
# Definition for a Node.
class Node(object):
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: Node
		:rtype: Node
		"""
		if not node: return node
		
		
		visted = dict()
		visted[node] = Node(node.val,[])
		q = collections.deque([node])

		while q:
			n = q.popleft()
			
			for e in n.neighbors:
				if e not in visted:
					visted[e] = Node(e.val,[])
					q.append(e)
				visted[n].neighbors.append(visted[e])	
				# visted[e].neighbors.append()
				
		return visted[node]



