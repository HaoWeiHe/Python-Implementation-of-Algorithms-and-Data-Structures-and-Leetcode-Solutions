class Solution(object):
    def threeSumClosest(self, nums, target):
        """
         
         [-4, -1,1, 2]
              ^ 
             l      r
                            -3, gap = 4  <  target, r 
                l   r        -1, target = 2 < target  
                 l   
     
        """
        nums.sort()
        gap = [float('inf'),float('inf')]
        for idx, now in enumerate(nums):
            l,r = idx+1, len(nums)-1
            while l < r:
                total = nums[l] + nums[r] + now
               
                if gap[0] > abs(total - target):
                    gap = [abs(total - target), total]
               
                if total < target:
                    l += 1
                else:
                    r -= 1
        return gap[1]
        