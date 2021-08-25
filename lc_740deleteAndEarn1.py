class Solution(object):
    def deleteAndEarn(self, nums):
        """
        [2,2,3,3,3,4]
        (2:2, 3:3, 4:1) 
        
        if 2: left_over: {4:1}, tmp= 4
            if 4 : tmp = 4 + 4 =8
        if 3: left_over:{0}, tmp = 9
        if 4: left_over: {2:2} , tmp = 4
        """
        c = Counter(nums)
        self.ans = 0
        
        def dfs(d, acc):
            if not d:
                self.ans = max(self.ans, acc)
                return 
            tmp = {}
            for cur in d:
                if cur +1 in d:
                    tmp[cur+1]  = d[cur+1]
                    del d[cur+1]
                if cur -1 in d:
                    tmp[cur-1] = d[cur-1]
                    del d[cur-1]
                tmp[cur] =  d[cur]
                del d[cur]
                dfs(d, acc+ cur*tmp[cur])
                for k,v in tmp.items():
                    d[k] = v
            
                    
        dfs(c,0)
        return self.ans
               
        