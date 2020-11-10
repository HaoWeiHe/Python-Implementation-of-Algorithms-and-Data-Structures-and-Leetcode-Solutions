class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <=1 :
            return N
        
        cur, fir, sec = 0,0,1
        for n in range(2,N+1):
            cur = fir + sec
            fir = sec
            sec = cur
        return cur
            
    def fib2(self, N):
        def fibmem(n):
        
            if n in memo:
                return memo[n]
          
            fibmem(1)
            memo[n] = fibmem(n-1) + fibmem(n-2)
            return memo[n]
        if N <=1:
            return N
         
        memo = {0:0, 1:1}
        return fibmem(N)
    
    def fib2(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(n):
            if n ==0 or n ==1: 
                return n
            return dfs(n-1) + dfs(n-2)
        return dfs(N)