"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
       [[[1,2],[5,6]],[[1,3]],[[4,10]]]
       [1,2] [1,3] [4,10] [5,6]
end  = 2       3    10     
res =[]       []  [3,4] (start > preend)

         
        """
        ints = sorted([i for s in schedule for i in s], key = lambda x: x.start)
        ans = []
        end = ints[0].end
        for e in ints[1:]: 
            if e.start > end: #end = 3
                ans.append(Interval(end, e.start))
            end = max(e.end, end)
        return ans
    def employeeFreeTime2(self, schedule):
        """
        [[[1,2],[5,6]],[[1,3]],[[4,10]]]
        [1,3], [4,10]
        1,3  if overlap
        4,10 if not, append a new one
        
        """
        h =[]
        for ele in schedule:
            for sub in ele:
                heappush(h, (sub.start, sub))
        bz = []
        while h:
            _, sub = heappop(h)
            if not bz:
                bz.append(sub)
                continue
            #overlap
          
            if sub.end < bz[-1].start or sub.start > bz[-1].end:
                bz.append(sub)
            else:
                bz[-1].end = max(bz[-1].end , sub.end)
                bz[-1].start = min(bz[-1].start, sub.start)
#         [1,3], [4,10]
        if len(bz) == 1:
            return bz
        ans = []
        for idx in range(1, len(bz)):
            ans.append(Interval(bz[idx-1].end, bz[idx].start))
        return ans
            