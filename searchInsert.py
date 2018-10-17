class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        for idx in xrange(len(nums)):
            if target <= nums[idx]:
                # print(idx, nums[idx])
                return idx
            # if target < nums[idx]:
            #     return idx 
        