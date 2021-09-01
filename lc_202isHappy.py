class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h = set()
        while n and n not in h:
            tmp =  0
            h.add(n)
            while n:
                q,r = divmod(n,10)
                tmp += r**2
                n = q
            
            n = tmp
           
        return n == 1