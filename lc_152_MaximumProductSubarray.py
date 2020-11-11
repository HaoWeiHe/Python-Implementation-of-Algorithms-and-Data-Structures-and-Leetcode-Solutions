
class Solution(object):
    def maxProduct(self, nums):
        """
     [2,3,-2,  4,  -1]
max   2 6  6   24  48
min   2 6 -12 -48  -24

keep tracking the cur_max and cur_min, keep comparing cur, cur* cur_max and cur*cur_min
         
        """
        if not nums:
            return 0

        cur_max, cur_min = nums[0], nums[0]
        res = cur_max
        for cur in nums[1:]:
            tmp_max = max(cur, cur_max* cur, cur_min*cur)
            cur_min = min(cur, cur_max* cur, cur_min*cur)
            cur_max = tmp_max
            res = max(res, cur_max)
        return res