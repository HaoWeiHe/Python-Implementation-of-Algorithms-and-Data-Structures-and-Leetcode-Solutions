class Solution(object):
    def rearrangeString(self, s, k):
        """
        aabbcc
        {a:2,b:2,c:2}
        
        ab_ab_
        
        most_freq = 2
        2*k+ (size_same_most_freq -1) must > len(s) -> invalid
        j = 0 
       
        loop all charcter by (a,freq, idx)
            for f in range(count[c]):
                res[i] = c
                i += k 
                if i >= n:
                
                idx, idx + 
                
                
        """
        if not k:
            return s
        C = Counter(s) #{a:2,b:2,c :2}
        most_freq = max(C.values()) # 2
        if most_freq* k + C.values().count(most_freq) - k > len(s):  #[2,2,2].count(2)  = 6 + 3 - 3
            return ""
        
        n = len(s)
        ans = [0] * n
        i = (n - 1) % k  
        
        for chrc, freq in sorted(C.items(), key = lambda ele:-ele[1]):
            for _ in range(freq): 
                ans[i] = chrc #"aaadbbcc" [a,b,a,b,a,,_]
                i += k  #6
                if i >= n:#
                    i = (i-1) % k # 7%3 = 1

        return "".join(ans)