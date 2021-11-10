class UnionFind():
    def __init__(self, voc):
        self.rank = {word: 0 for word in voc}
        self.parent = {word: word for word in voc}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
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
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        """
        :type sentence1: List[str]
        :type sentence2: List[str]
        :type similarPairs: List[List[str]]
        :rtype: bool
        """
        if len(sentence1) != len(sentence2):
            return False

        voc = set()
        for w1,w2 in similarPairs:
            voc.add(w1)
            voc.add(w2)
        
        for w in sentence1:
            voc.add(w)
        for w in sentence2:
            voc.add(w)

        uf = UnionFind(list(voc))

        for w1, w2 in similarPairs:
            uf.union(w1,w2)
       
        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if uf.find(w1) != uf.find(w2):
                return False
        return True
