class Solution(object):
    def maxPoints(self, points):
        """
        
p1
    p2
        p3
p5          p4

# for each point i, 
    compute the each j after i. 
        compute the slope and get the local max
    global_max here
        """
        def div(a,b):
            if a == 0 :
                return b
            if b ==0:return a
            return div(b,a%b)
            
        n = len(points)
        ans = 0 
        for i in range(n):
            local_max = 1
            slope = defaultdict(lambda :1)
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                a,b = p1[0] - p2[0], p1[1] - p2[1]
                mod = div(a,b)
                slope[(a/mod,b/mod)] += 1
                local_max = max(local_max,slope[(a/mod,b/mod)] )
            ans = max(ans, local_max)
        return ans
                
                