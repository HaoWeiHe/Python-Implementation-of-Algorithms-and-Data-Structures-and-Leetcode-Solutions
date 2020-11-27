
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()

        for i in xrange(n-2):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, n-1
            while l < r:
                b,c = nums[l], nums[r]
                if a + b+ c  == 0:
                    res.append([a,b,c])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l += 1
                    r -= 1
                elif a +b +c < 0:
                    l += 1
                else:
                    r -= 1

        return res
