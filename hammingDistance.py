class Solution(object):
	def hammingDistance(self, x, y):
		_max = max(x,y)
		res = 0 
		while(_max):
			if not x%2 == y%2:
				res +=1
			x = x / 2
			y = y / 2 
			_max = _max/2
			
		return res

