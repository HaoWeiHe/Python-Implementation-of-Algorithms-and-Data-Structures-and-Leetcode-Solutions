class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        profit, _min, _max = 0, prices[0], prices[0]
        pre_price = prices[0]

        
        # [7,1,5,3,6,4][6,1,3,2,4,7]
        for price in prices:
            if pre_price > price:
                profit = profit + (_max - _min)
                _min = price
                _max = price

            if _min > price:
                _min = price

            if _max < price:
                _max = price
                
            pre_price = price
        
        profit = profit + (_max - _min)
        
        return profit
