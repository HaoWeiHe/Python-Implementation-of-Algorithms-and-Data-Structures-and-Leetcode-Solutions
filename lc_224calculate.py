from collections import deque
class Solution(object):
    def calculate(self, s):
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
