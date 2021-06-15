
class Solution(object):
    def findMin(self, nums):
        if nums[0] < nums[len(nums) -1 ]:
            return nums[0]
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)/2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = m 
        return nums[l]

class Solution(object):
    def findMin(self, nums):
        """
        3,4,5,1,2,3
            m
        (3,4) (5 1,2,3)
        r  l 
        (3,4,5) (1,2,3)
           
        """
        def qs(l,r):
            if r - l <= 1:
                return min(nums[l], nums[r])
            if nums[r] > nums[l]:
                return nums[l]
            m = l + (r-l)/2
            return min(qs(l, m), qs(m+1,r))
        return qs(0,len(nums)-1)
                
        