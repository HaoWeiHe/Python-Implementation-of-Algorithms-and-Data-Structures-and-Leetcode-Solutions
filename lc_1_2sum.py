class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for idx,n in enumerate(nums):
            if target - n in h:
                return [h[target-n],idx]
            h[n] = idx
        