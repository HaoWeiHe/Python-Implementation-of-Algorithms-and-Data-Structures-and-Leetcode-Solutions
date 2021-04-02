# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0 
        for i in range(1,n):
            if knows(candidate,i):
                candidate = i
        
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate,i) or not knows(i,candidate):
                return -1
        return candidate
    def findCelebrity2(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        for b in range(n):
            flag = 1
            for a in range(n):
                if b ==a:continue
                if knows(b,a) or knows(a, b) == 0:
                    flag = 0
                    break

            if flag:
                return b 
            
        return -1
                    
        
        