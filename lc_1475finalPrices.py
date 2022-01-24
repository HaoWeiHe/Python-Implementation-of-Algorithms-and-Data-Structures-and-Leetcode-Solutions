class Solution(object):
	def finalPrices(self, prices):

		# n = len(prices)
		# ans = []
		# for i in range(n):
		#	 flag = True
		#	 for j in range(i+1,n):#[8,9,10,4,6,2,3]
		#		 if prices[j] <= prices[i]:
		#			 ans.append(prices[i] - prices[j])
		#			 flag = False
		#			 break
		#	 if flag:
		#		 ans.append(prices[i])
		# return ans
		"""
		#[8,4,7,10,12,14,15]
				w	  
						  r
		 if w not reach n, disocunt = 0 
		 0 1 2 3 4 5 6 7 8  9
		[8,7,4,2,8,1,7,7,10,1]
	   	[] #idx whos A[idx] <= cur_val
	   
		
		"""

		stack = []
		for idx, val in enumerate(prices): #[8,4,6,2,3]
			while stack and prices[stack[-1]] >= val: #[(0,8),]
				prices[stack.pop()] -= val
			stack.append(idx)
		return prices

       
       