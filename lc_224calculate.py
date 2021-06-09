class Solution(object):
    def calculate(self, s):
        """
        if inner: sign delay happen (sign * op)
        else: sign always can be assign (sign = op)
        (13-(4+5-2)) + 6 -2
                      ^
                     
        res = 0 
        num = 0 
        (
        count = 1
        sign = 1
        num = 13
        res +=  sign * 13 =13 (inner, count!=0)
        
        4 - (2-6+8-(3+4))
        first counter = -1
        [-1, +1] 
        """
        res, num, sign = 0, 0 , 1
        counter = 0 
        singlevel = [1]
        for idx, e in enumerate(s):
            if e ==" ":
                continue
                
            if e.isdigit():
                num = num*10 + int(e)

            if not e.isdigit() or idx == len(s)-1:
                res += sign * num                
                if e == "(":
                    singlevel.append(sign)
                if e == ")":
                    singlevel.pop()

                if e == "+":
                    sign = singlevel[-1]
                if e == "-":
                    sign = singlevel[-1] * -1
                num = 0
        if num:
            res += sign * num
        return res
    def calculate3(self, s):
        """
        s = "((1-(6+-18) -+ 3) - 14)"
              v  
        ) 14 - ) 3 + ) 18 +- 6 >> pop until )
        ) 14 - ) 3 + ) 18 +- 6 , a = pop(), peak top and pop, b = pop, after compute, put back to stack
        ) 14 - ) 3 +  12 - 1 (
        ) 14 - ) 3 + 11 (
        ) 14 - 14 (
        
        (7-8+9) ->  )9+8-7(
        [)9+8-7]
         
        7 - 8
        res = pop

        """
        num = ""
        stack = []
        def eva_expr(stack):
            if stack[-1] == "+":
                stack.pop()
            neg = 1
            if stack[-1] == "-":
                stack.pop()
                neg = -1
            res = neg*int(stack.pop()) if stack else 0 
            op = ""
            while stack and stack[-1] != ")" :
                top = stack.pop()
                if not top.lstrip("-").isdigit():
                    op = op + top
                else:
                    if op in ["++", "--","+"]:
                        res += int(top)
                    if op in ["+-", "-+","-"]:
                        res -= int(top)
                    op = ""
            
            return str(res)

        for idx in range(len(s)-1,-1,-1):
            e = s[idx]
            if e == " ":
                continue
            if e.isdigit():
                num = e + num
                continue
            if num :
                stack.append(num)
                num = ""
            if e == "(":
                tmp_res = eva_expr(stack)
                stack.pop()
                stack.append(tmp_res)
            else:
                stack.append(e)

        if num:
            stack.append(num)
        
        return eva_expr(stack)

            
    def calculate2(self, s):
        """
        removed if i ==0 and s[i] =  "+" 
         " 7*0-8 + (1+(4+5+2)-3)+3+5-(6+8)-5"
                   ^                ^   
          start_idx =[0,8,13,20,24,end]
          0:8, 8:13, 13:20, 20:24
          
         if no "(":
            return compute(s)
         A =  dfs(1+(4+5+2)-3)  
         B =  dfs(6+8)
         return dfs(-8 + A + B -5)
         
         1) preprocess num and "()", compute num and dfs()
         2) helper funcion for compute number without 
        
        "12-1 + 2 "
           ^
[]       [][12] [12,-1] [2,-1] [2,-1,2]
[+]      [+][-]  []    [+]    []

         "48 * -48"
[]       [][] [48] [48, -48]
[+]      [    [* -  [*]
         +]     ]
          
        """
        s = s.replace(" ","")
        
        def compute(s):
            s = s.replace("+-","-")
            s = s.replace("--","+")
            s = s.replace("-+","-")
            num = 0 
            ops, ns = deque(["+"]),[0]
            for i,e in enumerate(s):
                if e.isdigit():
                    num = num*10 + int(e)
                if not e.isdigit() or i == len(s) - 1:

                    op = ops.popleft()
                    
                    if op == "+":
                        ns.append(num)
                    if op == "-":
                        ns.append(-num)
                    if op == "*":
                        ns.append(ns.pop() * num)
                    if op == "/":
                        ns.append(ns.pop()/num)
                    ops.append(e)
                    num = 0 
            return sum(ns)
       
        def dfs(s):
            if "(" not in s:
                return compute(s)

            p_counter = 0 
            stack = []
            new_s = ""
            for idx, e in enumerate(s):
                if e not in ["(", ")"] :
                    stack.append(e)
                    if idx != len(s)-1:
                        continue

                if p_counter == 0 and e == "(" :
                    new_s = new_s + "".join(stack)
                    stack = [] 
                if p_counter !=0  and e in ["(", ")"]:
                    stack.append(e)
                if e == ")":
                    p_counter -=1

                if e == "(":
                    p_counter += 1

                if p_counter == 0 and e == ")":
                    sub_ans = dfs("".join(stack))
                    new_s  = new_s + str(sub_ans)
                    stack = []

                    
                elif idx == len(s)-1:
                    new_s = new_s + "".join(stack)
                    stack = []

            return compute(new_s)
          
        return dfs(s)
