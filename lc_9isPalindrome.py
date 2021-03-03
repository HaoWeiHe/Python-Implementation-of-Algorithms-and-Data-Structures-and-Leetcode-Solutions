class Solution(object):
    def isPalindrome(self, x):
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