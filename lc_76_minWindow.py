class Solution(object):
    def minWindow(self, s, t):

        if not s or not t: return ""
        l,r = 0,0
        
        target_dic = collections.Counter(t)
        window_C = collections.defaultdict(int)
        res, ans = "", float('inf')
        required = len(target_dic)
        tmp_req = 0
        visted = set()
        t = set(t)
        for r,char in enumerate(s):

            if char in t:
                window_C[char] += 1
                
                if window_C[char] ==  target_dic[char] and char not in visted:
                    tmp_req += 1
                    visted.add(char)
                
                while l <= r and tmp_req == required:

                    if tmp_req == required:
                    
                        if ans > r - l+1 :
                            ans = r- l+1
                            res = s[l:r+1]
                    if s[l] in t:
                        window_C[s[l]] -=1
                        if window_C[s[l]] < target_dic[s[l]] :
                            tmp_req -= 1
                            visted.remove(s[l])
                    l += 1

        return res 

           
    def minWindow2(self, s, t):
        """
        consider this quesiotn as LRU, but only put
        insert: when ele in T
        capacity <-> check_if_full
        
        S = "ADOBECODEBANC", 
        T = "ABC"

        ADOBECODEB  A  N  C
        0123456789  10 11 12
        A  B C   B   

lst   [ABC]   [C B] [CBA]    [BA] [BAC] 
      [0,3,5] [5,9] [5,9,10] [9,10] [9,10,12]
len   6        5       6             4
        
        if hit:
            orderest: remove to end 
            
        if full
            count firstele and lastele in ordered
            remove first 
            update mappingLst: remove first
        

        """
        C = collections.Counter(t)
        def is_full(d):
            
            for key in C:    
                if key not in d or d[key] <= C[key]: return False
            return True
        
        d = collections.OrderedDict()
       
        t = set(t)
        lst = []
        res, minLength = 0, float('inf')
        for idx,c in enumerate(s):
            if c in t:
                if c not in d:
                    d[c] = 1
                else:
                    d.move_to_end(c)
                
            if is_full(d):
                orderedlst = list(d)
                first_idx, end_idx = orderedlst[0], orderedlst[-1]

                if minLength < end_idx -first_idx + 1:
                    minLength = end_idx -first_idx + 1
                    res = s[first_idx: end_idx + 1]
        return res

s,t =  "ADOBECODEBANC", "ABC"
Solution().minLength(s,t)