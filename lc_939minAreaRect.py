class Solution(object):
    def minAreaRect(self, points):
        """

        (a,b)     (a,d)
        
        
        (c,b)     (c,d)
        
        (d-b) * (c-a)
        
        """
        ps = set([tuple(e) for e in points])
        n = len(points)
        ans = float("inf")
        
        for i in range(n):
            for j in range(i+1,n):
                a,b = points[i]
                c,d = points[j]
 
                if not (((c > a ) and (d > b)) or  ((a > c ) and (b > d))):
                    continue
                
                if (a,d) in ps and (c,b) in ps:
                    ans = min(ans, (d-b) * (c-a))
                   
        return ans if ans != float("inf") else 0