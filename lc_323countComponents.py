
class UnionFind():
    def __init__(self, n):
        self.parent = [ele for ele in range(n)]
        self.rank = [0] * n 

    def union(self,x,y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return 
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    


class Solution(object):
    def countComponents(self, n, edges):
        uf = UnionFind(n)
        ans = 0 
        for a,b in edges:
            uf.union(a,b)
        for ele in range(n):
            uf.find(ele)
        
        return len(set(uf.parent))
        
    def countComponents2(self, n, edges):
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

n, edges = 4, [[0,1],[2,3],[1,2]]
print(Solution().countComponents(n,edges))