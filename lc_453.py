class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        ans = 0 
        for e in nums:
            ans += e - mn
        return ans
