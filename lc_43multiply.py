class Solution(object):
    def multiply(self, num1, num2):
        """
        1 10
        123
        456
rem =   518
         5
          10
         123
           4
          32
        """
        
        def layer(num1,num2):
            c = 0
            res = ""
            for e in num1[::-1]:
                e, num2 = int(e), int(num2)
               
                c,b = divmod( e * num2 + c, 10)
                res = str(b) + res
            
            return res if c == 0 else str(c) + res
        res = 0
        for i, v in enumerate(num2[::-1]):
            res += int(layer(num1,10**i*int(v)))
        return str(res)