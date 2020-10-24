class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        self.res = 0
        def dfs(lst):
            while len(lst) >1:
                idx = lst.index(min(lst))
                if idx !=0 or idx!=len(lst)-1:
                    self.res += min(lst[idx-1], lst[idx+1])*lst[idx]
                else:
                    self.res += lst[idx]*lst[1] if idx ==0 else lst[idx]*lst[n-1]
                lst.pop(idx)
        dfs(lst)
        return res
arr = [6,2,4]
print(Solution().dfs(arr))