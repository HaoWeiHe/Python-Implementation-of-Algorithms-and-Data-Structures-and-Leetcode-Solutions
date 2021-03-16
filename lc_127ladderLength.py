class Solution(object):
    def ladderLength(self, beginWord, endWord, ws):
        """
        "hit" -> "hot" -> "dot" -> "dog" -> "cog"
        hit hot
        go through : hxt xit hix catelogry and move on until readch to the end
        
        bfs
        
        hit -> explore xit, hxt, hix -> if exist append to queue
        hit -> hot/dot/lot/ -> 
        0      1                2
        
        """
        g = collections.defaultdict(list)
        #make xit
        for w in ws:
            for idx in range(len(w)):
                c = w[:idx] + "x" + w[idx+1:]
                g[c].append(w)
        q = deque([(beginWord,1)])
        v = set()
        while q:
            top, lvl = q.popleft()
           
            for idx in range(len(top)):
                
                c = top[:idx] + "x" + top[idx+1:]
                if c in v:continue
                v.add(c)
                if c in g:
                    for can in g[c]:
                        if can == endWord: return lvl + 1
                        q.append((can, lvl + 1))
        return 0
                        