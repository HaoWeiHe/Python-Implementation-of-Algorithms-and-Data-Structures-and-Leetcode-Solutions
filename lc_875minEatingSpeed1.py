class Solution(object):
    def minEatingSpeed(self, p, H):
        """
        def canfinish function (she can finish all cake on time)
        l,r = 0, piles +1
        [l,r)
        binary seach from range [l,r)
        return l 
        """
        
        l, r = 1, max(p) + 1
        
        def canfinish(m):
            h = 0
            for i in p:
                h += (i + m - 1)/m
            return h <= H
        while l < r:
            m = (l+r)/2
            if canfinish(m):
                r = m
            else: 
                l = m + 1
        return l