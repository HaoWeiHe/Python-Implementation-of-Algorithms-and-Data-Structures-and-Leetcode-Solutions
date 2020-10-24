class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in nums:
            
            
            nums[abs(idx)-1] = -1 * abs(nums[abs(idx)-1] )
            
        res = []
        
        for idx in range(len(nums)):
            num = nums[idx]
            if num > 0 :
                res.append(idx+1)
        return res