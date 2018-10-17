class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for idx in nums:
            
            if nums[abs(idx)-1] < 0:
                res.append(abs(idx))
            else:
                nums[abs(idx)-1] = -1 * nums[abs(idx)-1] 
            
                
        return res