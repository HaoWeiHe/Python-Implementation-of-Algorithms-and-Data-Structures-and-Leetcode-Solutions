
class Solution(object):
    def reorganizeString(self, S):
        """
        1. sort like aaabb (highest freq from left)
        2. if the number of top freq < len(S)/2 return ""
        3. s[0::2],s[1::2] = s[n/2:],s[:n/2]
        """
        n  = len(S)
        c = collections.Counter(S) 
       
        sortedS = [val* freq for (val, freq) in sorted(c.items(), key = lambda x: x[1])]
        
        s = "".join(sortedS)
        if c.most_common(1)[0][1] > math.ceil(len(S)/2.0):
            return ""
        
        ans = [None] * n
        ans[::2], ans[1::2] = s[n/2:],s[:n/2]
       
        return "".join(ans)