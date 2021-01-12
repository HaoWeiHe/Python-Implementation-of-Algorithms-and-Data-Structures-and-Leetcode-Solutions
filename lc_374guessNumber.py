# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 0, n+1 
        while l < r:
            m = (l+r)/2
            res = guess(m)
            if res == 0 : return m
            if res == -1:
                r = m 
            else:
                l = m + 1
        
            