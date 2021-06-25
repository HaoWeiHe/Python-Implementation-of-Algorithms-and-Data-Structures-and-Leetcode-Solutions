"""
x,y (1,4)
4.parent == 1.parent ring!
"""
class Unifind():
    def __init__(self,n):
        self.parent = [e for e in range(n+1)]
        self.rank = [0] * (n+1)
        
    def getParent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.getParent(self.parent[n] )
        return self.parent[n]
    
    def uni(self,x,y):
        px, py = self.getParent(x), self.getParent(y)
        if px == py :
            return True
        
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.rank[px] += 1
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
            self.rank[py] +=  1
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
        uinf = Unifind(len(edges))
        
        for ele in edges:
            if uinf.uni(ele[0], ele[1]):
                return ele
      
            