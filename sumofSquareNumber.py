class Solution(object):
    
    def is_square(self, x):
        x = math.sqrt(x)
        return x == int(x)
    
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in xrange(int(c**0.5) + 1 ):
            if self.is_square(c - a**2):
                return True
               
            
        return False
        