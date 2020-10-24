
# import collections
# class Solution(object):
# 	def ladderLength(self, beginWord, endWord, wordList):
		
# 		g = collections.defaultdict(list)
# 		n = len(wordList)
# 		# for i in range(n):
# 		# 	for j in range(i+1,n):
# 		# 		for c in range(len(beginWord)):
# 		# 			A,B = wordList[i], wordList[j]
# 		# 			# print(A,B)
# 		# 			if A[:c]+A[c+1:] == B[:c]+B[c+1:]:
# 		# 				g[A].append(B)
# 						# break
# 		for word in wordList:
# 			for i in range(len(beginWord)):
			
# 				g[word[:i] + "*" + word[i+1:]].append(word)

# 		visted = set()
# 		# q = [beginWord]
# 		queue = collections.deque([beginWord])
# 		# collections.deque
# 		length  = 1 
		
# 		while q:
# 			for _ in range(len(q)):
# 				top = q.popleft() 
				
# 				if top in visted: continue
# 				for i in range(len(beginWord)):
# 					intermediate_word = top[:i] + "*" + top[i+1:]
# 					for word in g[intermediate_word]:
# 						if top == endWord: return length
						
# 						q.extend(g[intermediate_word])
# 				visted.add(top)
# 			length+=1
# 		return 0

# # q.ex[]

# beginWord,endWord,wordList = "hit","cog",["hot","dot","dog","lot","log","cog"]
# print(Solution().ladderLength(beginWord, endWord, wordList))


import collections
class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		
		g = collections.defaultdict(list)
		wordList = [beginWord] + wordList

		n = len(wordList)
		# for i in range(n):
		# 	for j in range(i+1,n):
		# 		for c in range(len(beginWord)):
		# 			A,B = wordList[i], wordList[j]
		# 			if A[:c]+A[c+1:] == B[:c]+B[c+1:] and B not in g[A] and A not in g[B]:
		# 				g[A].append(B)
		# 				g[B].append(A)

		for word in wordList:
			for i in range(len(beginWord)):
				g[word[:i]+"*"+word[i+1:]].append(word)

		# print(g)
		# for word in wordList:
		# 	for i in range(len(beginWord)):
			
		# 		g[word[:i] + "*" + word[i+1:]].append(word)
		# print(g)
		visted = set()
		
		q = collections.deque([beginWord])
		length  = 1 
		
		while q:
			for _ in range(len(q)):
				top = q.popleft() 
				
				if top in visted: continue
				
				if top == endWord: return length
				for i in range(len(beginWord)):
					intermediate_word  = top[:i]+"*" + top[i+1:]
					for w in g[intermediate_word]:
						if w == endWord: return length
						if w not in visted:
							q.extend(g[intermediate_word])

				
				visted.add(top)
			# print(top)
			length+=1
		return 0

# q.ex[]