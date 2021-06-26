class Solution(object):
    def canBeIncreasing(self, nums):
        """
       
        """
        counter = 0 
        def dfs(nums, count = 0):
            
            for i, e in enumerate(nums):
                if i == 0:
                    continue
                if nums[i-1] >= nums[i]:
                    if count == 1:
                        return False

                    return dfs(nums[:i] + nums[i+1:], 1) or  dfs(nums[:i-1] + nums[i:], 1)
            return True
        return dfs(nums)
                