from  heapq import heappop as pop, heappush as push


class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        compute yi + yj + xj - xi = (xj + yj) + yi - xi
        and xj - xi <= k 
        store: xi as key and yi-xi as value
         [[1,3],[2,0],[5,10],[6,-10]]
 
        ele    | max_heap           |   ans
        (1,3)    [(2,1) ]               -inf
        (2,0)   [(2,2),(2,1)]              4
        (5,10)  [(5,5)]                    4  
        """
        h = []
        ans = float('-inf')
        for e in points:
            xj, yj = e
            while h and xj - h[0][1] > k:
                pop(h)
            if h:
                ans = max(ans, -1 * h[0][0] + xj + yj)
            push(h,(-1*(yj - xj), xj))
        return ans
            
	def findMaxValueOfEquation2(self, points, k):
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
				
				i -=1 
			j += 1
		return ans
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
print(Solution().findMaxValueOfEquation(points,k))