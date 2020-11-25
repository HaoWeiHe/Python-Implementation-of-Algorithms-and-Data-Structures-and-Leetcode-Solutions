class Solution(object):
    def pivotIndex(self, nums):
        """
        
        """
        if not nums:
            return -1
        #prefix sum
        acc = [nums[0]]
        for e in nums[1:]:
            acc.append(acc[-1] + e)
        lf = 0
        for idx in range(len(nums)):
            if idx >0: 
                lf = acc[idx-1]
            if (acc[-1] - acc[idx]) == lf:
                return idx
        
        return -1
        
lc_
