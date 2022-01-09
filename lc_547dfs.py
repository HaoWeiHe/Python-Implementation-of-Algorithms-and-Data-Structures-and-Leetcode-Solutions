class Solution(object):
    def findCircleNum(self, M):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        self.v = set()
        n = len(M)
        def dfs(i):
            if i in self.v:
                return
            self.v.add(i)
            for j in range(n):
                if M[i][j] == 1:
                    dfs(j)
        ans = 0 
        for i in range(n):
            if i not in self.v:
                ans += 1
                dfs(i)
        return ans