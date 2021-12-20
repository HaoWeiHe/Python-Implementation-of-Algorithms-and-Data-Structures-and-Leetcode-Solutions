class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)
        while l < r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m 
        
        return l if (0 <= l < len(nums) and nums[l] == target) else -1
                