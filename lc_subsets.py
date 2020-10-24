class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        
        
        for num in nums:
            subSet = []
            for elem in res:
                subSet.append(elem + [num])
            res.extend(subSet)
        return res