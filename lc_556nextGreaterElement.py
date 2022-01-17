class Solution(object):
    def nextGreaterElement(self, s):
        """
        47893241
             ^
             412
             first decay 
             -> find out the min num X > cur
             swap X, cur
             sorted after X
        """
        s = [int(e) for e in str(s)]
        n = len(s)
        cur = s[-1] 
        target = n-1
        while target >= 0:
            if s[target] < cur :
                break
            cur = s[target]
            target -= 1
        if target == -1:
            return -1
        
        next_greater =float("inf")
        next_greater_idx = target
        for idx in range(target,n):
         
            if s[idx] > s[target] and s[idx] < next_greater:
                next_greater = min(next_greater, s[idx])
                next_greater_idx = idx
                
        s[target], s[next_greater_idx] = s[next_greater_idx] , s[target]
        s = s[:target+1] + sorted(s[target+1:])
        ans = int("".join(map(str,s))) 
        return ans if ans <= 2147483647 else -1