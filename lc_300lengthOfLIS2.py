from heapq import heappop, heappush
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        [10,9,2,5,3,7,101,18]
         10,1
         9,1
         2,1
         5,1
         3,2
         7,3
         101,4
        """
        def insert(target):
            l, r= 0, len(h)
            
            while l < r:
                m = (l  + r) / 2
                if target <= h[m][0]:
                    r = m 
                else:
                    l = m + 1
                
            return l  #0,1 ->m = 0
        h = []
        ans = 0 
        for e in nums:
           
            idx = insert(e)
            tmp = 0 
            for i in range(0,idx):
                value, count = h[i]
                tmp = max(tmp, count)
            h = h[:idx] + [(e, tmp+1)] + h[idx:]
        return max([x[1] for x in h])