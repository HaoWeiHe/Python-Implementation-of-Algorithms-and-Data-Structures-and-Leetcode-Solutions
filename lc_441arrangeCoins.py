class Solution(object):
    def arrangeCoins(self, n):
        """
        equation: x(x+1)/2 <= n 
                 x^2 + x -2n <= 0 
                 recall if ax^2 + bx + c = 0 
                 a = 1, b = 1, c = -2

        -1 + sqrt(1 + 8n)/2
        """
        
        return int((-1 + (1+8*n)**0.5)/2)
    def arrangeCoins2(self, n):
        """
        area= (1+n)*n/2
        1 3 6  10
              ^
       |       |
        """
        def get_area(n):
            return ((1+n)*n)/2
        
        l, r = 0, n 
        while l < r:

            m = (l+r)/2
            
            if get_area(m) < n:
                r = m 
            else:
                l = m + 1
        return l -1
            
