class Solution(object):
    def findCircleNum(self, M):
        """
       [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
        [0,3] 
    v = {0,3,2}
        """
        v = set()
        n = len(M)
        ans = 0 
        for i in range(n):
            if i in v:
                continue
            ans += 1
            q = deque([i])
            while q:
                top = q.popleft() #[0]
                if top in v:
                    continue
                v.add(top)
                for j in range(n): 
                    if M[top][j] == 1:
                        q.append(j) #[0,3]
                
        return ans