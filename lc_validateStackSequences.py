import collections
class Solution(object):
    def validateStackSequences(self, a, b):
        # [1,2,3,4,5]
        d = collections.OrderedDict()
        
        i,j = 0,0
        while j <len(b) :
            
            if b[j] not in d: #a: 1,2,
                d[a[i]] = 1 
                i+=1
            else:
               
                if d.items()[-1][0] == b[j] : #{1,2,3,}
                    del d[b[j]]
                    j+=1 
                            
                else: 
                    # print(lst, d,i,j) #[1,2,5]
                    return False
        return True
a,b  = [1,2,3,4,5], [4,3,5,1,2]
print(Solution().validateStackSequences(a,b))