import collections
class Solution(object):
    def minTransfers(self, transactions):
        """
        dfs: min(dfs(pick_i, pick_j) + 1) 
        pruning - pick_i * pick_j < 0 
        early stop - pick_i + pick_j ==0
        """
        d = collections.defaultdict(int)
        for frm, to, cost in transactions:
            d[frm] -= cost
            d[to] += cost
        lst = [ e for e in d.values() if e!=0]
        
        if not lst:
            return 0
        
        self.ans = float('inf')
        
        def dfs(idx, trans, lst):
            while idx < len(lst) and lst[idx] == 0:
                idx += 1

            if idx >= len(lst):
                self.ans = min(self.ans, trans)
                return 
            
            n = len(lst)
            waive = lst[idx]
            for j in range(idx + 1, n):
                if lst[j] * waive > 0:
                    continue
                lst[j] += waive
                dfs(idx + 1, trans + 1,lst)
                lst[j] -= waive                 

        dfs(0,0,lst)
        return self.ans
            
