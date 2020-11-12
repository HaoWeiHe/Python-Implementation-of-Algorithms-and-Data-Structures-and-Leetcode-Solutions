class Solution(object):
    def firstMissingPositive(self, nums):
        """
        nums = [3,4,-1,1]
        form 1 to 

        """

        n = len(nums)
        nums = set(nums)
        for e in xrange(1, 2 + n):
            if e > 0 and e not in nums:
                return e