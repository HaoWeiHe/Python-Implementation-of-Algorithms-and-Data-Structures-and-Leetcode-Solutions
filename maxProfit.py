class Solution:
    def maxProfit(self, prices):
        res = 0 

        if not prices:
            return 0

        _min = prices[0]

        for elem in prices:
            _min = min(elem, _min)
            res = max(res, elem -_min)
        
        return res
