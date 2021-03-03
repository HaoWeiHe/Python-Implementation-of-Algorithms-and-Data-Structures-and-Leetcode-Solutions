class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 10 and x%10 == 0): return False
        return x == self.reverse(x)
    
    def reverse(self, x):
        res = 0 
        
        while x !=0:
            tail = x %10
            res = res* 10 + tail
            x = x / 10 
        
        return res
        
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x = str(x)
        l,r = 0, len(x)-1
        while l < r:
            if x[l]!= x[r]:
                return 0
            l +=1 
            r -=1
        return 1

