class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = ""
        for idx,e in enumerate(s):
            if e ==" " and (sign in ["+","-"]):
                break
                
            if not stack and e ==" ":
                continue
            
            if stack  and e ==" ":
                break
            if  sign and e in ["-","+"] and s[idx-1] in  ["-","+"] :
                return 0
            if not stack and e in ["-","+"] :
                sign = e
                continue
            if  stack and not e.isdigit():
                break
            if  e.isdigit() :
                stack.append(e)
            if not stack and not e.isdigit():
                return 0
        if not stack: 
            return 0

        if sign and not stack:
            return 0
        res = int("".join(stack))
        return min(2**31-1, res ) if not sign or sign =="+" else max(-2**31,res*-1)