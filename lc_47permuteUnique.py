class Solution(object):
    def permuteUnique(self, nums):
        """
        [1,1,2]
        [1] [1,2]
            [2]
               [1] -> 1 2 1
            [1]
                [2] -> 1 1 2
        f(1,2) = [[1,2] , [2,1]]
        [2] [1,1] 
            [1]
                [1] -> 2 1 1
        
        f(1) + f(1,2)
            
        f(2) + f(1,1)
        """
        nums.sort()
        def dfs(cur):
            if not cur:
                return [[]]
            res = []
            for idx,e in enumerate(cur):
                if idx > 0 and cur[idx-1] == cur[idx]:
                    continue
                res.extend([ [e] + sub_arry for sub_arry in dfs(cur[:idx] + cur[idx+1:])])
               
            
            return res
        return dfs(nums)
                
        