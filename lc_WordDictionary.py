class Node():
	def __init__(self):
		self.isWord = False
		self.children = collections.defaultdict(Node)
		
class WordDictionary(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = Node()
		

	def addWord(self, word):
		"""
		Adds a word into the data structure.
		:type word: str
		:rtype: None
		"""
		node = self.root
		
		for c in word:
			
			node = node.children[c]
		node.isWord = True

	def search(self, word):
		"""
		Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
		:type word: str
		:rtype: bool
		"""
		node = self.root
		prenode = node
		for i,c in enumerate(word):
			print(i,c,word[i-1], prenode.children[word[i-1]])
			if c != "." and c not in node.children: return False
			if c =="." :
				return [self.search(word[:i] + anyC + word[i+1:]) for anyC in node.children]
				
			prenode = node
			node = node.children[c]
			{f{r,p,g}}]}
			{f{.,}}
		return node.isWord

{b{a{d},e{d}}}
{b{}}
{.{}}
bad
bed
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)