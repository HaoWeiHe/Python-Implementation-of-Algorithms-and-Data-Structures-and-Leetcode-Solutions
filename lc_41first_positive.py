class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if 1 not in nums:return 1
        if nums == [1]:return 2
        for idx, n in enumerate(nums):
            if n <= 0 or n > len(nums):
                nums[idx] = 1
        
        for ele in nums:
            a = abs(ele)
           
            if a == len(nums):
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        
        for idx, v in enumerate(nums):
            if idx ==0:continue
            if v > 0:return idx
#[2,1]
        if nums[0] > 0:
            return len(nums)
        return len(nums)  +1
         