class Solution(object):
    def minAddToMakeValid(self, s):
        """
            "())"
             10 
             if c == 0 and ) ans +1
            "(((" c == 3:
            in the end ans += c
            "()))(("
              00012
        ans  0012 -> 
            
        """
        c, ans = 0,0
        for e in s:
            if e == "(":
                c += 1
                
            if e == ")" :
                if c == 0:
                    ans += 1
                c = max(0, c-1)

            
        return ans + c
        