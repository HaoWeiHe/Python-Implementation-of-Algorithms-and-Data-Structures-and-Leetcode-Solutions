class Solution(object):
    def canConvert(self, str1, str2):
     
        """
       aabcc
       ccdee

       a -> c
       b -> d
       c -> e
       if conflict, fail?
        """
        d = {}
        for i, e in enumerate(str1):
            if e not in d:
                d[e] = str2[i]
            else:
                if d[e]!=str2[i]:
                    return False
       
        if str1!=str2 and len(d) == 26 and len(set(str2))==26:
           
            return False
        return True