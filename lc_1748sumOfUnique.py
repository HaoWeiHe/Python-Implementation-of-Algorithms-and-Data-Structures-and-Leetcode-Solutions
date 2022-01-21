class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums) #{1:3}
        ans = 0 
        for k,v in c.items():
            if v == 1:
                ans += k
        return ans
        