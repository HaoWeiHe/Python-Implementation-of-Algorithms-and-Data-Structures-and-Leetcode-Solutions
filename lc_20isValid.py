class Solution(object):
    def isValid(self, s):
        """
         "("
         s = [(]
         if ):
            cmp if top of s is the pair of ) 
        use hash! 
        """
        stk = []
        pairs = {")":"(", "}":"{", "]":"["}
        for e in s:
            if e in ["(", "{","["]:
                stk.append(e)
            else:
                if not stk or pairs[e] != stk.pop():
                    return False
            
        return True if not stk else False
                