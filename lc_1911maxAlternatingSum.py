class Solution(object):
    def maxAlternatingSum(self, nums):
        odd,even = 0, 0 
        for e in nums:
            odd = max(-e + even, odd)
            even = max(e + odd, even)
        return even

    def maxAlternatingSum4(self, nums):
        """
             *
             /\
           +7  X
           /\
        -2   X
        [7,2,5,3]
         0 1 2 3
         even, or not 
        dp[(i, even)] = max(cur_val + dp[(i, -1*even)], dp[(i,even)])

        """
        dp = {}
        def dfs(i, even):
            if i == len(nums):
                return 0
            if (i,even) in dp:
                return dp[(i, even)]
            cur = nums[i] if even else -1 * nums[i]
            dp[(i, even)] = max(cur + dfs(i + 1, not even), dfs(i + 1, even))
            return dp[(i, even)]

        return dfs(0, True)

    def maxAlternatingSum3(self, nums):
        """
         can I always put 0 here: [+4,-2,+5,-3,-0]
                                            51
         0 3 5 2 4
          3 2   2
          
        [5,6,7,8,0]
        0 8 7 6 5
         8    
         
        """
        nums = nums+[0]
        res = 0 
        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx - 1]:
                res += (nums[idx-1] - nums[idx])
        return res

    def maxAlternatingSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peak, btm = [],[]
        tmp = []
        for idx, e in enumerate(nums):
  
            if nums[idx] == nums[idx-1] and idx > 0:
                continue
            tmp.append(e)
        nums = [0] + tmp[:] + [0]
        
        for idx, e in enumerate(nums):
            if idx == 0 or idx == len(nums) -1:
                continue
            if nums[idx-1] < nums[idx] and nums[idx] > nums[idx+1]:
                
                peak.append(nums[idx])
            if nums[idx-1] > nums[idx] and nums[idx] < nums[idx+1]:
                btm.append(nums[idx])
      
        if len(peak) - len(btm) ==2:
            peak.pop()
        return sum(peak) - sum(btm)
            