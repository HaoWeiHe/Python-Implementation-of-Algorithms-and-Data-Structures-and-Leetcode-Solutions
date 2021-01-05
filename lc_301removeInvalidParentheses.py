class Solution(object):
    def removeInvalidParentheses(self, s):
        """
         "()())()"
          (: c +=1
          ): c-= 1
          else: just pass and n +1
          if c < 0: cut the branch
         
        """
        acc, bal = 0,0
        for e in s:
            if e not in ["(",")"]:
                continue
            if e ==")":
                bal -=1
            if e == "(":
                bal +=1
            if bal < 0 :
                acc +=1
            bal = max(0,bal)

        delnum = acc + bal
        self.res = []
        self.v = set()
        def dfs(record, balance_value, i,d_c):
            
            if d_c > delnum or balance_value < 0 :return 
            if i == len(s):
                if balance_value == 0:
                    self.res.append(record)
                return 
            cur = s[i]
            if cur not in [")","("]:
                dfs(record + cur, balance_value, i + 1, d_c)
            else:
                dfs(record , balance_value, i+1, d_c+1 ) #delete
                if cur == ")": balance_value -= 1
                if cur == "(": balance_value += 1 
                dfs(record + cur, balance_value, i+1, d_c )
                    
               
        dfs("",0,0,0)
       
        return list(set(self.res)) if  self.res else [""]
