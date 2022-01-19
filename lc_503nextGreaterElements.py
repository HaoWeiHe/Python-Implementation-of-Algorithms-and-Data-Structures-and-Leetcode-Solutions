"""
    [1,2,1]
          v
s   [1(2),2(1),]
ans [2, -1, 2]
"""

class Solution(object):
    def nextGreaterElements(self, A):
        s, n = [], len(A)
        ans = [-1] * n
        for i in range(n) * 2:
            while s and A[s[-1]] < A[i]:
                ans[s.pop()] = A[i]
            s.append(i)
        return ans

  