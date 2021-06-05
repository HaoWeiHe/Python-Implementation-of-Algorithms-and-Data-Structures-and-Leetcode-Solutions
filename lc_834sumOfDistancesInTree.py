import collections
class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] *N
        g = collections.defaultdict(list)
        g_i = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g_i[b].append(a)

        indgree = [{}] * N 
        for i in range(N):
            if i not in g:
                continue
            v = {i}
            q = collections.deque([(i,g[i],0)])
            tmp = 0
            while q: 
                cur, ns, lvl = q.popleft() #ele = [1,2]
                indgree[i][cur] = lvl #[1: 0:2, 2: ]
                for n in ns: 
                    if n in v:continue
                    q.append((n, g[n], lvl + 1))

                    v.add(n)
            ans[i] = tmp

        for i in range(len(indgree)):
            v = {i}
            q = collections.deque([])
            for ele,lvl in indgree[i].items(): 
                q.append((g_i[ele],lvl))
            while q:
                ns, lvl  = q.popleft()
                tmp += lvl
                for n in ns:
                    if n in v: continue
                    q.append((g_i[n], lvl+1))
                    v.add(n)
            ans[i] = tmp

        return ans

N, edges =  6 , [[0,1],[0,2],[2,3],[2,4],[2,5]]

print(Solution().sumOfDistancesInTree(N, edges))
