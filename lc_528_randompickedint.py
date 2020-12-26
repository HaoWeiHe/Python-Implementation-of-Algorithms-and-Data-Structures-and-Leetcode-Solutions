class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        
        for i in range(len(w)):
            if i>0:
                w[i]+=w[i-1]
        self.w= w

    def pickIndex(self):
        """
        :rtype: int
        """
        
        rand=random.randint(1,self.w[-1])
        return bisect.bisect_left(self.w,rand)
