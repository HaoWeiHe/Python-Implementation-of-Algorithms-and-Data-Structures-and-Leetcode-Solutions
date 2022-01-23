class Solution(object):
    def minSteps(self, s, t):
        """
        c = {b:2, a:1}
        """
        c = Counter(list(s)) 
        
        for e in t: #aba
            if e not in c:
                continue
            c[e] = max(0, c[e] - 1) #{b:1, a:0}
        return sum(c.values())