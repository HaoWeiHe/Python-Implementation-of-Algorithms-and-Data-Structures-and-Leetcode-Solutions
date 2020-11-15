class Solution(object):
    def rob(self, nums):
        """
        dp[i] = maxProfix from 0->i
        dp[i] = max(dp[i] + cur , dp[i-1])
        """
        n = len(nums)
        pre, cur = 0,0
        for c in nums:
            tmp =  cur
            cur = max(pre +c, cur )
            pre = tmp
        return cur
          
    def rob2(self,nums):
        n = len(nums)
        if not n:
            return 0
        if n <2:
            return max(nums)
  
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,n ):
            cur = nums[i]
            dp[i] = max(dp[i-2] + cur , dp[i-1])
        return dp[-1]
        