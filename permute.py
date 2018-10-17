class Solution(object):
    
    def __init__(self):
        self.total = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.total = []
        def helper(nums,l,r):
            if l == r:
                
                self.total.append(nums[:])
                return nums
            
            for inx in range(l,r):
                nums[l], nums[inx]  = nums[inx], nums[l]
                helper(nums,l+1,r)
                nums[inx], nums[l] = nums[l], nums[inx]

        
        
        r = len(nums)
        l = 0
        helper(nums,l,r)
        return self.total
                