class Solution(object):
    def calculate(self, s):
        """
        "13 + 2*20"
        stack = [13, 2]
        """
        s =  s.replace(" ","")
        op = ["+"]
        stack = []
        num = 0 
        for idx, c in enumerate(s):
            if c.isdigit() :
                num = num * 10 + int(c)
            if  idx == len(s)-1 or not c.isdigit():
                cur_op = op.pop()
                if cur_op == "+":
                    stack.append(num)
                if cur_op == "-":
                    stack.append(-num)
                if cur_op == "/":
                    stack.append(int(float(stack.pop()) / num))
                   
                if cur_op == "*":
                    stack.append(num * stack.pop())
                op.append(c)
                num = 0
          
         
        return sum(stack)