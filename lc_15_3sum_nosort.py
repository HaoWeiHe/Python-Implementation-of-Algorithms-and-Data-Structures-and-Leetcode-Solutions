class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dup,ans = set(), set()
        seen  = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dup:
                dup.add(nums[i])
                for j in range(i+1,n):
                    c = -1*(nums[i] + nums[j])
                    if c in seen and seen[c]==i:
                        ans.add(tuple(sorted((nums[i],nums[j], c))))
                    seen[nums[j]] = i
        return ans