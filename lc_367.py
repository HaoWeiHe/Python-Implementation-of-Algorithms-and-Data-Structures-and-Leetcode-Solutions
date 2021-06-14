class Solution(object):
    def isPerfectSquare(self, num):
        """
        16:
        1 2 4
        1 4 16 bingo
        
        14
        1 2 4
        1 4 16
        target = 16
        1,16 49
        1,6  3
        3~6 
        
        """
        
        low, high = 1, num
        
        def bs(low, high):
            if low > high:
                return False
            mid = (low + high) / 2
            if mid* mid == num:
                return mid
            
            if mid* mid < num:
                return bs(mid+1, num)
            return bs(low, mid -1 )
        return bs(0, num/2)
    def isPerfectSquare2(self, num):
        """
        16:
        1 2 4
        1 4 16 bingo
        
        14
        1 2 4
        1 4 16
        target = 16
        1,16 49
        1,6  3
        3~6 
        
        """
        
        low, high = 1, num
        
        def bs(low, high):
            if low > high:
                return False
            mid = (low + high) / 2
            if mid* mid == num:
                return mid
            
            if mid* mid < num:
                return bs(mid+1, num)
            return bs(low, mid -1 )
        return bs(0, num)