class Solution(object):
    def calculate(self, s):
        """
        "13+2*2"
               ^
              default = +, num = 13
        [13]  push 13, sign +, num = 0
              num = 3
        [13,2] push 2, sing = *, num = 0
        [13,4] if * pop top and times cur
        
        
        """
        sign = "+"
        stack = []
        num = 0 
        " 3/2 "
        #  ^
        s = s.replace(" ","")
        for idx, e in enumerate(s):
            if e == " ":
                continue
            if e.isdigit():
                num = num*10 + int(e)
            if not e.isdigit() or idx == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign =="-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    stack.append(int(stack.pop()  / float(num)))
                sign = e
                num = 0
        
        return sum(stack)