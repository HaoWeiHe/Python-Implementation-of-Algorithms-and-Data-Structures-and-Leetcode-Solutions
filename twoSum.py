class Solution(object):
    def twoSum(self, nums, target):
        d = dict()

        for idx in range(0,len(nums)):
            complemantary = target - nums[idx]
            if nums[idx] in d:
                return [d[nums[idx]], idx]
            else:
                d[complemantary] = idx

        return None
            
            

