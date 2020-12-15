class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        (()
        [(]
        
        """
        
        stack = []
        for i,e in enumerate(s):
            if e in ["(",")"]:
                if stack and e == ")" and stack[-1][0]=="(":
                    stack.pop()
                else:
                    stack.append((e,i))
        res = []
        tmp = set([i for e,i in stack])
        for i in range(len(s)):
            if i not in tmp:
                res.append(s[i])
        return "".join(res)
                    