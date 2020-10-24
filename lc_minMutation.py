import collections
class Solution(object):
	def minMutation(self, start, end, bank):
		idx,n = 0 , len(start)
		length = 0
		bank =set(bank)
		choices = ["A", "C", "G", "T"]
		def mutation(A):
			res = []		
			for i in range(len(A)):
					for c in choices:
						newDNA = A[:i]+ c + A[i+1:]
						if newDNA in bank: 
							res.append(newDNA)
			return res
			

		q = collections.deque([start])
		visited = set()
		while q:
			for _ in range(len(q)):
				top = q.popleft()
				if top in visited: continue
				if top ==end: return length
				newDNA = mutation(top)
				q.extend(newDNA)
				visited.add(top)
			length+=1

		return -1
		# "AAACCCCC" -> if exist, start form here
		# "AACCCCCC"
		#    	v -> start from here 
start = "AACCGGTT"
end=   "AAACGGTA"
bank= ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# start = "AACCGGTT"
# end = "AACCGGTA"
# bank= []

# start= "AACCGGTT"
# end=  "AAACGGTA"
# bank=["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
# start = "AAAAACCC"
# end =   "AACCCCCC"
# bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]#["AACCGGTA", "AACCGCTA", "AAACGGTA"]
print(Solution().minMutation(start,end,bank))
