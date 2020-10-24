
class Solution(object):



	def minDistance(self, word1, word2):
		res = []
		m,n = len(word1),len(word2)
		D = map(lambda y : map( lambda x, y: y if x ==0 else x if y ==0 else 0 , range(n+1), [y]*(n+1)), range(m+1))
		# map(lambad y: _fuc_, range(m+1)) //from 1 to len_of_y )
		for x in range(1, m+1):
			for y in range(1,n+1):
				# print(D[x],D[y])
				D[x][y] = min(D[x][y-1]+1, D[x-1][y]+1, D[x-1][y-1] + apply(lambda : 0 if word1[x-1] == word2[y-1] else 1))


		
		return D[-1][-1]