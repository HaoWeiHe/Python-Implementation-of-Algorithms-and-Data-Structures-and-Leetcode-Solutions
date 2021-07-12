class Solution(object):
    def removeDuplicates(self, nums):
        """
        [0,0,1,1,1,2,2,3,3,4]
                   i
        [0,1,]
        """
        j = 0 
        for i,v in enumerate(nums):
            if i == 0 or nums[i]!= nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j