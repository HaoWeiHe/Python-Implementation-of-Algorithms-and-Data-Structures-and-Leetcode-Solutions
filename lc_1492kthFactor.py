from heapq import heappop as pop, heappush as push
class Solution(object):
    def kthFactor(self, n, k):
        """
       [1, 2, 3, 4, 6, 12]
       1, 12
       2,6
       3,4
       sqrt(12) = 3.33 -> 3)
        """
        q = []
        for ele in range(1,int(n**0.5) + 1 ):
            factor, remind = divmod(n, ele)
            if remind == 0:
                push(q, factor)
                if ele != factor:
                    push(q, ele)
        ans = 0 
        if k > len(q):
            return -1
        for _ in range(k):
            ans = pop(q)
        return ans 
        