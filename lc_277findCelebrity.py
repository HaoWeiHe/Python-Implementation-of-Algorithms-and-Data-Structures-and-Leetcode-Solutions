from functools import lru_cache

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0 
        @lru_cache()
        def history_know(self,a,b):
            return knows(a,b)

        for i in range(1,n):
            if history_know(candidate,i):
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
                    
        
        