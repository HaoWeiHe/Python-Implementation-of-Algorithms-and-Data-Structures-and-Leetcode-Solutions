class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        [1,3,5,4,7]
             3 1 2
        
        """
        if len(nums) == 1:
            return 1
        pre = nums[0] 
        #[1,3,5,4,7]
        # 
        ans = float("-inf")
        tmp = 1
        for cur in nums[1:]:
            if pre < cur:
                tmp += 1
            else:
                tmp = 1
            ans = max(ans, tmp)
            pre = cur
        return ans
        