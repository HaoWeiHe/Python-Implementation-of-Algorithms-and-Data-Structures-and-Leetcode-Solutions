class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak, btm = [],[]
        tmp = []
        for idx, e in enumerate(nums):
  
            if nums[idx] == nums[idx-1] and idx > 0:
                continue
            tmp.append(e)
        nums = [0] + tmp[:] + [0]
        
        for idx, e in enumerate(nums):
            if idx == 0 or idx == len(nums) -1:
                continue
            if nums[idx-1] < nums[idx] and nums[idx] > nums[idx+1]:
                
                peak.append(nums[idx])
            if nums[idx-1] > nums[idx] and nums[idx] < nums[idx+1]:
                btm.append(nums[idx])
      
        if len(peak) - len(btm) ==2:
            peak.pop()
        return sum(peak) - sum(btm)
            