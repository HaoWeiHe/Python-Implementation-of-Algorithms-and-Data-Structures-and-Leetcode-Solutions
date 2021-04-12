class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        [1,2,3,4,5,6,1] 
        rt, lf
        (0,k)
        (1,k-1)
        (2, k-2)
        .
        (k, 0)
          
        """
        res = 0
        for i in range(k+1):
            pre = sum(cardPoints[:i])
            post = sum(cardPoints[-(k-i):]) if i!=k else 0
            
            res = max(res,pre + post )
        return res