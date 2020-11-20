class Solution(object):
    def longestOnes(self, A, K):
        """
        sliding windows
        """
        left = 0
        res = 0
        for right in range(len(A)):
            K -= 1 - A[right] 
            if K < 0 :
                K += 1 - A[left]
                left += 1
            res = max(res, right - left + 1)

        return res
