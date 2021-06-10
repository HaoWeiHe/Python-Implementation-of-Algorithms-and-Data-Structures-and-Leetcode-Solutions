class Solution(object):
    def subsets(self, nums):
        """
        []
        [], 1
        [],1,2, 12 
        [],1,2,12,3,13,23,123
        
        """
        res = [[]]
        for e in nums:
            subs = []
            for sub_e in res:
                subs.append( sub_e + [e])
            res.extend(subs)
        return res
            