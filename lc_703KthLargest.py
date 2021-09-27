"""
[4, 5, 8, 2]
[2,3,4,5,5,8]


"""

class KthLargest(object):
    def insert(self, target):
        l, r= 0 , len(self.h)
        while l < r:
            m = (l+r)/2
            if target < self.h[m]:
                r = m
            else:
                l = m +1
        self.h = self.h[:l] + [target] + self.h[l:]
    
    def __init__(self, k, nums):

        self.h = []
        self.k = k 
        
        for e in nums:
            self.insert(e)

    def add(self, val):
        self.insert(val)
       
        return self.h[-self.k]