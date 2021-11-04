# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        go through
        check if everyone knows i except him/herself
        """
        
        for candidate in range(n):
            flag = 0
            for i in range(n):
                if i == candidate:
                    continue
                if knows(candidate,i) or not knows(i,candidate):
                    
                    break
                flag += 1
            if flag == n-1:
                return candidate
            
        return -1
                    