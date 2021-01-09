class Solution(object):
    def addOperators(self, num, target):
        """
        1+2 + 3 : if +, acc= res+3, prev: 3
          V
        1+2 - 3 : if +, acc= res-3, prev: -3
        1+2 * 3 : if *, acc = res - prev + prev* 3
             
        dfs(pfx, ops, acc, prev):
        pfx + "+" + "num[ops: ops+]" :
        
        function decription:
        pref is the representation, eg. 1+2
        cur is the result of representation, eg.  cur = 3 when "1+2"
        pos: num[:pos] #when pos == len(num), means we have done
        """
        self.res =[]
        def dfs(pref, pos, cur, prev): 
            
            if pos == len(num):
                if cur == target:
                    self.res.append(pref)
                return 
            
            for i in range(pos + 1, len(num)+1): 
                n = num[pos: i]
                if n[0] == "0" and len(n) > 1:
                    break 
                n = int(n)
                if pos == 0 :
                    dfs(str(n),i,n,n)
                    continue
                
                dfs(pref + "+" + str(n),  i, cur + n, n)
                dfs(pref + "-"+ str(n), i , cur - n , -n )
                dfs(pref + "*" + str(n), i , cur - prev + prev * n, prev*n)
        dfs("",0,0,0)
        return self.res
