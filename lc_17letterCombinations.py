class Solution(object):
    def letterCombinations(self, d):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not d:return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        self.ans = []
        def dfs(i,his):
            if i == len(d):
                self.ans.append(his)
                return 
            
            cur = d[i]
            for c in phone[cur]:
                dfs(i+1, his + c )
        dfs(0,"")
        return self.ans