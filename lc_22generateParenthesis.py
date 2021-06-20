class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        """

        """
        def dfs(left, right, arr):
            if left < 0 or right < 0 or right < left:
                return 
            if left == 0 and right == 0:
                ans.append(arr)
            dfs(left - 1, right, arr +"(")
            dfs(left, right - 1, arr + ")")

        dfs(n,n, "")
        return ans

    def generateParenthesis2(self, n):
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

n = 3
print(Solution().generateParenthesis(n))