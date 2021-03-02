class Solution(object):
    def maxProfit(self, prices):
        """
                [1,2,3,0,2]
buy    -inf max() 
sell   -inf
cool    0

1) buy : max(cool_pre - cur, buy) / sell: max(buy_pre + cur) / cool: max(cool_pre, sell_pre)

        """
        buy, sell, cool = float('-inf'), float('-inf'), 0
        for p in prices:
            sell_pre = sell
            sell = buy + p
            buy = max(cool - p, buy)
            cool = max(cool,sell_pre )
        return max(sell,buy, cool)