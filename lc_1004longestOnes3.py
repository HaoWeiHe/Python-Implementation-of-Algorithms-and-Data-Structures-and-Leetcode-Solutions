class Solution(object):
    def longestOnes(self, nums, k):
        """
       [1,1,1,0,0,0,1,1,1,1,0]
                  r
                l
        """
        l,ans = 0, 0
        used = 0
        for r in range(len(nums)):
            
            if nums[r] == 0:
                used += 1
                
            if used > k:
                while used > k:
                    if nums[l] == 0:
                        used -= 1
                    l += 1
            ans  = max(ans, r - l + 1)
        return ans
       