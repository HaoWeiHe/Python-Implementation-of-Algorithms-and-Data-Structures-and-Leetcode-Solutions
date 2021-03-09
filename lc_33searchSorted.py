class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r :
            m = (l+r)/2
            if nums[m] == target:return m
            
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r-1]:
                    l = m + 1
                else:
                    r = m
        return -1