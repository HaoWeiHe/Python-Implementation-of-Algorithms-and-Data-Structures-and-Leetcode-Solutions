
from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words) :
        g = defaultdict(list)
        
        indegree = {c : 0 for w in words for c in w}
        for firstw, secw in zip(words, words[1:]):
            for c1, c2 in zip(firstw, secw):
                if c1 != c2:
                   
                    if c2 not in g[c1] :
                        g[c1].append(c2)
                        indegree[c2] += 1
                    break
            else:
                if len(secw) < len(firstw): return ""
        q = deque([c for c in indegree if indegree[c]==0])
        res = ""

        while q:
            top = q.popleft()
            res = res + top
            for ele in g[top]:
                indegree[ele] -= 1
                if indegree[ele] ==0:
                    q.append(ele)
        if len(res) < len(indegree):
            return ""
        return res