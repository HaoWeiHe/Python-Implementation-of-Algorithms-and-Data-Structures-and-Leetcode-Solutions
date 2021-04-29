from collections import defaultdict
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        dfs unti i is lastest and d == 2
        A = i is lastest 
        B = d ==2
        if A or B:
            if A and B:
                cmp the ans
                return 
            else:
                return float('inf')
        """
        self.ans = float('inf')
        def dfs(i,cur,lst):
            if cur > d:return 
            if i == len(jobDifficulty):
                if cur == d :
                    self.ans = min(self.ans,sum([max(v) for v in lst.values() if v]) + sum(jobDifficulty[i:]))
                return 
            
            if cur > 1 and lst[cur-1]==[]:
                return
            lst[cur].append(jobDifficulty[i])
            dfs(i + 1, cur , lst)
            lst[cur].pop()
            
            #keep cur in previoust  bucket
            if cur > 1 and lst[cur-1]==[]:return 
            lst[cur + 1].append(jobDifficulty[i])
            dfs(i +1, cur + 1 , lst)
            lst[cur+1].pop()
       
        dfs(0,1,defaultdict(list))
        return  -1 if self.ans == float('inf') else self.ans
