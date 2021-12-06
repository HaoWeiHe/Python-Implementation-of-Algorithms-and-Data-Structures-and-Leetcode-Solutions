class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        g = defaultdict(list)
        ans = 0 
        
        for idx, ele in enumerate(s):
            if not g[ele]:
                g[ele].append(-1)
            g[ele].append(idx)
        for key, lst in g.items():
            for i in range(1,len(lst)-1):
                ans += (lst[i] - lst[i-1]) * (lst[i+1] - lst[i])
            ans += (len(s) - lst[-1]) * (lst[-1] - lst[-2])
        return ans
        