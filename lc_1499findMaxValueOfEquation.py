class Solution(object):
	def findMaxValueOfEquation(self, points, k):
		"""
		:type points: List[List[int]]
		:type k: int
		:rtype: int
		"""
		j = 1 
		ans= float('-inf')
		while j < len(points):
			i = j -1
			while i >= 0 and abs(points[i][0] - points[j][0]) <= k:
				ans = max(ans, abs(points[i][0] - points[j][0]) + points[i][1] + points[j][1] )
				print(ans, points[i], points[j])
				i -=1 
			j += 1
		return ans
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(Solution().findMaxValueOfEquation(points,k))