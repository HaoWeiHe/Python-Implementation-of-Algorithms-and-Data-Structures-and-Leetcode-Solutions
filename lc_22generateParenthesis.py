class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        ans = set()
        for ele in self.generateParenthesis(n-1):
            for idx, cur in enumerate(ele):
                if cur == "(":
                    ans.add(ele[:idx+1] + '()' + ele[idx+1:])
            ans.add(ele + "()")
                
        return ans
        