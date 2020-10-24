
# class Solution:
#     def stoneGameII(self, A: List[int]) -> int:
#         N = len(A)
#         for i in range(N - 2, -1, -1):
#             A[i] += A[i + 1]
#         print(A)
#         print([sum(A[i:]) for i in range(N)])
#         from functools import lru_cache
#         @lru_cache(None)
#         def dp(i, m):
#             if i + 2 * m >= N: return A[i]
#             return max([A[i] - dp(i + x, max(m, x)) for x in range(1, 2 * m + 1)])
#         return dp(0, 1)


class Solution(object):
    def stoneGameII(self, A):
        N = len(A)
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
                
        def dp(i, m):
            if i >= len(A): return 0
            if i + 2*m >= N: return A[i]#sum(A[i:])

            return max( [ A[i] - dp(i+x, max(m,x)) for x in range(1, 2*m+1 )])
        return dp(0,1)

A = [2,7,9,4,4]
print(Solution().stoneGameII(A))