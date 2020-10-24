	
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
				

		def visited(q, visted, vistedOther,parent):
			
			top, level = q.popleft()
			for i in range(self.length):
				combineW = top[:i] + "*" + top[i+1:]
				for w in g[combineW]:
					if w in vistedOther:
						return top,vistedOther[w] + level, w #v2: {"cog":1} v1{hit:1}
					if w not in visted:
						q.append((w, level+1))
						visted[w] = level +1
						parent[w].append(top)


			return top,None,None

		visted1 = {beginWord: 1}
		visted2 = {endWord: 1}
		p1, p2 = collections.defaultdict(list),collections.defaultdict(list)
		q1, q2 = collections.deque([(beginWord,1)]), collections.deque([(endWord,1)])


		def explore(node,history,visted,level,mid,parents):
			# print(level)
			if len(history) > level: return 
			if node == mid: 
				self.res.append(history[::-1])
				return 

			if node in visted: return 
			visted.add(node)
			for subnode in parents[node]:
				explore(subnode,history+[subnode],visted,level,mid,parents)
			visted.remove(node)


		self.res = []
		while q1 and q2 and len(visted1) <= len(wordList) and len(visted2) <= len(wordList):
			
			node, ans, mid= visited(q1, visted1, visted2,p1)
			if ans : 
				explore(node, [node],set(),ans,p1)
				return self.res if ans else []
			ans = visited(q2, visted2,visted1,p2)
			if ans: 
				explore(node, [node],set(),ans,mid,p2)
				return self.res if ans else []


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




# print(Solution().ladderLength(beginWord, endWord, wordList))

print(Solution().ladderLength(beginWord, endWord, wordList))
