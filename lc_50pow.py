class Solution(object):
    def myPow(self, x, n):
        """
     3-> 1*1*1 
      if n%2 ==0:
          res = f(n/2)*f(n/2)
      else:
        return f(n/2)*f(n/2)* x
        """
        abs_n = abs(n)
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
        res = helper(abs_n)
        return res if n > 0 else 1/res
        