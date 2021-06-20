



class Solution(object):
    def numDecodings(self, s):
        """
         "12"
          -> 1 + f(2) if 1 in s
          -> 12 + f(""), if 12 in s,  return, counter + 1
        hashtable = {1:A, 2:B, 3:..}
        
        2326
      [2]326   [23]26
 2[3]26  2[32]6 23[2]6
        
        
        """
        h = {str(no - 64): chr(no) for no in range(65,91)}
        mem = {}
        #226
        #012
        def dfs(s):
            ans = 0 

            if s == "": 
                return 1
            
            if s in mem:
                return mem[s]
            
            if s[:2] in h and len(s)>1: 
                ans += dfs(s[2:])

            if s[:1] in h:
                ans += dfs(s[1:])
            
            mem[s] = ans
            return ans

        return dfs(s)

    def numDecodings2(self, s):
        """
         "12"
          -> 1 + f(2) if 1 in s
          -> 12 + f(""), if 12 in s,  return, counter + 1
        hashtable = {1:A, 2:B, 3:..}
        
        2326
      [2]326   [23]26
 2[3]26  2[32]6 23[2]6
        
        
        """
        h = {str(no - 64): chr(no) for no in range(65,91)}
        mem = {}
        
        def dfs(idx):
            ans = 0 

            if idx == len(s):
                return 1
            
            if idx > len(s):
                return 0
            if idx in mem:
                return mem[idx]
            
            if s[idx] == "0":
                return 0
            
            if s[idx: idx + 2] in h:
                ans += dfs(idx+2)
                
            ans += dfs(idx+1)
            mem[idx] = ans
            return ans
        return dfs(0)
