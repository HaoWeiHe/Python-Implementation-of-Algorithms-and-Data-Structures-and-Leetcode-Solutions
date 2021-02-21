class Solution(object):
    def maxSubArray(self, nums):
        """
        [-2,1,-3,4,-1,2,1,-5,4]
    now  -2 1 -2 4  3 5 6
    res  -2 1  1 4  4 5 6
        """
        if not nums:return 0
        res, now = nums[-1],0
        
        for e in nums:
            now = e + now
            res = max(now,res)
            now = max(0,now)
        return res