	
import collections
class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		if not beginWord or not endWord in wordList or not wordList: return 0
		self.length = len(beginWord)	
		g = collections.defaultdict(list)
		
		if beginWord not in wordList: wordList+= [beginWord]
		
	
		for w in wordList:
			for i in range(self.length):
				g[w[:i]+"*"+w[i+1:]].append(w)
				# {'do*': ['dot', 'dog'], 'h*t': ['hot', 'hit'], '*ot': ['hot', 'dot', 'lot'], 'd*t': ['dot'], 'lo*': ['lot', 'log'], 'ho*': ['hot'], 'c*g': ['cog'], 'l*g': ['log'], '*it': ['hit'], 'd*g': ['dog'], '*og': ['dog', 'log', 'cog'], 'hi*': ['hit'], 'co*': ['cog'], 'l*t': ['lot']})

		def visited(q, visted, vistedOther):
			
			top, level = q.popleft()
			for i in range(self.length):
				combineW = top[:i] + "*" + top[i+1:]
				for w in g[combineW]:
					if w in vistedOther:
						return vistedOther[w] + level #v2: {"cog":1} v1{hit:1}
					if w not in visted:
						q.append((w, level+1))
						visted[w] = level +1

			return None

		visted1 = {beginWord: 1}
		visted2 = {endWord: 1}
	

		q1, q2 = collections.deque([(beginWord,1)]), collections.deque([(endWord,1)])

		while q1 and q2 and len(visted1) <= len(wordList) and len(visted2) <= len(wordList):
			
			ans = visited(q1, visted1, visted2)
			if ans : return ans
			ans = visited(q2, visted2,visted1)
			if ans: return ans	

		return 0

beginWord = "hot"#"hit"
endWord = "dog"
wordList = ["hot","dog"]#["hot","dot","dog","lot","log","cog"]


# "dog"

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]

beginWord = "hot"#"hit"
endWord = "dog"
wordList = ["hot","dot","dog","lot","log","cog"]




print(Solution().ladderLength(beginWord, endWord, wordList))
