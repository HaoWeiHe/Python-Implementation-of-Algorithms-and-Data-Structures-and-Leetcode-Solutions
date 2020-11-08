class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: 
            return x
        
        lf,rt = 0, x
        
        while 1:
            mid = (lf + rt)//2
            if mid ** 2 <= x < (mid+1)**2:
                return mid
            if mid ** 2 > x:
                rt = mid - 1
            else:
                lf = mid + 1

