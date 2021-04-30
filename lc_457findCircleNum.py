class Solution(object):
    def findCircleNum(self, isConnected):
        """
        bfs with V
        n = len(isConnected) 
        
        iternate n, if n not visted, ans + 1
        
        """
        n = len(isConnected)
        v = set()
        ans =0 
        def bfs(i):
            q = deque([i])
            while q:
                top = q.popleft()
                v.add(top)
                for idx, e in enumerate(isConnected[top]):
                    if idx in v: 
                        continue
                    if e == 1:
                       
                        q.append(idx)
                
            
        for i in range(n):
            if i not in v:
                bfs(i)
              
                ans +=1
        return ans