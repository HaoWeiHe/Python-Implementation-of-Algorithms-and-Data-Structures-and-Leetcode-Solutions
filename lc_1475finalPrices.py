class Solution(object):
    def finalPrices(self, prices):
        """
        [8,4,6,2,3]
               
    
        """
        n = len(prices)
        ans = []
        for i in range(n):
            flag = True
            for j in range(i+1,n):#[8,4,6,2,3]
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    flag = False
                    break
            if flag:
                ans.append(prices[i])
        return ans