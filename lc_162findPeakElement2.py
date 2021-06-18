        return l
class Solution(object):
    def findPeakElement(self, nums):
        """
        [1,2,3,1]
         l     r
           m m+1
             l
             r
           
        """
        if len(nums) <=1:
            return 0
        
        l,r = 0 , len(nums) - 1
        while l < r:
            m = l + (r-l)/2  
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l