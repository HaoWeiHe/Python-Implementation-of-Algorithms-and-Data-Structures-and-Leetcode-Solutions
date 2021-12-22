class UnionFind():
    def __init__(self, n):
        self.parent = [ele for ele in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x, y):
        x, y = x - 1, y - 1
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] <  self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return False
    
class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        trios = []
        degree = defaultdict(set)
        uf = UnionFind(n)
        for a,b in edges:
            degree[a].add(b)
            degree[b].add(a)
            
            if uf.union(a,b):
                trios.extend([[a,b,c] for c in degree[b].intersection(degree[a])])

        ans = float('inf')

        for t in trios:
            ans = min(ans, sum([abs(len(degree[e]) - 2) for e in t]))
                
        return  -1 if ans == float('inf')  else ans
        
        