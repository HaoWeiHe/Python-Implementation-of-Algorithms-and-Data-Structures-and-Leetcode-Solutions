class Solution(object):
    def isValid(self, s):
        """
        if close sign appear:
            not stack and top of stack should be paird 
        """
        stack = []
        pairs = {"}":"{",")":"(","]":"["}
        for e in s:
            if e in ["}",")","]"]:
                
                if not stack or pairs[e]!=stack.pop():
                    return False
            else:
                stack.append(e)
        
        return not stack