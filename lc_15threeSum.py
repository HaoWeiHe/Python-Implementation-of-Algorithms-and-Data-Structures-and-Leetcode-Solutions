class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            i, j = idx +1 , len(nums)-1
            while i < j:
                cur = nums[idx] + nums[i] + nums[j] 
                if cur == 0:
                    res.append([nums[idx], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i +=1
                elif cur < 0:
                    i += 1
                else:
                    j -=1 
            
        return res