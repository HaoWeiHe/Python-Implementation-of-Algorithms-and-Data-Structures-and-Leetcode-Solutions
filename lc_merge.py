
class Solution(object):
	def merge(self, intervals):
		if not intervals:
			return [] 

		startLst = []
		endLst = []
		# [[1,3],[2,6],[8,10],[15,18]]】
		for elem in intervals:
			startLst.append(elem.start)
			endLst.append(elem.end)

		startLst.sort()
		endLst.sort()
		i, j, res = 0,0, []
		# print(startLst)
		# print(endLst)

		n = len(intervals)
		while(i < n):
			if(i == n-1 or startLst[i+1] > endLst[i]):
				
				res.append([startLst[j],endLst[i]])
				j = i +1
			i +=1
			
		# print(res)
		return res


