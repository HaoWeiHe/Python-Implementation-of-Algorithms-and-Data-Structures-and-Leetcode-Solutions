class Solution(object):
    def mySqrt(self, x):
        """
        bfs
        lo ** 2 < x <= right **2
        
        [l,r)
        """
        if x < 2: return x
        l,r = 0,x
        
        while l < r: 
            m = (l+r)/2 
            if m **2 > x:
                r = m  #[l,m)
            else:
                l = m + 1 #[m+1,r)
        return l - 1