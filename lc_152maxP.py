class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn, mx, ans = 1,1,float('-inf')
        for e in nums:
            mn, mx = min(e, mn*e, mx*e), max(e,mn*e, mx*e)
            
            ans =max(ans, mx, mn)
        return ans