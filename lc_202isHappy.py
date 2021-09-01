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
        fast, slow = get_next(n) ,n
        while fast != 1 and fast!= slow:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
            
           
        return fast == 1 
    def isHappy2(self, n):
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
        fast, slow = n, get_next(n)   
        while fast != 1 and fast!= slow:
            fast = get_next(get_next(fast))
            slow = get_next(slow)
            
           
        return fast == 1 