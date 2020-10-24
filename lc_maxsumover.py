
class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        n = len(A)
        
        def helper(s1, left, right):
            
            res = 0
            if len(left) >= M:
                for i in range(len(left) - M+1):
                    res = max(res, sum(left[i:i+M]))
            
            return s1+res
        res = 0
        for i in range(n - L+1): #10-5+1
            cur = sum(A[i:i+L])
            
            res = max(res, helper(cur,A[:i],A[i+L:]))
        print(res)
        return res

A,L,M = [4,5,14,16,16,20,7,13,8,15] ,3,5
Solution().maxSumTwoNoOverlap(A,L,M)