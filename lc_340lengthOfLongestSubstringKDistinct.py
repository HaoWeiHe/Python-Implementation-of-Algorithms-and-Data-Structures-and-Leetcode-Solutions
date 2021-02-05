class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        eceba
        01234
            i
        {e:2,b = 3}
        lf = first_item + 1 = 2
        max = max(3,3-2+1 = 2)
        {e:2, b=3, a = 4}
max =   123
        """
        j = 0 
        res = 0 #min()
        counter  = collections.OrderedDict()
        for i,ele in enumerate(s):
            if ele in counter:
                del counter[ele]
            counter[ele] = i
            if len(counter) > k:
                _, del_idx = counter.popitem(last = False)
                j = del_idx+1
            if len(counter) <= k:
                res= max(res, i-j+1)
        return res
    def lengthOfLongestSubstringKDistinct2(self, s, k):
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