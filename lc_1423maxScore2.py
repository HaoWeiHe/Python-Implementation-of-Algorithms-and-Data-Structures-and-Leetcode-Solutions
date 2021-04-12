class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        [1,2,3,4,5,6,1] 
        retain = 
        sum_all - min(sublist whose lenght == n - k ) where n = len(cardPoints)
        pre = (0~ (n-k))
        """
        if k >= len(cardPoints):
            return sum(cardPoints)
        n = len(cardPoints)
        sublst_number = n-k #[100,40,17,9,73,75] n = 6, k = 3
        
        cur = sum(cardPoints[:sublst_number])
        
        mn = cur

        for i in range(sublst_number, n):
             
            cur = cur -  cardPoints[i-sublst_number] + cardPoints[i]
            mn = min(mn,cur )
        return sum(cardPoints) - mn
    def maxScore2(self, cardPoints, k):
        """
        [1,2,3,4,5,6,1] 
        retain = 
        sum_all - min(sublist whose lenght == n - k ) where n = len(cardPoints)
        pre = (0~ (n-k))
        """
        if k <= len(cardPoints):
            return sum(cardPoints)
        n = len(cardPoints)
        tmp = cardPoints[:n-k]
        mn = tmp
        for i in range(n-k, n):
            mn = min(tmp, tmp - cardPoints[i-k] + cardPoints[i])
        return sum(cardPoints) - tmp


sol = Solution()
cardPoints, k = [100,40,17,9,73,75], 3
print(cardPoints)
print(sol.maxScore(cardPoints, k ))