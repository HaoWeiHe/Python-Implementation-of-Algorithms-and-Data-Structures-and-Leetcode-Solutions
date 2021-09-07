class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        1. find the hand of forest
        2. iterate hands and dfs using v 
        """
        g = defaultdict(list)
        hands = {i: True for i in range(len(colors))}
        for (a,b) in edges:
            g[a].append(b)
            hands[b] = False
        self.ans = []
        def dfs(r, v, h):
            if len(g[r]) == 0:
                if self.ans != -1:
                    self.ans.append(h)
                return 
           
            for node in g[r]:
                if node in v:
                    self.ans = -1
                    return
                dfs(node, v+[node],h+[colors[node]] )
   
            return 
        
        
        res = 0
        h = []
        
        
            
        for hd in hands:   
            if hands[hd] == False:
                continue
            dfs(hd,[hd], h+[colors[hd]]) 
            
        for e in self.ans:    
            res =  max(res, max(Counter(e).values()))
        
        return res if self.ans else -1