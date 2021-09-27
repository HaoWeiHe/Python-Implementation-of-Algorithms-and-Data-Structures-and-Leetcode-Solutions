"""
[4, 5, 8, 2]
[2,3,4,5,5,8]


"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k 
        self.h = nums
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class KthLargest2(object):
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