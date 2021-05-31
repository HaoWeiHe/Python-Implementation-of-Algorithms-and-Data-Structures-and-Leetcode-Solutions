class UnionFindSet():
    def __init__(self, n ):
        self.parent = [x for x in range(n)]
        self.rank = [0]*n
        
    def Union(self,u,v):
        pu, pv  = self.Find(u), self.Find(v)
        if pu == pv:return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True
    
    def Find(self, x):
        if x !=self.parent[x]:
            self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]
class Solution(object):
    def areSentencesSimilarTwo(self, w1, w2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # pairs = {0: word1, 1:word2, 2:word3..}
        g = {}
        
        if len(w1)!=len(w2):
            return False
        s = UnionFindSet(len(pairs)*2)
        for e in pairs:
            u,v = e
            if u not in g:
                g[u] = len(g)
            if v not in g:
                g[v] = len(g)
            s.Union(g[u],g[v])
       
        for idx, w in enumerate(w1):
            uid, vid = g.get(w1[idx], -1), g.get(w2[idx], -1)
          
            if uid == -1 or vid == -1:
                return False
            if s.Find(uid) != s.Find(vid):
                return False
        return True