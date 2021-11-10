class Unionfind():
    def __init__(self,n ):
        self.parent = [ele for ele in range(n)]
        self.rank = [0] *n 
    
    def find(self,x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
            
    def union(self, x, y ):
        px, py = self.find(x), self.find(y)
        if px == py:
            return True
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        return False

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = Unionfind(len(edges))
        for e in edges:
            if uf.union(e[0] - 1, e[1]-1):
                return e
        