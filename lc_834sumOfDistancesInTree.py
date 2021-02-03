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
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
    
        for i in range(N):
            v = {i}
            q = collections.deque([(g[i],0)])
            tmp = 0
            while q: 
                ns, lvl = q.popleft() #ele = [1,2]
                tmp += lvl
                for n in ns: 
                    if n in v:continue
                    
                    q.append((g[n], lvl + 1))
                    v.add(n)
            ans[i] = tmp
        return ans

N, edges = 6, [[0,1],[0,2],[0,3],[2,3],[2,4],[2,5]]
print(Solution().sumOfDistancesInTree(N,edges))