class Solution(object):
    def allPathsSourceTarget(self, g):
        """
        q = [(0,[0])]
    step1:top, his = 1, [0], for e in g[top], append(e,[0,e])..
    step2:
    if top == n-1:
        ans.append(his)
        """
        ans = []
        q = deque([(0,[0])])
        if not g:
            return []
        
        while q:
           
            top, his = q.popleft()
            for e in g[top]:
                q.append((e, his + [e]))
            if top == len(g)-1:
                ans.append(his)
        return ans