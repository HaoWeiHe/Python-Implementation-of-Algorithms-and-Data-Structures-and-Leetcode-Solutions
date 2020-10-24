class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        self.d = dict()
        def dfs(node, visited,level):
            if node in self.d: return self.d[node] + level

            if node in visited: 
                return level 

            self.d[node] = level

            return dfs(nums[node],visited+[node], level+1)
            
            
        for e in nums:
            self.res = max(self.res, dfs(e, [],0))
        return self.res