class Solution(object):
    def numSubseq(self, A, target):
        """
        1. sort 
        2. two pointer
        3. if T[i~j] is satisfy, and we use i as our min value, then we have 2^(j-i) counts
        """
        A.sort()
        res = 0
        l,r = 0, len(A) - 1
        mod = 10**9 + 7
        while l <= r:
            if A[l] + A[r] > target:
                r -= 1
            else:
                res  += 2**(r-l) % mod
                l += 1
        return res % mod
