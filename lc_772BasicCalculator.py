class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","")

        def helper(s):
            stack = []
            opt = ["+"]
            num = 0
            for idx, e in enumerate(s):
                
                if e.isdigit():# or e[0]=="-":
                    num = num *10 + int(e)
                if len(e) > 1 and e[0] =="-":
                    num = int(e[1:])
                    num = -1 * num
                    
                if not e.isdigit() or idx == len(s)-1:
                    cur_opt = opt.pop()
                    
                    if cur_opt == "+":
                        stack.append(num)
                    if cur_opt == "-":
                        stack.append(-num)
                    if cur_opt == "/":
                        pre_ele = stack.pop()
                        if pre_ele > 0:
                            stack.append(pre_ele / num)
                        else:
                            stack.append( -1 * (abs(pre_ele) / num))
                    if cur_opt == "*":
                        stack.append(stack.pop() * num)
                    opt.append(e)

                    num = 0
            
            return str(sum(stack))

        stack = [] 
        for ele in s:
            if ele == ")":
                tmp = []
                top = stack.pop()
                while top != "(":
                    tmp.append(top)
                    top = stack.pop()
                stack.append(helper(tmp[::-1]))
            else:
                stack.append(ele)
        
        return helper(stack)
