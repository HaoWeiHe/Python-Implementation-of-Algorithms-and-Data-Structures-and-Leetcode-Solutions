class Solution:
    def singleNumber(self, nums):
      
        res = nums[0]

        for elem in nums[1:]:
            res = res ^ elem
        return res