class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ans = 0 
        self.v = set()
        g = collections.defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
            
        def bfs(ele):
            q = deque([ele])
            while q:
                top =  q.popleft()
                self.v.add(top)
                for e in g[top]:
                    if e not in self.v:
                        q.append(e)
            
            
        for ele in range(n):
            if ele in self.v:
                continue
            
            bfs(ele)
            ans += 1
        return ans