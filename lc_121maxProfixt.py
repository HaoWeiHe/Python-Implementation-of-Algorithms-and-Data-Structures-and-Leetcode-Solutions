class Solution(object):
    def maxProfit(self, p):
        """
        [7,1,5,3,6,4]
res =   0  0 4 4 5 5
min =   7  1 1 1 1 1 
        """
        if not p:return 0
        res, mn = 0, p[0]
        for ele in p[1:]:
            res = max(res, ele - mn)
            mn = min(mn,ele)
        return res
        