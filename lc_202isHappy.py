class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        h = set()
        def get_next(n):
            tmp =  0
            while n:
                q,r = divmod(n,10)
                tmp += r**2
                n = q
            return tmp
                
        while n and n not in h:
            h.add(n)
            n = get_next(n)
            
           
        return n == 1 