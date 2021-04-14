class Solution(object):
    def longestStrChain2(self, words):
        """
        ["a","b","ba","bca","bda","bdca"]
        a = 1
        b = 1
        ba = [a,b]
        bca = []
    """
        g = defaultdict(int)
        for w in sorted(words, key = lambda x : len(x)):
            g[w] = 1
            for i in range(len(w)):
                g[w] = max(g[w], g[w[:i] + w[i+1:]] + 1)
        return max(g.values())
    def longestStrChain(self, words):
        """
        a - ba
           
        b - ba
        ba - bca
        bca - bdca
        bda - bdca
        
        * bfs and begin with the shortest w
        
        n*26 create map 
        """
        if not words:return 0
        
        s = set(words)
        g = defaultdict(list)
        words.sort( key= lambda x: len(x))
        q = deque([(w,1) for w in words])
    
        def helper(w1,w2):
            #w1 is shorter then w2
            if len(w1) != len(w2)-1:
                return False
            flag = 0
            """
            ba 
             i 
            bca
            """
            i,j = 0,0
            while i < len(w1):
                if w1[i] == w2[j]:
                    i+= 1
                    j+=1
                else:
                    j +=1
                    flag +=1
                if flag ==2:
                    return 0
            return 1
                
            
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j: 
                    continue
                w1, w2 = words[i], words[j]
                if helper(w1, w2):
                    g[w1].append(w2)
        res = 0 
        
        while q:
            top, lvl = q.popleft()
            
            for e in g[top]:
                q.append((e, lvl + 1))
            res = max(res, lvl)
        return res
            