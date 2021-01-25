import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        "ADOBECODEBANC"
         ^    ^ 
         ABC: good
         res, num = ADOBEC, 6
         if not satisfy: lf, else: cmp_leg and  rt ++
        """
        need = collections.Counter(t)
        def satisfy(increased, idx):
            """
            ADAOBEC : A:2, B:1, C:1, O:1
            AABC : A:2, B:1, C:1
            """
            char = s[idx]
            if increased:
                self.freq[char] += 1
                if char in need and self.freq[char] == need[char]:
                    self.n +=1
                #if ori is not satisfy,but now satisfy, self.n +=1 

            else:
                #if ori is satisfy, but now are not, self.n -=1
                if self.freq[char] == need[char]:
                    self.n -=1
                self.freq[char] -=1
            return  self.n == len(need)
        rt, lf = 0,0
        res, num = "", float('inf')
        s = s + " "
        self.n, self.freq = 0 ,collections.defaultdict(int)
            
        for rt in range(len(s)-1):
            is_satisfy = satisfy(True, rt) 
            while is_satisfy and lf < rt+1: 
                if (rt-lf) < num:
                    num = rt-lf
                    res = s[lf:rt+1]
                    
                is_satisfy = satisfy(False,lf)
                lf += 1
        return res
            
