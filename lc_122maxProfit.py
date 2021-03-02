class Solution(object):
    def maxProfit(self, prices):
        """
          [7, 1, 5, 3, 6, 4]
          if cur is larger than previous, add
          
profit    0   0  4  4   7  7
        """
        if len(prices) < 2 :return 0
        pre = prices[0]
        res = 0
        for p in prices[1:]:
            if p > pre:
                res += (p-pre)
            pre = p
        return res
        