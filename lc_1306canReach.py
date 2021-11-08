class Solution(object):
    def canReach(self, arr, start):
        """
         0 1 2 3 4 5 6 
        [4,2,3,0,3,1,2]
        5 + 1 
        5 - 1
        """
        self.ans = False
        def dfs(start, v):
            if self.ans:
                return
            if arr[start] == 0:
                self.ans = True
                return 
            if start in v:
                return 
            v.add(start)
            if arr[start] + start < len(arr):
                dfs(arr[start] + start, v)
            if start - arr[start] >= 0 :
                dfs(start - arr[start] , v)
            v.remove(start)
        dfs(start, set())
        return self.ans
            