class Solution(object):
    """
    f(10) = f(5) * f(5) 
    base if f(1) return x
    f(9) = f(4) * f(4) * x


    """
    def myPow(self, x, n):
        def f(n):

          if n == 1:
            return x
          ans = 1
          half = f(n/2)
          if n % 2 == 1:
            ans = x * half * half
          else:
            ans = half * half
          return ans
        if n < 0:
          x = 1.0/ x
          n = abs(n)
        return f(n)

    """
    base x
    x*x 
    """
    def myPow2(self, x, n):
        """
        n = 10 > 1010
        
        1010 
           2  pow(2,1)   = 2    
          4   pow(2,2)  = 4
         16   pow(2,4) = 16
        256   pow(2,8) = 256

        pow(2,10)
        1010 
           2  pow(n,1)   = x    
          4   pow(n,2)  = x * x  note as X2
         16   pow(n,4) = X2 * X2 (as X3)
        256   pow(n,8) = X3 * X3
        
        pow(2,9) =  pow(2,8)  *pow(2,1) = 256*2 = 516
        """
        if n < 0 :
          x = 1.0/x
          n = abs(n)
        ans = 1
        while n:
            if n % 2:
                ans *= x
            x *= x 
            n /= 2
        return ans
