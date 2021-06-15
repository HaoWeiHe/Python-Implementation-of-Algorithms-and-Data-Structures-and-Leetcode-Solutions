class Solution(object):
    def mySqrt(self, x):
        """
        (l,r]
        
        if fun(m) > x: find right
        else: find left
        """
        l, r = 0, x + 1
        while l < r:
            m = l + (r-l)/2
            if m*m > x:
                r = m 
            else:
                l = m + 1
        return l -1
        