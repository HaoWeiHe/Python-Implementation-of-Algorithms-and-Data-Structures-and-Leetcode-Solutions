class Solution(object):
    def moveZeroes(self, nums):

        nzv = 0

        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[nzv] = nums[i]
                nzv = nzv+1
                
            
        while(nzv < len(nums)):
            nums[nzv] = 0
            nzv = nzv+1
                
        