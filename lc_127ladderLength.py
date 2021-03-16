import collections

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


        def helper(q, visted, other_visted):
            top, lvl = q.popleft()
            for idx in range(len(top)):
                c = top[:idx] + "x" + top[idx+1:]
                for w in g[c]:
                    if w in other_visted:
                        return lvl + other_visted[w]
                    if w not in visted:
                        visted[w] = lvl + 1
                        q.append((w, lvl +1))
            return None
        if endWord not in ws or not endWord or not beginWord or not ws:return 0
        ans = None
        q_begin = collections.deque([(beginWord,1)])
        q_end = collections.deque([(endWord, 1)])
        beginWord_visted = {beginWord:1}
        endWord_visted = {endWord:1}

        while q_begin and q_end:
                
            ans = helper(q_begin, beginWord_visted, endWord_visted)
            if ans: 
                return ans
            ans = helper(q_end, endWord_visted, beginWord_visted)
            if ans: 
                return ans

        return 0
 