class Solution(object):
    def removeOccurrences(self, s, part):
        """
        daabcbaabcbc 
        01234
        4-3+1, 4+1
        2:5
        abc
        daabc 
        n = len(part)
        if k >= n: top[k-n:] == part? if yes pop() n times
        """
        n = len(part)
        sb = []
        for idx, e in enumerate(s):
            sb.append(e)
            if len(sb) >= n:
                if "".join(sb[-n:]) == part:
                    for _ in range(n):
                        sb.pop()
            
        return "".join(sb)
