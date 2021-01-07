class Solution(object):
    def mySqrt(self, x):
        """
        bfs
        lo ** 2 < x <= right **2
        
        (l,r]
        """
        l,r = 0,x

        while l <= r:
            m = (l+r)/2 #2
            if m ** 2 == x:
                return m
            if m **2 >= x:
                r = m -1 #(l,m-1]
            else:
                l = m + 1 #(m+1, r]
        return r