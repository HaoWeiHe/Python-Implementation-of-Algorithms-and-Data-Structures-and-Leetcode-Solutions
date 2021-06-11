class Solution(object):
    def subsetsWithDup(self, nums):
        """
        [1,2,2]
         i   j
        [[],
        [1],
        [1,2],

        [1,2,2],
        [2],[2,2]]

        """
        nums.sort()
        res = []
        self.counter = 1
        def dfs(start, end, cur): 
            self.counter += 1
            res.append(cur[:])

            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                dfs(i+1, end, cur + [nums[i]])
                
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
