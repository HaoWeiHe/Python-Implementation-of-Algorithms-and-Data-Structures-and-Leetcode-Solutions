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
            if tuple(acc) in self.his:
                return 
            if cur_sum > target:
                return 
            if cur_sum == target :
                self.ans.append(acc)
                self.his.add((tuple(acc)))
                return 1
            
            for idx in range(i, len(candidates)):
                self.his.add(tuple(acc))
                res = dfs(idx+1, acc + [candidates[idx]], cur_sum + candidates[idx] )
                
        dfs(0, [],0)
        
        return self.ans