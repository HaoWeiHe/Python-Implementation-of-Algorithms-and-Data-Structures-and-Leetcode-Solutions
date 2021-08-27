class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        self.ans = []
        self.his = set()
        def dfs(i,acc,cur_sum):
    
            if cur_sum == target:
                if tuple(acc) not in self.his:
                    self.ans.append(acc)
                self.his.add(tuple(acc))
                return 
            for idx in range(i, len(candidates)):
                dfs(idx+1, acc + [candidates[idx]], cur_sum + candidates[idx] )
                
        dfs(0, [],0)
        return self.ans