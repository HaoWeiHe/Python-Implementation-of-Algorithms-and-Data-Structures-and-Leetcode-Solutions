class Solution(object):
    def numFriendRequests(self, age):
        """
        if x!=y:
            valid(x,y) * c[x]* c[y]
        if x == y
            c[x] * (c[x] - 1)
        """
        def valid(x,y):
            return not(y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100)) 
        
        c = Counter(age)
        ages = c.keys()
        ans = 0 
        for x in ages:
            for y in ages:
                if x == y:
                    ans += valid(x,y) * c[x] * (c[x]-1)
                else:
                    ans += valid(x,y) * c[x] * c[y]
        
        return ans
                