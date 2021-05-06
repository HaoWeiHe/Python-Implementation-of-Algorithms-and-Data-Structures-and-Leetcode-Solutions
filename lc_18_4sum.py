class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        def thresssum(nums, ori):
            new_target = target - ori
            ans = set()
            for i, val1 in enumerate(nums):
                if i == 0 or nums[i-1]!= nums[i]:
                    lo, hi = i+1, len(nums)-1 
                    while lo < hi:
                        cur_sum = ori + nums[i] + nums[lo] + nums[hi]
                        if cur_sum > target:
                            hi -=1
                        elif cur_sum < target:
                            lo +=1
                        else:
                            ans.add(tuple([ori,nums[i], nums[lo], nums[hi]]) )
                            lo +=1
                            hi -=1
            return ans
        
        for i,val1 in enumerate(nums):
            if i == 0 or val1!= nums[i-1]:
                res = thresssum(nums[i+1:], val1)
                if res:
                    
                    ans += res
        return ans
        
                