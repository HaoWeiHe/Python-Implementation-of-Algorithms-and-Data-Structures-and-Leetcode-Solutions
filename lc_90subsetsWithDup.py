class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        """
        [1,2,3]
       
        
        [] 
        [1] 
            [1 2] 
                 [1,2,3]
            [1 3]
        [2] 
            [2,3]
        [3]
        
        
        [1,2,2]
        
        []
        [1]
            [1,2]
                [1,2,2]    
            [1,2]X
        [2]
            [2,2]
        
        """
        res = []
        def dfs(start, end, h):
            res.append(h)
            for idx in range(start, end):
                if idx > start and nums[idx -1] == nums[idx]:
                    continue
                dfs(idx + 1, end, h + [nums[idx]])
        dfs(0, len(nums), [])
        return res
        
    def subsetsWithDup2(self, nums):
        """
        []
        1    iterate all
        2 12 iterate all
        22 122 >> if == pre, iterate previous one
        222 1222
        """
        nums.sort()
       
        res =[[]]
        for idx, e in enumerate(nums):
            
            if idx > 0 and nums[idx-1] == nums[idx]:
                ssub = []
                for tmp in sub:
                    ssub.append(tmp + [e])
                res.extend(ssub)
                sub = ssub
            else:
                sub = []
                for tmp in res:
                    sub.append(tmp + [e])
                    #iterate all
                res.extend(sub)
        return res
