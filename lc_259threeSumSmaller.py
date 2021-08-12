class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        
        res = 0 
        for idx, cur in enumerate(nums):
       
            if idx ==  max(0,len(nums) -2):
                break
            
            l,r = idx+1, len(nums) - 1
            while l < r:
                s = cur + nums[l] + nums[r]
                if s < target:
                    res += (r-l)
                    l += 1
                else:
                    r -= 1
                     
                
           
        return res