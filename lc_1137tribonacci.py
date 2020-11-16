class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = {}
        def T(n):
            if n ==0: return 0
            if n < 3: return 1
            if n in self.memo : 
                return self.memo[n]
            self.memo[n] = T(n-1) + T(n-2) + T(n-3)
            return self.memo[n]
        return T(n)