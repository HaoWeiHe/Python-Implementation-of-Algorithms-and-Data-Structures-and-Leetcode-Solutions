class Solution(object):
    def isMonotonic(self, l):
        """
        [1,1,2,2,3]
       >= 0 
       or <=0 
        """

        def inc():
            for a,b in zip(l,l[1:]):
                if b < a:
                    return False
            return True
        def dec():
            for a,b in zip(l, l[1:]):
                if a < b:
                    return False
            return True
                    
        return inc() or dec()