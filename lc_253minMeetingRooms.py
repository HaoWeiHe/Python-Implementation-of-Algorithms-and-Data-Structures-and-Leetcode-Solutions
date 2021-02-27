import collections
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        d, t = collections.defaultdict(int), set()
        for i,j in intervals:
            d[i] += 1
            d[j] -= 1
            t.add(i)
            t.add(j)
        t = list(t)
        t.sort()
        
        res, acc = 0, 0
        for i in t:
            acc += d[i]
            res = max(res, acc)
        return res
