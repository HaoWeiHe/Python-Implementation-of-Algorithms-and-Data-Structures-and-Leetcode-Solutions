class UnionFind():
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True
    
    def find(self, u):        
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        if union(a,b) is False(same parent. ring detect), return 
        """
        u = UnionFind(len(edges))
        for e in edges:
            if not u.union(e[0]-1,e[1]-1):
                return e
        return None
            