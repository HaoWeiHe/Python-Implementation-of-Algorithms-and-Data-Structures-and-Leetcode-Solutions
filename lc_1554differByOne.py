class Solution(object):
    def differByOne2(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        def valid(i,j):
            s1, s2 = dict[i], dict[j] #"abcd", "aacd"
            ans = 0 
            for idx in range(len(s1)):
                if s1[idx] == s2[idx]:
                    continue
                ans += 1
                if ans == 2:
                    return False
            return True
        
        n = len(dict)
        for i in range(n):
            for j in range(i + 1, n):
                if valid(i,j):
                    return True
        return False
    def differByOne(self, dict):
        """
        :type dict: List[str]
        :rtype: bool
        """
        d = defaultdict(int)
        for s in dict:
            for i in range(len(s)):
                current = s[:i]+"*"+s[i+1:]
                d[current] += 1
                if d[current] == 2:
                    return True
        return False
                
        
