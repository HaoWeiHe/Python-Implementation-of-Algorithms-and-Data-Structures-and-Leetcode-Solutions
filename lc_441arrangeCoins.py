class Solution(object):
    def arrangeCoins(self, n):
        """
        area= (1+n)*n/2
        1 3 6  10
              ^
       |       |
        """
        def get_area(n):
            return ((1+n)*n)/2
        
        l, r = 0, n 
        if n == 1:
            return 1
        while l < r:

            m = (l+r)/2
            
            if get_area(m) > n:
                r = m 
            else:
                l = m + 1
        return l -1
  