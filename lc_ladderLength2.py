
import collections
class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		self.res = []
		def callback(record, history,cur,visted,level):
			if cur == beginWord: 
				print("re")
				self.res.append(history)
				# return 
			
			if cur in visted :#and visted[cur]!=len(history): 
				# print(cur, level,visted[cur],len(history))
				return
			for ele in record[cur]:
				# print(cur, record[cur],ele)
				visted[cur] = level
				history.append(ele)
				callback(record,history, ele,visted,level+1)
				del visted[cur]
				history.pop()


		g = collections.defaultdict(list)
		wordList = [beginWord] + wordList

		n = len(wordList)

		for word in wordList:
			for i in range(len(beginWord)):
				g[word[:i]+"*"+word[i+1:]].append(word)

		visted = dict()
		q = collections.deque([(beginWord, 1)])
				
		record = collections.defaultdict(set)
		while q:
			
			top, level = q.popleft() 
		
			for i in range(len(beginWord)):
				intermediate_word  = top[:i]+"*" + top[i+1:]
				for w in g[intermediate_word]:
					if w in visted and level!= visted[w]: continue
					if w!=top:
						record[w].add(top)
					if w == endWord:
						print(record,w)
						callback(record,[],w,{w:0},0)
						print(self.res[0][::-1])
						return level+1
					
					q.append((w, level + 1))
			intermedate_w = endWord
			res = []
			
			
			visted[top]= level


		return 0

#  ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
beginWord,endWord,wordList = "hit","cog",["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

# defaultdict(<type 'list'>, {'hit': ['hit'], 'log': ['lot', 'log'], 'dog': ['dot', 'dog'], 'hot': ['hot'], 'lot': ['lot', 'log'], 'dot': ['dot', 'dog']})

