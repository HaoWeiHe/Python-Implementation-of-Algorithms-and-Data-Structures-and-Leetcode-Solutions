class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        S = set(map(tuple, points))
        
        N = len(points)
        res = float('inf')
        for i in range(N):
            for j in range(i):
                a,b = points[i]
                c,d = points[j]
                if (a < c and b < d) or (a > c and b > d) : 
                    if (c,b) in S and (a,d) in S:
                        res = min(res, abs(c-a) *abs(d-b))
               
        return res if res != float('inf') else 0
 
points =[[1,3],[2,1],[2,0],[4,3],[0,4],[4,2],[1,0],[3,4],[2,4],[4,0]]
print(Solution().minAreaRect(points))
