class Solution(object):
    def calculate(self, s):
        def check_boundary(s):
            n = 0
            for e in s[:-1]:
                
                if e == "(": n+= 1
                if e ==")": n -= 1
                if n ==0: return 1
            return 0
        if check_boundary(s): s = "("+s+")"
        # print(s, check_boundary(s))
        s = s.replace(" ","")
        stack = []
        def helper(s):
            # print(s)
            s = s[1:-1]
            
            res, num = [], 0
            ops = ["+"]
            for idx, e in enumerate(s):
                # print(e)
                if e.isdigit():
                    num = num*10 + int(e)
                if (not e.isdigit()) or idx == len(s)-1:
                    op = ops.pop()
                    
                    if op == "+": res.append(num)
                    if op =="-": res.append(-num)
                    ops.append(e)
                    num = 0
            
            return sum(res)
        for e in s:
            stack.append(e)
            # print(stack)
            if e == ")":
                tmp = []
                top = stack.pop()
                while(top !="(" and stack):
                    tmp.append(top)
                    top = stack.pop()
                
                tmp.append(top)
               
                tmp = tmp[::-1]
                cur = helper(tmp)
               
                if cur < 0 and stack:
                    prev_op = stack.pop()
                    if prev_op == "+": 
                        stack.append("-")
                        
                    if prev_op == "-": 
                        stack.append("+")
                    stack.append(str(abs(cur)))
                else: 
                    stack.append(str(cur))
            
        return stack[0]

s = "(1+(4+5+2)-3)+(6+8)"
# s = "1+1"
# s = "2-(5-6)"
s ="1-11"
# s = "(5-6)"
# s = "(1+(4+5+2)-3)+(6+8)"
print(Solution().calculate(s))