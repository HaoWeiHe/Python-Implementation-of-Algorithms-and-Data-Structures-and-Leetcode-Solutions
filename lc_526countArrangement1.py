

class Solution(object):
	def countArrangement(self, n):
		if n == 0 :
			return 0

		num = [e for e in range(1, n + 1)]
		self.ans = 0 
		
		def permute(num, l):
			if l == len(num):
				self.ans += 1
				
				return

			for i in range(l, n ):
				
				num[i], num[l] = num[l], num[i]
				if ( num[l] % (l + 1) == 0) or ( (l + 1) % num[l] == 0 ):
					permute(num[:],l + 1)
				num[i], num[l] = num[l], num[i]
				


		permute(num, 0)
		return self.ans

n = 4
print(Solution().countArrangement(n))