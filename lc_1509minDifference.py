class Solution(object):
    def minDifference(self, nums):
        """
        [5,3,2,4]
            2 3 4 5  
        [1,5,0,10,14]
        only 
        len = 5 
        5-4 = 0
        0 1 2 3  4 
        0 1 5 10 14
        1 2 3 4 5 
        5 -3 +1 = num_j = 3
        num_i = i + 1
        total = n - j + 1 + i + 1 = n -j + i + 2
        """
        if len(nums) <=3 :
            return 0
        i, j = 0, len(nums)
        nums.sort()
        ans = float('inf')
        for i in range(4):
            j = len(nums) - 1
            while j >= i and j >= len(nums) -4  + i  :
                
                ans = min(ans, abs(nums[i] - nums[j]))
                j -= 1
        return ans