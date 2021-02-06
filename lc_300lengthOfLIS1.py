from  bisect import bisect_left
class Solution(object):
    def insert(self, lst, n):
        if not lst:
            return 0

        l, r = 0, len(lst) #(l,r]
        while l < r:
            m = (l+r)/2
            if lst[m] > n: 
                r = m
            else:
                l = m +1
        return l - 1
    def lengthOfLIS(self, nums):
        """
        [10,9,2,5,3,7,101,18]
    lst=[10] 
    lst=[9]
    lst=[2]
    lst=[2,5]
        """
        lst = []
        res = 0
        for e in nums:
            # idx = self.insert(lst,e)
            idx = bisect_left(lst, e)
            if idx >= len(lst):
                lst.append(e)
            else:
                lst[idx] = e
        return len(lst)


    def lengthOfLIS2(self, nums):
        """
        [10,9,2,5,3,7,101,18]
          1 1 1 2 2 3  4   
        """
        h = {}
        for i,n in enumerate(nums):
            tmp = 0
            for ele in h:
                if ele < n:
                    tmp = max(tmp, h[ele])
            h[n] = tmp + 1
        
        return max(h.values())

    def insert(self, lst, target):

        l, r = 0, len(lst) #(l,r]
        while l < r:
            m = (l+r)/2
            if lst[m] >= target: 
                r = m
            else:
                l = m +1
        return l 
    def lengthOfLIS3(self, nums):
        """
        [10,9,2,5,3,7,101,18]
    lst=[10] 
    lst=[9]
    lst=[2]
    lst=[2,5]
    lst=[2,3]
        """
        lst = [float('inf')]
        res = 0
        for e in nums:
            idx = self.insert(lst,e)

            if idx >= len(lst):
                lst.append(e)
            else:
                lst[idx] = e
            print(e,lst)
        return len(lst)


   