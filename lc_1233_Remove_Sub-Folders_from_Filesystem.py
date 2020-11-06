import collections
class Node():
	def __init__(self):
		self.children = collections.defaultdict(Node)
		self.isWord = False
		self.word = ""

class Trie():
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		r = self.root
		
		for c in word.split("/")[1:]:
			r = r.children[c]
		r.isWord = True
		r.word = word


	def getPrefixs(self):
		r = self.root
		res = []
		def dfs(node, predir):
			if node.isWord:
				res.append("/" + '/'.join(predir))
				return 
				
			for c in node.children:
				dfs(node.children[c], predir + [c])
		dfs(r, [])
		return res

	
class Solution(object):
	def removeSubfolders(self, folder):
		""" 
		use trie:
		if reach isWord, then terminate this path
		"""
		trie, res = Trie(), []

		for ele in folder:
			trie.insert(ele)

		return trie.getPrefixs()
		
		
folder =["/ah/al/am","/ah/al"]# ["/a","/a/b/c","/a/b/d"]#["/a","/a/b","/c/d","/c/d/e","/c/f"]
a = Solution().removeSubfolders(folder)
print(a)
