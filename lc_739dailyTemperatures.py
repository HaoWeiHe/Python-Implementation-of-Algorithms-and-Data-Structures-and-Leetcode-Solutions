from heapq import heappop, heappush
class Solution(object):
    def dailyTemperatures(self, tmpr):
        """
         [73,74, 75, 71,  69,72,76,73]
                                 ^
    heap:             75:2, 69:3  72:4
        [1,1,_,5-3, ]
        """
        h = []
        ans = [0] * len(tmpr)
        for i,t in enumerate(tmpr):
           
            while h and h[0][0] < t:
                _, res_i = heappop(h)
                ans[res_i] = i - res_i
            heappush(h,(t,i) )
            
        return ans