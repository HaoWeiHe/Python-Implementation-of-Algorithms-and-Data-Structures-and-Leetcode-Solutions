from  bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        dp[i] = the longest increasing subsequ from 0 -> i 
        [10,9,2,5,3,7,101,18]
        
        [ 0,0,0,0,0,0, 0, 0]
        [ 10,0,0,0,0,0, 0, 0]  cur = 10, bisect_left = 0 res =0
        [ 9,0,0,0,0,0, 0, 0]  cur= 9   bisect_left = 0  res = 1
        [ 2,0,0,0,0,0, 0, 0]  cur = 2 bisect_left = 0  res = 1
        [ 2,5,0,0,0,0, 0, 0]
        [ 2,3,0,0,0,0, 0, 0]
        [ 2,3,7,0,0,0, 0, 0]
        [ 2,3,7,101,0,0, 0, 0]
        ...
        """
       
        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            insert_idx = bisect_left(dp, nums[i], hi= res)
            dp[insert_idx] = nums[i]
            if insert_idx == res:
                res += 1
        return res
        
    def lengthOfLIS2(self, nums):
        """
        dp[i] = the longest increasing subsequ from 0 -> i 
        [10,9,2,5,3,7,101,18]
                    i
        
         j j j j jj           
        [1 ,1,1,2,2,3, 4,4 ]
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * (n)
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
