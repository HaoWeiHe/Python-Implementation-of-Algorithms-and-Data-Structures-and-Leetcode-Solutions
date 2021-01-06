
class Solution(object):
    def myPow(self, x, n):
        #if n = 10 -> (1,0,1,0) -> 2^3 * 2^2
        if n < 0:
            x = 1/x
            n = -1*n
        ans = 1
        while n:
            if n%2:
                ans *= x
            x = x*x
            n /=2
        return ans

    def myPow1(self, x, n):
        """
        10 ->5 -> 2*2*1
        top down approach
          if n%2 ==0:
              res = f(n/2)*f(n/2)
          else:
            return f(n/2)*f(n/2)* x
        """
        if n < 0:
            x = 1/x
            n = -1*n

        def helper(n): 
            if n ==0:
                return 1
            if n == 1:
                return x
            helf = helper(n/2)
            if n%2 == 0:
                return helf * helf
            else:
                return helf * helf * x
        res = helper(n)
        return res 
        