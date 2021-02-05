class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        ["eceba"]
              i
            j
          {e:1,c:1}
          {c:0,e:1} len = i-j +1
    res = 123
        """
        j = 0 
        res = 0
        counter  = collections.defaultdict(int)
        for i in range(len(s)):
            counter[s[i]]+=1
            while len(counter) > k:
                counter[s[j]]-=1
                if counter[s[j]] ==0:
                    del counter[s[j]]
                j +=1 
            if len(counter) <= k:
                res = max(res, i -j + 1)
        return res