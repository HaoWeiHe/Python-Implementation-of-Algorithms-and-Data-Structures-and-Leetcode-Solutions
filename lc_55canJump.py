class Solution(object):
    def canJump(self, nums):
        """
        [2,3,1,1,4] 
         ^
           X X
             X X X
        """
        self.mem ={}
        def dfs(i):
            if i in self.mem:
                return self.mem[i]
            v = nums[i]
            if i == len(nums) -1:
                return True
            ans = False
            for jump in range(1,v+1):
                ans = ans or dfs(i+jump)
            self.mem[i] = ans
            return self.mem[i]
                
        
        return dfs(0)
        