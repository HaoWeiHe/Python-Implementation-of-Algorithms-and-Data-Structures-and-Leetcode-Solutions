class Solution(object):
    def minWindow(self, s1, s2):
        """
        "abcdebdde"
         0123456
        "bde" 
         
        abcdebdde , de. [1] #i = lst[-1], j = 1
        abcdebdde   , e  [1,3]
        abcdebdde, ""   [1,3,4] 
        if e == "", cmp to the global value, return the min one
        
        
        """
        if s1 == s2: 
            return s1

        self.ans = [0, len(s1)]
        def dfs(j,record):
            if record and  (record[-1] - record[0 ]) > (self.ans[-1] - self.ans[0]) :
                return 
            if j == len(s2):
                
                if (self.ans[-1] - self.ans[0]) > (record[-1] - record[0]) :
                    self.ans = [record[0],record[-1] ]
                if (self.ans[-1] - self.ans[0]) == (record[-1] - record[0]) and self.ans[0] > record[0]:
                    self.ans = [record[0], record[-1] ]                                                                                
                return 
            #abcdebdde
            i = -1 if not record else record[-1]
            for idx in range(i+1, len(s1)):
                if s1[idx] == s2[j]: #j = 1, record = [1]
                    dfs(j+1, record + [idx])
        dfs(0, [])
        return s1[self.ans[0]:self.ans[-1]+1] if [0, len(s1)]!= self.ans else ""
                