class Solution(object):
    def shortestToChar(self, s, c):
        """
      [ 3, 5, 6]
        i
        if chose i+1, go next
        
        """
        ids = []
        for i,e in enumerate(s):
            if e == c:
                ids.append(i)
        
        ids.append(float('inf'))
        
        i = 0
        ans = []
        for j in range(len(s)):
            pre, nxt  = abs(ids[i]-j), abs(ids[i+1] - j)
            if pre > nxt:
                i += 1
            
            ans.append(min(pre,nxt ))
        return ans