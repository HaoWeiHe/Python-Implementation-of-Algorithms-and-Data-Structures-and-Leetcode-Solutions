class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        [5,10,-5]
        [5,10]
        if cur is neg, cmp top, if top*cur < 0 and top < abs(cur):pop, until empty or top > cur
        if top*cur < 0 and  cur == top, both boo
        
        """
        
        ans = []
        
        for cur in asteroids:
            while ans and cur < 0 < ans[-1]:
                if ans[-1] < -cur:
                    ans.pop()
                    continue
                elif ans[-1] == -cur:
                    ans.pop()
                break
            else:
                ans.append(cur)
        return ans