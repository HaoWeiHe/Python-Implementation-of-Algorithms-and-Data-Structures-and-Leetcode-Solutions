class Solution(object):
    def lengthOfLIS(self, nums):
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