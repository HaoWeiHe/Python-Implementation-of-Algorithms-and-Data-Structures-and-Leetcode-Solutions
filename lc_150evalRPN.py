class Solution(object):
    def evalRPN(self, tokens):
        """
         ["2","1","+","3","*"]
         2,1, + 
         3,3*
         
          ["4","13","5","/","+"]
          if op, pop 2 ele, compute
          append back
          [4, 13,5 ]
         / 
         [4,2], + 
         [6]
        """
        s = []
        for tkn in tokens:
            if tkn in ["+", "-","/","*"]: 
                b, a = s.pop(), s.pop() #a op b
                if tkn == "+":
                    s.append(a + b)
                if tkn == "-":
                    s.append(a - b)
                if tkn == "*":
                    s.append(a * b)
                if tkn == "/":
                    s.append(int(float(a)/b))
               
            else:
                s.append(int(tkn))
        
        return s[0]