
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        
        #    S = "ADOBECODEBANC", 
        #    T = "ABC"

        if still find keep looking

        """

#    def minWindow2(self, s, t):

#         """
#         consider this quesiotn as LRU, but only put
#         insert: when ele in T
#         capacity <-> check_if_full
        
#         S = "ADOBECODEBANC", 
#         T = "ABC"

#         ADOBECODEB  A  N  C
#         0123456789  10 11 12
#         A  B C   B   

# lst   [ABC]   [C B] [CBA]    [BA] [BAC] 
#       [0,3,5] [5,9] [5,9,10] [9,10] [9,10,12]
# len   6        5       6             4
        
#         if hit:
#             orderest: remove to end 
            
#         if full
#             count firstele and lastele in ordered
#             remove first 
#             update mappingLst: remove first
        
#         """
        C = collections.Counter(t)
     
        def is_full(window_counts):
            # lst = [s[e] for e in d ]
            # window_counts = collections.Counter(lst)
            
            for key in C:    
                if key not in window_counts or window_counts[key] < C[key]: return False
            return True
        
        d = collections.OrderedDict()
        window_counts = collections.defaultdict(int)
        s = s
        t = set(t)
        lst = []
        res, minLength = "", float('inf')
        for idx,c in enumerate(s):
            if c in t:
                if c not in d:
                    d[idx] = 1

                else:
                    d.move_to_end(idx)
                window_counts[c]  += 1
            
            while is_full(window_counts):
                
                end_idx = d.popitem(last = True)[0]
                d[end_idx] = 1
                first_idx = next(iter(d))
                
                if minLength > end_idx -first_idx + 1:
                    minLength = end_idx -first_idx + 1
                    res = s[first_idx: end_idx + 1]
                frist_item = d.popitem(last = False)
                window_counts[s[frist_item[0]]] -= 1
                
        return res

s,t = "ADOBECODEBANC", "ABC"
a = Solution().minWindow(s,t)
print(a)
