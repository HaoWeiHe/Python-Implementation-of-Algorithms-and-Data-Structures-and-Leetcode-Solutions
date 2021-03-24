class Solution(object):
    def maxLength(self, arr):
        """
        dp[i]  = max(cur, dp[i-1] + len(arr[i]))
        dp[i] = max(arr[0:i])
        
        dp[0] = 0
        dp[1] = len(arr[0])
        dp[2] = len()
         
        
        """
        
        self.ans = 0
        def dfs(i, visited, lgth):
            if i == len(arr):
                self.ans = max(self.ans, lgth)
                return 
            
            dfs(i+1, visited, lgth)
            if len(visited.union(set(arr[i])) ) == len(visited) + len(arr[i]):
                dfs(i+1,visited.union(set(arr[i])), lgth + len(arr[i]) )
        dfs(0,set(),0)
        return self.ans