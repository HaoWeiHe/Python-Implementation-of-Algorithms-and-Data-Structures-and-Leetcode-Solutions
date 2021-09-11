class Solution(object):
    def missingNumber(self, nums):
        """
        [0,1,3]
           ^
        """
        nums.sort()
        start = 0 
        for ele in nums:
            if ele != start:return start
            start += 1
        return len(nums)
            