
class Solution(object):
	def trap(self, arr):
		
		if not arr:
			return 0
		n = len(arr)
		lft,right = [0]*n,[0]*n
		
		lft[0], right[-1] = arr[0], arr[-1]

		for i in range( 1, n):
			lft[i] = max(lft[i-1], arr[i])
	
		
		for i in range(n-2, -1, -1):
			right[i] = max(right[i+1],arr[i])
		
		res = 0 
		for i in range(n):
			res+= min(lft[i], right[i]) - arr[i]
	
		return res
