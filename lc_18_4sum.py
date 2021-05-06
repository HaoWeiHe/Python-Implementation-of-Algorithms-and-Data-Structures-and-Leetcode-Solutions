class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        def twosum(nums, target):
            ans = []
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                if lo  !=0 and nums[lo] == nums[lo-1]:
                    lo += 1
                    continue
                if hi < len(nums) - 1 and nums[hi] == nums[hi+1]:
                    hi -= 1
                    continue
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -=1
                else:
                    ans.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

            return ans

        def ksum(nums, k,target):

            ans = []
            if not nums or target > nums[-1]*k or target < nums[0]*k:
                return []
            if k == 2:
                return twosum(nums, target)
            for i,val1 in enumerate(nums):
                if i == 0 or val1!= nums[i-1]:
                    for e in  ksum(nums[i+1:], k - 1, target - val1):
                        ans.append(e + [val1])

                    
            return ans
        return ksum(nums, 4,target)
[[-2,-1,1,2],[-1,-1,1,1]]
nums, target = [-2,-1,-1,1,1,2,2], 0
print(Solution().fourSum(nums, target))