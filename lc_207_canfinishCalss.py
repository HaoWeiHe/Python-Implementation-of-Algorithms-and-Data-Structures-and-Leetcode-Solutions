class Solution(object):
    def canFinish(self, n, prerequisites):
        ind = collections.defaultdict(int)
        g = collections.defaultdict(list)
        for a,b in prerequisites:
            ind[a] += 1
            g[b].append(a)
        q = deque([e for e in range(n) if e not in ind])
        res = 0
        while q:
            top = q.popleft()
            res +=1
            for end in g[top]:
                ind[end] -=1
                if ind[end] ==0:
                    q.append(end)
        return res == n