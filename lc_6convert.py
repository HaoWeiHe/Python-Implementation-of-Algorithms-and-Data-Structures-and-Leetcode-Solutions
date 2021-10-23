class Solution(object):
    def convert(self, s, numRows):
        """
        n = 13
        i = 0 (0,6,12)
        i = 1 (1,7,13) -> (1,5,7,11,13)
        i = 2
        i = 3
        
        """
        ans = set()
        res = ""
        n = len(s)
        gap = 2*(numRows-1)
        if numRows == 1:
            return s
        for i in range(numRows):
            idx = i
            while idx < n:
                
                ans.add(idx)
                res += s[idx]
                if i > 0 and idx + 2 *(numRows - i - 1) < n:
                    
                    if (idx + 2*(numRows-i-1)) not in ans:
                        ans.add(idx + 2*(numRows-i-1))
                        res += s[idx + 2*(numRows-i-1)]
                
                idx += gap
         
        return res
        