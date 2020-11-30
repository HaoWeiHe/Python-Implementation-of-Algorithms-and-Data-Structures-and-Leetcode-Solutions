
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        
        [0,4,9,9,7,4,5]
        module by K
        [0,4,4,4,2,4,0]
        C(n,2) = (n * (n-1))/2 
        """
        n= len(A)
        if not A:
            return 0
        
        presum = [0] 
        
        for ele in A:
            presum.append((presum[-1] + ele) % K)
        
        c = collections.Counter(presum)
        
                    
        return sum((v*(v-1))/2 for v in c.values())