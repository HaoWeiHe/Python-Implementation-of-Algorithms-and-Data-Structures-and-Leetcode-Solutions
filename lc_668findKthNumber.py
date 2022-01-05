class Solution(object):
    def findKthNumber(self, m, n, k):
        def feasible(num):
            hold = 0 
            for i in range(1, m + 1):
                cur = min(num /i, n )
                if cur == 0:
                    break
                hold += cur
            return hold >= k
        l, r = 1, m*n
        while l < r:
            mid = l + (r-l)/2
            if feasible(mid):
                r = mid 
            else:
                l = mid + 1
        return l
