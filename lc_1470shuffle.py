class Solution(object):
    def shuffle(self, nums, n):
        """
        nums = [2,5,1,3,4,7], n = 3
        [2,5,1]
        [3,4,7]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        
       
        