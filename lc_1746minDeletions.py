class Solution(object):
    def minDeletions(self, s):
        """
            ceabaacb
            
            c:2
            e:1
            a:3
            b:2
        
        1223
          ^
        ans = 2 (c from 2 to 0 if c not exist in d, d[c] = 1, break and ans += cur - c)
        
        """
        ans, d = 0, {}
        counter = Counter(s)
        s = sorted(counter.values())
        
        for cur in s:
            if cur in d:
                tmp = cur
                for ele in range(cur, -1, -1):
                    if ele not in d:
                        tmp = cur - ele
                        break
                ans += tmp
                if tmp:
                    d[cur - tmp] = 1
            else:
                d[cur] = 1
        print(d)
        return ans